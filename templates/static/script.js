const details = document.querySelectorAll("details");

details.forEach((targetDetail) => {
    targetDetail.addEventListener("click", () => {
        // Close all the details that are not targetDetail.
        details.forEach((detail) => {
            if (detail !== targetDetail) {
                detail.removeAttribute("open");
            }
        });
    });
});

function menuOpen() {
    var menu = document.querySelectorAll(".side-menu");
    for (i = 0; i <= menu.length; i++) {
        menu[i].classList.toggle("open");
    }
}
