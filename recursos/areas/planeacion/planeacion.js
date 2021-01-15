let planeacion1 = "/static/areas/planeacion.pdf";
let planeacion2 =
  "Es el programa mediante el cual se actualizan " +
  "y/o elaboran proyectos ejecutivos de construcción " +
  "de aulas, talleres, laboratorios y edificios " +
  "administrativos que se requieren para la operación " +
  "de los Colegios CECyTE.";

let planeacion3 =
  "Con el objetivo de dar seguimiento a los Programas " +
  "Anuales y así contar con la información correspondiente " +
  "a la Infraestructura Física y/o Equipamiento, se les " +
  "solicitara a los 30 Colegios la información cuantitativa, " +
  "la cual está respaldada de los indicadores en el Proyecto " +
  "No. 5 Fortalecimiento en Infraestructura y Equipamiento " +
  "reportados en su Programa Anual 2020, en reportes trimestrales.";

let planeacion4 =
  "Se les solicitara a los 30 Colegios el " +
  "Historial y el Crecimiento del 2018 y 2019, " +
  "en Infraestructura Física.";

let planeacion5 =
  "Se recibirá la documentación correspondiente por parte " +
  "de los Colegios, para cotejar los criterios y requisitos " +
  "para la creación o conversión de instituciones de " +
  "educación media superior, en la modalidad de organismos " +
  "descentralizados locales (ODES), así como para la creación de planteles.";

let textos = {
  2: planeacion2,
  3: planeacion3,
  4: planeacion4,
  5: planeacion5,
};
function openModal(id) {
  if ([1].includes(id)) showPdfModal(planeacion1);
  if ([2, 3, 4, 5].includes(id)) showModalTexto(textos[id]);
}
