"""Publica Issues de mejora y enlaza sus URL reales. Requiere GitHub CLI autenticado."""
from pathlib import Path
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
REPO='william-martinez5101/IHC_APE6'
REG=ROOT/'Fase4-Cierre/issues/registro_issues.json'

def gh(*args):
    p=subprocess.run(['gh',*args],cwd=ROOT,text=True,capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or 'GitHub CLI no pudo completar la operacion')
    return p.stdout.strip()

def actualizar_enlaces(registros):
    urls={x['hallazgo']:x['url'] for x in registros if x.get('url')}
    for rel in ['README.md','Fase4-Cierre/Backlog.md']:
        path=ROOT/rel
        lines=path.read_text(encoding='utf8').splitlines()
        for i,line in enumerate(lines):
            if not line.startswith('| P'):
                continue
            cols=line.split('|')
            for key,url in urls.items():
                if any(c.strip()==key for c in cols):
                    cols[-2]=' [Issue]('+url+') '
                    lines[i]='|'.join(cols)
        if len(urls)==len(registros):
            for i,line in enumerate(lines):
                if line.startswith('No se crearon Issues:'):
                    lines[i]='Los cinco Issues se publicaron o reutilizaron mediante GitHub CLI; sus URLs reales se muestran en el backlog. [Registro](Fase4-Cierre/issues/registro_issues.json). Las mejoras siguen sujetas a implementacion y validacion.'
            if rel.endswith('Backlog.md'):
                lines.append('\nActualizacion: todos los Issues del registro tienen URL real. El primer intento por la integracion devolvio HTTP 403; la publicacion posterior uso la cuenta autenticada en GitHub CLI.')
        path.write_text('\n'.join(lines)+'\n',encoding='utf8')
    path=ROOT/'Fase4-Cierre/hallazgos.json'
    hallazgos=json.loads(path.read_text(encoding='utf8'))
    for h in hallazgos:
        if h['id'] in urls:
            h['issue_url']=urls[h['id']];h['issue_estado']='creado_o_reutilizado'
    path.write_text(json.dumps(hallazgos,ensure_ascii=False,indent=2)+'\n',encoding='utf8')

def main():
    if not shutil.which('gh'):
        raise RuntimeError('Instala GitHub CLI oficial y ejecuta gh auth login con tu cuenta autorizada.')
    gh('auth','status')
    registros=json.loads(REG.read_text(encoding='utf8'))
    existentes=json.loads(gh('issue','list','--repo',REPO,'--state','all','--limit','500','--json','title,url'))
    for record in registros:
        found=[i for i in existentes if i['title']==record['title']]
        if len(found)>1:
            raise RuntimeError('Hay varios Issues con el mismo titulo; revisa duplicados antes de continuar.')
        if found:
            url=found[0]['url']
        else:
            url=gh('issue','create','--repo',REPO,'--title',record['title'],'--body-file',str(ROOT/record['body_file']))
            if not url.startswith('https://github.com/'+REPO+'/issues/'):
                raise RuntimeError('La respuesta no contiene una URL de Issue reconocida; verifica antes de reintentar.')
            existentes.append({'title':record['title'],'url':url})
        record['url']=url;record['estado']='creado_o_reutilizado'
        REG.write_text(json.dumps(registros,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        actualizar_enlaces(registros)
        print(record['hallazgo']+': '+url)

if __name__=='__main__':
    try:main()
    except (RuntimeError,OSError,ValueError) as e:
        sys.exit('No se completo la publicacion: '+str(e))
