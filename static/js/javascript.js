document.getElementById("asal-prov").addEventListener("change", function () {
  const provinceId = this.value;
  const citySelect = document.getElementById("asal-city");

  // reset kota
  citySelect.innerHTML = '<option value="">Loading...</option>';

  if (!provinceId) {
    citySelect.innerHTML = '<option value="">Pilih Kota</option>';
    return;
  }

  fetch(`/ajax/cities/?province_id=${provinceId}`)
    .then((response) => response.json())
    .then((data) => {
      citySelect.innerHTML = '<option value="">Pilih Kota</option>';

      data.cities.forEach((city) => {
        const option = document.createElement("option");
        option.value = city.id;
        option.textContent = `${city.type} ${city.name}`;
        citySelect.appendChild(option);
      });
    })
    .catch((error) => {
      console.error(error);
      citySelect.innerHTML = '<option value="">Gagal memuat kota</option>';
    });
});
