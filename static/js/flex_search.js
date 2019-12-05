let $flexIndex, $results, pagesIndex;

function getQueryVariable(variable) {
    const query = window.location.search.substring(1);
    const vars = query.split('&');

    for (let i = 0; i < vars.length; i++) {
        const pair = vars[i].split('=');

        if (pair[0] === variable) {
            return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
        }
    }
}

let searchTerm = getQueryVariable('query');

// Initialize flexsearch.js using our generated index file
const initFlexSearch = () => {
    // First retrieve the index file
    $.getJSON("/index.json")
        .done(function (index) {
            pagesIndex = index;
            $flexIndex = new FlexSearch({
                tokenize: "forward",
                encode: "extra",
                resolution: 10,
                threshold: 7,
                depth: 3,
                doc: {
                    id: "uri",
                    field: ["title",
                        "content"]
                }
            });
            $flexIndex.add(index)
        })
        .fail(function (jqxhr, textStatus, error) {
            const err = textStatus + ", " + error;
            console.error("Error getting Hugo index file:", err);
        });
}

// Nothing crazy here, just hook up a listener on the input field
const initUI = () => {
    $results = $("#results");
    const searchResult = $("#search-results");
    const api = $("#menu")[0].mmApi;

    $(".flex-search").keyup(function () {
        $results.empty();

        // Only trigger a search when 2 chars. at least have been provided
        const query = $(this).val();
        if (query.length < 2) {
            return;
        }
        search(query, $results);
    });

    $(".mm-searchfield__input").find("input").on("keyup", function() {
        searchResult.empty();

        // Only trigger a search when 2 chars. at least have been provided
        const query = $(this).val();
        if (query.length < 2) {
            api.closeAllPanels();
            return;
        }
        search(query, searchResult);
        api.openPanel(document.getElementById("search-results"))
    });
}

/**
 * Trigger a search in flexsearch and transform the result
 *
 * @param  {String} query
 * @return {Array}  results
 */
const search = (query, sr, amount = 10) => {
    const results = $flexIndex.search({

        field: ["title", "content"],
        query: query,
        bool: "or"
    });
    renderResults(results, sr, amount)
}

/**
 * Display the 10 first results
 *
 * @param  {Array} results to display
 */
const renderResults = (results, sr, amount) => {
    if (!results.length) {
        sr.append("<p>No results found</p>");
        return;
    }

    // Only show the ten first results
    results.slice(0, amount).forEach((result) => {
        const $result = "<div class='result' role='option'>" +
            "<a href='" + result.uri + "'>" +
            result.title +
            "</a>" +
            "</div>";
        sr.append($result);
    });
}

// Let's get started
initFlexSearch();

$(document).ready(function () {
    initUI();
}); 