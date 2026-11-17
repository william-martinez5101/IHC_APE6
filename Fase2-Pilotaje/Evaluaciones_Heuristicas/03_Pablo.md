# Evaluación heurística de Lozada Marcial Pablo Damian

Cuenta: @idk-Damian. Fecha: 13/11/2026.

Escala: 0 sin problema; 1 cosmético; 2 menor; 3 mayor; 4 impeditivo. La comparación con usuarios se realiza después de la inspección individual. La revisión editorial conserva resultado y severidad; la correspondencia original se encuentra en Datos/trazabilidad_redaccion_heuristica.csv.

## H1 Visibilidad del estado del sistema

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Edición del pedido / T4

**Observación:** Al cambiar la cantidad y tratar de regresar, resulta ambiguo si la edición ya quedó registrada.

**Recomendación:** Indicar antes de regresar que el ajuste de cantidad aún necesita guardarse.

**Comparación posterior:** T4: P1 y P3 necesitaron pista; P2 corrigió el intento de volver.

## H2 Correspondencia con el mundo real

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú y revisión / T1, T3

**Observación:** La revisión conserva nombres familiares y un total coherente con los precios de ambas tarjetas.

**Recomendación:** Preservar la correspondencia entre la tarjeta del producto y el total.

**Comparación posterior:** T1 y T3: 3/3 completaron sin pista.

## H3 Control y libertad del usuario

**Resultado:** Problema observado. **Severidad:** 3.

**Pantalla/tarea:** Edición y borrador / T5

**Observación:** El paso de una eliminación temporal a un cambio guardado exige distinguir dos estados que pueden confundirse.

**Recomendación:** Añadir una distinción visible entre conservar, descartar y mantener la edición.

**Comparación posterior:** T5: P1 guardó antes de detenerse; P2 y P3 conservaron el borrador.

## H4 Consistencia y estándares

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú, edición y resumen / T1–T6

**Observación:** La información de los productos es consistente entre el catálogo, la edición y la revisión.

**Recomendación:** Preservar el formato de precios al pasar de menú a edición y revisión.

**Comparación posterior:** No se registraron errores de precios en las 18 tareas.

## H5 Prevención de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Controles de cantidad / T3, T5

**Observación:** La variación de unidades no ofrece una confirmación visual lo bastante destacada para evitar un toque adicional.

**Recomendación:** Actualizar el subtotal junto a la cantidad y separar mejor los controles.

**Comparación posterior:** P1 añadió un café extra en T3; P3 redujo el café a cero en T5.

## H6 Reconocer antes que recordar

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Resumen y comprobante / T3, T6

**Observación:** Los datos de revisión se pueden consultar sin reconstruir de memoria la selección de productos.

**Recomendación:** Preservar la consulta de productos, unidades y total sin exigir memorizarlos.

**Comparación posterior:** T3 y T6: 3/3 completaron sin pista.

## H7 Flexibilidad y eficiencia

**Resultado:** Problema observado. **Severidad:** 1.

**Pantalla/tarea:** Búsqueda / T2

**Observación:** La recuperación de toda la oferta exige coordinar la limpieza de la consulta con el filtro del catálogo.

**Recomendación:** Unificar la recuperación del catálogo mediante una acción «Restablecer».

**Comparación posterior:** T2: los tres probaron un filtro antes de limpiar; P1 requirió pista.

## H8 Diseño estético y minimalista

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Tarjetas de menú / T1

**Observación:** El menú presenta la información relevante de cada producto de manera diferenciada.

**Recomendación:** Preservar el orden de la información principal de cada producto.

**Comparación posterior:** T1: tiempos 42, 24 y 31 s; éxito 3/3.

## H9 Reconocer, diagnosticar y recuperarse de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda sin coincidencias / T2

**Observación:** La ausencia de coincidencias se comunica, aunque el siguiente paso para recuperar todos los productos podría indicarse mejor.

**Recomendación:** Relacionar el aviso sin coincidencias con una salida visible hacia el catálogo.

**Comparación posterior:** T2: recuperación con pista en P1 y autónoma en P2 y P3.

## H10 Ayuda y documentación

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Ayuda en edición / T4, T5

**Observación:** El recorrido carece de una explicación local sobre el momento en que los cambios pasan a quedar guardados.

**Recomendación:** Aclarar junto a las acciones cuándo se guardan y cuándo se envían los cambios.

**Comparación posterior:** Las dudas se concentraron en guardado de T4 y punto de detención de T5.
