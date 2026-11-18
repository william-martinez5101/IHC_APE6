# Backlog de mejoras consensuadas

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

La prioridad es una decisión de orden de trabajo y no el número inverso de severidad. P1 reúne búsqueda, confirmación de guardado y separación del borrador por su impacto en autonomía o en el estado final.

## Publicación de Issues

No se crearon Issues: GitHub devolvió HTTP 403, Resource not accessible by integration, al intentar la publicación. Se verificó el listado remoto y no contenía Issues. No se inventan números ni enlaces. Los diez títulos y cuerpos están en issues/.

Desde la raíz del clon, con GitHub CLI oficial instalado y autenticado mediante `gh auth login`, ejecutar `python Fase4-Cierre/publicar_issues.py`. El programa consulta títulos existentes, evita duplicados y crea solo los ausentes. Actualiza las URLs del registro, README, backlog y hallazgos. No aplica cambios a la interfaz ni cierra Issues.

Publicar antes del commit final de integración. El ZIP documenta las pruebas recibidas, el consenso y el backlog; el historial colaborativo y los Issues requieren las acciones reales de las cuentas del grupo.
