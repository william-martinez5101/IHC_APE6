// Sin datos personales ni valores imputados.
(function(root){
  function calcularSUS(valores){
    if(valores.length!==10 || valores.some(v=>!Number.isInteger(v)||v<1||v>5))return null;
    return valores.reduce((s,v,i)=>s+(i%2===0?v-1:5-v),0)*2.5;
  }
  if(typeof module!=="undefined" && module.exports)module.exports={calcularSUS};
  else root.calcularSUS=calcularSUS;
})(typeof globalThis!=="undefined"?globalThis:this);
