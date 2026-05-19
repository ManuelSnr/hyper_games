// Smooth scroll animation for carousel rows
document.addEventListener("DOMContentLoaded", () => {
  // CTA Button handlers
  const downloadBtn = document.querySelector(".cta-primary");
  const playWebBtn = document.querySelector(".cta-secondary");

  if (downloadBtn) {
    downloadBtn.addEventListener("click", () => {
      // Add your app store link here
      // For iOS: window.location.href = 'https://apps.apple.com/app/your-app-id';
      // For Android: window.location.href = 'https://play.google.com/store/apps/details?id=your.package.name';

      // Detect platform and redirect accordingly
      const userAgent = navigator.userAgent || navigator.vendor || window.opera;

      if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
        // iOS device
        alert("Download on the App Store - Coming Soon!");
        // window.location.href = 'YOUR_IOS_APP_STORE_LINK';
      } else if (/android/i.test(userAgent)) {
        // Android device
        alert("Download on Google Play - Coming Soon!");
        // window.location.href = 'YOUR_GOOGLE_PLAY_LINK';
      } else {
        // Desktop or other
        alert("Download our mobile app from the App Store or Google Play!");
      }
    });
  }

  if (playWebBtn) {
    playWebBtn.addEventListener("click", () => {
      // Add your web app URL here
      alert("Play on Web - Coming Soon!");
      // window.location.href = 'YOUR_WEB_APP_URL';
    });
  }
});
