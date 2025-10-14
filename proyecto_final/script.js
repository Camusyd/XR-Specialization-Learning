// script.js

// Solo manejamos el marcador
const marker = document.getElementById("markerMonalisa");

// Mensajes en consola cuando el marcador se detecta o se pierde
marker.addEventListener("markerFound", () => {
  console.log("Marcador detectado: Mona Lisa 🖼️");
});

marker.addEventListener("markerLost", () => {
  console.log("Marcador perdido ❌");
});

