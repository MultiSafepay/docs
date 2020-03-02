const scrollOffset = (id, offset) => {
    let target = document.querySelector(id);
    if (target) {
        let y = target.offsetTop - offset;
        window.scroll(0, y);
    }
}