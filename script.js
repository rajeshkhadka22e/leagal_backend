

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
