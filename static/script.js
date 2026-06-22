document.addEventListener("DOMContentLoaded", function () {
  var bars = document.querySelectorAll(".bar");
  bars.forEach(function (bar) {
    var target = bar.style.height;
    bar.style.height = "0%";
    requestAnimationFrame(function () {
      bar.style.transition = "height 0.6s ease";
      bar.style.height = target;
    });
  });

  var statusDot = document.querySelector(".topbar-status .dot");
  if (statusDot) {
    setInterval(function () {
      statusDot.style.opacity = statusDot.style.opacity === "0.4" ? "1" : "0.4";
    }, 1200);
  }
});
