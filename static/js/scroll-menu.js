window.addEventListener('load', () => {
    let offset = document.querySelector("div.breadcrumb-box").offsetHeight + document.querySelector("nav.navbar").offsetHeight;
    tocbot.init({
        // Where to render the table of contents.
        tocSelector: '.js-toc',
        // Where to grab the headings to build the table of contents.
        contentSelector: '.js-toc-content',
        // Which headings to grab inside of the contentSelector element.
        headingSelector: 'h2, h3, h4, h5',
        headingsOffset: offset,
        scrollSmooth: false,
        onClick: (e) => {
            e.preventDefault();
            window.location.hash = e.target.hash;
            scrollOffset(e.target.hash, offset);
        }
    });
    scrollOffset(location.hash, offset);
});