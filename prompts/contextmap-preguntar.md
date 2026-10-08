---
description: Pregunta a la memoria de todos tus proyectos (ContextMap personal + Second Brain)
argument-hint: "<pregunta o tema>"
---
Responde esta pregunta usando la memoria acumulada de mis proyectos, no tu
conocimiento general:

1. Busca en la memoria multi-proyecto: `ctxmap personal query "${1:-tema}"`
   (o `mcp__contextmap__personal_query`). Devuelve qué proyecto lo dijo y cuándo.
2. Si la pregunta es sobre mi Second Brain / wiki, usa
   `ctxmap wiki ask "${1:-pregunta}"` (o `mcp__contextmap__knowledge_wiki_ask`):
   responde de forma extractiva con citas `[n]`.
3. Si hace falta el estado global, mira `ctxmap personal panorama`.

Contesta en español, breve, **citando de qué proyecto y nota sale cada dato**.
Si la memoria no tiene la respuesta, dilo con claridad en lugar de inventar.
