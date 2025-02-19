
    document.addEventListener("DOMContentLoaded", function () {
        const mobileMenu = document.getElementById("mobile-menu");
        const menuBtn = document.getElementById("menu-btn");
        const closeMenu = document.getElementById("close-menu");
        const overlay = document.getElementById("overlay");

        // Function to open the mobile menu
        function openMenu() {
            mobileMenu.classList.remove("translate-x-full"); // Show the menu by removing translate-x-full
            overlay.classList.remove("hidden"); // Show overlay
        }

        // Function to close the mobile menu
        function closeMenuFunc() {
            mobileMenu.classList.add("translate-x-full"); // Hide the menu by adding translate-x-full
            overlay.classList.add("hidden"); // Hide overlay
        }

        // Event listeners for opening and closing the menu
        menuBtn.addEventListener("click", openMenu); // Open menu when menu button is clicked
        closeMenu.addEventListener("click", closeMenuFunc); // Close menu when close button is clicked
        overlay.addEventListener("click", closeMenuFunc); // Close menu when overlay is clicked
    });



//  JavaScript for Toggle 

    const menuToggle = document.getElementById("menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");

    menuToggle.addEventListener("click", () => {
        mobileMenu.classList.toggle("hidden");
    });



// popup for readmore in our practice area

document.addEventListener("DOMContentLoaded", function () {
    const popupModal = document.getElementById("popupModal");
    const popupContent = popupModal.querySelector("div"); // The inner content box
    const popupOverlay = document.getElementById("popupOverlay");


    function openPopup(element) {
        const title = element.querySelector("h3").innerText;
        const content = element.querySelector("p").innerText;
        // popupOverlay.classList.remove("hidden");
        document.getElementById("popupTitle").innerText = title;
        document.getElementById("popupContent").innerText = content;
        popupModal.classList.remove("hidden");
    }

    function closePopup() {
        popupModal.classList.add("hidden");
        // popupOverlay.classList.add("hidden");

    }

    // Close when clicking outside the content box
    popupModal.addEventListener("click", function (event) {
        if (!popupContent.contains(event.target)) {
            closePopup();
        }
    });

    window.openPopup = openPopup;
    window.closePopup = closePopup;
});
