# Triangulación metodológica de F3

| ID | Evidencia usuarios | Evidencia heurística | Clasificación |
| --- | --- | --- | --- |
| H-01 | P1/T2 (fila 7): 78 s y pista; P2/T2 (14): 39 s, recuperación autónoma; P3/T2 (21): 64 s y pista. 3/3 tuvieron un desvío. | Heuristicas!A12:O12, Heuristicas!A22:O22, Heuristicas!A32:O32, Heuristicas!A42:O42, Heuristicas!A52:O52 | Confirmado por ambos métodos |
| H-02 | P1/T4 (fila 9): pista y 138 s; P3/T4 (23): reabrió edición y 112 s. P2/T4 (16): sin error, 71 s. | Heuristicas!A6:O6, Heuristicas!A16:O16, Heuristicas!A26:O26, Heuristicas!A36:O36, Heuristicas!A46:O46 | Confirmado por ambos métodos |
| H-03 | P1/T5 (fila 10): guardó antes del punto pedido; resultado No, 1 error crítico. P2/T5 (17) y P3/T5 (24) conservaron borrador. T7: 3/3 conservaron el pedido. | Heuristicas!A8:O8, Heuristicas!A11:O11, Heuristicas!A18:O18, Heuristicas!A21:O21, Heuristicas!A28:O28, Heuristicas!A31:O31, Heuristicas!A38:O38, Heuristicas!A41:O41, Heuristicas!A48:O48, Heuristicas!A51:O51 | Confirmado por ambos métodos |
| H-04 | P1/T3 (fila 8): café extra corregido. P3/T5 (24): incremento accidental corregido. 2 personas afectadas. | Heuristicas!A10:O10, Heuristicas!A20:O20, Heuristicas!A30:O30, Heuristicas!A40:O40, Heuristicas!A50:O50 | Confirmado por ambos métodos |
| H-05 | P1/T6 (fila 11) buscó el estado en otra zona. P2/T6 (18) y P3/T6 (25) lo interpretaron sin error de significado. | Heuristicas!A7:O7, Heuristicas!A17:O17, Heuristicas!A27:O27, Heuristicas!A37:O37, Heuristicas!A47:O47, Heuristicas!A56:O56, Heuristicas!A58:O58, Heuristicas!A60:O60, Heuristicas!A62:O62, Heuristicas!A64:O64 | Confirmado por ambos métodos |
| H-06 | P1/T7 (fila 12): cerró y reabrió el modal, 62 s y 1 desvío. P2/T7 (19) y P3/T7 (26): sin errores. | Heuristicas!A57:O57, Heuristicas!A59:O59, Heuristicas!A61:O61, Heuristicas!A63:O63, Heuristicas!A65:O65 | Confirmado por ambos métodos |
| H-07 | P1/T2 (7) y P3/T2 (21): no identificaron cómo salir del vacío y recibieron pista. P2/T2 (14): recuperó borrando la consulta. | Heuristicas!A14:O14, Heuristicas!A24:O24, Heuristicas!A34:O34, Heuristicas!A44:O44, Heuristicas!A54:O54 | Confirmado por ambos métodos |
| H-08 | P3/T6 (fila 25): volvió al comprobante por duda; luego reconoció selección vacía. P1/T6 (11) y P2/T6 (18): nuevo pedido identificado. | Heuristicas!A43:O43 | Confirmado por ambos métodos |
| H-09 | Sin evidencia de usuarios que aísle esta inconsistencia entre pantallas; N=3. No se imputa la causa de las dudas de T4 o T7 a este hallazgo. | Heuristicas!A9:O9, Heuristicas!A19:O19, Heuristicas!A29:O29, Heuristicas!A39:O39, Heuristicas!A49:O49 | Solo heurística |
| H-10 | Sin observación que permita aislar la falta de ayuda como causa de un error; N=3. Las dudas de guardado se registran en H-02 y H-03. | Heuristicas!A15:O15, Heuristicas!A25:O25, Heuristicas!A35:O35, Heuristicas!A45:O45, Heuristicas!A55:O55 | Solo heurística |

Balance: ocho hallazgos confirmados por ambos métodos, dos Solo heurística y ninguno Solo usuarios. La ausencia de una categoría no es una omisión: se conserva la clasificación documentada.

H-05 ahora dispone de inspecciones H1 específicas del comprobante, a diferencia del cruce histórico de F2. H-08 tiene evidencia analítica de Manuel en Heuristicas!A43:O43 y empírica de P3/T6. No se afirma que los cinco detectaron H-08 porque los cinco le asignaran severidad en el consenso.

H-09 y H-10 son riesgos analíticos: los registros no permiten aislar las etiquetas o la ausencia de ayuda como causa de un error. Se conservan como Solo heurística. En T7 se observó una duda recuperable, mientras la cancelación preservó los productos en tres de tres casos.
