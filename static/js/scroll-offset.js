const scrollOffset = (id, offset) => {
    let target = document.getElementById(id);
    if (target) {
        let y = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scroll(0, y);
    }
}