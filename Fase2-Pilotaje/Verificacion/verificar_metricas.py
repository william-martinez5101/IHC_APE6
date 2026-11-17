from pathlib import Path
import json, statistics
base=Path(__file__).resolve().parents[1]
p=json.loads((base/'Datos/participantes_anonimizados.json').read_text(encoding='utf8'))
expected=json.loads((base/'Datos/resumen_metricas.json').read_text(encoding='utf8'))
sus=[];success=assisted=failed=critical=noncritical=0
for person in p:
 a=person['sus_respuestas']
 assert len(a)==10 and all(isinstance(x,int) and 1<=x<=5 for x in a)
 score=sum(x-1 if i%2==0 else 5-x for i,x in enumerate(a))*2.5
 assert score==person['sus'];sus.append(score)
 assert len(person['tareas'])==6
 for r in person['tareas']:
  assert r['resultado'] in ['Sí','Con ayuda','No'] and r['tiempo_s']>=0
  assert r['errores_criticos']>=0 and r['errores_no_criticos']>=0
  assert r['pista_aplicada']!='Sí' or 0<=r['segundo_pista']<=r['tiempo_s']
  assert r['resultado']!='Sí' or r['pista_aplicada']=='No'
  success+=r['resultado']=='Sí';assisted+=r['resultado']=='Con ayuda';failed+=r['resultado']=='No'
  critical+=r['errores_criticos'];noncritical+=r['errores_no_criticos']
for i,m in enumerate(expected):
 r=[x['tareas'][i] for x in p]
 assert sum(x['resultado']=='Sí' for x in r)==m['exitos_sin_ayuda']
 assert statistics.median(x['tiempo_s'] for x in r)==m['mediana_tiempo_s']
 assert sum(x['errores_criticos'] for x in r)==m['errores_criticos']
 assert sum(x['errores_no_criticos'] for x in r)==m['errores_no_criticos']
 assert all(x['tiempo_s']<=m['maximo_s'] for x in r)
h=json.loads((base/'Datos/evaluaciones_heuristicas.json').read_text(encoding='utf8'))
assert len(h)==50 and len({x['evaluador'] for x in h})==5
for name in {x['evaluador'] for x in h}:
 assert {x['heuristica'] for x in h if x['evaluador']==name}=={f'H{i}' for i in range(1,11)}
assert (success,assisted,failed,critical,noncritical)==(14,3,1,1,9)
result={'participantes':len(p),'intentos':18,'exitos_sin_ayuda':success,'con_ayuda':assisted,'no_completadas':failed,'tasa_exito':success/18,'errores_criticos':critical,'errores_no_criticos':noncritical,'sus':sus,'sus_medio':statistics.mean(sus),'evaluaciones_heuristicas':len(h),'resultado':'Comprobaciones aritméticas y de estructura satisfactorias'}
print(json.dumps(result,ensure_ascii=False,indent=2))
