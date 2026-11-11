// Casos de control aritmetico; no son respuestas de participantes.
const {calcularSUS}=require('../instrumentos/calculo_sus.js');
const casos=[
 ['SUS01','Extremo favorable', [5,1,5,1,5,1,5,1,5,1],100],
 ['SUS02','Extremo desfavorable',[1,5,1,5,1,5,1,5,1,5],0],
 ['SUS03','Patron de control',[4,2,4,2,4,2,4,2,4,2],75],
 ['SUS04','Diez respuestas neutras',[3,3,3,3,3,3,3,3,3,3],50],
 ['SUS05','Incompleto',[4,2],null],
 ['SUS06','Fuera de rango',[6,1,5,1,5,1,5,1,5,1],null],
 ['SUS07','Valor ausente',[null,1,5,1,5,1,5,1,5,1],null],
 ['SUS08','Respuesta fraccionaria',[4.5,1,5,1,5,1,5,1,5,1],null]
];
const resultados=casos.map(([id,descripcion,v,e])=>{const obtenido=calcularSUS(v);return{id,descripcion,esperado:e,obtenido,conforme:obtenido===e};});
console.log(JSON.stringify(resultados));
if(resultados.some(r=>!r.conforme))process.exitCode=1;
