# Guía de evaluación heurística de CaféU

## I04 Heurísticas H1 a H5

Responsable: Gamboa Guaman Jonathan Alexis. Evaluadores E1 William, E2 Emilio, E3 Pablo, E4 Manuel y E5 Jonathan. Inspección independiente, sin listas compartidas antes de concluir.

## H1 Visibilidad del estado del sistema

Comprobación: Revisar feedback de agregado, contador de unidades, cambios sin guardar, guardado, envío y Recibido.

Criterio: El usuario distingue borrador, pedido guardado y comprobante.

## H2 Correspondencia con el mundo real

Comprobación: Revisar nombres, dólares, unidades, cantidad por precio y significado de Recibido.

Criterio: Lenguaje familiar e importes comprensibles; no equiparar recepción con preparación terminada.

## H3 Control y libertad

Comprobación: Revisar retorno al menú, cancelar eliminación, descartar edición y empezar otro pedido.

Criterio: Una salida no borra datos guardados sin informar sus consecuencias.

## H4 Consistencia y estándares

Comprobación: Comparar etiquetas, posiciones y aspecto de acciones equivalentes en P1 a P6.

Criterio: Mismas palabras y comportamientos para acciones equivalentes; contexto Borrador explícito.

## H5 Prevención de errores

Comprobación: Revisar cero, campo vacío, pedido vacío y confirmación de eliminación.

Criterio: No se guarda una cantidad inválida ni se confirma una selección vacía.

## I04 Heurísticas H6 a H10

Responsable: Gamboa Guaman Jonathan Alexis. Evaluadores E1 William, E2 Emilio, E3 Pablo, E4 Manuel y E5 Jonathan. Inspección independiente, sin listas compartidas antes de concluir.

## H6 Reconocer antes que recordar

Comprobación: Revisar nombres, precios unitarios, cantidades, importes y total mientras se edita.

Criterio: No se exige memorizar el pedido para comprobar el cambio.

## H7 Flexibilidad y eficiencia de uso

Comprobación: Revisar búsqueda, filtros y posibilidad de volver a editar sin perder el contexto.

Criterio: Se encuentran productos y se recupera el catálogo; no se presupone que Figma implemente teclado web nativo.

## H8 Diseño estético y minimalista

Comprobación: Examinar legibilidad, jerarquía del total, avisos y densidad de P2 a P6.

Criterio: La información necesaria para decidir se distingue sin ruido ni texto ilegible.

## H9 Reconocimiento y recuperación de errores

Comprobación: Revisar cantidad inválida, búsqueda sin coincidencias y fallo de envío con selección conservada.

Criterio: Cada aviso explica qué ocurrió y ofrece una recuperación; la causa se clasifica sin culpar al usuario.

## H10 Ayuda y documentación

Comprobación: Revisar explicación de guardado manual, regla de cantidad y conservación del número.

Criterio: La ayuda acompaña la tarea; no se inventan horarios, pagos ni condiciones de retiro no documentados.

## Registro de hallazgo

| Campo | Regla |
| --- | --- |
| Identificador | E1-H01 y así sucesivamente; conservar origen al consolidar. |
| Versión y ubicación | CaféU, página y estado de referencia; anotar si es Figma en vivo o captura. |
| Reproducción | Estado inicial, acciones y efecto observado; no confundir interacción prevista con ejecutada. |
| Heurística | H1 a H10, con explicación. |
| Severidad individual | 0 sin problema; 1 cosmético; 2 menor; 3 mayor; 4 bloqueante. |
| Fundamento | Frecuencia estimada u observada, impacto y persistencia. |
| Evidencia | Captura sin datos privados o descripción reproducible. |
| Recomendación | Cambio medible relacionado con la dificultad. |

Cada evaluador dedica 10 minutos de exploración y 10 con la lista. Si un criterio no se puede ejecutar por límites del prototipo, anotar esa limitación; no marcarlo automáticamente conforme. No se exige que un prototipo de Figma implemente semántica HTML o anuncios de lector de pantalla.

La consolidación posterior conserva severidades individuales y justifica la final. La triangulación de Fase 2 añade tarea, evidencia, n/N y comentario anónimo. No extrapolar resultados antiguos de APE 4 ni del repositorio G5 a estos tres participantes.
