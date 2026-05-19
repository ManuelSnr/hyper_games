// Smooth scroll animation for carousel rows
document.addEventListener("DOMContentLoaded", () => {
  // CTA Button handlers
  const downloadBtn = document.querySelector(".cta-primary");
  const playWebBtn = document.querySelector(".cta-secondary");

  if (downloadBtn) {
    downloadBtn.addEventListener("click", () => {
      // Detect platform and redirect accordingly
      const userAgent = navigator.userAgent || navigator.vendor || window.opera;

      if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
        // iOS device
        window.location.href =
          "https://apps.apple.com/ng/app/hyper-play-1v1-games-for-cash/id1631502021";
      } else if (/android/i.test(userAgent)) {
        // Android device
        window.location.href = "https://hyper.mvm.gg/";
      } else {
        // Desktop or other
        window.location.href =
          "https://apps.apple.com/ng/app/hyper-play-1v1-games-for-cash/id1631502021";
      }
    });
  }

  if (playWebBtn) {
    playWebBtn.addEventListener("click", () => {
      // Open in new tab to avoid deep linking to mobile app
      window.open("https://hypergames.gg", "_blank", "noopener,noreferrer");
    });
  }
});
