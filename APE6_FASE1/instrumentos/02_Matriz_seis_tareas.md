# Matriz de seis tareas de CaféU

## I02 Tareas 1 y 2

Responsable: Abril Lara Emilio Alexander. Leer solo la consigna. No mostrar respuesta, controles de preparación ni ruta de solución.

## T1 Consulta de productos y precios

Consigna: Tienes cinco dólares para tu descanso. Averigua cuánto cuesta un café americano y un sánduche, e indica si te alcanza para comprar uno de cada uno.

| Campo | Definición |
| --- | --- |
| Objetivo y máximo | 30 s / 60 s |
| Estado inicial | Inicio, selección vacía; todavía no se ha enviado ningún pedido. |
| Éxito | Identifica ambos precios y responde que alcanza para las dos unidades. |
| Respuesta correcta | Café americano $1,50; sánduche $2,75; total $4,25. Sí alcanza con $5,00; sobran $0,75. |
| Evidencia de referencia | C02. No necesita agregar productos; selección inicial vacía. |

## T2 Búsqueda y recuperación del catálogo

Consigna: Hoy prefieres un té. Averigua si la cafetería lo ofrece. Si no lo encuentras, deja nuevamente visible la oferta completa para elegir otra cosa.

| Campo | Definición |
| --- | --- |
| Objetivo y máximo | 45 s / 90 s |
| Estado inicial | Menú completo, búsqueda vacía, filtro Todo, selección vacía. |
| Éxito | Comprueba la ausencia de té y restablece el catálogo completo sin ayuda. |
| Respuesta correcta | La consulta té no tiene coincidencias; al recuperar el catálogo se ven 2 productos: café americano y sánduche. |
| Evidencia de referencia | C02, C06. Menú completo con los 2 productos y selección vacía. |

## I02 Tareas 3 y 4

Responsable: Abril Lara Emilio Alexander. Leer solo la consigna. No mostrar respuesta, controles de preparación ni ruta de solución.

## T3 Preparación del pedido base

Consigna: Para tu descanso quieres un café americano y un sánduche. Prepara ese pedido sin enviarlo todavía, y di cuántas unidades contiene y cuánto cuesta.

| Campo | Definición |
| --- | --- |
| Objetivo y máximo | 90 s / 180 s |
| Estado inicial | Inicio con selección vacía y sin pedido enviado. |
| Éxito | Deja en revisión 1 café y 1 sánduche, sin confirmar, y comunica unidades y total. |
| Respuesta correcta | 2 unidades en 2 líneas: 1 café americano por $1,50 y 1 sánduche por $2,75. Total $4,25. |
| Evidencia de referencia | C12. Pedido guardado de 2 unidades por $4,25, sin enviar. |

## T4 Edición de cantidades y guardado

Consigna: Un compañero se une a tu descanso y también quiere café. Ajusta el pedido para que tenga dos cafés americanos y un sánduche, deja el cambio guardado sin enviarlo y comunica el nuevo total.

| Campo | Definición |
| --- | --- |
| Objetivo y máximo | 90 s / 180 s |
| Estado inicial | Pedido base guardado: 1 café y 1 sánduche, 2 unidades y $4,25. Preparación independiente de T3. |
| Éxito | Guarda 2 cafés y 1 sánduche, regresa a revisión y reconoce el total actualizado. |
| Respuesta correcta | 3 unidades en 2 líneas. Café: 2 × $1,50 = $3,00; sánduche: 1 × $2,75 = $2,75. Total $5,75; se reconoce que los cambios quedaron guardados. |
| Evidencia de referencia | C15, C21. Pedido modificado guardado: 3 unidades y $5,75, sin enviar. |

## I02 Tareas 5 y 6

Responsable: Abril Lara Emilio Alexander. Leer solo la consigna. No mostrar respuesta, controles de preparación ni ruta de solución.

## T5 Eliminación y control del borrador

Consigna: Partes de un pedido de un café americano y un sánduche. Ya no quieres el sánduche. Retíralo y, antes de guardar el cambio, indica qué queda y cuánto pagarías.

| Campo | Definición |
| --- | --- |
| Objetivo y máximo | 60 s / 120 s |
| Estado inicial | Pedido base guardado de 1 café y 1 sánduche por $4,25, preparado de nuevo e independiente de T4. |
| Éxito | Retira el sánduche del borrador, identifica el café restante y reconoce que el cambio aún no está guardado. |
| Respuesta correcta | Borrador con 1 café americano, 1 unidad y $1,50. La edición mantiene cambios sin guardar; el pedido guardado original no se considera modificado todavía. |
| Evidencia de referencia | C16, C17. Borrador de 1 café por $1,50, cambios sin guardar; no se exige guardarlo. |

## T6 Confirmación y comienzo de otro pedido

Consigna: Tu pedido final será un café americano y un sánduche. Envíalo, indica el número y qué significa el estado que recibes. Después deja todo listo para empezar otro pedido sin productos seleccionados.

| Campo | Definición |
| --- | --- |
| Objetivo y máximo | 90 s / 180 s |
| Estado inicial | Pedido base guardado de 1 café y 1 sánduche por $4,25; primer envío del flujo, independiente de T4 y T5. |
| Éxito | Reconoce CU-104 recibido por $4,25 y luego inicia una nueva selección vacía. |
| Respuesta correcta | Comprobante CU-104, estado Recibido, 2 unidades y $4,25. Recibido significa que la cafetería recibió el pedido, no que esté listo para retirar. La nueva selección queda con contador 0. |
| Evidencia de referencia | C25, C28. Nuevo pedido vacío; el comprobante anterior queda diferenciado de la selección actual. |
