function showModalTexto(texto) {
  let pTexto = document.getElementById("p-texto");
  pTexto.innerText = texto;
  $("#modal-texto").modal("toggle");
}

function showPdfModal(ruta) {
  let pdfModalBody = document.getElementById("pdf-modal-body");
  let pdfEmbed = document.createElement("embed");
  pdfEmbed.id = "pdf-modal";
  pdfEmbed.src = ruta;
  pdfEmbed.style.minWidth = "100%";
  pdfEmbed.style.height = "30em";

  pdfModalBody.innerHTML = "";
  pdfModalBody.appendChild(pdfEmbed);
  $("#modal-pdf").modal("toggle");
}

function showModalImagen(ruta) {
  let imagenModalBody = document.getElementById("imagen-modal-body");
  let imagenImg = document.createElement("img");
  imagenImg.id = "imagen-modal";
  imagenImg.src = ruta;
  imagenImg.className = "img-responsive";

  imagenModalBody.innerHTML = "";
  imagenModalBody.appendChild(imagenImg);
  $("#modal-imagen").modal("toggle");
}
