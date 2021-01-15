function loadPdf(ruta) {
  console.log(ruta);
  let embedAcuerdo = document.createElement("embed");
  embedAcuerdo.src = ruta;
  embedAcuerdo.style.minWidth = "100%";
  embedAcuerdo.style.height = "30em";

  let divAcuerdo = document.getElementById("acuerdo-div");
  divAcuerdo.innerHTML = "";
  divAcuerdo.appendChild(embedAcuerdo);
}
