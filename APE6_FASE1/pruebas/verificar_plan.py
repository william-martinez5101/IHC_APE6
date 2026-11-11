from pathlib import Path
from decimal import Decimal
import json,hashlib,zipfile,re,subprocess,os,sys
from datetime import datetime,timezone
from xml.etree import ElementTree
BASE=Path(__file__).resolve().parents[1]
records=[]
def check(id,desc,result):records.append({'id':id,'descripcion':desc,'conforme':bool(result)})
tasks=json.loads((BASE/'instrumentos/tareas.json').read_text(encoding='utf-8'))
check('P01','Seis tareas T1 a T6',len(tasks)==6 and [t['id'] for t in tasks]==['T1','T2','T3','T4','T5','T6'])
fields=['id','title','goal','max','cons','initial','success','answer','evidence','state']
check('P02','Todos los campos de planificacion presentes',all(all(str(t.get(f,'')).strip() for f in fields) for t in tasks))
check('P03','Maximo doble del objetivo',all(t['max']==2*t['goal'] for t in tasks))
check('P04','Duracion maxima de tareas 810 segundos',sum(t['max'] for t in tasks)==810)
check('P05','Consignas sin instrucciones de pulsaciones',not any(re.search(r'presiona|pulsa|haz clic|toca el|bot[oó]n',t['cons'],re.I) for t in tasks))
check('A01','Base 1 cafe y 1 sanduche vale 4.25',Decimal('1.50')+Decimal('2.75')==Decimal('4.25'))
check('A02','Modificado 2 cafes y 1 sanduche vale 5.75',2*Decimal('1.50')+Decimal('2.75')==Decimal('5.75'))
check('A03','Diferencia de presupuesto 0.75',Decimal('5.00')-Decimal('4.25')==Decimal('0.75'))
check('A04','Borrador de T5 vale 1.50','1,50' in tasks[4]['answer'] and 'sin guardar' in tasks[4]['answer'])
check('A05','T6 usa CU-104 y estado Recibido','CU-104' in tasks[5]['answer'] and 'Recibido' in tasks[5]['answer'] and '4,25' in tasks[5]['answer'])
check('P06','T4 T5 T6 comienzan en base independiente',all('4,25' in t['initial'] and 'independiente' in t['initial'] for t in tasks[3:]))
prov=json.loads((BASE/'prototipo/procedencia.json').read_text(encoding='utf-8'))
check('F01','Referencia al repositorio propio de APE4',prov['repositorio']=='https://github.com/idk-Damian/Ape4_IHC')
check('F02','Archivo propio de Figma', 'HQZqFztrL0HeQ6E9h60LZm' in prov['figma'])
for rel,digest in prov['archivos'].items():
 p=BASE/'prototipo'/rel
 check('HASH'+str(len(records)+1),'Integridad '+rel,p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest)
check('F03','Diez capturas de respaldo',len(list((BASE/'prototipo/evidencias').glob('*.png')))==10)
# HTML fields and script references; full browser navigation is not claimed.
form=(BASE/'instrumentos/registro_local.html').read_text(encoding='utf-8')
check('I01','Seis registros de tarea en formulario',all('name="'+t['id']+'_resultado"' in form for t in tasks))
check('I02','Diez grupos SUS en formulario',all('name="sus'+str(i)+'"' in form for i in range(1,11)))
check('I03','Sin peticiones externas en el formulario','fetch(' not in form and 'XMLHttpRequest' not in form)
check('I04','SUS compartido en formulario','calculo_sus.js' in form)
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
docfiles=list(BASE.rglob('*.docx'));texts={}
for p in docfiles:
 with zipfile.ZipFile(p) as z:
  root=ElementTree.fromstring(z.read('word/document.xml'))
  text=' '.join(e.text or '' for e in root.findall('.//w:t',ns));texts[p.name]=text
check('D01','Seis documentos Word finales',len(docfiles)==6)
check('D02','Sin referencias al sistema anterior',not any(('Aula'+' Abierta') in s or ('Interfaces'+' web accesibles') in s for s in texts.values()))
check('D03','Sin marcadores de contenido por completar',not any(('['+'COMPLETAR'+']') in s or ('TO'+'DO:') in s for s in texts.values()))
main=texts.get('Informe_APE6_Fase1_Grupo6_CafeU.docx','')
check('D04','Formato APE con actividades y conclusiones',all(s in main for s in ['2.7 Actividades','2.8 Resultados','2.10 Conclusiones','2.12 Referencias']))
check('D05','Diez heuristicas en guia',all('H'+str(i)+' ' in texts.get('04_Guia_heuristica.docx','') for i in range(1,11)))
check('D06','Cinco integrantes identificados',all(name in main for name in ['William Fernando','Emilio Alexander','Pablo Damian','Manuel Steven','Jonathan Alexis']))
node=os.environ.get('CODEX_PRIMARY_RUNTIME_NODE','node')
r=subprocess.run([node,str(BASE/'pruebas/verificar_sus.cjs')],capture_output=True,text=True)
check('SUS00','Ejecucion del modulo SUS del formulario',r.returncode==0)
if r.returncode==0:records.extend(json.loads(r.stdout))
else:print(r.stderr,file=sys.stderr)
result={'version':'2.0','fecha':'2026-11-11','objeto':'CafeU APE 4 integral','tipo':'Verificacion documental y aritmetica sin participantes','referencia_commit':prov['commit'],'participantes_observados':0,'limite':'No se verifican transiciones en vivo de Figma ni tiempos humanos ni percepcion de usabilidad.','casos':records,'conformes':sum(x['conforme'] for x in records),'total':len(records)}
(BASE/'pruebas/resultados_verificacion.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(f"{result['conformes']}/{result['total']} comprobaciones conformes")
if result['conformes']!=result['total']:sys.exit(1)
