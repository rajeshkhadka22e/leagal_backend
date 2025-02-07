

  // leagel person
  const slider = document.getElementById("slider");

  function slideLeft() {
      slider.scrollBy({ left: -310, behavior: "smooth" }); // Adjust scroll distance as needed
  }

  function slideRight() {
      slider.scrollBy({ left: 310, behavior: "smooth" }); // Adjust scroll distance as needed
  }



  // faq section
  function toggleFaq(id) {
    let faqs = document.querySelectorAll("[id^=faq]");
    
    faqs.forEach(faq => {
        if (faq.id !== "faq" + id) {
            faq.classList.add("hidden");
        }
    });

    document.getElementById("faq" + id).classList.toggle("hidden");
}



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

    function openPopup(element) {
        const title = element.querySelector("h3").innerText;
        const content = element.querySelector("p").innerText;
        document.getElementById("popupTitle").innerText = title;
        document.getElementById("popupContent").innerText = content;
        popupModal.classList.remove("hidden");
    }

    function closePopup() {
        popupModal.classList.add("hidden");
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
