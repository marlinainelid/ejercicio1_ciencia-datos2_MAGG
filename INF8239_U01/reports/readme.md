# INF-8239 U01 - Reproducible Environment

## Sistema operativo
- Windows 10

## Versiones
- Python: 3.13.0  
- Git: 2.45.0  

## Entorno virtual
- Intérprete usado: `.venv`  
- Verificado en notebook con `sys.executable` → contiene `.venv`

## Pruebas
- Ejecución de `pytest` → salida: `1 passed`

## Estructura del proyecto


## Git
- Primer commit:  

- Verificado con `git log --oneline`

## Comandos usados
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
git init
git add .
git commit -m "chore: create INF-8239 reproducible environment"

