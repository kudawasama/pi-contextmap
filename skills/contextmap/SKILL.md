---
name: contextmap
description: Protocolo para trabajar con la memoria viva de ContextMap (brief del proyecto, vault de Obsidian, Second Brain y lecciones multi-proyecto). Úsala al empezar a trabajar en un proyecto con ContextMap, al preguntar «qué quedó pendiente», al cerrar una sesión o al buscar en la memoria de otros proyectos.
---

# ContextMap — memoria viva del proyecto

ContextMap convierte lo que se conversa y decide en un **contexto reutilizable**
para las IAs: un brief (`.context-map/CONTEXT.md`), un vault de Obsidian
navegable y una memoria personal multi-proyecto. El script propone, **el agente
dispone**: el contexto solo es válido cuando el agente lo revisó y lo corrigió.

Herramientas MCP disponibles: `mcp__contextmap__context` (brief),
`personal_panorama`, `personal_query`, `knowledge_wiki_ask` (siempre visibles) y
el resto en codemode: `refresh`, `scan`, `build`, `check`, `doctor`,
`knowledge_inbox_*`, `knowledge_wiki_*`, `knowledge_review_*`, `export`…

## Protocolo de inicio (leer en este orden)

1. **Verifica el proyecto**: el vault es `.context-map/vault-<Proyecto>/`. Si el
   usuario pregunta por otro proyecto, dilo ANTES de responder.
2. **Brief**: lee `.context-map/CONTEXT.md` (o usa `mcp__contextmap__context`).
   Mira su sección **«Estado del Contexto»**: si avisa de que el diario manual es
   más nuevo que el build, el contexto está viejo → `ctxmap refresh .` primero.
3. **Pendientes REALES** (cruce obligatorio, nunca una sola fuente):
   - `7.0-MANUAL/BACKLOG.md` — pendientes conversados con el usuario.
   - `7.0-MANUAL/Diario/` — el diario más reciente (lo hecho y lo decidido).
   - `5.0-BACKLOG/5.1-Tareas.md` — TODOs del código (deuda técnica).
   - `.context-map/raw/docs/` y `3.2-DOCUMENTOS/` — conocimiento documental.
4. **Riesgos y propósito**: `4.0-RIESGOS/` y `1.0-PROPOSITO/` antes de proponer
   cambios.
5. **Código real** antes de diagnosticar: nunca supongas rutas ni lógica.

> ⚠️ Nunca respondas «¿qué quedó pendiente?» con un solo documento (auditoría,
> CHANGELOG, docs sueltos). La fuente de verdad es brief + backlog manual +
> diario + documentos.

## Comandos esenciales

```bash
ctxmap refresh .                 # scan + build (preserva manuales) + check
ctxmap build --clean --brief     # reconstruir vault + brief desde cero
ctxmap check .                   # readiness 0-100 y salud del vault
ctxmap wrap .                    # cierre de sesión (refresh + resumen)
ctxmap personal panorama         # semáforo de TODOS los proyectos
ctxmap personal query "tema"     # buscar en lecciones y decisiones (FTS5/BM25)
ctxmap inbox add --clipboard     # capturar una web (Web Clipper) al Second Brain
ctxmap wiki ask "pregunta"       # responder con citas de la wiki (local)
```

## Ciclo de actualización (no basta con correr el script)

1. **Ejecuta** `ctxmap refresh .`.
2. **Verifica** los criterios: `check` sin alertas, títulos legibles (sin
   `TODO (ruta.py:Ln):` crudo), índices con propósito y no solo conteos, riesgos
   deduplicados, sin plantillas vacías.
3. **Corrige** lo tosco: lo técnico como tarjeta técnica honesta; lo conversado
   como nota con alma en `7.0-MANUAL/` (frontmatter `preserve: true`).
4. **Regenera y re-verifica** si corregiste.

## Memoria viva (regla fundamental)

- **Documenta en el momento**: si surge una idea, decisión, porqué o lección,
  escríbela sin esperar a que te lo pidan.
- **Nota del día**: `7.0-MANUAL/Diario/<fecha>.md` — qué se hizo, qué se decidió,
  qué falta.
- **Lección reutilizable**: `8.0-KNOWLEDGE/` con el formato fijo
  (🎯 Lección · 🛠️ Cómo se resolvió · 💬 Prompt específico · 📋 Instrucción ·
  🔗 Conexiones).
- **Nunca borres historia**: lo tosco se redacta, no se elimina.

## Límites (lo que NO se hace)

- No meter dependencias pesadas en la base: OCR, embeddings y LLM son
  **opcionales** y se activan por decisión del usuario.
- No usar red en `build`/`refresh`: cualquier captura es explícita.
- `7.0-MANUAL/` es zona protegida: el build jamás la borra.

## Topología del vault (regla inamovible)

Cada nota cuelga de **exactamente un padre** (árbol puro). Los índices de concepto
usan nombre único por estado (`X-Pendientes.md` ≠ `X-Completas.md`). Las notas
hoja solo enlazan a su padre con `⬅ Volver a …`. Un enlace roto o una nota sin
padre es un bug: verifícalo con `ctxmap check .` y
`python -m pytest context_map/__tests__/test_topologia_arbol.py`.
