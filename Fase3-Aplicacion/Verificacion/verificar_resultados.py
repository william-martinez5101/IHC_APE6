from pathlib import Path
import json,statistics,re
base=Path(__file__).resolve().parents[1]
p=json.loads((base/'Datos/participantes_anonimizados.json').read_text(encoding='utf8'))
h=json.loads((base/'Datos/evaluaciones_heuristicas.json').read_text(encoding='utf8'))
c=json.loads((base/'Datos/consenso_transcrito.json').read_text(encoding='utf8'))
m=json.loads((base/'Datos/metricas_fase3.json').read_text(encoding='utf8'))
assert len(p)==3 and len({x['codigo'] for x in p})==3
flat=[];scores=[]
for x in p:
 assert x['ronda']=='F3' and len(x['tareas'])==7
 assert {r['tarea'] for r in x['tareas']}=={f'T{i}' for i in range(1,8)}
 assert x['consentimiento'] and x['publicacion_individual'] and x['agregados_autorizados']
 a=x['sus_respuestas'];assert len(a)==10 and all(isinstance(i,int) and 1<=i<=5 for i in a)
 s=sum(i-1 if k%2==0 else 5-i for k,i in enumerate(a))*2.5
 assert s==x['SUS'];scores.append(s)
 for r in x['tareas']:
  assert r['resultado'] in ['Sí','Con ayuda','No'] and r['tiempo_s']>=0
  assert r['errores_criticos']>=0 and r['errores_no_criticos']>=0
  if r['resultado']=='Sí':assert r['pista']=='No' and r['punto_detencion_correcto']=='Sí'
  if r['pista']=='Sí':assert r['segundo_pista']-r['ultimo_avance_s']>=30 and r['segundo_pista']<=r['tiempo_s']
  flat.append(r)
for x in m['por_tarea']:
 rs=[r for r in flat if r['tarea']==x['tarea']]
 assert len(rs)==x['intentos_validos']==3
 assert sum(r['resultado']=='Sí' for r in rs)==x['autonomos']
 assert statistics.median(r['tiempo_s'] for r in rs)==x['mediana_s']
 assert sum(r['errores_criticos'] for r in rs)==x['errores_criticos']
 assert sum(r['errores_no_criticos'] for r in rs)==x['errores_no_criticos']
 assert all(r['tiempo_s']<=x['maximo_s'] for r in rs)
assert len(h)==60 and len({x['evaluador'] for x in h})==5
for who in {x['evaluador'] for x in h}:
 rs=[x for x in h if x['evaluador']==who]
 assert len(rs)==12 and {x['heuristica'] for x in rs}=={f'H{i}' for i in range(1,11)}
for x in h:
 if x['resultado']=='Problema observado':assert x['severidad'] in [1,2,3,4]
 else:assert x['severidad'] is None
assert len(c)==10 and {x['id'] for x in c}=={f'H-{i:02}' for i in range(1,11)}
for x in c:
 assert x['acuerdo_registrado'] and x['severidad_consensuada'] in [1,2,3,4]
 assert len(x['valoraciones_individuales'])==5 and x['prioridad'] in ['P1','P2','P3','P4']
assert sum(r['resultado']=='Sí' for r in flat)==17
assert sum(r['resultado']=='Con ayuda' for r in flat)==3
assert sum(r['resultado']=='No' for r in flat)==1
assert sum(r['errores_criticos'] for r in flat)==1
assert sum(r['errores_no_criticos'] for r in flat)==10
assert scores==[62.5,90,72.5] and statistics.mean(scores)==75
assert sum(x['triangulacion']=='Confirmado por ambos métodos' for x in c)==8
assert sum(x['triangulacion']=='Solo heurística' for x in c)==2
print(json.dumps({'resultado':'Comprobaciones satisfactorias','ronda':'F3','intentos':len(flat),'autonomos':17,'SUS':scores,'SUS_medio':75,'heuristicas':60,'consensos':10},ensure_ascii=False,indent=2))
