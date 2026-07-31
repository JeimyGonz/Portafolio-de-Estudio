# generar.py
# Lee datos.py y genera index.html automáticamente.

from datos import documentos

# --- Plantilla de una tarjeta individual ---
def crear_tarjeta(doc):
    return f"""
    <a class="card" href="./{doc['carpeta']}/{doc['archivo']}">
      <span class="code">{doc['codigo']}</span>
      <h2>{doc['titulo']}</h2>
      <p>{doc['descripcion']}</p>
      <span class="stamp">interactivo</span>
    </a>
    """

# --- Construir todas las tarjetas juntas ---
tarjetas_html = ""
for doc in documentos:
    tarjetas_html += crear_tarjeta(doc)

# --- Plantilla completa de la página ---
pagina = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Índice de Estudio — Jeimy González</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Special+Elite&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{{
    --paper: #F3ECDC;
    --paper-card: #FBF7EC;
    --ink: #22303F;
    --kraft: #C9AD7F;
    --stamp: #9E3B34;
    --line: #C3B392;
    --accent: #3F6357;
  }}
  *{{ box-sizing: border-box; }}
  body{{
    margin:0;
    background: var(--paper);
    color: var(--ink);
    font-family: 'IBM Plex Sans', sans-serif;
  }}
  a{{ color: inherit; }}
  .drawer{{ max-width: 920px; margin: 0 auto; padding: 64px 24px 32px; }}
  .drawer-label{{
    display:inline-block; font-family:'IBM Plex Mono', monospace;
    font-size: 0.75rem; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--accent); border: 1px solid var(--accent); padding: 4px 10px; margin-bottom: 20px;
  }}
  h1{{
    font-family: 'Special Elite', monospace; font-weight: 400;
    font-size: clamp(2.2rem, 5vw, 3.4rem); line-height: 1.15; margin: 0 0 12px;
  }}
  .drawer p.sub{{ max-width: 56ch; font-size: 1.05rem; line-height: 1.6; color: #4A5A68; }}
  .drawer .meta{{ font-family:'IBM Plex Mono', monospace; font-size: 0.8rem; color: #7A6C4E; margin-top: 18px; }}
  hr.divider{{ max-width: 920px; margin: 8px auto 0; border: none; border-top: 2px solid var(--ink); }}
  .catalog{{
    max-width: 920px; margin: 40px auto 100px; padding: 0 24px;
    display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 28px;
  }}
  .card{{
    position: relative; background: var(--paper-card); border: 1px solid var(--line);
    box-shadow: 3px 3px 0 rgba(34,48,63,0.08); padding: 22px 20px 20px;
    text-decoration: none; color: var(--ink);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    display: flex; flex-direction: column; min-height: 190px;
  }}
  .card:hover, .card:focus-visible{{
    transform: translate(-2px,-2px); box-shadow: 5px 5px 0 rgba(34,48,63,0.16); outline: none;
  }}
  .card:focus-visible{{ outline: 2px solid var(--accent); outline-offset: 2px; }}
  .card::before{{
    content:''; position:absolute; top: 14px; left: 14px; width: 10px; height: 10px;
    border-radius: 50%; background: var(--paper); box-shadow: inset 0 0 0 1px var(--line);
  }}
  .card .code{{
    font-family: 'IBM Plex Mono', monospace; font-size: 0.72rem; letter-spacing: 0.08em;
    color: var(--stamp); margin-left: 26px; margin-bottom: 10px;
  }}
  .card h2{{ font-family: 'Special Elite', monospace; font-weight: 400; font-size: 1.25rem; margin: 0 0 10px; }}
  .card p{{ font-size: 0.9rem; line-height: 1.55; color: #4A5A68; margin: 0; flex-grow: 1; }}
  .card .stamp{{
    align-self: flex-end; margin-top: 14px; font-family: 'IBM Plex Mono', monospace;
    font-size: 0.68rem; letter-spacing: 0.05em; text-transform: uppercase; color: var(--accent);
    border: 1px dashed var(--accent); padding: 3px 8px; transform: rotate(-2deg);
  }}
  footer{{
    max-width: 920px; margin: 0 auto 60px; padding: 0 24px;
    font-family:'IBM Plex Mono', monospace; font-size: 0.75rem; color: #8A7C5E;
  }}
</style>
</head>
<body>
  <div class="drawer">
    <span class="drawer-label">USAC · Ciencias y Sistemas</span>
    <h1>Índice de Estudio</h1>
    <p class="sub">Un fichero de los documentos interactivos que voy creando mientras estudio.</p>
    <p class="meta">Jeimy González — actualizado continuamente</p>
  </div>
  <hr class="divider">
  <div class="catalog">
    {tarjetas_html}
  </div>
  <footer>github.com/JeimyGonz/Portafolio-de-Estudio</footer>
</body>
</html>
"""

# --- Guardar el resultado en index.html ---
with open("index.html", "w", encoding="utf-8") as archivo:
    archivo.write(pagina)

print("¡Listo! index.html fue generado correctamente.")