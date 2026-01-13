document.addEventListener("DOMContentLoaded", function () {
  const provinceSelects = document.querySelectorAll("select[data-target][data-city-url]");

  provinceSelects.forEach((provSelect) => {
    provSelect.addEventListener("change", function () {
      const provinceId = this.value;
      const citySelectId = this.dataset.target;
      const cityUrl = this.dataset.cityUrl;

      const citySelect = document.getElementById(citySelectId);
      citySelect.innerHTML = "<option>Loading...</option>";

      if (!provinceId) {
        citySelect.innerHTML = '<option value="">Pilih Kota</option>';
        return;
      }

      fetch(`${cityUrl}?province_id=${provinceId}`)
        .then((res) => res.json())
        .then((data) => {
          citySelect.innerHTML = '<option value="">Pilih Kota</option>';
          data.cities.forEach((city) => {
            const opt = document.createElement("option");
            opt.value = city.id;
            opt.textContent = city.name;
            citySelect.appendChild(opt);
          });
        })
        .catch(() => {
          citySelect.innerHTML = '<option value="">Gagal memuat kota</option>';
        });
    });
  });
});
