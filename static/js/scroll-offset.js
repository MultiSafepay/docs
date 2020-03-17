const scrollOffset = (id, offset) => {
    let target = document.querySelector(id);
    if (target) {
        let y = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scroll(0, y);
    }
}