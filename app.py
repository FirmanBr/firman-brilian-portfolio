import streamlit as st
from data import PROFILE, SERVICES, EXPERIENCE, SKILLS, CERTIFICATIONS, EDUCATION, MENTORING, SPEAKER

st.set_page_config(
    page_title=f"{PROFILE['name']} — {PROFILE['role']}",
    page_icon="🗂️",
    layout="centered",
)

# ---------- THEME (dark navy, matches the original site design) ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

    html, body, [class*="css"]  {
        font-family: 'IBM Plex Sans', sans-serif;
    }
    .stApp {
        background-color: #0F1B2D;
        color: #E9EDF2;
    }
    h1, h2, h3 {
        font-family: 'IBM Plex Serif', serif !important;
    }
    .role-tag {
        color: #E8A33D;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 16px;
        margin-bottom: 14px;
    }
    .summary {
        color: #93A6BC;
        font-size: 15.5px;
        max-width: 65ch;
    }
    .meta {
        color: #93A6BC;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 13px;
        margin-bottom: 8px;
    }
    .chip {
        display: inline-block;
        border: 1px solid rgba(233,237,242,0.18);
        background: #14253C;
        color: #E9EDF2;
        border-radius: 6px;
        padding: 4px 10px;
        margin: 3px 4px 3px 0;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 12.5px;
    }
    .cert-row {
        display:flex; justify-content:space-between;
        border-bottom: 1px dashed rgba(233,237,242,0.18);
        padding: 8px 0; font-size: 14.5px;
    }
    .cert-year { color: #3FA796; font-family: 'IBM Plex Mono', monospace; font-size: 13px; }
    a { color: #3FA796 !important; }
    .cta-btn {
        display: inline-block;
        background: #E8A33D; color: #0F1B2D !important;
        font-weight: 600; padding: 10px 20px; border-radius: 8px;
        text-decoration: none !important; margin: 4px 6px 4px 0;
    }
    .whatsapp-btn {
        display: inline-block;
        background: #25D366; color: #06210f !important;
        font-weight: 600; padding: 10px 20px; border-radius: 8px;
        text-decoration: none !important; margin: 4px 6px 4px 0;
    }
    .ghost-btn {
        display: inline-block;
        background: transparent; color: #E9EDF2 !important;
        border: 1px solid rgba(233,237,242,0.25);
        font-weight: 500; padding: 10px 20px; border-radius: 8px;
        text-decoration: none !important; margin: 4px 6px 4px 0;
    }
    .service-card {
        background: #14253C; border: 1px solid rgba(233,237,242,0.14);
        border-radius: 10px; padding: 16px 18px; margin-bottom: 12px;
    }
    .service-card b { color: #E9EDF2; }
    .badge {
        display:inline-flex; align-items:center; gap:7px;
        border:1px solid rgba(63,167,150,0.35); background:rgba(63,167,150,0.08);
        color:#3FA796; font-family:'IBM Plex Mono', monospace; font-size:12.5px;
        padding:5px 12px; border-radius:999px; margin-bottom:14px;
    }
    .skill-card {
        border-radius: 12px; padding: 18px 18px 14px; margin-bottom: 14px;
        background: #14253C; border: 1px solid rgba(233,237,242,0.14);
    }
    .skill-card .icon-row { display:flex; align-items:center; gap:10px; margin-bottom:10px; }
    .skill-card .icon {
        width:32px; height:32px; border-radius:8px; display:flex; align-items:center;
        justify-content:center; font-size:15px; background:rgba(255,255,255,0.05);
    }
    .skill-card .title { font-weight:600; color:#E9EDF2; font-size:14.5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

SKILL_ICONS = ["🗄️", "🔀", "📡", "☁️", "🛡️", "📊"]

# ---------- HERO ----------
st.markdown("<div class='badge'>● Available for freelance &amp; consulting projects</div>", unsafe_allow_html=True)
st.title(PROFILE["name"])
st.markdown(f"<div class='role-tag'>{PROFILE['role']}</div>", unsafe_allow_html=True)
st.markdown(f"<p class='summary'>{PROFILE['summary']}</p>", unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)
c1.markdown(f"📍 {PROFILE['location']}")
c2.markdown(f"💬 [WhatsApp](https://wa.me/{PROFILE['whatsapp']})")
c3.markdown(f"✉️ [Email](mailto:{PROFILE['email']})")
c4.markdown(f"💼 [LinkedIn]({PROFILE['linkedin']})")
c5.markdown(f"✍️ [Medium]({PROFILE['medium']})")

wa_text = "Hi%20Firman%2C%20I%27d%20like%20to%20discuss%20a%20data%20project."
st.markdown(
    f"""
    <div style="margin-top:18px;">
        <a class="whatsapp-btn" href="https://wa.me/{PROFILE['whatsapp']}?text={wa_text}" target="_blank">Chat on WhatsApp</a>
        <a class="ghost-btn" href="#services">View services</a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ---------- SERVICES ----------
st.header("Services", anchor="services")
st.markdown(
    "<p class='summary'>Helping companies build a reliable data foundation — from architecture, "
    "pipelines, to governance.</p>",
    unsafe_allow_html=True,
)
col_a, col_b = st.columns(2)
for i, (title, desc) in enumerate(SERVICES):
    target = col_a if i % 2 == 0 else col_b
    target.markdown(
        f"<div class='service-card'><b>{title}</b><br><span style='color:#93A6BC; font-size:14px;'>{desc}</span></div>",
        unsafe_allow_html=True,
    )

st.divider()

# ---------- EXPERIENCE ----------
st.header("Experience")
for job in EXPERIENCE:
    with st.expander(f"{job['company']} — {job['role']} ({job['period']})"):
        for bullet in job["bullets"]:
            st.markdown(f"- {bullet}")

st.divider()

# ---------- SKILLS ----------
st.header("Skills & Tools")
st.markdown(
    "<p class='summary'>The stack behind every architecture, pipeline, and platform listed above.</p>",
    unsafe_allow_html=True,
)
sk_col1, sk_col2 = st.columns(2)
for i, group in enumerate(SKILLS):
    target = sk_col1 if i % 2 == 0 else sk_col2
    icon = SKILL_ICONS[i % len(SKILL_ICONS)]
    chips_html = "".join(f"<span class='chip'>{item}</span>" for item in group["items"])
    target.markdown(
        f"""
        <div class="skill-card">
            <div class="icon-row">
                <div class="icon">{icon}</div>
                <span class="title">{group['group']}</span>
            </div>
            <div>{chips_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# ---------- CERTIFICATIONS ----------
st.header("Certifications")
cert_html = "".join(
    f"<div class='cert-row'><span>{name}</span><span class='cert-year'>{year}</span></div>"
    for name, year in CERTIFICATIONS
)
st.markdown(cert_html, unsafe_allow_html=True)

st.divider()

# ---------- EDUCATION ----------
st.header("Education")
st.markdown(f"**{EDUCATION['school']}**")
st.markdown(f"<span class='meta'>{EDUCATION['degree']}</span>", unsafe_allow_html=True)
st.markdown(EDUCATION["thesis"])

st.divider()

# ---------- MENTORING & SPEAKER ----------
st.header("Mentoring & Speaker")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Mentoring")
    for name, year in MENTORING:
        st.markdown(f"- {name} · *{year}*")
with col2:
    st.subheader("Speaker")
    for name, year in SPEAKER:
        st.markdown(f"- {name} · *{year}*")

st.divider()

# ---------- CONTACT CTA ----------
st.header("Have a data project that needs sorting out?")
st.markdown(
    "<p class='summary'>Whether it's building a new architecture, fixing a broken pipeline, "
    "or restructuring your company's data governance — I'm open to discussing your needs.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <a class="whatsapp-btn" href="https://wa.me/{PROFILE['whatsapp']}?text={wa_text}" target="_blank">Chat on WhatsApp</a>
    <a class="cta-btn" href="mailto:{PROFILE['email']}?subject=Data%20Project%20Inquiry">Send an email</a>
    <a class="ghost-btn" href="{PROFILE['linkedin']}" target="_blank">Message on LinkedIn</a>
    """,
    unsafe_allow_html=True,
)

st.divider()
st.caption(f"{PROFILE['name']} · {PROFILE['location']} · {PROFILE['email']}")
