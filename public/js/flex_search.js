var $flexIndex, $results, pagesIndex;

function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');

    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');

        if (pair[0] === variable) {
            return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
        }
    }
}

var searchTerm = getQueryVariable('query');

// Initialize flexsearch.js using our generated index file
function initFlexSearch() {
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
            var err = textStatus + ", " + error;
            console.error("Error getting Hugo index file:", err);
        });
}

// Nothing crazy here, just hook up a listener on the input field
function initUI() {
    $results = $("#results");
    $("#search-input").keyup(function () {
        $results.empty();

        // Only trigger a search when 2 chars. at least have been provided
        var query = $(this).val();
        if (query.length < 2) {
            return;
        }

        search(query);
    });
}

/**
 * Trigger a search in flexsearch and transform the result
 *
 * @param  {String} query
 * @return {Array}  results
 */
function search(query) {
    var results = $flexIndex.search({

        field: ["title", "content"],
        query: query,
        bool: "or"
    });
    renderResults(results)
}

/**
 * Display the 10 first results
 *
 * @param  {Array} results to display
 */
function renderResults(results) {
    if (!results.length) {
        $results.append("<p>No results found</p>");
        return;
    }

    // Only show the ten first results
    results.slice(0, 10).forEach(function (result) {
        var $result = "<div class='result' role='option'>" +
            "<a href='" + result.uri + "'>" +
            result.title +
            "</a>" +
            "</div>";
        $results.append($result);
    });
}

// Let's get started
initFlexSearch();

$(document).ready(function () {
    initUI();
}); 