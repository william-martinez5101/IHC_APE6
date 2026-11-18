# APE 6: Fases 3 y 4 de CaféU

Universidad Técnica de Ambato · Facultad de Ingeniería en Sistemas, Electrónica e Industrial · Ingeniería de Software · Quinto A · Grupo 6. Asignatura: Interacción Humano-Computador. Docente: Ing. José Rubén Caiza Caizabuano, Mg.

## Objetivo general

Evaluar formativamente el prototipo CaféU del APE 4 integral mediante inspecciones heurísticas y pruebas de usabilidad con estudiantes externos, para fundamentar criterios verificables y una priorización de mejoras a partir de eficacia, eficiencia y satisfacción.

## Tres objetivos específicos

1. Inspeccionar las diez heurísticas y justificar severidades individuales y consensuadas mediante frecuencia, impacto y persistencia.
2. Aplicar siete tareas y SUS a tres participantes externos, consolidando éxito autónomo, tiempos y errores sin alterar los registros.
3. Triangular problemas analíticos y empíricos y convertirlos en criterios técnicos y backlog trazable que respondan a la distinción entre verificación y validación.

## Continuidad con Fases 1 y 2

Fase 1 conserva la planificación, el consentimiento, seis situaciones, SUS y metas. Fase 2 aportó tres sesiones y el procedimiento V2. La aplicación F3 mantiene CaféU y T1–T6, incorpora la cancelación de una retirada en T7 y especifica F5 más verificación de estado. Las versiones de procedimiento no se confunden con versiones de interfaz. El repositorio conserva ambas fases previas y su documentación académica.

## Método y aplicación

Las inspecciones se declaran independientes y están fechadas el 17/11/2026. Cada integrante cubrió las diez heurísticas y dos anotaciones adicionales. La transcripción conserva coincidencias de redacción y valoraciones. El consenso del 18/11/2026 registra cinco puntuaciones individuales por hallazgo, decisión final y justificación.

El 18/11/2026 se registraron tres sesiones de 27, 20 y 24 min con estudiantes adultos externos al diseño, sin participación declarada en F2. El entorno común fue portátil Windows 11, Microsoft Edge 142, resolución 1366 × 768 y escala 100 %. La etiqueta declarada CaféU F3 v3.0 se conserva, sin afirmar un rediseño.

| Rol | Responsable efectivo registrado |
| --- | --- |
| Moderador | Emilio Abril |
| Usuario | Externo F3-P1, F3-P2 o F3-P3 |
| Cronometrista | Pablo Lozada |
| Observador | Jonathan Gamboa |
| Apoyo previsto de preparación y consentimiento | Manuel Cusme |
| Coordinación prevista | William Martínez |

Se registraron consentimiento y autorizaciones anónimas, sin retiros ni grabaciones. El moderador utilizó consignas y tarjetas; el cronómetro excluyó preparación. Se aplicaron tres pistas neutrales por bloqueo: P1/T2 a 48 s (último avance 18), P1/T4 a 82 s (último avance 52) y P3/T2 a 44 s (último avance 14). Cada intervalo fue de 30 s. La relectura literal y la tarjeta no se contaron como pistas.

Las fichas declaran F5, Inicio, contador cero, búsqueda vacía y filtro Todo. T4–T7 parten de bases independientes por $4,25. T7 preservó ambos productos y total en tres casos. Los registros escritos son evidencia de la aplicación aportada, no una inspección independiente del navegador por el asistente.

## Resultados ISO/SUS

| Tarea | Autónomos / N | Éxito autónomo | Mediana s | Meta s | Diferencia s | Máximo s | Críticos | No críticos | Mediana autónomos s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | 3/3 | 100.00 % | 27 | 30 | -3 | 60 | 0 | 0 | 27 |
| T2 | 1/3 | 33.33 % | 64 | 45 | 19 | 90 | 0 | 3 | 39 |
| T3 | 3/3 | 100.00 % | 83 | 90 | -7 | 180 | 0 | 1 | 83 |
| T4 | 2/3 | 66.67 % | 112 | 90 | 22 | 180 | 0 | 2 | 91,5 |
| T5 | 2/3 | 66.67 % | 77 | 60 | 17 | 120 | 1 | 1 | 60 |
| T6 | 3/3 | 100.00 % | 94 | 90 | 4 | 180 | 0 | 2 | 94 |
| T7 | 3/3 | 100.00 % | 41 | 45 | -4 | 90 | 0 | 1 | 41 |

| Participante F3 | Autónomos / 7 | Con ayuda | No | SUS | Diferencia vs 68 | Sesión min |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 4 | 2 | 1 | 62,5 | -5,5 | 27 |
| P2 | 7 | 0 | 0 | 90 | 22 | 20 |
| P3 | 6 | 1 | 0 | 72,5 | 4,5 | 24 |

El global fue 17/21 = 80,95 % autónomos, tres asistidos y un fracaso; errores 1 crítico y 10 no críticos. SUS medio 75,0. La finalización asistida de 95,24 % se informa separadamente. El fracaso de T5 cerró por abandono a 96 s y no se sustituyó por el máximo. Las fichas individuales conservan contenido final y condición de guardado, necesarios para distinguir éxito de una coincidencia parcial de productos.

## Matriz, triangulación y criterios

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

| Criterio | Componente, cambio y aceptación | Hallazgo | Respaldo |
| --- | --- | --- | --- |
| C-01 | Buscador: Mostrar todos vacía consulta y filtros y muestra los 2 productos en una acción, sin alterar el pedido. | H-01 | Nielsen H3 y H7; ISO 9241-11: eficacia y eficiencia. |
| C-02 | Revisión: después de guardar se muestra confirmación visible y 2 cafés, 1 sánduche y $5,75; volver a abrir conserva esos datos. | H-02 | Nielsen H1; ISO 9241-11: eficacia y eficiencia. |
| C-03 | Edición: al quitar el sánduche se indica borrador de 1 café por $1,50; el guardado original sigue en $4,25 hasta Guardar cambios. Descartar restaura el original. | H-03 | Nielsen H1, H3 y H6; ISO 9241-11: eficacia. |
| C-04 | Línea de producto: separar visualmente Retirar de +/−; al activar Retirar no cambia la cantidad de otra línea; total y cantidad se actualizan juntos. | H-04 | Nielsen H5; ISO 9241-11: eficacia. |
| C-05 | Comprobante: junto a CU-104 se muestra Recibido y Recibimos tu pedido; te avisaremos cuando esté listo, diferenciando ambos estados. | H-05 | Nielsen H1 y H2; ISO 9241-11: eficiencia. |
| C-06 | Modal: identificar el producto; Conservar sánduche mantiene las 2 líneas y $4,25; Retirar sánduche solo afecta esa línea tras confirmación. | H-06 | Nielsen H3 y H5. |
| C-07 | Estado vacío: mostrar la consulta activa, indicar que no hay coincidencias y ofrecer una salida directa al catálogo sin perder el pedido. | H-07 | Nielsen H9 y H10. |
| C-08 | Inicio de pedido: al elegir Nuevo pedido se muestra ese título y contador 0; CU-104 queda identificado como comprobante anterior y no integra la selección actual. | H-08 | Nielsen H1 y H8; ISO 9241-11: eficacia. |
| C-09 | Navegación: la misma etiqueta produce el mismo efecto sobre los cambios en todas las pantallas; cada salida informa si guarda, descarta o conserva. | H-09 | Nielsen H4. |
| C-10 | Ayuda contextual: junto a editar, guardar y enviar se explica el efecto de cada acción; la ayuda puede consultarse sin perder el borrador. | H-10 | Nielsen H10. |

Ocho hallazgos se confirman por ambos métodos; H-09 y H-10 son Solo heurística. H-08 fue detectado analíticamente por Manuel y observado en P3/T6. El consenso de otros evaluadores no se presenta como cinco detecciones independientes del mismo problema. H-01 y H-07 se separan por acción y mensaje, manteniendo tres episodios de error en T2 sin doble conteo.

## Priorización y backlog

| Prioridad | Hallazgo | Severidad | Criterio | Issue |
| --- | --- | --- | --- | --- |
| P1 | H-01 | 3 | C-01 | No creado (HTTP 403) |
| P1 | H-02 | 3 | C-02 | No creado (HTTP 403) |
| P1 | H-03 | 3 | C-03 | No creado (HTTP 403) |
| P2 | H-04 | 2 | C-04 | No creado (HTTP 403) |
| P2 | H-06 | 2 | C-06 | No creado (HTTP 403) |
| P2 | H-07 | 2 | C-07 | No creado (HTTP 403) |
| P2 | H-08 | 2 | C-08 | No creado (HTTP 403) |
| P3 | H-05 | 2 | C-05 | No creado (HTTP 403) |
| P3 | H-09 | 2 | C-09 | No creado (HTTP 403) |
| P3 | H-10 | 2 | C-10 | No creado (HTTP 403) |

Las prioridades son acuerdos del equipo. No hay P4 asignados. No es necesario llenar una categoría sin evidencia. Los diez cuerpos de Issue contienen origen, severidad, prioridad, aceptación y comprobaciones del cambio. La publicación remota fue rechazada con HTTP 403; se proporciona publicación idempotente desde una cuenta autorizada. No se incluyen números inexistentes.

## Interpretación: verificación y validación

En T5 pudo ejecutarse Guardar y, aun así, no se alcanzó la condición de borrador requerida. T2 ofrece una recuperación posible que dos usuarios no identificaron sin ayuda. Estas observaciones responden afirmativamente a la pregunta del laboratorio: la disponibilidad técnica no garantiza adecuación de uso. La cancelación T7, por su parte, funcionó según los tres registros; su mejora propuesta trata claridad y no corrige una pérdida de productos observada.

En el núcleo T1–T6 hay 14/18 éxitos autónomos, igual que F2. El aumento del porcentaje global se debe a incluir T7 y no demuestra mejora de interfaz. Las diferencias de tiempo son descriptivas y están condicionadas por muestra, protocolo y entorno. No se realizó una evaluación posterior a implementar el backlog.

## Conclusiones y recomendaciones

Las tres conclusiones y tres recomendaciones vinculadas a los objetivos se desarrollan en [conclusiones.md](conclusiones.md), con alcance y límites de inferencia. Las [referencias](referencias_fases3_4.md) complementan el marco de Boehm, Nielsen, ISO y SUS.

## Repositorio y ubicación de evidencias

Enlace: https://github.com/william-martinez5101/IHC_APE6.

| Ruta | Contenido |
| --- | --- |
| APE6_FASE1/ | Planificación e instrumentos históricos existentes |
| Fase2-Pilotaje/ | Pilotaje histórico existente, sin modificar |
| Fase3-Aplicacion/ | Protocolo, siete tareas, datos y métricas de aplicación |
| resultados/ | P1–P3 y cinco evaluaciones individuales de F3 |
| Fase4-Cierre/ | Hallazgos, consenso, criterios y backlog |
| docs/ | Informes históricos y documentación Markdown de cierre |
| Evidencias_Colaboracion/ | Distribución y aportes; historial efectivo en GitHub |

El Excel original se conserva en el paquete privado. Las fichas públicas incluyen solo códigos y datos autorizados. Los soportes identificables, si existieran fuera de este libro, permanecen privados. Los compromisos de implementación no se presentan como cambios ya realizados.
