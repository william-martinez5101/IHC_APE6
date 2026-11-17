# Evaluación heurística de Cusme Velez Manuel Steven

Cuenta: @ManuelCusme. Fecha: 13/11/2026.

Escala: 0 sin problema; 1 cosmético; 2 menor; 3 mayor; 4 impeditivo. La comparación con usuarios se realiza después de la inspección individual. La revisión editorial conserva resultado y severidad; la correspondencia original se encuentra en Datos/trazabilidad_redaccion_heuristica.csv.

## H1 Visibilidad del estado del sistema

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Edición del pedido / T4

**Observación:** El retorno desde la edición no comunica con claridad si el ajuste de cantidad se conserva antes de guardarlo.

**Recomendación:** Hacer visible el estado pendiente junto al retorno a revisión.

**Comparación posterior:** T4: P1 y P3 necesitaron pista; P2 corrigió el intento de volver.

## H2 Correspondencia con el mundo real

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú y revisión / T1, T3

**Observación:** Los productos están denominados de forma habitual y sus importes coinciden al revisar el pedido.

**Recomendación:** Continuar mostrando nombre y precio en las pantallas de selección.

**Comparación posterior:** T1 y T3: 3/3 completaron sin pista.

## H3 Control y libertad del usuario

**Resultado:** Problema observado. **Severidad:** 3.

**Pantalla/tarea:** Edición y borrador / T5

**Observación:** La edición temporal del pedido puede confundirse con su versión guardada al eliminar un producto.

**Recomendación:** Identificar el estado temporal y permitir descartar la modificación.

**Comparación posterior:** T5: P1 guardó antes de detenerse; P2 y P3 conservaron el borrador.

## H4 Consistencia y estándares

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú, edición y resumen / T1–T6

**Observación:** No se aprecia variación de nombres o precios al recorrer las pantallas de menú y pedido.

**Recomendación:** Mantener la consistencia actual de nombres e importes.

**Comparación posterior:** No se registraron errores de precios en las 18 tareas.

## H5 Prevención de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Controles de cantidad / T3, T5

**Observación:** La modificación involuntaria de una cantidad exige una acción correctiva antes de finalizar el pedido.

**Recomendación:** Mostrar de forma más visible las unidades y el importe después de cada cambio.

**Comparación posterior:** P1 añadió un café extra en T3; P3 redujo el café a cero en T5.

## H6 Reconocer antes que recordar

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Resumen y comprobante / T3, T6

**Observación:** El resumen reúne productos, cantidad y total, y la confirmación identifica el pedido enviado.

**Recomendación:** Sostener la disponibilidad del resumen y la identificación del comprobante.

**Comparación posterior:** T3 y T6: 3/3 completaron sin pista.

## H7 Flexibilidad y eficiencia

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda / T2

**Observación:** La búsqueda activa limita los resultados aunque se cambie el filtro, lo que añade pasos para volver al catálogo.

**Recomendación:** Permitir limpiar la consulta y volver a todos los productos con una acción clara.

**Comparación posterior:** T2: los tres probaron un filtro antes de limpiar; P1 requirió pista.

## H8 Diseño estético y minimalista

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Tarjetas de menú / T1

**Observación:** Los elementos principales de las tarjetas se reconocen sin que el contenido del menú oculte los precios.

**Recomendación:** Conservar la presentación que permite identificar la oferta y sus importes.

**Comparación posterior:** T1: tiempos 42, 24 y 31 s; éxito 3/3.

## H9 Reconocer, diagnosticar y recuperarse de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda sin coincidencias / T2

**Observación:** La búsqueda de un producto ausente requiere una indicación más clara sobre cómo restablecer los resultados.

**Recomendación:** Explicar cómo recuperar la oferta desde el estado de búsqueda vacía.

**Comparación posterior:** T2: recuperación con pista en P1 y autónoma en P2 y P3.

## H10 Ayuda y documentación

**Resultado:** Problema observado. **Severidad:** 1.

**Pantalla/tarea:** Ayuda en edición / T4, T5

**Observación:** No se encuentra una indicación cercana que explique la persistencia de los cambios al volver desde edición.

**Recomendación:** Incluir un texto breve sobre la necesidad de guardar antes de volver.

**Comparación posterior:** Las dudas se concentraron en guardado de T4 y punto de detención de T5.
