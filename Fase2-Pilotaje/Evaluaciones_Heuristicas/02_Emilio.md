# Evaluación heurística de Abril Lara Emilio Alexander

Cuenta: @EMILIOABRIL05. Fecha: 13/11/2026.

Escala: 0 sin problema; 1 cosmético; 2 menor; 3 mayor; 4 impeditivo. La comparación con usuarios se realiza después de la inspección individual. La revisión editorial conserva resultado y severidad; la correspondencia original se encuentra en Datos/trazabilidad_redaccion_heuristica.csv.

## H1 Visibilidad del estado del sistema

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Edición del pedido / T4

**Observación:** La edición requiere una señal más inequívoca de que el nuevo número de cafés aún está pendiente de guardado.

**Recomendación:** Resaltar «Cambios sin guardar» hasta que se conserve la edición.

**Comparación posterior:** T4: P1 y P3 necesitaron pista; P2 corrigió el intento de volver.

## H2 Correspondencia con el mundo real

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú y revisión / T1, T3

**Observación:** La terminología cotidiana del menú permite reconocer el café y el sánduche y relacionarlos con sus precios.

**Recomendación:** Mantener el lenguaje habitual de cafetería en menú y revisión.

**Comparación posterior:** T1 y T3: 3/3 completaron sin pista.

## H3 Control y libertad del usuario

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Edición y borrador / T5

**Observación:** La retirada del sánduche deja un borrador cuya diferencia con el pedido ya guardado no resulta suficientemente evidente.

**Recomendación:** Separar visualmente la edición temporal del pedido que ya está guardado.

**Comparación posterior:** T5: P1 guardó antes de detenerse; P2 y P3 conservaron el borrador.

## H4 Consistencia y estándares

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Menú, edición y resumen / T1–T6

**Observación:** Las pantallas consultadas conservan las denominaciones de productos y el formato de sus precios.

**Recomendación:** Conservar la denominación de cada producto durante todo el recorrido.

**Comparación posterior:** No se registraron errores de precios en las 18 tareas.

## H5 Prevención de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Controles de cantidad / T3, T5

**Observación:** El control de cantidad admite cambios accidentales que deben detectarse y corregirse durante la revisión.

**Recomendación:** Hacer perceptible de inmediato el efecto de aumentar o reducir unidades.

**Comparación posterior:** P1 añadió un café extra en T3; P3 redujo el café a cero en T5.

## H6 Reconocer antes que recordar

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Resumen y comprobante / T3, T6

**Observación:** La información necesaria para verificar el pedido permanece disponible antes del envío y en el comprobante.

**Recomendación:** Mantener los datos de revisión visibles para comprobar la selección.

**Comparación posterior:** T3 y T6: 3/3 completaron sin pista.

## H7 Flexibilidad y eficiencia

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda / T2

**Observación:** Cambiar el filtro mientras se conserva el texto de búsqueda no restablece por sí solo la oferta.

**Recomendación:** Añadir un acceso para recuperar toda la oferta desde la búsqueda activa.

**Comparación posterior:** T2: los tres probaron un filtro antes de limpiar; P1 requirió pista.

## H8 Diseño estético y minimalista

**Resultado:** Sin problema observado. **Severidad:** 0.

**Pantalla/tarea:** Tarjetas de menú / T1

**Observación:** La jerarquía del menú permite localizar el nombre y el precio sin interferencias de contenido accesorio.

**Recomendación:** Mantener la distinción actual entre nombre, precio y selección.

**Comparación posterior:** T1: tiempos 42, 24 y 31 s; éxito 3/3.

## H9 Reconocer, diagnosticar y recuperarse de errores

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Búsqueda sin coincidencias / T2

**Observación:** El mensaje de búsqueda sin resultados no proporciona un acceso directo para volver a la oferta completa.

**Recomendación:** Situar una acción de limpieza de consulta dentro del mensaje sin resultados.

**Comparación posterior:** T2: recuperación con pista en P1 y autónoma en P2 y P3.

## H10 Ayuda y documentación

**Resultado:** Problema observado. **Severidad:** 2.

**Pantalla/tarea:** Ayuda en edición / T4, T5

**Observación:** La ayuda contextual no aclara suficientemente el efecto de guardar frente a continuar o confirmar.

**Recomendación:** Explicar localmente qué conserva cada acción antes de salir de edición.

**Comparación posterior:** Las dudas se concentraron en guardado de T4 y punto de detención de T5.
