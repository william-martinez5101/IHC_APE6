# Evaluación heurística de Gamboa Guaman Jonathan Alexis

Cuenta: @Jonathan305g. Fecha: 13/11/2026.

Escala: 0 sin problema; 1 cosmético; 2 menor; 3 mayor; 4 impeditivo. La comparación con usuarios se realiza después de la inspección individual. La revisión editorial conserva resultado y severidad; la correspondencia original se encuentra en Datos/trazabilidad_redaccion_heuristica.csv.

## H1 Visibilidad del estado del sistema

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Edición del pedido / T4

**Observación:** Después de variar la cantidad, falta una indicación persistente que diferencie la edición pendiente del pedido guardado.

**Recomendación:** Mantener el aviso de edición pendiente hasta completar el guardado.

**Comparación posterior:** T4: P1 y P3 necesitaron pista; P2 corrigió el intento de volver.

## H2 Correspondencia con el mundo real

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú y revisión / T1, T3

**Observación:** La relación entre producto, precio y total se expresa con un vocabulario reconocible en una cafetería.

**Recomendación:** Mantener la terminología y la relación visible entre producto e importe.

**Comparación posterior:** T1 y T3: 3/3 completaron sin pista.

## H3 Control y libertad del usuario

**Resultado:** Problema observado. **Severidad:** 3.

**Pantalla/tarea:** Edición y borrador / T5

**Observación:** La eliminación del producto necesita una distinción más clara entre los cambios provisionales y los que ya se conservaron.

**Recomendación:** Mostrar con claridad cuándo el cambio es provisional y cómo se descarta.

**Comparación posterior:** T5: P1 guardó antes de detenerse; P2 y P3 conservaron el borrador.

## H4 Consistencia y estándares

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú, edición y resumen / T1–T6

**Observación:** Las etiquetas de los productos y sus precios mantienen el mismo significado en los recorridos revisados.

**Recomendación:** Reutilizar las etiquetas y el formato monetario en las pantallas del pedido.

**Comparación posterior:** No se registraron errores de precios en las 18 tareas.

## H5 Prevención de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Controles de cantidad / T3, T5

**Observación:** Un cambio accidental en las unidades puede pasar a la selección y requerir su posterior corrección.

**Recomendación:** Resaltar la actualización de la cantidad y el subtotal para facilitar su comprobación.

**Comparación posterior:** P1 añadió un café extra en T3; P3 redujo el café a cero en T5.

## H6 Reconocer antes que recordar

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Resumen y comprobante / T3, T6

**Observación:** La selección y su importe quedan expuestos en revisión y el número del pedido aparece en el comprobante.

**Recomendación:** Mantener un resumen claro antes de confirmar y en la recepción del pedido.

**Comparación posterior:** T3 y T6: 3/3 completaron sin pista.

## H7 Flexibilidad y eficiencia

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda / T2

**Observación:** El texto del buscador sigue condicionando la oferta después de cambiar de filtro y dificulta restablecerla.

**Recomendación:** Facilitar un retorno directo al catálogo completo desde el buscador.

**Comparación posterior:** T2: los tres probaron un filtro antes de limpiar; P1 requirió pista.

## H8 Diseño estético y minimalista

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Tarjetas de menú / T1

**Observación:** Nombre, importe y acción de selección se distinguen en las tarjetas del catálogo.

**Recomendación:** Mantener una composición centrada en producto, precio y acción disponible.

**Comparación posterior:** T1: tiempos 42, 24 y 31 s; éxito 3/3.

## H9 Reconocer, diagnosticar y recuperarse de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda sin coincidencias / T2

**Observación:** El estado sin coincidencias comunica la ausencia del producto, pero ofrece poca orientación para regresar al menú completo.

**Recomendación:** Añadir al aviso una acción directa para restablecer todos los productos.

**Comparación posterior:** T2: recuperación con pista en P1 y autónoma en P2 y P3.

## H10 Ayuda y documentación

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Ayuda en edición / T4, T5

**Observación:** Las acciones de edición necesitan una explicación breve que permita diferenciar guardado y confirmación.

**Recomendación:** Dar orientación contextual que diferencie editar, guardar y confirmar.

**Comparación posterior:** Las dudas se concentraron en guardado de T4 y punto de detención de T5.
