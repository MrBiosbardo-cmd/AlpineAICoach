window.AlpineSiteConfig = {
  riderWebAppBaseUrl: "https://alpinecyclingcoach-production.up.railway.app/rider",
  getRiderWebAppUrl: function(locale) {
    var lang = locale || "en";
    return this.riderWebAppBaseUrl + "?lang=" + encodeURIComponent(lang);
  }
};
