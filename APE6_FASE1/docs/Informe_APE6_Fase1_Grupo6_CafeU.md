# Planificación de la evaluación de usabilidad de CaféU

FACULTAD DE INGENIERÍA EN SISTEMAS, ELECTRÓNICA E INDUSTRIAL
CARRERA DE SOFTWARE
INFORME DE GUÍA PRÁCTICA DE APLICACIÓN Y EXPERIMENTACIÓN

## APE 6 Fase 1 Planificación de la evaluación de usabilidad

Prototipo CaféU del APE 4
Grupo 6 · Quinto semestre · Paralelo A
Ciclo académico julio a diciembre de 2026
Fecha 11 de noviembre de 2026 · Protocolo v2.0

## Integrantes

| Apellidos y nombres | Cuenta GitHub |
| --- | --- |
| Martínez Jiménez William Fernando | william-martinez5101 |
| Abril Lara Emilio Alexander | EMILIOABRIL05 |
| Lozada Marcial Pablo Damian | idk-Damian |
| Cusme Velez Manuel Steven | ManuelCusme |
| Gamboa Guaman Jonathan Alexis | Jonathan305g |

Docente: Ing. José Rubén Caiza Caizabuano, Mg.
Modalidad: trabajo grupal presencial
Tiempo de preparación: 2 horas
Valoración: 3,00 puntos

Se entrega el plan de evaluación del prototipo propio CaféU, desarrollado en el APE 4. Incluye dos métodos, perfiles de tres participantes externos, seis tareas con respuestas, métricas, consentimiento, roles, hoja de observación y SUS, y condiciones de validación. Esta Fase 1 diseña los instrumentos; su aplicación con usuarios pertenece a la Fase 2.

Repositorio de entrega: https://github.com/william-martinez5101/IHC_APE6

## 1 Datos generales

Práctica 6 de Interacción Humano Computador. Facultad de Ingeniería en Sistemas, Electrónica e Industrial; carrera de Software; quinto A; Unidad de Organización Curricular Profesional. Se desarrolla la secuencia del formulario UTA [5] en los apartados 2.1 a 2.12. Las 2 horas de esta entrega corresponden a la planificación; el APE general contempla 8 horas para el conjunto de fases.

## 2 Desarrollo de la guía APE

## 2.1 Tema

Evaluación y validación de interfaces. Planificación de la evaluación de usabilidad de CaféU.

## 2.2 Objetivos

Objetivo general: diseñar un protocolo reproducible para evaluar la usabilidad de CaféU con estudiantes universitarios ajenos a su desarrollo, combinando inspección heurística y pensamiento en voz alta, con tareas observables, métricas de eficacia, eficiencia y satisfacción y condiciones éticas que permitan organizar el pilotaje de la Fase 2.

- Caracterizar CaféU, sus usuarios y contexto, y definir la pregunta y los métodos de evaluación apropiados para sus seis pantallas.
- Diseñar seis situaciones de uso, reglas de medición y una hoja de observación con SUS que permitan registrar desempeño y percepción sin dirigir las acciones.
- Establecer criterios de selección, consentimiento, cinco roles y validación del protocolo, con distribución documental para la colaboración en GitHub.

## 2.3 Modalidad

Trabajo grupal presencial con cinco integrantes y preparación documental colaborativa.

## 2.4 Tiempo de duración

120 minutos: revisión del prototipo 15; pregunta y métodos 15; tareas 25; métricas e instrumentos 20; consentimiento y roles 15; revisión y organización 30.

## 2.5 Instrucciones aplicadas

Revisar guía y prototipo; formular criterios antes de recoger datos; definir instrumentos; comprobar consistencia; organizar aportes de los cinco integrantes.

## 2.6 Equipos materiales y recursos

Computador con navegador, Figma en modo Presentación, conexión a internet, ratón o panel táctil, cronómetro, documentos PDF y Word, formulario de registro local, Git, GitHub, aula virtual y bibliografía.

## 2.7 Actividades desarrolladas

## 2.7.1 Definición del prototipo y contexto

CaféU representa una cafetería universitaria. Permite consultar productos y precios, buscar y filtrar, seleccionar cantidades, revisar un pedido, editar un borrador y reconocer su recepción. El estudiante dispone de un descanso breve y necesita comprobar qué pidió, cuánto cuesta y si la cafetería recibió la orden.

| Pantalla | Finalidad |
| --- | --- |
| P1 Inicio | Acceso al catálogo y selección inicialmente vacía. |
| P2 Menú | Dos productos: café americano $1,50 y sánduche $2,75; búsqueda y categorías. |
| P3 Detalle | Cantidad, precio unitario, subtotal, recuperación de dato inválido y agregado. |
| P4 Revisión | Líneas, unidades, total, edición y confirmación. |
| P5 Edición | Borrador, cantidades, eliminación, guardado y descarte. |
| P6 Confirmación | Número, estado Recibido, detalle y nueva selección vacía. |

## Objeto y versión de referencia

Se evalúa el prototipo del APE 4 integral del Grupo 6 [7], enlazado en Figma [8]. La referencia documental queda fijada al commit 822fbbf4c1d4011c399e4753d85e6f3d2167ff34. El paquete conserva diez capturas de esa versión y sus fuentes. El catálogo de dos productos y los estados de edición son los del equipo, no los del ejemplo del Grupo 5.

La revisión directa de Figma no estuvo disponible con el acceso de esta sesión; se contrastaron recorridos y capturas del repositorio. Este informe no acredita una ejecución de sus transiciones. El pilotaje se aplicará al archivo de Figma en Presentación; las capturas sirven como referencia del instrumento, sin sustituir una interacción observada.

## Alcance

No se incluyen pago, autenticación, preparación terminada ni administración. El estado Recibido informa recepción y no que el pedido esté listo. El número CU-104 identifica el primer comprobante del escenario, no un cobro ni un pedido real.

## 2.7.2 Pregunta y fundamento de la evaluación

Pregunta: ¿en qué medida CaféU permite a estudiantes universitarios ajenos a su desarrollo consultar la oferta, preparar y modificar un pedido y reconocer su recepción con eficacia, eficiencia y satisfacción, y qué dificultades de la interfaz limitan esos objetivos?

ISO 9241-11 [1] relaciona usabilidad con usuarios, objetivos y contexto: eficacia en el resultado, eficiencia en los recursos empleados y satisfacción durante el uso. Aquí se miden éxito, duración, errores y percepción mediante SUS. La norma no impone esos instrumentos ni una nota mínima.

Verificar es comprobar que la representación y el comportamiento previsto cumplen sus reglas. Validar implica observar si usuarios concretos alcanzan sus objetivos. Un total correcto en una captura no demuestra que la persona entienda que la edición debe guardarse. La evaluación será formativa, orientada a encontrar mejoras, sin generalizar con tres participantes.

| Método | Procedimiento previsto | Aporte |
| --- | --- | --- |
| Evaluación heurística [2] | Los cinco integrantes revisan por separado P1 a P6, sus retornos y estados. Registran H1 a H10, reproducción y severidad. | Identifica posibles problemas y amplía cobertura. |
| Usuarios con pensamiento en voz alta | Tres personas externas realizan T1 a T6. Se leen las consignas, se cronometran intentos y se registran acciones y frases. | Contrasta impacto y recoge eficacia, eficiencia y satisfacción. |

## Inspección y consolidación

Cada evaluador: 10 minutos de recorrido libre y 10 minutos con la guía H1 a H10, sin consultar a los demás. Después se consolidan duplicados conservando los códigos individuales. Severidad: 0 sin problema; 1 cosmético; 2 menor; 3 mayor; 4 bloqueante. Justificar con frecuencia, impacto y persistencia, distinguiendo evidencia de hipótesis.

## Contraste posterior

En Fase 2 se relacionará cada hallazgo con tarea, evidencia, frecuencia n/N, heurística y recomendación. Se distinguirán hallazgos de ambos métodos, solo heurísticos y solo de usuarios; que una tarea termine bien no elimina las dudas o errores observados.

## 2.7.3 Participantes ética y roles

Se definen tres plazas de pilotaje P1, P2 y P3. Los perfiles siguientes son la selección prevista del plan; no representan personas reclutadas ni consentimientos ya obtenidos. Manuel coordinará el reclutamiento y William verificará los criterios antes de cada sesión.

| ID | Perfil de selección | Propósito |
| --- | --- | --- |
| P1 | Estudiante universitario de 18 años o más con poca experiencia en pedidos digitales. | Comprensión inicial de productos, importes y estado. |
| P2 | Estudiante universitario de 18 años o más que use habitualmente aplicaciones de pedidos. | Eficiencia del flujo de selección y modificación. |
| P3 | Estudiante universitario de 18 años o más con experiencia intermedia en aplicaciones de pedidos. | Reconocimiento del guardado y de la recepción. |

Inclusión: estudiantes universitarios de 18 años o más, comprensión de español y manejo básico de un dispositivo. Exclusión: integrantes o colaboradores del diseño, personas que conocen las consignas y quienes ya probaron esta misma versión. No se solicita nombre, matrícula, carrera exacta, edad precisa ni contacto en el registro público.

Invitación presencial neutral, sin incentivos ni consecuencias académicas. Si alguien no cumple o rechaza, se selecciona otra persona con el mismo perfil. El consentimiento se lee y se registra por código antes de iniciar. No se graba pantalla, voz ni rostro. La aceptación no se presume.

| Integrante | Responsabilidad de sesión |
| --- | --- |
| Martínez Jiménez William Fernando | Coordinación y revisión del protocolo |
| Abril Lara Emilio Alexander | Moderación |
| Lozada Marcial Pablo Damian | Registro de métricas |
| Cusme Velez Manuel Steven | Soporte técnico y consentimiento |
| Gamboa Guaman Jonathan Alexis | Observación |

Los cinco realizan también la revisión heurística independiente. Pablo es el único cronometrista; Jonathan registra frases sin interrumpir; Emilio no guía; Manuel prepara estados fuera de la vista del participante y solo interviene después de cerrar un intento; William coordina incidencias y versiones.

## Confidencialidad

Registros individuales y JSON en carpeta privada del equipo; acceso del equipo y docente. Eliminación 30 días después de la calificación. Publicación únicamente de instrumentos y agregados revisados sin identificadores. Participación, pausas, omisión de SUS y retiro son voluntarios; se atiende una solicitud de eliminación mediante el código antes de consolidar los datos.

## 2.7.4 Matriz de tareas

Leer solo la consigna, sin mostrar respuestas ni rutas. El máximo es el doble de la meta. Los tiempos son objetivos de planificación y no mediciones de personas. T4, T5 y T6 parten cada una de un pedido base preparado por soporte; no heredan los cambios de la anterior.

| ID | Objetivo | Máximo | Cobertura |
| --- | --- | --- | --- |
| T1 | 30 s | 60 s | Consulta de productos y precios |
| T2 | 45 s | 90 s | Búsqueda y recuperación del catálogo |
| T3 | 90 s | 180 s | Preparación del pedido base |
| T4 | 90 s | 180 s | Edición de cantidades y guardado |
| T5 | 60 s | 120 s | Eliminación y control del borrador |
| T6 | 90 s | 180 s | Confirmación y comienzo de otro pedido |

## T1 Consulta de productos y precios

Consigna: Tienes cinco dólares para tu descanso. Averigua cuánto cuesta un café americano y un sánduche, e indica si te alcanza para comprar uno de cada uno.

Inicio: Inicio, selección vacía; todavía no se ha enviado ningún pedido.

Éxito: Identifica ambos precios y responde que alcanza para las dos unidades.

Respuesta correcta: Café americano $1,50; sánduche $2,75; total $4,25. Sí alcanza con $5,00; sobran $0,75.

## T2 Búsqueda y recuperación del catálogo

Consigna: Hoy prefieres un té. Averigua si la cafetería lo ofrece. Si no lo encuentras, deja nuevamente visible la oferta completa para elegir otra cosa.

Inicio: Menú completo, búsqueda vacía, filtro Todo, selección vacía.

Éxito: Comprueba la ausencia de té y restablece el catálogo completo sin ayuda.

Respuesta correcta: La consulta té no tiene coincidencias; al recuperar el catálogo se ven 2 productos: café americano y sánduche.

## T3 Preparación del pedido base

Consigna: Para tu descanso quieres un café americano y un sánduche. Prepara ese pedido sin enviarlo todavía, y di cuántas unidades contiene y cuánto cuesta.

Inicio: Inicio con selección vacía y sin pedido enviado.

Éxito: Deja en revisión 1 café y 1 sánduche, sin confirmar, y comunica unidades y total.

Respuesta correcta: 2 unidades en 2 líneas: 1 café americano por $1,50 y 1 sánduche por $2,75. Total $4,25.

## Matriz de tareas continuación

## T4 Edición de cantidades y guardado

Consigna: Un compañero se une a tu descanso y también quiere café. Ajusta el pedido para que tenga dos cafés americanos y un sánduche, deja el cambio guardado sin enviarlo y comunica el nuevo total.

Meta 90 s; máximo 180 s.

Inicio: Pedido base guardado: 1 café y 1 sánduche, 2 unidades y $4,25. Preparación independiente de T3.

Éxito: Guarda 2 cafés y 1 sánduche, regresa a revisión y reconoce el total actualizado.

Respuesta correcta: 3 unidades en 2 líneas. Café: 2 × $1,50 = $3,00; sánduche: 1 × $2,75 = $2,75. Total $5,75; se reconoce que los cambios quedaron guardados.

## T5 Eliminación y control del borrador

Consigna: Partes de un pedido de un café americano y un sánduche. Ya no quieres el sánduche. Retíralo y, antes de guardar el cambio, indica qué queda y cuánto pagarías.

Meta 60 s; máximo 120 s.

Inicio: Pedido base guardado de 1 café y 1 sánduche por $4,25, preparado de nuevo e independiente de T4.

Éxito: Retira el sánduche del borrador, identifica el café restante y reconoce que el cambio aún no está guardado.

Respuesta correcta: Borrador con 1 café americano, 1 unidad y $1,50. La edición mantiene cambios sin guardar; el pedido guardado original no se considera modificado todavía.

## T6 Confirmación y comienzo de otro pedido

Consigna: Tu pedido final será un café americano y un sánduche. Envíalo, indica el número y qué significa el estado que recibes. Después deja todo listo para empezar otro pedido sin productos seleccionados.

Meta 90 s; máximo 180 s.

Inicio: Pedido base guardado de 1 café y 1 sánduche por $4,25; primer envío del flujo, independiente de T4 y T5.

Éxito: Reconoce CU-104 recibido por $4,25 y luego inicia una nueva selección vacía.

Respuesta correcta: Comprobante CU-104, estado Recibido, 2 unidades y $4,25. Recibido significa que la cafetería recibió el pedido, no que esté listo para retirar. La nueva selección queda con contador 0.

## 2.7.5 Reglas del protocolo y preparación

Orden fijo T1 a T6. Antes de T1, T2 y T3 se establece la selección vacía; para T2 se deja el menú completo. Antes de T4, T5 y T6 se prepara de forma independiente 1 café y 1 sánduche por $4,25. La preparación ocurre fuera de la vista del participante y antes de leer la consigna. Su duración no entra en el tiempo de tarea.

En T6 se restablece el escenario de primer envío, para que el número esperado sea CU-104. C25 (base) y C27 (modificado) del APE 4 son variantes alternativas, no dos envíos consecutivos. Esta prueba usa el comprobante base C25; no mezcla $5,75 con $4,25 en una misma confirmación.

Después de T5 se descarta el borrador y se prepara de nuevo el pedido base de T6. Si una tarea falla, primero se registra su resultado; soporte restablece el inicio de la siguiente sin convertir la intervención en éxito. Entre participantes se reinicia el flujo de Figma desde Inicio y se comprueba el contador 0. Recargar una página no se asume equivalente a reiniciar un flujo de Figma.

## Pista y moderación

Pista única: “Vuelve a leer la situación y revisa las opciones disponibles”. Se lee una sola vez cuando la persona la solicita o pasa 30 segundos sin avanzar. No se señala ni se nombran controles. Completar después de la pista se registra Con ayuda. Repetir literalmente la consigna se registra aparte; no es ayuda.

Si deja de verbalizar, recordar “Cuéntame qué estás pensando”, sin sugerir acciones. Si pide pausa, detener el cronómetro y registrar su duración aparte. Si desiste o alcanza el máximo, cerrar el intento; no prolongarlo para obtener éxito.

## Entorno fijo

Computador con ventana 1366 × 768 px y zoom del navegador 100 %, mismo equipo y configuración para las tres personas; prototipo móvil a escala de presentación idéntica en las sesiones. Registrar navegador, versión y escala efectivas. Se evalúa uso con puntero; no se atribuye accesibilidad con lector de pantalla, adaptación móvil real ni teclado nativo a un prototipo de Figma.

Si no carga el prototipo o una transición necesaria no está disponible, se registra Incidencia técnica y se detiene esa tarea. No se reemplazan interacciones por respuestas inferidas de capturas para calcular éxito de usuarios.

## 2.7.6 Métricas y SUS

| Métrica | Regla operativa |
| --- | --- |
| Éxito | Sí: criterio completo sin pista; Con ayuda: criterio completo después de la pista; No: intento fallido, abandono o máximo alcanzado. Solo Sí cuenta como éxito autónomo. |
| Tiempo | Segundos desde terminar la consigna hasta alcanzar todo el criterio. Registrar meta y máximo por separado del tiempo observado. |
| Errores | Crítico: impide terminar o exige intervención. No crítico: desvío con recuperación autónoma. Contar un episodio una vez, con contexto. |
| SUS | Diez ítems 1 a 5; impares respuesta menos 1 y pares 5 menos respuesta. Suma por 2,5. Rango de 0 a 100, sin unidad porcentual. |

Tasa por tarea = casos Sí / intentos válidos × 100; global = suma de casos Sí / suma de intentos válidos × 100. Informar n/N. No intentada por retiro se excluye; un intento iniciado que abandona es No. Incidencia técnica impide interpretar desempeño y se informa por separado, fuera del denominador. Si no hay intentos válidos, no calcular tasa.

Tiempo: registrar duración real de todos los intentos válidos y reportar mediana por tarea; presentar además la mediana de los exitosos. Etiquetar los máximos alcanzados como intentos censurados por límite, sin llamarlos tiempos de finalización. No convertir un dato faltante en cero.

Errores: registrar episodio, efecto y recuperación. Ejemplos no críticos: confundir unidades con líneas y corregirse; incrementar de más y recuperarse. Ejemplos críticos: no poder guardar el objetivo sin intervención o no reconocer el envío dentro del máximo. No se induce una cantidad inválida en las seis tareas; una prueba deliberada del evaluador no se cuenta como error espontáneo de un participante.

## Satisfacción percibida

SUS [3]: diez afirmaciones con escala de 1 totalmente en desacuerdo a 5 totalmente de acuerdo. Responder individualmente al finalizar. La redacción en español es una adaptación académica; no se afirma equivalencia psicométrica con la versión validada de [4]. Se mantienen cinco enunciados positivos y cinco negativos.

Puntuación = 2,5 × suma de contribuciones: impares respuesta − 1; pares 5 − respuesta. Si falta un ítem, no se calcula ni imputa SUS individual. La media usa solo cuestionarios completos y declara N. Se toma 68 como referencia orientativa del plan, no como requisito ISO ni porcentaje de usabilidad. Ejemplo de control, sin participante: 4,2,4,2,4,2,4,2,4,2 produce 75.

## 2.7.7 Instrumentos y procedimiento

| Código | Documento y función |
| --- | --- |
| I01 | Consentimiento informado: información, decisión y reglas de retiro. |
| I02 | Matriz de seis tareas: lectura de consignas y respuestas para el equipo. |
| I03 | Hoja de observación y SUS: seis registros, diez ítems y cierre. |
| I04 | Guía heurística: H1 a H10, códigos de evaluador y severidad. |
| I05 | Guion de sesión: tiempos, neutralidad, estados y contingencias. |

Todos se entregan en PDF, Word y Markdown. registro_local.html ofrece una copia operativa por P1, P2 o P3; permite registrar decisión, seis tareas, frases y SUS y exportar JSON privado sin transmitir datos. Los campos de aplicación no son resultados prellenados.

| Etapa | Minutos | Aplicación |
| --- | --- | --- |
| Filtro y bienvenida | 2 | Verificar perfil y exclusiones; asignar código sin nombres. |
| Consentimiento | 2 | Lectura y decisión explícita; ante rechazo no iniciar. |
| Preparación | 1 | Comprobar entorno y explicar pensamiento en voz alta con ejemplo ajeno al prototipo. |
| Seis tareas | 6 min 45 s de metas; 13 min 30 s de máximos | Leer en orden y preparar los estados independientes. |
| SUS | 3 | Responder sin orientación del equipo. |
| Cierre | 2 | Lo más confuso y lo que funcionó mejor. |
| Margen | 1 min 30 s | Pausas breves y preparación técnica fuera del cronometraje. |

Máximo previsto: 25 minutos por sesión. Tres sesiones más 5 minutos entre ellas suman 85 minutos de pilotaje. La preparación de Fase 1 mantiene su duración académica de 2 horas; no se confunde con este tiempo futuro de aplicación.

## 2.7.8 Condiciones de validación

Al terminar el pilotaje de Fase 2 se contrastarán los siguientes criterios. Su definición está terminada; su cumplimiento empírico se determina con datos de aplicación.

| ID | Dimensión | Condición |
| --- | --- | --- |
| CV1 | Comprensión | Ninguno de los tres necesita reformular o explicar las consignas; una repetición literal se registra y no se cuenta como pista. |
| CV2 | Factibilidad | Al menos 2 de 3 completan cada tarea dentro de su máximo; reportar además si se alcanzó el tiempo objetivo. |
| CV3 | Registro | Existen seis filas por persona y diez respuestas SUS, o un motivo explícito para cualquier dato no obtenido. |
| CV4 | Estabilidad y reinicio | Sin incidencias técnicas que impidan completar; los estados independientes de T4, T5 y T6 se preparan sin contaminar intentos. |
| CV5 | Duración | Cada sesión completa dura como máximo 25 minutos, sin presionar ni recortar la participación voluntaria. |
| CV6 | Ética | Perfil verificado, consentimiento explícito antes de iniciar y ausencia de identificadores personales en lo publicado. |

Si un criterio no se alcanza, documentar causa y modificación, aumentar la versión y repetir la parte afectada con personas nuevas. No alterar registros anteriores ni agrupar versiones distintas como si fueran equivalentes.

## Metas exploratorias del producto

Al menos 2 de 3 éxitos sin ayuda por tarea, ausencia de errores críticos y SUS medio orientativo de al menos 68 en cuestionarios completos. Estas son metas del equipo, no garantías ni condiciones prescritas por ISO. Los criterios CV1 a CV6 evalúan preparación del protocolo; las metas de producto describen desempeño observado.

## Cronograma y responsabilidades

11 de noviembre de 2026: preparación de la Fase 1 en 120 minutos con el reparto de cinco integrantes. En la fase siguiente, Manuel contacta perfiles externos, William verifica inclusión, Emilio modera, Pablo cronometra y Jonathan observa; la fecha efectiva se registra cuando se acuerda la participación. La aplicación de instrumentos se mantiene fuera de esta entrega de planificación.

## 2.7.9 Pruebas realizadas

Se contrastaron las seis tareas con los recorridos y capturas de la versión del APE 4. Se ejecutaron comprobaciones de precios, cantidades, totales, duraciones y cálculo SUS, y se verificó la organización de archivos. El registro reproducible está en pruebas/resultados_verificacion.json. Son verificaciones documentales y aritméticas, sin atribuir resultados a usuarios.

| Área | Comprobación |
| --- | --- |
| Catálogo | Solo café americano y sánduche; precios $1,50 y $2,75. |
| Base | 1 café + 1 sánduche = 2 unidades y $4,25, C12. |
| Edición | 2 cafés + 1 sánduche = 3 unidades y $5,75, C15 y C21. |
| Eliminación | Borrador con 1 café = 1 unidad y $1,50; sin guardar, C17. |
| Confirmación | CU-104 base, Recibido, 2 unidades y $4,25; nueva selección 0, C25 y C28. |
| Instrumentos | Seis tareas completas; máximo = 2 × meta; diez ítems SUS; cinco roles. |
| Paquetes | Un aporte por integrante, rutas sin conflicto y todos los documentos incluidos. |

No se ejecutó una sesión de usuarios ni se comprobó la navegación en vivo de Figma con el acceso disponible. Las pruebas de esta página no validan percepción de estados, tiempos humanos ni accesibilidad. Los participantes y resultados del repositorio del Grupo 5 no se reutilizan como evidencia propia.

## 2.8 Resultados obtenidos

Se obtiene un protocolo v2.0 de CaféU con pregunta, dos métodos, tres perfiles externos, seis tareas respaldadas por estados del APE 4, instrumentos completos, cinco roles y seis condiciones de validación. La distribución prepara publicación desde las cuentas de los cinco integrantes. Los registros de aplicación se completan durante la Fase 2, como corresponde a un instrumento.

## 2.9 Habilidades blandas

Liderazgo en control de versión; trabajo en equipo mediante revisión cruzada; responsabilidad al proteger identidades y no atribuir resultados inexistentes; comunicación mediante consignas neutrales y separación entre lectura, observación y soporte.

## 2.10 Conclusiones

- La delimitación de CaféU del APE 4 conserva la correspondencia entre el objeto evaluado y el proyecto del equipo. La combinación de heurísticas y pensamiento en voz alta permitirá observar tanto problemas previstos como dificultades reales de uso.
- Las seis tareas cubren consulta, búsqueda, selección, edición, eliminación y recepción. Sus criterios distinguen unidades, total, borrador y pedido guardado, lo que evita considerar exitosa una acción que no alcanza el resultado esperado.
- El consentimiento, la selección por códigos, los cinco roles y las condiciones de validación estructuran el pilotaje de forma ética y reproducible. El reparto por integrante permite publicar y revisar aportes desde las cuentas personales.

## 2.11 Recomendaciones

- Mantener la versión y escala de presentación constantes y reiniciar los escenarios fijados antes de T4, T5 y T6. No emplear el estado resultante de T4 como inicio de T5.
- Verificar inclusión antes del consentimiento; registrar incidencias de acceso o navegación sin inferir éxitos a partir de capturas.
- Aplicar las tareas con personas externas en Fase 2, mantener los datos individuales privados y publicar agregados revisados.
- Publicar los cinco aportes desde sus cuentas y verificar los commits reales antes de enviar a Moodle el PDF y el repositorio.

## Participación y entrega

Repositorio: https://github.com/william-martinez5101/IHC_APE6. William publica informe y coordinación; Emilio tareas y referencias del prototipo; Pablo observación y SUS; Manuel consentimiento y perfiles; Jonathan heurística, guion y verificación. Cada ZIP individual conserva las rutas definitivas y contiene instrucciones de rama y dos commits.

Los commits y pull requests reales constituyen la evidencia de publicación. El reparto y los mensajes sugeridos no los sustituyen. El script colaboracion/verificar_autorias.py extrae hashes y autores del historial local después de integrar las ramas, sin crear ni suplantar autorías.

## 2.12 Referencias

[1] ISO, ISO 9241-11:2018, Ergonomics of human-system interaction - Part 11: Usability: Definitions and concepts, 2018. [En línea]. Disponible: https://www.iso.org/standard/63500.html. [Consulta: 11-nov-2026].

[2] J. Nielsen, “10 Usability Heuristics for User Interface Design”, Nielsen Norman Group. [En línea]. Disponible: https://www.nngroup.com/articles/ten-usability-heuristics/. [Consulta: 11-nov-2026].

[3] J. Brooke, “SUS: A quick and dirty usability scale”, en Usability Evaluation in Industry, P. W. Jordan et al., Eds. Londres, Reino Unido: Taylor & Francis, 1996, pp. 189-194.

[4] M. R. Sevilla-González et al., “Spanish Version of the System Usability Scale for the Assessment of Electronic Tools: Development and Validation”, JMIR Human Factors, vol. 7, n.º 4, e21161, 2020, doi: 10.2196/21161. Antecedente de la versión española; la redacción adjunta es una adaptación académica.

[5] J. R. Caiza Caizabuano, “APE 6. Evaluación y validación”, guía práctica, Universidad Técnica de Ambato, 2026. Material proporcionado por el docente.

[6] Grupo 5, “Guía de réplica APE 6 Fase 1”, Universidad Técnica de Ambato, 2026. [En línea]. Disponible: https://github.com/carlitosgiovanniramos/HCI-2026-G5. [Consulta: 11-nov-2026].

[7] Grupo 6, “CaféU, APE 4 integral”, GitHub, versión 822fbbf, 2026. [En línea]. Disponible: https://github.com/idk-Damian/Ape4_IHC/tree/822fbbf4c1d4011c399e4753d85e6f3d2167ff34/APE4-integral. [Consulta: 11-nov-2026].

[8] Grupo 6, “CaféU, prototipo de Figma”, 2026. [En línea]. Disponible: https://www.figma.com/design/HQZqFztrL0HeQ6E9h60LZm/Sin-t%C3%ADtulo?node-id=0-1. Enlace identificado en el repositorio APE 4; la inspección directa no estuvo disponible con el acceso de esta revisión.

## 3 Anexos y trazabilidad

I01 a I05 se localizan en instrumentos/. Las diez capturas y los textos de referencia de APE 4 están en prototipo/. La procedencia y las huellas están en prototipo/procedencia.json. Pruebas y aritmética reproducibles en pruebas/. La distribución, aportes y comandos están en colaboracion/.

El catálogo de este prototipo no incluye croissant, horario de atención ni tres productos de comida. Esas respuestas pertenecen a otro ejemplo y no forman parte de las tareas de CaféU del Grupo 6.

## Anexo A Capturas que respaldan las tareas

Fuentes: repositorio propio APE 4 integral, versión 822fbbf. Capturas originales conservadas sin alterar. Sirven como evidencia visual del estado esperado, sin demostrar por sí solas la navegación.

Capturas: C02 Catálogo; C12 Base; C21 Edición guardada

T1 identifica los dos productos y sus precios en C02. T3 termina en C12, con 2 unidades por $4,25. T4 termina en C21, con 3 unidades por $5,75 y reconocimiento del guardado. Los criterios de éxito exigen tanto estado visible como respuesta verbal cuando la consigna la pide.

## Anexo B Borrador comprobante y nueva selección

Capturas: C17 Borrador; C25 Recibido; C28 Otro pedido

T5 termina en C17: queda 1 café por $1,50 y el borrador tiene cambios sin guardar. T6 se prepara nuevamente desde la base y debe reconocer C25: CU-104, Recibido y $4,25. Después se inicia una selección vacía, C28. El contador 0 de una nueva selección no significa que el comprobante recibido carezca de productos.
