# Evaluación heurística de Martínez Jiménez William Fernando

Cuenta: @william-martinez5101. Fecha: 13/11/2026.

Escala: 0 sin problema; 1 cosmético; 2 menor; 3 mayor; 4 impeditivo. La comparación con usuarios se realiza después de la inspección individual. La revisión editorial conserva resultado y severidad; la correspondencia original se encuentra en Datos/trazabilidad_redaccion_heuristica.csv.

## H1 Visibilidad del estado del sistema

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Edición del pedido / T4

**Observación:** El aumento de café no deja suficientemente claro, antes de guardar, qué cambios se conservarán al volver.

**Recomendación:** Incorporar un aviso de cambios pendientes junto a la acción de volver.

**Comparación posterior:** T4: P1 y P3 necesitaron pista; P2 corrigió el intento de volver.

## H2 Correspondencia con el mundo real

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú y revisión / T1, T3

**Observación:** Los nombres de los productos y sus precios resultan comprensibles; el total coincide con la suma.

**Recomendación:** Conservar los nombres cotidianos y los precios junto a los productos.

**Comparación posterior:** T1 y T3: 3/3 completaron sin pista.

## H3 Control y libertad del usuario

**Resultado:** Problema observado. **Severidad:** 3.

**Pantalla/tarea:** Edición y borrador / T5

**Observación:** Guardar después de quitar el sánduche modifica el estado solicitado y puede dificultar distinguir borrador de pedido guardado.

**Recomendación:** Diferenciar el borrador y ofrecer una acción clara para descartar los cambios.

**Comparación posterior:** T5: P1 guardó antes de detenerse; P2 y P3 conservaron el borrador.

## H4 Consistencia y estándares

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú, edición y resumen / T1–T6

**Observación:** Los nombres y los importes se mantienen al pasar del menú a la revisión del pedido.

**Recomendación:** Mantener las mismas etiquetas y el formato de moneda entre pantallas.

**Comparación posterior:** No se registraron errores de precios en las 18 tareas.

## H5 Prevención de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Controles de cantidad / T3, T5

**Observación:** Un toque adicional puede variar las unidades y obliga a corregirlas antes de continuar con el pedido.

**Recomendación:** Destacar la cantidad resultante y su subtotal al utilizar cada control.

**Comparación posterior:** P1 añadió un café extra en T3; P3 redujo el café a cero en T5.

## H6 Reconocer antes que recordar

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Resumen y comprobante / T3, T6

**Observación:** La revisión mantiene visibles los productos, las unidades y el total; el comprobante permite reconocer el pedido.

**Recomendación:** Conservar el resumen accesible antes de enviar el pedido.

**Comparación posterior:** T3 y T6: 3/3 completaron sin pista.

## H7 Flexibilidad y eficiencia

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda / T2

**Observación:** El filtro no recupera el catálogo completo si la consulta de té sigue activa en el buscador.

**Recomendación:** Ofrecer una acción visible que limpie la búsqueda y restablezca el catálogo.

**Comparación posterior:** T2: los tres probaron un filtro antes de limpiar; P1 requirió pista.

## H8 Diseño estético y minimalista

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Tarjetas de menú / T1

**Observación:** Las tarjetas distinguen el producto, su precio y la acción de añadir sin ocultar la oferta.

**Recomendación:** Conservar la jerarquía visual del menú y de sus tarjetas.

**Comparación posterior:** T1: tiempos 42, 24 y 31 s; éxito 3/3.

## H9 Reconocer, diagnosticar y recuperarse de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda sin coincidencias / T2

**Observación:** Se informa que no hay té, pero la búsqueda sin coincidencias necesita una orientación más directa para recuperar el catálogo.

**Recomendación:** Incluir «Sin resultados para té» y una acción para ver todos los productos.

**Comparación posterior:** T2: recuperación con pista en P1 y autónoma en P2 y P3.

## H10 Ayuda y documentación

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Ayuda en edición / T4, T5

**Observación:** No se explica junto al flujo de edición qué diferencia hay entre editar, guardar y confirmar el pedido.

**Recomendación:** Agregar ayuda breve junto a Guardar y Confirmar que explique sus efectos.

**Comparación posterior:** Las dudas se concentraron en guardado de T4 y punto de detención de T5.
