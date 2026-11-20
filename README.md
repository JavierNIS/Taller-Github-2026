# Calculadora - ETSIIT Tech Club

```
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
``` 

Javi buapetón

Proyecto de práctica del taller **Git para expertos**. 
Es una calculadora en Python con interfaz gráfica (tkinter) y tests. 
No hace falta saber Python: lo que vamos a practicar es git.

```
calc/core.py     lógica y registro de operaciones (OPERATIONS)
calc/ops/        un archivo por familia de operaciones
calc/gui.py      la ventana (un botón por cada operación registrada)
tests/           tests; se ejecutan con run_tests.py
.githooks/       hook que obliga a usar Conventional Commits
```

## 1. Preparación

```bash
git clone https://github.com/JavierNIS/Taller-GitHub.git
cd calculadora

# Ejecuta los tests (según tu sistema: python, python3 o py)
python run_tests.py

# Activa el hook de commits de este repo
git config core.hooksPath .githooks

# Opcional: abre la calculadora (necesita tkinter)
python -m calc
```

Configura una herramienta para `git difftool` (elige una):

```bash
git config --global diff.tool vimdiff     # viene con Git para Windows
git config --global diff.tool meld        # si tienes meld instalado
# VS Code:
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```

## 2. Trabajar en una issue

Cada issue dice qué archivos crear o modificar. El ciclo es siempre este:

```bash
git switch -c <nº-issue>-<nombre>   # una rama por issue
# ...cambios...
python run_tests.py
git diff                            # qué has cambiado
git add .
git commit -m "feat: añadir ..."
```

## 3. Mensajes de commit

Formato [Conventional Commits](https://www.conventionalcommits.org/es/): `<tipo>(<ámbito opcional>): <descripción>`

| Tipo | Para qué | Versión |
|---|---|---|
| `feat` | funcionalidad nueva | sube MINOR (0.**1**.0 → 0.**2**.0) |
| `fix` | corrección de un bug | sube PATCH (0.1.**0** → 0.1.**1**) |
| `feat!` / `BREAKING CHANGE:` | cambio incompatible | sube MAJOR |
| `docs`, `test`, `refactor`, `style`, `chore`… | el resto | no cambia la versión |

## 4. Pull request

```bash
# 1. Pulsa "Fork" en GitHub para tener tu copia del repo
# 2. Añádela como remoto y sube tu rama:
git remote add mifork https://github.com/<TU-USUARIO>/calculadora.git
git push mifork <tu-rama>
# 3. En GitHub, "Compare & pull request". En la descripción escribe: Closes #<nº-issue>
```
