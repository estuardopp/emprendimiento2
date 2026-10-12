"""SAVIA: prototipo interactivo de bienestar natural para Streamlit."""
from __future__ import annotations

from datetime import date
import html

import streamlit as st

st.set_page_config(page_title="SAVIA | Naturaleza que te guía", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")

PLANTS = [
    {
        "id": "pasiflora", "name": "Pasiflora", "latin": "Passiflora incarnata", "emoji": "🌸", "topic": "Descanso",
        "summary": "Tradicionalmente usada para el descanso. La evidencia sobre sus efectos es limitada.",
        "evidence": "Algunos estudios pequeños han examinado su posible utilidad para la ansiedad y el sueño, pero no permiten asegurar eficacia clínica.",
        "safety": "Puede causar somnolencia, mareos o confusión. Consulta a un profesional si tomas medicamentos o si estás embarazada o en lactancia.",
        "source": "NCCIH · Passionflower", "url": "https://www.nccih.nih.gov/health/passionflower", "color": "#e6efdf",
    },
    {
        "id": "manzanilla", "name": "Manzanilla", "latin": "Matricaria recutita", "emoji": "🌼", "topic": "Calma",
        "summary": "Planta tradicional en infusiones. La evidencia clínica depende del uso y de la preparación.",
        "evidence": "Se ha estudiado para distintas finalidades; los resultados no establecen que trate un problema de salud específico.",
        "safety": "Puede provocar alergias, especialmente en personas sensibles a plantas de la familia de las margaritas. Se han descrito posibles interacciones con warfarina y otros medicamentos.",
        "source": "NCCIH · Chamomile", "url": "https://www.nccih.nih.gov/health/chamomile", "color": "#f8efd8",
    },
    {
        "id": "menta", "name": "Menta piperita", "latin": "Mentha × piperita", "emoji": "🍃", "topic": "Digestión",
        "summary": "La hoja y el aceite de menta son preparaciones diferentes y no deben tratarse como equivalentes.",
        "evidence": "Existe cierta evidencia para cápsulas de aceite de menta con recubrimiento entérico en síntomas del síndrome de intestino irritable. Para la hoja hay poca investigación.",
        "safety": "El aceite puede causar efectos adversos, entre ellos reflujo o indigestión. Consulta al profesional de salud antes de usar preparados concentrados.",
        "source": "NCCIH · Peppermint Oil", "url": "https://www.nccih.nih.gov/health/peppermint-oil", "color": "#e1f1e9",
    },
]
PRODUCTS = [
    {"id": "infusion", "name": "Infusión de pasiflora", "kind": "Infusión", "price": 32, "plant": "pasiflora", "emoji": "🫖", "supplier": "Proveedor de ejemplo · validación pendiente"},
    {"id": "manzanilla", "name": "Manzanilla en flor", "kind": "Planta seca", "price": 28, "plant": "manzanilla", "emoji": "🌼", "supplier": "Proveedor de ejemplo · validación pendiente"},
    {"id": "menta", "name": "Infusión de menta", "kind": "Infusión", "price": 29, "plant": "menta", "emoji": "🍃", "supplier": "Proveedor de ejemplo · validación pendiente"},
]

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
:root{--ink:#173d31;--mint:#e7f0e4;--cream:#f8f6ed;--leaf:#467d52}
html,body,[class*="css"], [data-testid="stApp"]{font-family:'DM Sans',sans-serif;color:var(--ink)}
[data-testid="stApp"]{background:#f8f7f0}
[data-testid="stSidebar"]{background:#ecf0e4;border-right:1px solid #dce5d5}
.block-container{max-width:1160px;padding-top:1.7rem;padding-bottom:4rem}
h1,h2,h3{font-family:'Playfair Display',serif;color:var(--ink)}
h1{font-size:3rem!important;letter-spacing:-.04em} h2{font-size:2rem!important}
.hero{background:linear-gradient(110deg,#103e30 0%,#246748 65%,#478353 100%);color:#f5f7e9;border-radius:26px;padding:42px 46px;margin:8px 0 25px;position:relative;overflow:hidden}
.hero:after{content:'✧  ✿  ❧';position:absolute;right:28px;bottom:2px;font-size:110px;opacity:.13;transform:rotate(-12deg)}
.hero h1{color:#fff;margin:10px 0 12px;font-size:3.15rem!important}.hero p{color:#e2eedf;font-size:1.1rem;max-width:580px}.hero small{color:#c4dfc8;letter-spacing:.18em;text-transform:uppercase;font-weight:700}
.card{background:#fffefa;border:1px solid #e7e8dc;border-radius:20px;padding:22px;margin-bottom:16px;box-shadow:0 6px 24px #183b2310;min-height:190px}
.card h3{margin:6px 0;font-size:1.55rem}.card p{color:#52665a;line-height:1.55}
.chip{display:inline-block;background:#e8f1e3;color:#28603f;border-radius:99px;padding:5px 11px;font-size:.77rem;font-weight:700}
.muted{color:#657569;font-size:.9rem}.icon{font-size:2.2rem}.price{font-size:1.4rem;font-weight:700;color:#1b5a38}.eyebrow{font-size:.76rem;font-weight:700;letter-spacing:.13em;color:#4a7652;text-transform:uppercase}
.notice{background:#eef2e8;border:1px solid #d7e4cf;border-radius:14px;padding:13px 18px;color:#355a3c;margin:10px 0 20px}
.warning{background:#fff4e3;border:1px solid #f1d9a9;border-radius:14px;padding:13px 18px;color:#694920;margin:12px 0}
[data-testid="stMetric"]{background:#fffefa;padding:13px;border-radius:14px;border:1px solid #e7e8dc}
div.stButton>button[kind="primary"]{background:#195138;border-color:#195138;border-radius:10px}
.stTabs [data-baseweb="tab-list"]{gap:14px}.stTabs [data-baseweb="tab"]{font-weight:600}
</style>""", unsafe_allow_html=True)

if "saved" not in st.session_state:
    st.session_state.saved = []
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "habits" not in st.session_state:
    st.session_state.habits = {}
if "profile" not in st.session_state:
    st.session_state.profile = {"name": "Ana", "goal": "Descanso", "meds": False, "pregnancy": False}
if "page" not in st.session_state:
    st.session_state.page = "Inicio"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def go(page: str) -> None:
    st.session_state.page = page
    st.rerun()


def info_banner() -> None:
    st.markdown('<div class="notice">🧪 <b>Prototipo académico:</b> los precios, proveedores y operaciones comerciales son ilustrativos. Las fichas enlazan a fuentes externas y no sustituyen asesoramiento sanitario.</div>', unsafe_allow_html=True)


def safety_banner() -> None:
    p = st.session_state.profile
    if p["meds"] or p["pregnancy"]:
        st.markdown('<div class="warning">⚠️ Registraste medicamentos, embarazo o lactancia. SAVIA no evalúa interacciones ni recomienda productos para tu caso. Consulta a un profesional de salud antes de utilizar cualquier preparación.</div>', unsafe_allow_html=True)


def card(plant: dict) -> None:
    st.markdown(f'<div class="card" style="background:linear-gradient(150deg,{plant["color"]},#fffefa 65%)"><div class="icon">{plant["emoji"]}</div><span class="chip">{esc(plant["topic"])}</span><h3>{esc(plant["name"])}</h3><div class="muted"><i>{esc(plant["latin"])}</i></div><p>{esc(plant["summary"])}</p></div>', unsafe_allow_html=True)
    if st.button("Ver ficha y seguridad", key=f"plant_{plant['id']}", use_container_width=True):
        st.session_state.selected_plant = plant["id"]
        go("Explorar")


with st.sidebar:
    st.markdown("## 🌿 SAVIA")
    st.caption("Naturaleza que te guía")
    st.divider()
    for page, icon in [("Inicio", "⌂"), ("Explorar", "◈"), ("Mi plan", "◷"), ("Tienda", "▣"), ("Perfil", "♙")]:
        if st.button(f"{icon}   {page}", key=f"nav_{page}", use_container_width=True, type="primary" if st.session_state.page == page else "secondary"):
            go(page)
    st.divider()
    st.caption("Experiencia de demostración · SAVIA")
    st.caption("El perfil y el carrito solo duran durante esta sesión del navegador.")

page = st.session_state.page
if page == "Inicio":
    p = st.session_state.profile
    st.markdown(f'<div class="hero"><small>Bienvenida a SAVIA</small><h1>Hola, {esc(p["name"])} 🌿</h1><p>Conoce las plantas, explora la evidencia y construye hábitos de bienestar a tu ritmo.</p></div>', unsafe_allow_html=True)
    info_banner()
    safety_banner()
    a,b,c = st.columns(3)
    with a: st.metric("Plantas en el catálogo", len(PLANTS))
    with b: st.metric("En mi biblioteca", len(st.session_state.saved))
    with c: st.metric("Días registrados", sum(bool(x) for x in st.session_state.habits.values()))
    st.write("")
    st.markdown("## ¿Qué te gustaría explorar?")
    query = st.text_input("Buscar", placeholder="Ej. pasiflora, calma, descanso...", label_visibility="collapsed")
    if query.strip():
        st.session_state.search = query.strip()
        go("Explorar")
    col1,col2,col3 = st.columns(3)
    for col, label, dest, message in [(col1,"🔎 Explorar plantas","Explorar","Fichas con fuentes, evidencia y precauciones"),(col2,"🌱 Crear mi plan","Mi plan","Pequeños hábitos y seguimiento diario"),(col3,"🛍️ Ver productos","Tienda","Un recorrido de compra simulado")]:
        with col:
            st.markdown(f'<div class="card"><div class="icon">{label.split()[0]}</div><h3>{esc(" ".join(label.split()[1:]))}</h3><p>{esc(message)}</p></div>', unsafe_allow_html=True)
            if st.button("Abrir", key=f"home_{dest}", use_container_width=True): go(dest)
    st.markdown("## Para descubrir hoy")
    cols = st.columns(3)
    for col, plant in zip(cols, PLANTS):
        with col: card(plant)

elif page == "Explorar":
    st.markdown('<span class="eyebrow">Biblioteca botánica</span>', unsafe_allow_html=True)
    st.title("Explora con información clara")
    st.caption("El filtro por objetivo organiza las fichas; no calcula adecuación clínica individual.")
    info_banner()
    safety_banner()
    q = st.text_input("Buscar planta, nombre científico o tema", value=st.session_state.pop("search", ""), placeholder="Busca en el catálogo...")
    topics = ["Todos"] + sorted({x["topic"] for x in PLANTS})
    topic = st.selectbox("Tema", topics)
    found = [x for x in PLANTS if (topic == "Todos" or x["topic"] == topic) and (not q or q.casefold() in (x["name"]+" "+x["latin"]+" "+x["topic"]).casefold())]
    if not found: st.info("No hay fichas para esa búsqueda.")
    cols = st.columns(3)
    for i, plant in enumerate(found):
        with cols[i%3]: card(plant)
    selected = next((x for x in PLANTS if x["id"] == st.session_state.get("selected_plant")), None)
    if selected and selected in found:
        st.divider()
        st.subheader(f"{selected['emoji']} Ficha: {selected['name']}")
        st.caption(f"Nombre científico: {selected['latin']}")
        left,right = st.columns([1.5,1])
        with left:
            st.markdown("#### Qué se ha estudiado")
            st.write(selected["evidence"])
            st.markdown(f"**Fuente:** [{selected['source']}]({selected['url']})")
            st.caption("La fuente describe evidencia general, no valida ni certifica los productos de esta demostración.")
        with right:
            st.markdown("#### Precauciones")
            st.warning(selected["safety"])
            st.caption("No se incluyen dosis: dependen de la preparación, la persona y la evaluación profesional.")
        saved = selected["id"] in st.session_state.saved
        if st.button("Quitar de mi biblioteca" if saved else "Guardar en mi biblioteca", key="save_plant"):
            if saved: st.session_state.saved.remove(selected["id"])
            else: st.session_state.saved.append(selected["id"])
            st.rerun()

elif page == "Mi plan":
    st.markdown('<span class="eyebrow">Bienestar cotidiano</span>', unsafe_allow_html=True)
    st.title("Mi plan de bienestar")
    st.caption("Sugerencias de hábitos generales basadas en tu objetivo elegido, sin diagnóstico ni análisis médico.")
    info_banner()
    safety_banner()
    goal = st.session_state.profile["goal"]
    suggestions = {
        "Descanso": ["Preparar una rutina tranquila al terminar el día", "Reducir pantallas antes de dormir", "Registrar cómo dormiste"],
        "Calma": ["Tomar una pausa consciente", "Salir a caminar unos minutos", "Registrar cómo te sientes"],
        "Digestión": ["Comer con calma", "Registrar hábitos de alimentación", "Hacer una pausa breve después de comer"],
    }
    st.markdown(f"### Objetivo actual: {goal}")
    st.caption("Puedes cambiarlo en Perfil.")
    today = date.today().isoformat()
    checked = 0
    for idx, item in enumerate(suggestions[goal]):
        key = f"{today}:{goal}:{idx}"
        checked += int(st.checkbox(item, value=st.session_state.habits.get(key, False), key=f"habit_{key}"))
        st.session_state.habits[key] = st.session_state[f"habit_{key}"]
    st.progress(checked/3)
    st.caption(f"{checked} de 3 hábitos registrados hoy · {today}")
    st.divider()
    st.markdown("### Mi biblioteca")
    saved = [x for x in PLANTS if x["id"] in st.session_state.saved]
    if saved:
        for x in saved: st.markdown(f"**{x['emoji']} {x['name']}** · [{x['source']}]({x['url']})")
    else:
        st.info("Guarda una planta desde Explorar para verla aquí.")
    st.markdown("### Plan Premium · vista previa")
    st.markdown('<div class="card"><span class="chip">Concepto comercial</span><h3>Q99.00 / mes · precio ilustrativo</h3><p>La propuesta del proyecto contempla seguimiento de hábitos e información ampliada. Las recomendaciones clínicas y la evaluación de interacciones requieren desarrollo y validación profesional antes de ponerse a disposición del público.</p></div>', unsafe_allow_html=True)
    if st.button("Explorar fichas", key="plan_explore"): go("Explorar")

elif page == "Tienda":
    st.markdown('<span class="eyebrow">Marketplace · demostración</span>', unsafe_allow_html=True)
    st.title("Productos para explorar")
    st.caption("Catálogo y carrito ilustrativos. No se realizan pagos, envíos ni pedidos.")
    info_banner()
    safety_banner()
    st.warning("Los proveedores de esta maqueta no están verificados. Cada producto necesitaría trazabilidad, etiquetas, controles y validación antes de una venta real.")
    cols = st.columns(3)
    for col, product in zip(cols, PRODUCTS):
        with col:
            st.markdown(f'<div class="card"><div class="icon">{product["emoji"]}</div><span class="chip">{esc(product["kind"])}</span><h3>{esc(product["name"])}</h3><p>{esc(product["supplier"])}</p><div class="price">Q{product["price"]:.2f}</div></div>', unsafe_allow_html=True)
            if st.button("Añadir al carrito", key=f"buy_{product['id']}", use_container_width=True):
                st.session_state.cart[product["id"]] = st.session_state.cart.get(product["id"],0)+1
                st.toast("Producto añadido a la simulación")
    st.divider()
    st.subheader("Mi carrito")
    total=0
    for product in PRODUCTS:
        qty=st.session_state.cart.get(product["id"],0)
        if qty:
            a,b,c=st.columns([3,1,1]); a.write(f"{product['name']} × {qty}"); b.write(f"Q{qty*product['price']:.2f}")
            total += qty*product["price"]
            if c.button("Quitar", key=f"remove_{product['id']}"):
                if qty == 1: del st.session_state.cart[product["id"]]
                else: st.session_state.cart[product["id"]]-=1
                st.rerun()
    if not total: st.info("Tu carrito está vacío. Agrega un producto para probar el recorrido.")
    else:
        st.markdown(f"### Total ilustrativo: Q{total:.2f}")
        if st.button("Simular pedido", type="primary"):
            st.success("¡Recorrido completado! Este es un prototipo: no se registró ningún pedido ni se procesó un pago.")

elif page == "Perfil":
    st.markdown('<span class="eyebrow">Preferencias</span>', unsafe_allow_html=True)
    st.title("Tu experiencia SAVIA")
    st.caption("Datos locales de sesión para mostrar la experiencia de personalización del prototipo.")
    info_banner()
    p=st.session_state.profile
    with st.form("profile_form"):
        name=st.text_input("¿Cómo te llamas?", value=p["name"], max_chars=40)
        goal=st.selectbox("Objetivo de bienestar", ["Descanso","Calma","Digestión"], index=["Descanso","Calma","Digestión"].index(p["goal"]))
        st.markdown("#### Recordatorios de seguridad")
        meds=st.checkbox("Uso medicamentos",value=p["meds"])
        pregnancy=st.checkbox("Embarazo o lactancia",value=p["pregnancy"])
        st.caption("Estas opciones solo activan un aviso general. La app no determina interacciones ni si un producto es seguro para ti.")
        submit=st.form_submit_button("Guardar preferencias", type="primary")
    if submit:
        st.session_state.profile={"name":name.strip() or "Hola", "goal":goal,"meds":meds,"pregnancy":pregnancy}
        st.success("Preferencias actualizadas para esta sesión.")
    st.divider()
    if st.button("Restablecer datos de demostración"):
        for key in ["saved","cart","habits","profile","selected_plant","search"]:
            st.session_state.pop(key,None)
        st.rerun()
    st.markdown("### Sobre SAVIA")
    st.write("Una propuesta académica para conectar información sobre productos naturales, seguridad, hábitos y un marketplace. La evaluación de profesionales y proveedores forma parte del desarrollo futuro.")

st.divider()
st.caption("SAVIA · Prototipo académico de Emprendimiento e Innovación · La información es educativa y no reemplaza la consulta con profesionales de salud.")
