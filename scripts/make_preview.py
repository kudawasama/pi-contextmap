"""Genera la imagen de presentación (``assets/preview.png``) del paquete.

La usa la galería de pi (``pi.image`` en ``package.json``) como previsualización.

Uso:
    python scripts/make_preview.py
"""

from __future__ import annotations

import os

from PIL import Image, ImageDraw, ImageFont

ANCHO, ALTO = 1200, 630
AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(os.path.dirname(AQUI), "assets", "preview.png")

FONDO = (11, 16, 32)
PANEL = (17, 24, 46)
BLANCO = (240, 244, 255)
GRIS = (150, 163, 190)
ACENTO = (88, 166, 255)
ACENTO2 = (163, 113, 247)


def _fuente(nombre: str, tam: int) -> ImageFont.FreeTypeFont:
    """Carga una fuente de Windows con respaldo razonable."""
    for candidata in (nombre, "arial.ttf"):
        try:
            return ImageFont.truetype(os.path.join("C:/Windows/Fonts", candidata), tam)
        except OSError:
            continue
    return ImageFont.load_default()


def _degradado(imagen: Image.Image) -> None:
    """Pinta un degradado horizontal suave entre panel y fondo."""
    ancho, alto = imagen.size
    for x in range(ancho):
        t = x / ancho
        color = tuple(int(PANEL[i] * (1 - t) + FONDO[i] * t) for i in range(3))
        ImageDraw.Draw(imagen).line([(x, 0), (x, alto)], fill=color)


def _grafo(dibujo: ImageDraw.ImageDraw, origen_x: int) -> None:
    """Dibuja un pequeño grafo memoria-viva (nodos y aristas) a la derecha."""
    nodos = [
        (origen_x + 150, 200, 26, ACENTO),
        (origen_x + 300, 150, 18, ACENTO2),
        (origen_x + 320, 300, 22, ACENTO),
        (origen_x + 170, 380, 16, ACENTO2),
    ]
    aristas = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]
    for a, b in aristas:
        dibujo.line([nodos[a][:2], nodos[b][:2]], fill=(60, 78, 120), width=3)
    for x, y, r, color in nodos:
        dibujo.ellipse([x - r, y - r, x + r, y + r], fill=color)


def main() -> str:
    """Crea la imagen y devuelve la ruta escrita."""
    imagen = Image.new("RGB", (ANCHO, ALTO), FONDO)
    _degradado(imagen)
    dibujo = ImageDraw.Draw(imagen)

    # Barra de acento superior.
    for x in range(ANCHO):
        t = x / ANCHO
        color = tuple(int(ACENTO[i] * (1 - t) + ACENTO2[i] * t) for i in range(3))
        dibujo.line([(x, 0), (x, 8)], fill=color)

    dibujo.text((80, 122), "ContextMap IA", font=_fuente("arialbd.ttf", 78), fill=BLANCO)
    dibujo.text(
        (82, 226), "Memoria viva del proyecto para pi",
        font=_fuente("arial.ttf", 38), fill=ACENTO,
    )
    for i, linea in enumerate(
        [
            "brief ejecutivo · pendientes reales del proyecto",
            "vault de Obsidian con topología en árbol",
            "Second Brain con citas + memoria multi-proyecto",
        ]
    ):
        dibujo.ellipse([84, 306 + i * 46, 96, 318 + i * 46], fill=ACENTO2)
        dibujo.text((112, 298 + i * 46), linea, font=_fuente("arial.ttf", 30), fill=GRIS)

    pie = "pi install npm:@kudawa/pi-contextmap"
    caja = dibujo.textbbox((0, 0), pie, font=_fuente("arial.ttf", 26))
    dibujo.rounded_rectangle(
        [80, 512, 80 + (caja[2] - caja[0]) + 44, 566], radius=12, fill=(23, 32, 58)
    )
    dibujo.text((102, 526), pie, font=_fuente("arial.ttf", 26), fill=BLANCO)

    _grafo(dibujo, 720)

    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    imagen.save(SALIDA, "PNG", optimize=True)
    return SALIDA


if __name__ == "__main__":
    print(main())
