# Criterios técnicos verificables

| Criterio | Componente, cambio y aceptación | Hallazgo | Respaldo |
| --- | --- | --- | --- |
| C-01 | Buscador: Mostrar todos vacía consulta y filtros y muestra los 2 productos en una acción, sin alterar el pedido. | H-01 | Nielsen H3 y H7; ISO 9241-11: eficacia y eficiencia. |
| C-02 | Revisión: después de guardar se muestra confirmación visible y 2 cafés, 1 sánduche y $5,75; volver a abrir conserva esos datos. | H-02 | Nielsen H1; ISO 9241-11: eficacia y eficiencia. |
| C-03 | Edición: al quitar el sánduche se indica borrador de 1 café por $1,50; el guardado original sigue en $4,25 hasta Guardar cambios. Descartar restaura el original. | H-03 | Nielsen H1, H3 y H6; ISO 9241-11: eficacia. |
| C-04 | Línea de producto: separar visualmente Retirar de +/−; al activar Retirar no cambia la cantidad de otra línea; total y cantidad se actualizan juntos. | H-04 | Nielsen H5; ISO 9241-11: eficacia. |
| C-05 | Comprobante: junto a CU-104 se muestra Recibido y Recibimos tu pedido; te avisaremos cuando esté listo, diferenciando ambos estados. | H-05 | Nielsen H1 y H2; ISO 9241-11: eficiencia. |
| C-06 | Modal: identificar el producto; Conservar sánduche mantiene las 2 líneas y $4,25; Retirar sánduche solo afecta esa línea tras confirmación. | H-06 | Nielsen H3 y H5. |
| C-07 | Estado vacío: mostrar la consulta activa, indicar que no hay coincidencias y ofrecer una salida directa al catálogo sin perder el pedido. | H-07 | Nielsen H9 y H10. |
| C-08 | Inicio de pedido: al elegir Nuevo pedido se muestra ese título y contador 0; CU-104 queda identificado como comprobante anterior y no integra la selección actual. | H-08 | Nielsen H1 y H8; ISO 9241-11: eficacia. |
| C-09 | Navegación: la misma etiqueta produce el mismo efecto sobre los cambios en todas las pantallas; cada salida informa si guarda, descarta o conserva. | H-09 | Nielsen H4. |
| C-10 | Ayuda contextual: junto a editar, guardar y enviar se explica el efecto de cada acción; la ayuda puede consultarse sin perder el borrador. | H-10 | Nielsen H10. |

## Procedimiento de verificación del futuro cambio

Para cada criterio documentar versión, estado inicial, acción, resultado esperado y resultado observado. Los importes y estados deben comprobarse en el prototipo interactivo; un cambio de texto en el informe no implementa la mejora. La actividad solicita backlog de mejoras y criterios de aceptación; no se declara que estas diez mejoras ya estén desarrolladas.

ISO 9241-11 es un marco de evaluación en contexto. No impone los tiempos de las siete tareas ni SUS=68 como requisito universal. El respaldo Nielsen identifica el principio de interacción relacionado. Los criterios del Excel no constituyen una auditoría de WCAG ni verifican semántica HTML mediante Figma.

Los códigos definitivos C-01 a C-10 siguen el consenso del Excel recibido. En el ZIP preparatorio C-01 correspondía a borrador y C-03 a búsqueda; el consenso definitivo asigna C-01 a búsqueda y C-03 a borrador. Todas las referencias de esta entrega usan la codificación definitiva, sin modificar el archivo histórico preparatorio.
