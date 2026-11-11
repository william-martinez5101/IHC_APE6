from pathlib import Path
import json, subprocess
BASE=Path(__file__).resolve().parents[2]
TARGETS={"William":"APE6_FASE1/colaboracion/aportes/William.md","Emilio":"APE6_FASE1/colaboracion/aportes/Emilio.md","Pablo":"APE6_FASE1/colaboracion/aportes/Pablo.md","Manuel":"APE6_FASE1/colaboracion/aportes/Manuel.md","Jonathan":"APE6_FASE1/colaboracion/aportes/Jonathan.md"}
records=[]
for name,path in TARGETS.items():
 r=subprocess.run(["git","log","-1","--format=%H%x09%an%x09%ae%x09%aI","--",path],cwd=BASE,capture_output=True,text=True,check=True)
 fields=r.stdout.strip().split("\t")
 records.append({"integrante":name,"ruta":path,"evidencia":dict(zip(["sha","autor","correo_autor","fecha"],fields)) if len(fields)==4 else None})
output={"tipo":"Historial real del clon; revisar atribucion a cuentas en GitHub","aportes":records,"con_commit":sum(x["evidencia"] is not None for x in records)}
out=Path(__file__).with_name("evidencia_autorias.json");out.write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(output,ensure_ascii=False,indent=2))
