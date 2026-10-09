/**
 * ContextMap IA — memoria viva del proyecto para pi.
 *
 * Registra el servidor MCP de ContextMap (brief del proyecto, búsqueda en
 * lecciones y decisiones de todos los proyectos, Second Brain con citas,
 * captura de notas y sincronización del vault) y avisa con instrucciones
 * claras si el CLI `ctxmap` no está instalado.
 *
 * Requisito: `uv tool install "context-map-ai[mcp]"` (o `pip install
 * "context-map-ai[mcp]"`).
 */

import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const DESCRIPCION =
	"Memoria viva de ContextMap: brief del proyecto, busqueda en lecciones y decisiones de todos los proyectos, Second Brain (wiki con citas), captura de notas y sincronizacion del vault.";

const INSTALACION =
	'ContextMap no esta instalado: ejecuta `uv tool install "context-map-ai[mcp]"` (o `pip install "context-map-ai[mcp]"`) y reinicia pi.';

export default function (pi: ExtensionAPI) {
	// Se registra al cargar la extension para que el servidor conecte con la sesion.
	pi.registerMcpServer("contextmap", {
		command: "ctxmap",
		args: ["mcp"],
		description: DESCRIPCION,
		// Lectura de memoria: siempre visible (bajo coste, alto valor).
		// El resto de herramientas quedan en codemode, donde el modelo las alcanza
		// cuando las necesita sin llenar el contexto.
		toolExposure: {
			context: "direct",
			context_diff: "direct",
			personal_panorama: "direct",
			personal_query: "direct",
			knowledge_wiki_ask: "direct",
		},
	});

	// Si el CLI no existe, se retira el registro (evita errores de conexion
	// ruidosos) y se explica exactamente como instalarlo.
	pi.on("session_start", async (_event, ctx) => {
		const { code } = await pi.exec("ctxmap", ["--version"]);
		if (code !== 0) {
			pi.unregisterMcpServer("contextmap");
			if (ctx.hasUI) {
				ctx.ui.notify(INSTALACION, "warning");
			}
			return;
		}
		// Revision idempotente del ecosistema al iniciar: pone al dia SOLO las
		// reglas/skills propias de ContextMap (si ya estan al dia, no cambia nada).
		// NO bloquea el arranque; si falla, se ignora.
		void pi.exec("ctxmap", ["adapt", "--revisar", "--quiet"]).catch(() => {});
	});
}
