"""
Generates a LinkedIn-friendly OpenGraph preview banner for the
resume website (https://marshall-wagner.github.io).

Output: images/site-preview.png (1200x630, LinkedIn OG image ratio)

Usage:
    python3 generate_og_preview.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1200
HEIGHT = 630

BG = (249, 250, 251)
PRIMARY = (30, 58, 138)
ACCENT = (14, 165, 233)
TEXT = (31, 41, 55)
MUTED = (107, 114, 128)
BORDER = (229, 231, 235)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
FONT_REG = FONT_DIR / "DejaVuSans.ttf"
FONT_BOLD = FONT_DIR / "DejaVuSans-Bold.ttf"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(str(path), size)


def build(output_path: Path) -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # Left accent bar (visual identity continuity with architecture diagrams)
    draw.rectangle((0, 0, 18, HEIGHT), fill=ACCENT)

    left = 80

    # Name — large, primary blue
    name_font = font(92, bold=True)
    draw.text((left, 90), "MARSHALL WAGNER", fill=PRIMARY, font=name_font)

    # Role — medium, dark text
    role_font = font(50)
    draw.text((left, 220), "IT Administrator", fill=TEXT, font=role_font)

    # Subtitle — muted gray
    sub_font = font(32)
    draw.text(
        (left, 300),
        "Network & Cybersecurity  ·  Self-Hosted Infrastructure",
        fill=MUTED,
        font=sub_font,
    )

    # Separator line
    sep_y = 390
    draw.line((left, sep_y, WIDTH - 80, sep_y), fill=BORDER, width=2)

    # Tech keywords (two rows)
    kw_font = font(24)
    draw.text(
        (left, 420),
        "Enterprise Networks  ·  5G WAN  ·  WPA3-SAE  ·  Wireguard  ·  AdGuard Home",
        fill=TEXT,
        font=kw_font,
    )
    draw.text(
        (left, 462),
        "Vaultwarden  ·  Ubuntu Pro  ·  Defense-in-Depth Security  ·  Linux/Windows",
        fill=TEXT,
        font=kw_font,
    )

    # URL footer — accent blue, bold
    url_font = font(28, bold=True)
    draw.text((left, 545), "marshall-wagner.github.io", fill=ACCENT, font=url_font)

    img.save(str(output_path), format="PNG", optimize=True)


def main() -> None:
    out_path = Path(__file__).resolve().parent / "images" / "site-preview.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    build(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
