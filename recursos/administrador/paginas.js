let radios = document.getElementsByName("tipo_bloque");
let bloque_texto = document.getElementById("bloque-texto");
let bloque_imagen = document.getElementById("bloque-imagen");
let bloque_pdf = document.getElementById("bloque-pdf");

let ocultar_div = (e) => {
  bloque_texto.style.display = "none";
  bloque_imagen.style.display = "none";
  bloque_pdf.style.display = "none";
  if (e.target.value === "1") bloque_texto.style.display = "block";
  if (e.target.value === "2") bloque_pdf.style.display = "block";
  if (e.target.value === "3") bloque_imagen.style.display = "block";
};

for (let radio of radios) {
  radio.addEventListener("change", ocultar_div);
}
