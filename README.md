# @kudawa/pi-contextmap — ContextMap IA para pi

![ContextMap IA para pi](https://raw.githubusercontent.com/kudawasama/pi-contextmap/master/assets/preview.png)

Paquete de [pi](https://pi.dev) que trae **ContextMap IA** a tus sesiones:
memoria viva del proyecto (brief para agentes + vault de Obsidian), **Second
Brain** con citas y **memoria multi-proyecto** (lecciones y decisiones de todos
tus proyectos).

Instalas el paquete y ya tienes el servidor MCP registrado, una skill con el
protocolo y tres comandos listos.

## Requisitos

El paquete **no incluye** el motor: necesita el CLI de ContextMap.

```bash
uv tool install "context-map-ai[mcp]"     # recomendado
# o
pip install "context-map-ai[mcp]"
```

Si falta, la extensión te avisa al iniciar la sesión con el comando exacto.

## Instalación

```bash
pi install npm:@kudawa/pi-contextmap     # desde npm
pi install ./pi-contextmap               # desde una carpeta local
pi list                                  # verificar
```

Desde una sesión abierta, ejecuta `/reload` para que pi lo cargue.

## Qué añade

| Recurso | Nombre | Para qué |
|---|---|---|
| Extensión | `contextmap` (MCP) | Registra el servidor MCP con 29 herramientas y avisa si falta el CLI |
| Skill | `/skill:contextmap` | Protocolo: cómo ponerse en contexto, actualizar sin ensuciar y mantener la memoria viva |
| Prompt | `/contextmap-contexto` | Poner el agente en contexto (brief + pendientes reales) |
| Prompt | `/contextmap-cierre` | Cerrar sesión: refresh, verificar, documentar y resumir |
| Prompt | `/contextmap-preguntar` | Preguntar a la memoria de todos los proyectos, con citas |

### Herramientas MCP siempre visibles

- `mcp__contextmap__context` — leer el brief ejecutivo del proyecto.
- `mcp__contextmap__personal_panorama` — semáforo de todos tus proyectos.
- `mcp__contextmap__personal_query` — buscar en lecciones y decisiones.
- `mcp__contextmap__knowledge_wiki_ask` — preguntar al Second Brain con citas.

Las 25 restantes (escanear, construir el vault, capturar notas, wiki, repaso
espaciado, importadores…) quedan disponibles vía codemode, de modo que no llenan
el contexto hasta que se necesitan.

## Uso típico

```text
/contextmap-contexto            # al empezar: qué es, en qué estado, qué falta
/contextmap-cierre              # al terminar: actualizar y documentar
/contextmap-preguntar ¿por qué usamos BM25 y no embeddings?
```

## Límites

ContextMap es **local-first**: sin red en `build`/`refresh`, OCR/embeddings/LLM
opcionales y apagados por defecto, y tus notas manuales (`preserve: true`) nunca
se borran.

## Enlaces

- Proyecto: https://github.com/kudawasama/ContextMap
- Código del paquete: https://github.com/kudawasama/pi-contextmap
- Paquete Python: https://pypi.org/project/context-map-ai/
- Galería de pi: https://pi.dev/packages
- Cambios: https://github.com/kudawasama/ContextMap/blob/master/CHANGELOG.md

## Para mantenedores

Este paquete se publica solo: sube la versión en `package.json`, crea el tag y
empuja. El workflow `.github/workflows/publish.yml` publica en npm con
**Trusted Publishing (OIDC)** — sin tokens ni códigos (requiere haber autorizado
el repo como Trusted Publisher en npmjs.com).

```bash
# nueva versión
npm version patch --no-git-tag-version   # o edita package.json
python scripts/make_preview.py           # regenerar la imagen si cambia el texto
git commit -am "chore: vX.Y.Z" && git tag vX.Y.Z && git push --follow-tags
```

## Licencia

MIT
