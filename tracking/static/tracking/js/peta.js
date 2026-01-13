// Koordinat contoh (bisa dummy / dari DB)
const origin = [-6.9175, 107.6191]; // Bandung
const destination = [-6.2088, 106.8456]; // Jakarta

const map = L.map("shipment-map", {
  zoomControl: false,
  attributionControl: false,
}).setView(origin, 7);

// Map polos (abu gelap)
L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png").addTo(map);

// Marker Origin
L.marker(origin).addTo(map).bindPopup("Origin");

// Marker Destination
L.marker(destination).addTo(map).bindPopup("Destination");

// Garis Jalur Pengiriman
L.polyline([origin, destination], {
  color: "#38bdf8",
  weight: 4,
  dashArray: "6 8",
}).addTo(map);
