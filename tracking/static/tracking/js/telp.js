const jne = document.getElementById("jne");
const telpWrapper = document.getElementById("telp-wrapper");
const courierRadios = document.querySelectorAll('input[name="courier"]');
const telpInput = document.getElementById("telp");

function toggleTelp() {
  if (jne.checked) {
    telpWrapper.style.display = "block";
  } else {
    telpWrapper.style.display = "none";
    telpInput.value = ""; // reset kalau bukan JNE
  }
}

// listen ke SEMUA radio
courierRadios.forEach((radio) => {
  radio.addEventListener("change", toggleTelp);
});

// handle reload page (misal pakai back / refresh)
toggleTelp();
