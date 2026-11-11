# Pruebas realizadas

Objeto: CaféU del APE 4 integral del Grupo 6. Fecha: 11 de noviembre de 2026. Versión del protocolo: 2.0.

Se realizaron **47 comprobaciones conformes de 47** mediante verificar_plan.py y verificar_sus.cjs. El detalle está en resultados_verificacion.json.

## Cobertura

- Seis tareas T1 a T6 con consigna, estado inicial, meta, máximo, éxito, respuesta y evidencia.
- Máximo igual al doble de la meta; suma de máximos de 13 minutos y 30 segundos, dentro de una sesión prevista de 25 minutos.
- Pedidos y operaciones: base $4,25; edición $5,75; diferencia de presupuesto $0,75; borrador de un café $1,50; CU-104 recibido por $4,25 y nueva selección vacía.
- Diez capturas y referencias originales identificadas mediante huellas SHA-256.
- Seis documentos Word con contenido de CaféU, sin marcadores de redacción por completar ni referencias al sistema sustituido.
- Formulario con seis registros y diez grupos SUS, sin transmisión externa de datos.
- Ocho casos de control del módulo SUS real del formulario: extremos 0 y 100, patrón 75, neutro 50 y rechazo de respuestas incompletas, ausentes, fraccionarias o fuera de rango.

## Reproducir

Requiere Python 3 y Node.js. Desde la raíz del repositorio:

```bash
python APE6_FASE1/pruebas/verificar_plan.py
```

Para comprobar solo la puntuación:

```bash
node APE6_FASE1/pruebas/verificar_sus.cjs
```

Estas verificaciones son documentales y aritméticas. No constituyen tres sesiones humanas, no miden tiempos de personas y no acreditan transiciones en vivo de Figma. El acceso de esta revisión permitió consultar el repositorio y las capturas; la aplicación externa corresponde a Fase 2. La organización de los paquetes se verificó además al comprimir: cobertura completa y rutas sin duplicación.
