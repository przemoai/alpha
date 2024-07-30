# alpha


### linter & code checking
```bash
ruff format .
ruff check . --fix
mypy src
```

### uv pip compile
```bash
uv pip compile requirements/requirements.in -o requirements/requirements.txt 
uv pip compile requirements/requirements-dev.in -o requirements/requirements-dev.txt 
```