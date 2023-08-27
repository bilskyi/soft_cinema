const seats = document.querySelectorAll(".row .seat");

seats.forEach((seat) => {
  seat.addEventListener("click", () => {
    seat.classList.toggle("selected");
  });
});
