function showModalTexto(texto) { 
  let pTexto = document.getElementById("p-texto");
  pTexto.innerText = texto;
  $("#modal-texto").modal("toggle");
}

function showModalTextoEditor(texto) { 
  document.getElementById("texto-editor").innerHTML = texto;
  $("#modal-texto2").modal("toggle");
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

function showModalCuestionario(texto) {
 // let pTexto = document.getElementById("p-cuestionario");
  //pTexto.innerText = texto;
  $("#modal-cuestionario").modal("toggle");
}
//modal video
function showModalVideo(ruta,poster) {
  let videoModalBody = document.getElementById("video-modal-body");
  let elemVideo = document.createElement("video");
  elemVideo.src = ruta;
  elemVideo.poster=poster;
  elemVideo.width=510;
  elemVideo.height=310; 
  elemVideo.controls=true;
  elemVideo.id = "video-modal";
  videoModalBody.innerHTML ="";
  videoModalBody.appendChild(elemVideo);
  $("#modal-video").modal("toggle");
}

function showModalYoutube(ruta) {
  let videoModalBody = document.getElementById("youtube-modal-body");
  let elemVideo = document.createElement("iframe");
  elemVideo.src =ruta;
  elemVideo.width=510;
  elemVideo.height=315; 
  elemVideo.frameborder=0;
  elemVideo.title="YouTube video player";
  elemVideo.allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  elemVideo.allowfullscreen;
  elemVideo.id = "youtube-modal";
  videoModalBody.innerHTML ="";
  videoModalBody.appendChild(elemVideo);
  $("#modal-youtube").modal("toggle");
}
