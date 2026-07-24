window.AlpineSiteConfig = {
  riderWebAppBaseUrl: "https://strong-charm-production-bca3.up.railway.app/rider/login",
  getRiderWebAppUrl: function(locale) {
    var lang = locale || "en";
    return this.riderWebAppBaseUrl + "?lang=" + encodeURIComponent(lang);
  }
};
