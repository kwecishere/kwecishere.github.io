"""Static SEO site for Chucky Assets (https://kwecishere.github.io).

Run:  python3 _build/build.py
Data: _build/catalog.json (one entry per itch.io page: slug, title, desc, price, cover, tags, cls, shot)
Writes index.html, category pages, one page per pack under packs/<slug>/, sitemap.xml, robots.txt, 404.html.
Every page links to the itch.io store page; nothing is sold here.
"""
import json, os, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://kwecishere.github.io'
STORE = 'https://chuckyassets.itch.io'
BUNDLE = 'all-in-one-bundle'
TODAY = datetime.date.today().isoformat()
N_BUNDLE = 37   # packs inside the All-in-One Bundle
E = html.escape

CAT = json.load(open(os.path.join(ROOT, '_build', 'catalog.json')))
BY = {c['slug']: c for c in CAT}

# ------------------------------------------------------------------ collections
COLLECTIONS = [
    {
        'id': 'psx-horror-assets',
        'name': 'PSX Horror Asset Packs (LO-FI DREAD)',
        'short': 'PSX Horror',
        'title': 'PSX Horror Asset Packs for Godot 4, Unity & Unreal – PS1-Style Low-Poly',
        'meta': 'PS1-style low-poly horror asset packs: abandoned hospital, haunted forest, nuclear backrooms, dead mall, post-Soviet zone, weapons, textures and UI. GLB + OBJ, Godot 4 demos.',
        'intro': ('LO-FI DREAD is a series of PS1 / PSX-style horror asset packs. Every pack uses the same real-world scale, '
                  'a small 15-bit texture atlas and the same PSX shader (vertex snapping and affine texture warping), so you can '
                  'mix an abandoned hospital with a haunted forest or a dead shopping mall in one game. Most packs ship as a ready '
                  'Godot 4 project with a walkable demo level; the GLB and OBJ files also work in Unity, Unreal Engine and Blender.'),
        'slugs': ['dead-mall-psx-abandoned-shopping-mall', 'sector-7-psx-nuclear-backrooms-horror-asset-pack',
                  'ward-13-psx-abandoned-hospital-horror-asset-pack', 'hollow-pines-psx-haunted-forest-cabin-asset-pack',
                  'zona-86-psx-post-soviet-survival-horror-asset-pack', 'last-resort-psx-horror-weapons-items-ui-pack',
                  'psx-horror-textures', 'psx-survival-horror-ui-kit', 'psx-human-organs',
                  'shadow-systems-godot-4-survival-horror-systems-kit', 'lofi-dread-free-psx-horror-sampler',
                  'psx-survival-horror-ui-kit-free-sample', 'psx-survival-horror-ui-kit-vol2', 'dead-mall-free-sample'],
        'faq': [
            ('Which engines do the PSX horror packs support?', 'Godot 4 gets a ready project with demo levels and the PSX shader. The GLB and OBJ models import into Unity, Unreal Engine 5 and Blender; textures are plain PNG atlases.'),
            ('Do the packs share the same scale and style?', 'Yes. All LO-FI DREAD packs use real-world metres, a 2 m modular grid and the same PS1 shader, so pieces from different packs fit together.'),
            ('Is there a free version?', 'Yes, the LO-FI DREAD Free Sampler has 15 models, textures and the PSX shader in a small Godot 4 gallery.'),
        ],
    },
    {
        'id': 'modern-pixel-art-tilesets',
        'name': 'Modern Town – Top-Down 16x16 Tilesets & Characters',
        'short': 'Modern Town',
        'title': 'Modern Top-Down 16x16 Pixel Art Tilesets for Godot, RPG Maker MZ, Unity & Tiled',
        'meta': 'Modern top-down 16x16 pixel art tilesets: hospital, supermarket, subway, police station, airport, museum, science lab, space station, gym, vehicles and streets, plus animated 16x32 characters.',
        'intro': ('Modern Town is a set of top-down (3/4 view) pixel art tilesets drawn on the same 16 px grid with the same outline, '
                  'palette and light direction. Every pack comes in 16, 32 and 48 px, with and without baked shadows, and ships Tiled '
                  '(.tsx/.tmx) files, Godot 4 TileSets, RPG Maker MZ sheets and single PNG sprites for Unity and GameMaker. '
                  'The animated 16x32 characters (town NPCs and a sci-fi crew) use the same style.'),
        'slugs': ['modern-hospital-clinic-tileset', 'modern-supermarket-tileset', 'subway-station-tileset', 'science-lab-tileset',
                  'modern-police-station-jail-tileset', 'modern-airport-terminal-tileset', 'modern-museum-gallery-tileset',
                  'modern-space-station-tileset', 'modern-gym-fitness-tileset', 'modern-town-characters',
                  'space-crew-aliens-characters', 'modern-town-vehicles-streets', 'modern-town-tileset-free-sample',
                  'modern-gym-fitness-free-sample', 'space-crew-aliens-free-sample'],
        'faq': [
            ('What tile size are the Modern Town tilesets?', 'They are drawn at 16x16 and exported at 16, 32 and 48 px with nearest-neighbour scaling, so they stay crisp. Use the 48 px sheets for RPG Maker MZ.'),
            ('Do they work in Godot 4 and Tiled?', 'Yes. Each pack has Godot 4 .tres TileSets, Tiled .tsx tilesets and sample .tmx maps, plus single PNG sprites for any other engine.'),
            ('Are there characters that match?', 'Yes: Modern Town Characters (41 animated NPCs) and Space Crew & Aliens (54 sci-fi characters) use the same scale, outline and shadow.'),
        ],
    },
    {
        'id': 'psx-low-poly-3d-models',
        'name': 'PSX Low-Poly 3D: Nature, Farm, Christmas & Vehicles',
        'short': 'PSX World & Vehicles',
        'title': 'PSX Low-Poly 3D Models: Nature, Farm Animals, Christmas Village & Retro Cars (Godot 4)',
        'meta': 'PS1-style low-poly 3D models for cozy and retro games: trees in 4 seasons, farm and orchard, animated farm animals, Christmas village, Santa sleigh, retro cars and a drivable pickup.',
        'intro': ('PS1-style low-poly models for cozy, retro and seasonal games: forests in four seasons, a farm with an orchard, '
                  'animated farm animals, a snowy Christmas village with Santa\'s sleigh and a husky sled team, and drivable retro cars. '
                  'Models are GLB + OBJ with tiny textures; most packs include a Godot 4 demo you can walk around or drive.'),
        'slugs': ['psx-nature-pack', 'psx-farm-orchard', 'psx-farm-animals', 'psx-christmas-village',
                  'psx-santa-sleigh-flying-reindeer', 'psx-christmas-sled-team', 'psx-cars-low-poly-vehicle-pack',
                  'psx-80s-pickup-truck', 'psx-cars-free-sample', 'psx-farm-animals-free-sample',
                  'psx-farm-orchard-free-sample', 'psx-christmas-village-free-sample', 'psx-fruit-blaster'],
        'faq': [
            ('Are the animals and vehicles animated?', 'The farm animals, reindeer and huskies have baked animations (walk, run, idle and more). Cars and the pickup have separate wheel nodes and a drivable Godot 4 demo.'),
            ('Which formats are included?', 'GLB (glTF 2.0) and OBJ + MTL for every model, with small PNG textures. They import into Godot 4, Unity, Unreal and Blender.'),
            ('Can I try them first?', 'Yes, there are free samples for the cars, farm animals, orchard and Christmas village.'),
        ],
    },
    {
        'id': 'cozy-fantasy-pixel-art',
        'name': 'Cozy & Fantasy Pixel Art',
        'short': 'Cozy & Fantasy',
        'title': 'Cozy & Fantasy Pixel Art: Winter Village Tilesets, Interiors, Spell VFX & Characters',
        'meta': 'Cozy and fantasy pixel art for top-down and side-scrolling games: Frostbrook snow village tilesets, DLCs and villagers, bakery and school interiors, elemental spell VFX, caped fantasy heroes.',
        'intro': ('Pixel art for cozy and fantasy games: the Frostbrook snow village with its Christmas and town-interiors DLCs, '
                  'a bakery café and a school interior set, elemental spell effects, caped fantasy heroes and more. '
                  'Tilesets ship in 16, 32 and 48 px with Tiled, Godot 4 and RPG Maker MZ files.'),
        'slugs': ['frostbrook-snow-village-tileset', 'frostbrook-christmas-dlc', 'frostbrook-town-interiors-dlc',
                  'bakery-cafe-interiors', 'pixel-school-interiors', 'human-organs-pixel-art', 'elemental-spells',
                  'dungeon-warriors', 'sleepless-girl', 'frostbrook-snow-village-free-sample', 'elemental-spells-free-sample',
                  'dungeon-warriors-free-sample', 'frostbrook-villagers', 'frostbrook-town-interiors-free-sample'],
        'faq': [
            ('Do the Frostbrook DLCs need the base pack?', 'No. The Christmas DLC and the Town Interiors DLC work on their own, but they share the palette and grid of Frostbrook Snow Village so everything fits together.'),
            ('Which engines are supported?', 'Tilesets include Tiled, Godot 4 and RPG Maker MZ files; sprites and VFX are PNG sheets that work in Unity, GameMaker and any 2D engine.'),
            ('Is there a free sample?', 'Yes: Frostbrook, Elemental Spells and Dungeon Warriors each have a free sample.'),
        ],
    },
]
COL_OF = {}
for col in COLLECTIONS:
    for s in col['slugs']:
        COL_OF.setdefault(s, col)

# extra landing pages built from tags
FILTERS = [
    {'id': 'free-game-assets', 'name': 'Free Game Assets', 'title': 'Free Game Assets: PSX Low-Poly Models, 16x16 Tilesets, UI & VFX Samples',
     'meta': 'Free game assets from Chucky Assets: PS1-style low-poly models, 16x16 pixel art tiles, a horror UI sample, spell VFX and a fantasy character. Commercial use allowed.',
     'intro': 'Free samples of the paid packs, so you can check the style, scale and engine files before you buy. Commercial use is allowed under the same licence as the full packs.',
     'test': lambda c: c['price'] == 'free'},
    {'id': 'godot-4-assets', 'name': 'Godot 4 Assets', 'title': 'Godot 4 Assets: 3D PSX Packs, 2D TileSets & SpriteFrames Ready to Use',
     'meta': 'Asset packs made and tested for Godot 4: PSX 3D packs with walkable demo projects, TileSets for 16x16 pixel art, SpriteFrames for animated characters, a survival horror systems kit.',
     'intro': 'Packs that ship Godot 4 files: ready projects with demo scenes for the 3D packs, .tres TileSets for the tilesets and SpriteFrames for the characters. Tested in Godot 4.7.',
     'test': lambda c: any(t.lower() == 'godot' for t in c['tags'])},
    {'id': 'rpg-maker-mz-assets', 'name': 'RPG Maker MZ Assets', 'title': 'RPG Maker MZ Tilesets & Characters: Modern, Sci-Fi, Winter Village',
     'meta': 'RPG Maker MZ ready tilesets and character sheets: modern town interiors, space station, gym, snow village, bakery and school, animated $ character sheets.',
     'intro': 'Packs with RPG Maker MZ files: A5 / B-E tile sheets at 48 px and $ character sheets, including animated props for events.',
     'test': lambda c: any('rpg maker' in t.lower() for t in c['tags'])},
]

# ------------------------------------------------------------------ helpers
def clean_title(t):
    return t


def price_label(c):
    if c['price'] == 'free':
        return 'Free'
    return ''


def kind(c):
    t = ' '.join(c['tags']).lower()
    if c['cls'] == 'game':
        return 'Free browser game'
    if '3d' in t or 'low-poly' in t:
        return 'PSX low-poly 3D'
    if 'tileset' in t or '16x16' in t:
        return 'Pixel art tileset'
    return 'Pixel art'


def store(c):
    return f'{STORE}/{c["slug"]}'


CSS = open(os.path.join(ROOT, '_build', 'style.css')).read() if os.path.exists(os.path.join(ROOT, '_build', 'style.css')) else ''


def page(path, title, meta, body, canonical, og_image=None, jsonld=None, depth=0):
    up = '../' * depth
    og = og_image or BY[BUNDLE]['cover']
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    nav = ''.join(f'<a href="{up}{c["id"]}/">{E(c["short"])}</a>' for c in COLLECTIONS)
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(meta)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Chucky Assets">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(meta)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{E(og)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{up}style.css">
{ld}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{up}./"><img src="{up}favicon.svg" alt="" width="28" height="28">Chucky Assets</a>
<nav>{nav}<a href="{up}free-game-assets/">Free</a><a class="cta" href="{STORE}/{BUNDLE}">All-in-One Bundle</a></nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<p><strong>Chucky Assets</strong> makes PS1-style low-poly 3D packs and 16x16 pixel art for indie games. All packs are sold on <a href="{STORE}">itch.io</a>; commercial use allowed.</p>
<p class="links"><a href="{up}./">Home</a>{''.join(f' · <a href="{up}{c["id"]}/">{E(c["short"])}</a>' for c in COLLECTIONS)} · <a href="{up}godot-4-assets/">Godot 4</a> · <a href="{up}rpg-maker-mz-assets/">RPG Maker MZ</a> · <a href="{up}free-game-assets/">Free assets</a></p>
</div></footer>
</body>
</html>
'''
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(doc)


def card(c, up):
    badge = '<span class="badge free">Free</span>' if c['price'] == 'free' else ''
    return (f'<a class="card" href="{up}packs/{c["slug"]}/"><img src="{E(c["cover"])}" alt="{E(c["title"])}" loading="lazy" width="315" height="250">'
            f'<span class="ct">{E(c["title"])}</span><span class="cd">{E(c["desc"])}</span>{badge}</a>')


def grid(slugs, up):
    return '<div class="grid">' + ''.join(card(BY[s], up) for s in slugs if s in BY) + '</div>'


def bundle_box(up, exclude=False):
    b = BY[BUNDLE]
    return (f'<section class="bundle"><a href="{STORE}/{BUNDLE}"><img src="{E(b["cover"])}" alt="All-in-One Bundle" loading="lazy" width="315" height="250"></a>'
            f'<div><h2>Every pack in one download</h2><p>{E(b["desc"])}</p>'
            f'<p><a class="btn" href="{STORE}/{BUNDLE}">Get the All-in-One Bundle on itch.io</a></p></div></section>')


def faq_html(faq):
    return '<section class="faq"><h2>FAQ</h2>' + ''.join(f'<h3>{E(q)}</h3><p>{E(a)}</p>' for q, a in faq) + '</section>'


def faq_ld(faq):
    return {'@context': 'https://schema.org', '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]}


def crumbs_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(items)]}


# ------------------------------------------------------------------ pages
URLS = []


def build_home():
    up = ''
    paid = [c for c in CAT if c['price'] != 'free' and c['slug'] != BUNDLE and c['cls'] != 'game']
    body = [f'''<section class="hero"><div class="wrap">
<h1>PS1-style low-poly 3D and 16x16 pixel art for indie games</h1>
<p>{N_BUNDLE}+ asset packs for Godot 4, Unity, Unreal, RPG Maker MZ and Tiled: PSX horror levels, modern top-down tilesets, cozy winter villages, animated characters and more. Commercial use allowed, most packs have a free sample.</p>
<p><a class="btn" href="{STORE}/{BUNDLE}">All {N_BUNDLE} packs in the All-in-One Bundle</a> <a class="btn ghost" href="free-game-assets/">Free assets</a></p>
</div></section><div class="wrap">''']
    newest = ['dead-mall-psx-abandoned-shopping-mall', 'space-crew-aliens-characters', 'modern-gym-fitness-tileset', 'frostbrook-town-interiors-dlc']
    body.append('<h2>New releases</h2>' + grid(newest, up))
    for col in COLLECTIONS:
        body.append(f'<h2><a href="{col["id"]}/">{E(col["name"])}</a></h2><p class="lead">{E(col["intro"])}</p>' + grid(col['slugs'][:8], up) +
                    f'<p class="more"><a href="{col["id"]}/">All {len(col["slugs"])} {E(col["short"])} packs →</a></p>')
    body.append(bundle_box(up))
    body.append('</div>')
    ld = [{'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Chucky Assets', 'url': SITE + '/',
           'sameAs': [STORE], 'logo': SITE + '/favicon.svg'},
          {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Chucky Assets', 'url': SITE + '/'}]
    page('index.html', 'Chucky Assets – PSX Low-Poly 3D & 16x16 Pixel Art Game Assets (Godot 4, Unity, RPG Maker)',
         'PS1-style low-poly 3D asset packs and 16x16 pixel art tilesets for indie games: PSX horror, modern top-down towns, cozy winter villages, animated characters. Godot 4, Unity, RPG Maker MZ, Tiled.',
         ''.join(body), SITE + '/', jsonld=ld)
    URLS.append((SITE + '/', '1.0'))


def build_collection(col):
    up = '../'
    body = (f'<div class="wrap"><nav class="crumbs"><a href="../">Home</a> › {E(col["name"])}</nav>'
            f'<h1>{E(col["name"])}</h1><p class="lead">{E(col["intro"])}</p>' + grid(col['slugs'], up) +
            faq_html(col['faq']) + bundle_box(up) + '</div>')
    ld = [faq_ld(col['faq']), crumbs_ld([('Home', SITE + '/'), (col['name'], f'{SITE}/{col["id"]}/')]),
          {'@context': 'https://schema.org', '@type': 'ItemList', 'name': col['name'],
           'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': f'{SITE}/packs/{s}/'} for i, s in enumerate(col['slugs']) if s in BY]}]
    page(f'{col["id"]}/index.html', col['title'], col['meta'], body, f'{SITE}/{col["id"]}/', og_image=BY[col['slugs'][0]]['cover'], jsonld=ld, depth=1)
    URLS.append((f'{SITE}/{col["id"]}/', '0.9'))


def build_filter(f):
    up = '../'
    slugs = [c['slug'] for c in CAT if f['test'](c) and c['slug'] != BUNDLE]
    body = (f'<div class="wrap"><nav class="crumbs"><a href="../">Home</a> › {E(f["name"])}</nav>'
            f'<h1>{E(f["name"])}</h1><p class="lead">{E(f["intro"])}</p>' + grid(slugs, up) + bundle_box(up) + '</div>')
    page(f'{f["id"]}/index.html', f['title'], f['meta'], body, f'{SITE}/{f["id"]}/', og_image=BY[slugs[0]]['cover'],
         jsonld=[crumbs_ld([('Home', SITE + '/'), (f['name'], f'{SITE}/{f["id"]}/')])], depth=1)
    URLS.append((f'{SITE}/{f["id"]}/', '0.8'))


def engines(c):
    t = [x.lower() for x in c['tags']]
    e = []
    if 'godot' in t:
        e.append('Godot 4')
    if any('rpg maker' in x for x in t):
        e.append('RPG Maker MZ')
    if 'tiled' in t or 'tileset' in t:
        e.append('Tiled')
    if '3d' in t or 'low-poly' in t:
        e += ['Unity', 'Unreal Engine', 'Blender']
    else:
        e += ['Unity', 'GameMaker']
    seen = []
    for x in e:
        if x not in seen:
            seen.append(x)
    return seen


def build_pack(c):
    up = '../../'
    col = COL_OF.get(c['slug'])
    related = [s for s in (col['slugs'] if col else []) if s != c['slug']][:4]
    is_bundle = c['slug'] == BUNDLE
    eng = engines(c)
    k = kind(c)
    free = c['price'] == 'free'
    action = 'Download free on itch.io' if free else ('Play free in your browser' if c['cls'] == 'game' else 'Get it on itch.io')
    tags = ''.join(f'<span class="tag">{E(t)}</span>' for t in c['tags'])
    shot = f'<img class="shot" src="{E(c["shot"])}" alt="{E(c["title"])} preview" loading="lazy">' if c.get('shot') else ''
    if c['cls'] == 'game':
        what = f'{E(c["title"])} is a free PS1-style browser game made with the same tools as the asset packs.'
    else:
        what = (f'{E(c["title"])} is a {"free " if free else ""}{E(k)} asset pack by Chucky Assets. {E(c["desc"])} '
                f'It works with {E(", ".join(eng[:-1]) + " and " + eng[-1] if len(eng) > 1 else eng[0])}.')
    faq = []
    if c['cls'] != 'game':
        faq = [(f'Can I use {c["title"].split(" – ")[0]} in a commercial game?', 'Yes. You can use the assets in free and paid games on any platform. You may not resell or redistribute the assets themselves.'),
               (f'Which engines does it support?', f'{", ".join(eng)}. Files are standard formats ({"GLB, OBJ and PNG" if "3D" in k else "PNG sheets and engine files"}), so other engines work too.')]
        if not is_bundle and not free:
            faq.append(('Is it part of a bundle?', 'Yes, it is included in the Chucky Assets All-in-One Bundle together with every other pack.'))
    body = [f'<div class="wrap"><nav class="crumbs"><a href="{up}">Home</a>' + (f' › <a href="{up}{col["id"]}/">{E(col["short"])}</a>' if col else '') + f' › {E(c["title"].split(" – ")[0])}</nav>',
            f'<article class="pack"><div class="pmedia"><img src="{E(c["cover"])}" alt="{E(c["title"])} cover" width="630" height="500"></div>',
            f'<div class="pinfo"><p class="kind">{E(k)}{" · Free" if free else ""}</p><h1>{E(c["title"])}</h1><p class="lead">{E(c["desc"])}</p>',
            f'<p><a class="btn" href="{store(c)}">{action}</a></p><div class="tags">{tags}</div></div></article>',
            f'<section class="about"><h2>About this pack</h2><p>{what}</p>{shot}',
            f'<p>Full details, screenshots, file list and changelog are on the <a href="{store(c)}">itch.io page</a>.</p></section>']
    if faq:
        body.append(faq_html(faq))
    if related:
        body.append(f'<h2>More {E(col["short"])} packs</h2>' + grid(related, up))
    if not is_bundle:
        body.append(bundle_box(up))
    body.append('</div>')
    ld = [crumbs_ld([('Home', SITE + '/')] + ([(col['name'], f'{SITE}/{col["id"]}/')] if col else []) + [(c['title'], f'{SITE}/packs/{c["slug"]}/')]),
          {'@context': 'https://schema.org', '@type': 'CreativeWork' if c['cls'] != 'game' else 'VideoGame', 'name': c['title'], 'description': c['desc'],
           'image': c['cover'], 'url': store(c), 'keywords': ', '.join(c['tags']),
           'author': {'@type': 'Organization', 'name': 'Chucky Assets', 'url': STORE},
           'isAccessibleForFree': free}]
    if faq:
        ld.append(faq_ld(faq))
    title = c['title'] if len(c['title']) > 45 else f'{c["title"]} – {k} for {eng[0]}'
    page(f'packs/{c["slug"]}/index.html', title + ' | Chucky Assets', c['desc'], ''.join(body),
         f'{SITE}/packs/{c["slug"]}/', og_image=c['cover'], jsonld=ld, depth=2)
    URLS.append((f'{SITE}/packs/{c["slug"]}/', '0.7'))


def build_misc():
    css = open(os.path.join(ROOT, '_build', 'style.css')).read()
    open(os.path.join(ROOT, 'style.css'), 'w').write(css)
    open(os.path.join(ROOT, 'favicon.svg'), 'w').write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" shape-rendering="crispEdges">'
        '<rect width="16" height="16" rx="3" fill="#7c5cff"/><rect x="4" y="4" width="8" height="8" fill="#5ef2ff"/>'
        '<rect x="6" y="6" width="4" height="4" fill="#0b1028"/></svg>')
    open(os.path.join(ROOT, '.nojekyll'), 'w').write('')
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, p in URLS:
        sm.append(f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>')
    sm.append('</urlset>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
    page('404.html', 'Page not found | Chucky Assets', 'This page does not exist.',
         f'<div class="wrap"><h1>Page not found</h1><p>Try the <a href="{SITE}/">home page</a> or the <a href="{STORE}">itch.io store</a>.</p></div>',
         SITE + '/404.html')


if __name__ == '__main__':
    build_home()
    for col in COLLECTIONS:
        build_collection(col)
    for f in FILTERS:
        build_filter(f)
    for c in CAT:
        build_pack(c)
    build_misc()
    missing = [c['slug'] for c in CAT if c['slug'] not in COL_OF and c['slug'] != BUNDLE]
    print('pages', len(URLS) + 1, 'not in a collection:', missing)
