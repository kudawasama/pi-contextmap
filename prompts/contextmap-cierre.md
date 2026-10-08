---
description: Cierra la sesión con ContextMap (refresh + verificación + memoria viva)
argument-hint: "[qué se hizo / decisiones]"
---
Cierra esta sesión de trabajo con ContextMap:

1. **Ejecuta** `ctxmap refresh .` (scan + build preservando manuales + check).
2. **Verifica** el resultado: `ctxmap check .` sin alertas, títulos legibles,
   riesgos deduplicados, sin plantillas vacías ni `TODO (ruta.py:Ln):` crudos.
3. **Corrige** lo tosco que encontraste (lo técnico como tarjeta técnica honesta;
   lo conversado como nota con alma, con `preserve: true`).
4. **Documenta la memoria viva** (sin esperar a que te lo pidan):
   - Nota del día: `7.0-MANUAL/Diario/<fecha-de-hoy>.md` con qué se hizo, qué se
     decidió y qué queda pendiente.
   - Si hay una lección reutilizable, añádela a `8.0-KNOWLEDGE/` con el formato
     (🎯 Lección · 🛠️ Cómo se resolvió · 💬 Prompt específico · 📋 Instrucción ·
     🔗 Conexiones).
5. Regenera el vault si corregiste (`ctxmap refresh .`) y dime el resumen final:
   qué quedó cerrado, qué sigue abierto y qué commits/versiones se publicaron.

Contexto de lo trabajado: ${1:-según la conversación de esta sesión.}
