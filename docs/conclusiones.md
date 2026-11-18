# Conclusiones: evaluación formativa de CaféU

Universidad Técnica de Ambato · FISEI · Ingeniería de Software · Quinto A · Grupo 6.
Docente: Ing. José Rubén Caiza Caizabuano, Mg.

## Respuesta a la pregunta del laboratorio

**Sí, una interfaz que funciona técnicamente puede ser una mala interfaz para determinados objetivos de uso.** Verificar que una operación produce el estado especificado no demuestra que una persona encuentre esa operación, comprenda su efecto y complete su propósito sin ayuda. La distinción entre verificación y validación orienta el estudio; no se afirma haber auditado el sistema completo de una cafetería real.

## Conclusiones vinculadas a los objetivos específicos

1. **Inspección heurística.** Las cinco evaluaciones entregadas cubren las diez heurísticas mediante 60 registros y sustentan diez hallazgos únicos. La valoración de frecuencia, impacto y persistencia diferencia problemas de guardado, recuperación, prevención y orientación. El consenso registra discrepancias y conserva una severidad de 3 para H-01, H-02 y H-03. La severidad consensuada no equivale automáticamente a un fallo crítico de todo el sistema.
2. **Eficacia, eficiencia y satisfacción.** Las tres sesiones registran 17/21 éxitos autónomos, tres finalizaciones asistidas y un fracaso, con un error crítico y diez no críticos. T2 obtuvo solo 1/3 éxitos sin ayuda. En T5, P1 abandonó tras guardar antes del punto requerido; la operación de guardado pudo ejecutarse y el objetivo del usuario siguió incumplido. SUS medio fue 75,0, superior descriptivamente a 68,0, mientras P1 obtuvo 62,5. Estos datos muestran que satisfacción global favorable y funcionamiento de operaciones no garantizan autonomía en todos los recorridos.
3. **Integración y priorización.** Ocho hallazgos cuentan con evidencia de ambos métodos y dos permanecen Solo heurística. Se definieron criterios C-01 a C-10 y se acordaron tres prioridades P1, cuatro P2 y tres P3. T7 amplió la cobertura de cancelación: 3/3 conservaron los productos y total, aunque P1 tuvo una duda recuperable. Los criterios y el backlog fundamentan trabajo futuro; aún no prueban que las propuestas hayan mejorado la interfaz.

## Recomendaciones

1. Priorizar la recuperación de catálogo, la confirmación del guardado y la distinción de borrador/pedido guardado. Comprobar cada cambio con su criterio y una versión identificable del prototipo.
2. Mantener las mismas tareas, metas y política de ayuda en la evaluación posterior a cambios. Informar T1–T6 como núcleo comparable y T7 como cobertura adicional, sin atribuir a un rediseño diferencias producidas por composición de tareas o participantes.
3. Preservar las observaciones y citas originales, el anonimato y la trazabilidad de evaluaciones individuales. Publicar los diez Issues con URLs reales y conservar ramas, commits y Pull Requests de las cinco cuentas.

## Límites de la inferencia

Tres participantes constituyen una muestra formativa. No permiten estimar la frecuencia poblacional, demostrar diferencias estadísticas o medir persistencia longitudinal. Las referencias a observaciones se respaldan en fichas escritas aportadas por el equipo; no existen grabaciones públicas. La etiqueta CaféU F3 v3.0 identifica el entorno declarado y no acredita un rediseño. En T1–T6 la autonomía permanece en 14/18, igual que F2; el 80,95 % global incluye T7. El promedio SUS cambió de 75,83 a 75,0 y no demuestra una mejora.

Referencias complementarias: [bibliografía](referencias_fases3_4.md). Resultados: [métricas de F3](../Fase3-Aplicacion/Resumen_Metricas.md). Repositorio: https://github.com/william-martinez5101/IHC_APE6.
