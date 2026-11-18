# Matriz de siete tareas

T1–T6 conservan las consignas, respuestas y límites de Fase 1. T7 es nueva, con meta provisional fijada antes de medir: 45 s; máximo: 90 s. Las instrucciones al usuario se limitan al escenario. Los estados y respuestas son solo para el equipo.

## T1. Consulta de productos y precios

**Situación para leer:** Tienes cinco dólares para tu descanso. Averigua cuánto cuesta un café americano y un sánduche, e indica si te alcanza para comprar uno de cada uno.

**Inicio independiente:** Inicio, selección vacía; todavía no se ha enviado ningún pedido.

**Meta / máximo:** 30 / 60 s.

**Éxito:** Identifica ambos precios y responde que alcanza para las dos unidades.

**Respuesta de referencia:** Café americano $1,50; sánduche $2,75; total $4,25. Sí alcanza con $5,00; sobran $0,75.

**Estado final:** No necesita agregar productos; selección inicial vacía.

## T2. Búsqueda y recuperación del catálogo

**Situación para leer:** Hoy prefieres un té. Averigua si la cafetería lo ofrece. Si no lo encuentras, deja nuevamente visible la oferta completa para elegir otra cosa.

**Inicio independiente:** Menú completo, búsqueda vacía, filtro Todo, selección vacía.

**Meta / máximo:** 45 / 90 s.

**Éxito:** Comprueba la ausencia de té y restablece el catálogo completo sin ayuda.

**Respuesta de referencia:** La consulta té no tiene coincidencias; al recuperar el catálogo se ven 2 productos: café americano y sánduche.

**Estado final:** Menú completo con los 2 productos y selección vacía.

## T3. Preparación del pedido base

**Situación para leer:** Para tu descanso quieres un café americano y un sánduche. Prepara ese pedido sin enviarlo todavía, y di cuántas unidades contiene y cuánto cuesta.

**Inicio independiente:** Inicio con selección vacía y sin pedido enviado.

**Meta / máximo:** 90 / 180 s.

**Éxito:** Deja en revisión 1 café y 1 sánduche, sin confirmar, y comunica unidades y total.

**Respuesta de referencia:** 2 unidades en 2 líneas: 1 café americano por $1,50 y 1 sánduche por $2,75. Total $4,25.

**Estado final:** Pedido guardado de 2 unidades por $4,25, sin enviar.

## T4. Edición de cantidades y guardado

**Situación para leer:** Un compañero se une a tu descanso y también quiere café. Ajusta el pedido para que tenga dos cafés americanos y un sánduche, deja el cambio guardado sin enviarlo y comunica el nuevo total.

**Inicio independiente:** Pedido base guardado: 1 café y 1 sánduche, 2 unidades y $4,25. Preparación independiente de T3.

**Meta / máximo:** 90 / 180 s.

**Éxito:** Guarda 2 cafés y 1 sánduche, regresa a revisión y reconoce el total actualizado.

**Respuesta de referencia:** 3 unidades en 2 líneas. Café: 2 × $1,50 = $3,00; sánduche: 1 × $2,75 = $2,75. Total $5,75; se reconoce que los cambios quedaron guardados.

**Estado final:** Pedido modificado guardado: 3 unidades y $5,75, sin enviar.

## T5. Eliminación y control del borrador

**Situación para leer:** Partes de un pedido de un café americano y un sánduche. Ya no quieres el sánduche. Retíralo y, antes de guardar el cambio, indica qué queda y cuánto pagarías.

**Inicio independiente:** Pedido base guardado de 1 café y 1 sánduche por $4,25, preparado de nuevo e independiente de T4.

**Meta / máximo:** 60 / 120 s.

**Éxito:** Retira el sánduche del borrador, identifica el café restante y reconoce que el cambio aún no está guardado.

**Respuesta de referencia:** Borrador con 1 café americano, 1 unidad y $1,50. La edición mantiene cambios sin guardar; el pedido guardado original no se considera modificado todavía.

**Estado final:** Borrador de 1 café por $1,50, cambios sin guardar; no se exige guardarlo.

## T6. Confirmación y comienzo de otro pedido

**Situación para leer:** Tu pedido final será un café americano y un sánduche. Envíalo, indica el número y qué significa el estado que recibes. Después deja todo listo para empezar otro pedido sin productos seleccionados.

**Inicio independiente:** Pedido base guardado de 1 café y 1 sánduche por $4,25; primer envío del flujo, independiente de T4 y T5.

**Meta / máximo:** 90 / 180 s.

**Éxito:** Reconoce CU-104 recibido por $4,25 y luego inicia una nueva selección vacía.

**Respuesta de referencia:** Comprobante CU-104, estado Recibido, 2 unidades y $4,25. Recibido significa que la cafetería recibió el pedido, no que esté listo para retirar. La nueva selección queda con contador 0.

**Estado final:** Nuevo pedido vacío; el comprobante anterior queda diferenciado de la selección actual.

## T7. Cancelar una eliminación y conservar el pedido

**Situación para leer:** Tienes preparado un café americano y un sánduche. Empieza a retirar el sánduche, pero cambia de decisión cuando el sistema te pida confirmar. Conserva ambos productos y comprueba las cantidades y el total, sin enviar el pedido.

**Inicio independiente:** Pedido base guardado: 1 café y 1 sánduche, 2 unidades, $4,25, sin envío. Preparación independiente de T6.

**Meta / máximo:** 45 / 90 s.

**Éxito:** Abre la confirmación de eliminación del sánduche, cancela la retirada y conserva las dos líneas y sus cantidades. No envía ni guarda cambios inexistentes.

**Respuesta de referencia:** Siguen 1 café americano ($1,50) y 1 sánduche ($2,75), 2 unidades y total $4,25. No se elimina producto ni se crea un pedido nuevo.

**Estado final:** Pedido base intacto por $4,25; sin envío ni modificación del pedido guardado.

## Cobertura adicional

T2 ya probó búsqueda sin resultados; repetirla como refuerzo no ampliaría cobertura. T5 probó confirmar una retirada y detenerse antes de guardar. T7 comprueba la salida no destructiva desde la confirmación. Su aplicación del 18/11/2026 se registra en resultados/P1.md, P2.md y P3.md, y se resume en Resumen_Metricas.md. C16 documenta un modal y la opción Cancelar en un borrador de tres unidades; no se utiliza como evidencia del estado base de dos unidades de T7.
