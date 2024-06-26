from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Sharvil Oza"
PAGE_ICON = ":wave:"
NAME = "Sharvil Oza"
DESCRIPTION = """
Junior Undergraduate at DAIICT studying Computer Science, aspiring Quant and currently a Research Intern at Georgia Tech's Financial Services Innovation Lab working on quantitative trading strategies.
"""
EMAIL = "sharvil010@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/sharvil-oza-37b5a8264",
    "GitHub": "https://github.com/so-19",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "💻 Stock Trading Engine in Rust(Ongoing): ":" Implemented a Stock Trading Engine which uses a custom TCP-IP Stack and having all the core functionalities of L-3 Order Book ",
    "💻 LLM from Scratch(Ongoing): ":"Reproduced GPT-2 inspired by Andrej Karpathy",
    "💻 Operating System(Ongoing): ":"Trying to build my own operating system with Rust as the main language",
    "💻 Algorithmic Trading Strategies: ":"Implemented Momentum Trending and Mean Reversion trading stategies using Backtrader",
    "💻 Bank Management Software: ":"Made a fully functional GUI based bank management software in Python with database as MySQL ",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=330)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Research Interests")
st.write(
    """
- ► I am currently interested in Reinforcement Learning applied to Finance and robotics and eventually building an intelligent system capable of making it's own choice.
- ► Other Interests are in the field of Computer Vision along with Financial Engineering(Modeling Option Prices,Interest Rates).
"""
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Undergraduate in Computer Science with Exceptional Academic Performance
- ✔️ Strong hands on experience and knowledge in Python,C++,Rust
- ✔️ Good understanding of Deep Learning,Quantitative Finance
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, TensorFlow), SQL, Rust, C++
- 📊 Skills: Financial Modelling, Corporate Strategy, Portfolio Management, Computer Vision, Valuation and Strategy
- 📚 Relevant Courses: GPU Architecture,Reinforcement Learning, Mathematical Finance, Deep Learning
- 🗄️ Databases: MySQL,PostgreSQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Research Intern | Georgia Tech Financial Services Innovation Lab(FSIL)**")
st.write("04/2024 - Present")
st.write(
    """
- ► Implemented and BackTested Price based Quantitative Trading Strategies
- ► Made the Algorithm more robust by implementing a financial Risk Metric Class made of over 25 Risk metrics for comparing against benchmark returns
- ► Used OHLCV data in the model along with fetching data using API
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Winter Intern | Maitri Manthan Sansthan**")
st.write("12/2023 - 01/2024")
st.write(
    """
- ► Prepared a Pitch Deck for Sustainability of NGO by Performing a SWOT analysis
- ► Recommended for Opening Up of online internhip to boost the presence of NGO Nationwide
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, description in PROJECTS.items():
    st.write(f"{project}{description}")
