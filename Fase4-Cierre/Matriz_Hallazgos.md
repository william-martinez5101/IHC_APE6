# Matriz consolidada de hallazgos de F3 y cierre F4

Consenso registrado el 18/11/2026. Se conservan diez problemas únicos y las valoraciones individuales; no se fuerza un problema en cada nivel de severidad o prioridad.

| Hallazgo | Problema | Tarea | Severidad acordada | Prioridad | Triangulación | Criterio |
| --- | --- | --- | --- | --- | --- | --- |
| H-01 | Recuperación del catálogo tras una búsqueda sin resultados | T2 | 3 | P1 | Confirmado por ambos métodos | C-01 |
| H-02 | Cambios pendientes y conservación del pedido al volver | T4 | 3 | P1 | Confirmado por ambos métodos | C-02 |
| H-03 | Separación entre borrador, guardado y cancelación de cambios | T5; T7 | 3 | P1 | Confirmado por ambos métodos | C-03 |
| H-04 | Cambios involuntarios en la cantidad de productos | T3; T5 | 2 | P2 | Confirmado por ambos métodos | C-04 |
| H-05 | Localización del estado de recepción del pedido | T6 | 2 | P3 | Confirmado por ambos métodos | C-05 |
| H-06 | Alcance poco explícito de Cancelar en la retirada de productos | T7 | 2 | P2 | Confirmado por ambos métodos | C-06 |
| H-07 | Mensaje de búsqueda vacía sin orientación para recuperarse | T2 | 2 | P2 | Confirmado por ambos métodos | C-07 |
| H-08 | Comprobante anterior y nueva selección poco diferenciados | T6 | 2 | P2 | Confirmado por ambos métodos | C-08 |
| H-09 | Etiquetas de salida inconsistentes entre edición y confirmación | T4; T5; T7 | 2 | P3 | Solo heurística | C-09 |
| H-10 | Falta de ayuda contextual sobre editar y guardar | T3; T4; T5 | 2 | P3 | Solo heurística | C-10 |

## H-01. Recuperación del catálogo tras una búsqueda sin resultados

**Frecuencia y alcance:** 3/3 con desvío; 2/3 necesitaron pista. Mediana 64 s frente a meta 45 s.

**Impacto:** Solo 1/3 completó T2 sin ayuda; dos personas necesitaron una pista neutral.

**Persistencia y límite:** El obstáculo permanece con la consulta activa. No se midió aprendizaje entre sesiones.

**Evidencia empírica:** P1/T2 (fila 7): 78 s y pista; P2/T2 (14): 39 s, recuperación autónoma; P3/T2 (21): 64 s y pista. 3/3 tuvieron un desvío.

**Evidencia analítica original:** Heuristicas!12; Heuristicas!22; Heuristicas!32; Heuristicas!42; Heuristicas!52

**Valoraciones individuales:** William Martínez: 3; Emilio Abril: 3; Pablo Lozada: 2; Manuel Cusme: 3; Jonathan Gamboa: 3.

**Decisión:** severidad 3, prioridad P1. Se acordó 3 por bloquear la recuperación autónoma en dos casos, aunque existe una salida al borrar la consulta.

**Criterio:** C-01. Buscador: Mostrar todos vacía consulta y filtros y muestra los 2 productos en una acción, sin alterar el pedido.

**Respaldo:** Nielsen H3 y H7; ISO 9241-11: eficacia y eficiencia.

**Origen del acuerdo:** Consenso!A6:X6.

## H-02. Cambios pendientes y conservación del pedido al volver

**Frecuencia y alcance:** 2/3 con duda de guardado; 1/3 necesitó pista. Mediana 112 s frente a meta 90 s.

**Impacto:** Aumentó la comprobación y una persona no terminó de forma autónoma.

**Persistencia y límite:** La señal continúa ausente al repetir el recorrido. No se midió retención posterior.

**Evidencia empírica:** P1/T4 (fila 9): pista y 138 s; P3/T4 (23): reabrió edición y 112 s. P2/T4 (16): sin error, 71 s.

**Evidencia analítica original:** Heuristicas!6; Heuristicas!16; Heuristicas!26; Heuristicas!36; Heuristicas!46

**Valoraciones individuales:** William Martínez: 3; Emilio Abril: 3; Pablo Lozada: 3; Manuel Cusme: 3; Jonathan Gamboa: 2.

**Decisión:** severidad 3, prioridad P1. Se acordó 3 porque la falta de confirmación compromete la comprensión del estado guardado y produjo ayuda en T4.

**Criterio:** C-02. Revisión: después de guardar se muestra confirmación visible y 2 cafés, 1 sánduche y $5,75; volver a abrir conserva esos datos.

**Respaldo:** Nielsen H1; ISO 9241-11: eficacia y eficiencia.

**Origen del acuerdo:** Consenso!A7:X7.

## H-03. Separación entre borrador, guardado y cancelación de cambios

**Frecuencia y alcance:** 1/3 terminó T5 en un estado incorrecto. En T7 no hubo eliminación consumada por error.

**Impacto:** Un intento de T5 incumplió el estado exigido aunque productos y total coincidieran.

**Persistencia y límite:** La distinción sigue dependiendo de recordar acciones anteriores. Sin seguimiento longitudinal.

**Evidencia empírica:** P1/T5 (fila 10): guardó antes del punto pedido; resultado No, 1 error crítico. P2/T5 (17) y P3/T5 (24) conservaron borrador. T7: 3/3 conservaron el pedido.

**Evidencia analítica original:** Heuristicas!8; Heuristicas!11; Heuristicas!18; Heuristicas!21; Heuristicas!28; Heuristicas!31; Heuristicas!38; Heuristicas!41; Heuristicas!48; Heuristicas!51

**Valoraciones individuales:** William Martínez: 3; Emilio Abril: 3; Pablo Lozada: 4; Manuel Cusme: 3; Jonathan Gamboa: 3.

**Decisión:** severidad 3, prioridad P1. Se acordó 3: hubo un fracaso de estado, pero no pérdida irreversible ni bloqueo de todo el sistema que justificara 4.

**Criterio:** C-03. Edición: al quitar el sánduche se indica borrador de 1 café por $1,50; el guardado original sigue en $4,25 hasta Guardar cambios. Descartar restaura el original.

**Respaldo:** Nielsen H1, H3 y H6; ISO 9241-11: eficacia.

**Origen del acuerdo:** Consenso!A8:X8.

## H-04. Cambios involuntarios en la cantidad de productos

**Frecuencia y alcance:** 2/6 intentos de T3 y T5 tuvieron un cambio involuntario: P1/T3 y P3/T5.

**Impacto:** Dos errores no críticos, corregidos sin pista antes del cierre.

**Persistencia y límite:** La proximidad permanece durante la edición; no se midió recurrencia posterior al aprendizaje.

**Evidencia empírica:** P1/T3 (fila 8): café extra corregido. P3/T5 (24): incremento accidental corregido. 2 personas afectadas.

**Evidencia analítica original:** Heuristicas!10; Heuristicas!20; Heuristicas!30; Heuristicas!40; Heuristicas!50

**Valoraciones individuales:** William Martínez: 2; Emilio Abril: 2; Pablo Lozada: 2; Manuel Cusme: 3; Jonathan Gamboa: 2.

**Decisión:** severidad 2, prioridad P2. Se acordó 2 por errores recuperables; se priorizó evitar cambios silenciosos del importe.

**Criterio:** C-04. Línea de producto: separar visualmente Retirar de +/−; al activar Retirar no cambia la cantidad de otra línea; total y cantidad se actualizan juntos.

**Respaldo:** Nielsen H5; ISO 9241-11: eficacia.

**Origen del acuerdo:** Consenso!A9:X9.

## H-05. Localización del estado de recepción del pedido

**Frecuencia y alcance:** 1/3 buscó en una zona equivocada; 3/3 explicó correctamente Recibido.

**Impacto:** Un desvío recuperable; ningún caso confundió Recibido con Listo para retirar.

**Persistencia y límite:** La jerarquía visual se mantiene en el comprobante. No se midieron consultas posteriores.

**Evidencia empírica:** P1/T6 (fila 11) buscó el estado en otra zona. P2/T6 (18) y P3/T6 (25) lo interpretaron sin error de significado.

**Evidencia analítica original:** Heuristicas!7; Heuristicas!17; Heuristicas!27; Heuristicas!37; Heuristicas!47; Heuristicas!56; Heuristicas!58; Heuristicas!60; Heuristicas!62; Heuristicas!64

**Valoraciones individuales:** William Martínez: 2; Emilio Abril: 2; Pablo Lozada: 2; Manuel Cusme: 2; Jonathan Gamboa: 1.

**Decisión:** severidad 2, prioridad P3. Se acordó 2 por la dificultad de localización observada; no hubo pérdida de comprensión final.

**Criterio:** C-05. Comprobante: junto a CU-104 se muestra Recibido y Recibimos tu pedido; te avisaremos cuando esté listo, diferenciando ambos estados.

**Respaldo:** Nielsen H1 y H2; ISO 9241-11: eficiencia.

**Origen del acuerdo:** Consenso!A10:X10.

## H-06. Alcance poco explícito de Cancelar en la retirada de productos

**Frecuencia y alcance:** 1/3 dudó del alcance; 3/3 conservó productos y total.

**Impacto:** Un error no crítico; no hubo pérdida de productos ni necesidad de pista.

**Persistencia y límite:** La ambigüedad verbal permanece en el modal; no se probó retención entre sesiones.

**Evidencia empírica:** P1/T7 (fila 12): cerró y reabrió el modal, 62 s y 1 desvío. P2/T7 (19) y P3/T7 (26): sin errores.

**Evidencia analítica original:** Heuristicas!57; Heuristicas!59; Heuristicas!61; Heuristicas!63; Heuristicas!65

**Valoraciones individuales:** William Martínez: 2; Emilio Abril: 2; Pablo Lozada: 1; Manuel Cusme: 2; Jonathan Gamboa: 2.

**Decisión:** severidad 2, prioridad P2. Se acordó 2 por confusión recuperable en una decisión destructiva; la cancelación funcionó en los tres intentos.

**Criterio:** C-06. Modal: identificar el producto; Conservar sánduche mantiene las 2 líneas y $4,25; Retirar sánduche solo afecta esa línea tras confirmación.

**Respaldo:** Nielsen H3 y H5.

**Origen del acuerdo:** Consenso!A11:X11.

## H-07. Mensaje de búsqueda vacía sin orientación para recuperarse

**Frecuencia y alcance:** 3/3 encontraron el vacío; 2/3 necesitaron una pista para recuperarse.

**Impacto:** La ausencia de orientación acompañó el bloqueo de dos casos; no se atribuye causalidad exclusiva al mensaje.

**Persistencia y límite:** El texto no cambia mientras persiste el estado vacío. No se midió aprendizaje posterior.

**Evidencia empírica:** P1/T2 (7) y P3/T2 (21): no identificaron cómo salir del vacío y recibieron pista. P2/T2 (14): recuperó borrando la consulta.

**Evidencia analítica original:** Heuristicas!14; Heuristicas!24; Heuristicas!34; Heuristicas!44; Heuristicas!54

**Valoraciones individuales:** William Martínez: 2; Emilio Abril: 2; Pablo Lozada: 2; Manuel Cusme: 2; Jonathan Gamboa: 2.

**Decisión:** severidad 2, prioridad P2. Se separó de H-01 porque este hallazgo afecta el mensaje y la orientación; H-01 afecta la acción de restablecer.

**Criterio:** C-07. Estado vacío: mostrar la consulta activa, indicar que no hay coincidencias y ofrecer una salida directa al catálogo sin perder el pedido.

**Respaldo:** Nielsen H9 y H10.

**Origen del acuerdo:** Consenso!A12:X12.

## H-08. Comprobante anterior y nueva selección poco diferenciados

**Frecuencia y alcance:** 1/3 confundió temporalmente el contexto; 3/3 terminó con selección 0.

**Impacto:** Un desvío recuperable; no se envió un pedido duplicado.

**Persistencia y límite:** No medida en uso repetido; la inspección cubrió un único ciclo de pedido.

**Evidencia empírica:** P3/T6 (fila 25): volvió al comprobante por duda; luego reconoció selección vacía. P1/T6 (11) y P2/T6 (18): nuevo pedido identificado.

**Evidencia analítica original:** Heuristicas!43

**Valoraciones individuales:** William Martínez: 2; Emilio Abril: 2; Pablo Lozada: 2; Manuel Cusme: 2; Jonathan Gamboa: 2.

**Decisión:** severidad 2, prioridad P2. Se acordó 2 por una duda de contexto con recuperación autónoma, distinta de localizar Recibido en H-05.

**Criterio:** C-08. Inicio de pedido: al elegir Nuevo pedido se muestra ese título y contador 0; CU-104 queda identificado como comprobante anterior y no integra la selección actual.

**Respaldo:** Nielsen H1 y H8; ISO 9241-11: eficacia.

**Origen del acuerdo:** Consenso!A13:X13.

## H-09. Etiquetas de salida inconsistentes entre edición y confirmación

**Frecuencia y alcance:** 5/5 inspecciones registraron la diferencia. En usuarios no se aisló su efecto.

**Impacto:** Riesgo de interpretación identificado analíticamente; sin error empírico atribuible de forma específica.

**Persistencia y límite:** No medida en uso repetido; discrepancia identificada en inspección del conjunto de recorridos.

**Evidencia empírica:** Sin evidencia de usuarios que aísle esta inconsistencia entre pantallas; N=3. No se imputa la causa de las dudas de T4 o T7 a este hallazgo.

**Evidencia analítica original:** Heuristicas!9; Heuristicas!19; Heuristicas!29; Heuristicas!39; Heuristicas!49

**Valoraciones individuales:** William Martínez: 2; Emilio Abril: 2; Pablo Lozada: 1; Manuel Cusme: 2; Jonathan Gamboa: 2.

**Decisión:** severidad 2, prioridad P3. Se acordó 2 por inconsistencia funcional. Se mantiene como Solo heurística hasta evaluar el efecto de las etiquetas.

**Criterio:** C-09. Navegación: la misma etiqueta produce el mismo efecto sobre los cambios en todas las pantallas; cada salida informa si guarda, descarta o conserva.

**Respaldo:** Nielsen H4.

**Origen del acuerdo:** Consenso!A14:X14.

## H-10. Falta de ayuda contextual sobre editar y guardar

**Frecuencia y alcance:** 5/5 inspecciones señalan ausencia de orientación contextual; sin frecuencia empírica atribuible.

**Impacto:** Riesgo de comprensión para el primer uso; no se contabiliza como error adicional de usuario.

**Persistencia y límite:** No medida; la inspección revisó la disponibilidad de ayuda, no su aprendizaje a largo plazo.

**Evidencia empírica:** Sin observación que permita aislar la falta de ayuda como causa de un error; N=3. Las dudas de guardado se registran en H-02 y H-03.

**Evidencia analítica original:** Heuristicas!15; Heuristicas!25; Heuristicas!35; Heuristicas!45; Heuristicas!55

**Valoraciones individuales:** William Martínez: 2; Emilio Abril: 2; Pablo Lozada: 2; Manuel Cusme: 2; Jonathan Gamboa: 1.

**Decisión:** severidad 2, prioridad P3. Se acordó 2 como apoyo al primer uso; se priorizan antes los cambios directos de estado y prevención de errores.

**Criterio:** C-10. Ayuda contextual: junto a editar, guardar y enviar se explica el efecto de cada acción; la ayuda puede consultarse sin perder el borrador.

**Respaldo:** Nielsen H10.

**Origen del acuerdo:** Consenso!A15:X15.

## Control de doble conteo

H-01 y H-07 describen, respectivamente, la acción para restablecer y la orientación del estado vacío; comparten los tres episodios de T2 y no se suman de nuevo como seis errores. H-02 trata confirmación del guardado, H-03 separación borrador/guardado y H-10 ayuda contextual. Sus límites y evidencias se distinguen sin inventar errores adicionales.
