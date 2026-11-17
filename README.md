# APE 6 Evaluación de usabilidad de CaféU

Universidad Técnica de Ambato · FISEI · Software · Quinto A · Grupo 6.
Docente: Ing. José Rubén Caiza Caizabuano, Mg.

## Objetivo

Evaluar y validar mediante un pilotaje con tres usuarios externos el protocolo de usabilidad del prototipo CaféU del APE 4, dando continuidad a la planificación de la Fase 1 y combinando pensamiento en voz alta, métricas de eficacia, eficiencia y satisfacción y evaluación heurística individual para fundamentar ajustes del protocolo y mejoras de interacción con respeto a la participación voluntaria y al anonimato.

## Integrantes

| Integrante | GitHub | Rol |
| --- | --- | --- |
| Abril Lara Emilio Alexander | @EMILIOABRIL05 | Moderación |
| Cusme Velez Manuel Steven | @ManuelCusme | Soporte y consentimiento |
| Gamboa Guaman Jonathan Alexis | @Jonathan305g | Observación |
| Lozada Marcial Pablo Damian | @idk-Damian | Métricas |
| Martínez Jiménez William Fernando | @william-martinez5101 | Coordinación |

## Prototipo y repositorio

- [CaféU del APE 4 integral](https://www.figma.com/design/HQZqFztrL0HeQ6E9h60LZm/Sin-t%C3%ADtulo?node-id=0-1) — utilizar Presentación desde Inicio.
- [Repositorio único](https://github.com/william-martinez5101/IHC_APE6).

## Fase 1 Planificación

[APE6_FASE1/](APE6_FASE1/) conserva el plan, consentimiento, seis tareas, métricas, hoja SUS, heurísticas y guion. El protocolo documental v2.0 del 11/11/2026 constituye la línea base del pilotaje.

## Fase 2 Pilotaje

[Fase2-Pilotaje/](Fase2-Pilotaje/) reúne tres registros de participantes, resultados de seis tareas, SUS, cinco evaluaciones heurísticas, hallazgos y comparación V1 → V2. La ronda base se registra el 13/11/2026. V2 es el procedimiento revisado para una aplicación posterior; se conserva la separación entre datos observados y ajustes propuestos.

## Resultados principales

| Indicador | Resultado |
| --- | --- |
| Éxito sin ayuda | 14/18 = 77,8 % |
| Completadas con ayuda | 3/18 |
| No completadas | 1/18 |
| Errores críticos / no críticos | 1 / 9 |
| SUS P1 / P2 / P3 | 65 / 90 / 72,5 |
| SUS medio | 75,83 puntos |
| Duración de sesiones | 22 / 17 / 20 min |
| Tarea con menor autonomía | T4: 1/3 éxitos sin ayuda |

## Documentos y navegación

- [Informe integrado APE PDF](docs/Informe_APE6_Fases1_2_CafeU.pdf) y [Word](docs/Informe_APE6_Fases1_2_CafeU.docx), llenados sobre la plantilla institucional.
- [Informe histórico de Fase 1](docs/Informe_APE6_Fase1_Grupo6_CafeU.pdf).
- [P1](Fase2-Pilotaje/Participantes/P1.md), [P2](Fase2-Pilotaje/Participantes/P2.md), [P3](Fase2-Pilotaje/Participantes/P3.md).
- [Métricas](Fase2-Pilotaje/Resumen_Metricas.pdf), [ajustes V1 → V2](Fase2-Pilotaje/Ajustes_Protocolo_V1_V2.pdf) y [hallazgos](Fase2-Pilotaje/Hallazgos_Preliminares.pdf).
- [Evaluaciones heurísticas](Fase2-Pilotaje/Evaluaciones_Heuristicas/), [protocolo V2](Fase2-Pilotaje/Protocolo_V2/), [validación](Fase2-Pilotaje/Validacion_Fase1.pdf).
- [Datos anonimizados](Fase2-Pilotaje/Datos/) y [verificación reproducible](Fase2-Pilotaje/Verificacion/).
- [Registro de aportes](Evidencias_Colaboracion/Registro_Aportes.md).

## Organización

| Ruta | Contenido |
| --- | --- |
| docs/ | Informes de Fases 1 y 2 en Word y PDF. |
| APE6_FASE1/ | Planificación original e instrumentos. |
| Fase2-Pilotaje/Participantes/ | P1.md, P2.md y P3.md. |
| Fase2-Pilotaje/Datos/ | Mediciones, SUS, métricas y trazabilidad editorial. |
| Fase2-Pilotaje/Evaluaciones_Heuristicas/ | Cinco evaluaciones y comparación con usuarios. |
| Fase2-Pilotaje/Protocolo_V2/ | Guion, tarjetas y ajustes del procedimiento. |
| Fase2-Pilotaje/Verificacion/ | Programa Python y resultados de comprobación. |
| Evidencias_Colaboracion/ | Aportes individuales y acceso al historial. |

## Privacidad y reproducción

Se publican solo registros anónimos autorizados. Los consentimientos identificables y el libro original de trabajo se conservan en privado. Las citas de participantes mantienen su texto; las fichas heurísticas incluyen trazabilidad de su revisión editorial.

Para recalcular los resultados, ejecutar `python Fase2-Pilotaje/Verificacion/verificar_metricas.py`. Requiere Python 3 sin dependencias externas. Los criterios del protocolo se distinguen de las metas exploratorias del producto y la muestra de tres casos no representa una estimación poblacional.
