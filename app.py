import streamlit as st
from data import PROFILE, EXPERIENCE, SKILLS, CERTIFICATIONS, EDUCATION, MENTORING, SPEAKING

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
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- HERO ----------
st.title(PROFILE["name"])
st.markdown(f"<div class='role-tag'>{PROFILE['role']}</div>", unsafe_allow_html=True)
st.markdown(f"<p class='summary'>{PROFILE['summary']}</p>", unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)
c1.markdown(f"📍 {PROFILE['location']}")
c2.markdown(f"📞 [{PROFILE['phone']}](tel:{PROFILE['phone']})")
c3.markdown(f"✉️ [Email](mailto:{PROFILE['email']})")
c4.markdown(f"💼 [LinkedIn]({PROFILE['linkedin']})")
c5.markdown(f"✍️ [Medium]({PROFILE['medium']})")

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
for group in SKILLS:
    st.markdown(f"**{group['group']}**")
    chips_html = "".join(f"<span class='chip'>{item}</span>" for item in group["items"])
    st.markdown(chips_html, unsafe_allow_html=True)
    st.write("")

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

# ---------- MENTORING & SPEAKING ----------
st.header("Mentoring & Speaking")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Mentoring")
    for name, year in MENTORING:
        st.markdown(f"- {name} · *{year}*")
with col2:
    st.subheader("Speaking")
    for name, year in SPEAKING:
        st.markdown(f"- {name} · *{year}*")

st.divider()
st.caption(f"{PROFILE['name']} · {PROFILE['location']} · {PROFILE['email']}")
