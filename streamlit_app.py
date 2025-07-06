import streamlit as st

st.set_page_config(
    page_title="FAQ",
    layout="centered",
)

if "theme_dark" not in st.session_state:
    st.session_state.theme_dark = True
elif "theme_light" not in st.session_state:
    st.session_state.theme_light = False

col1, col2 = st.columns([6, 3])

with col2:
    st.title('❓FAQ')
with col1:
    st.write('ㅤ')
    if st.session_state.theme_dark:
        theme_toggle = st.toggle("темная тема", value=st.session_state.theme_dark, key="theme_dark")
    else:
        theme_toggle1 = st.toggle("светлая тема", value=st.session_state.theme_light, key="theme_light")

if st.session_state.theme_dark:
    st.markdown("""
    <style>
    body, .stApp {
        background-color: #222 !important;
        color: #eee !important;
    }
    .stExpanderHeader, .stExpanderContent {
        background-color: #333 !important;
        color: white !important;
        position: relative;
        z-index: 10;
    }
    /* Стили toggle (checkbox) в темной теме */
    div[role="switch"] > input[type="checkbox"] + div {
        background-color: #082BF0 !important;
        border-color: #082BF0 !important;
        z-index: 20;
    }
    div[role="switch"] > input[type="checkbox"]:checked + div {
        background-color: #082BF0 !important;
        border-color: #082BF0 !important;     
        z-index: 20;
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    body, .stApp {
        background-color: white !important;
        color: black !important;
    }
    .stExpanderHeader, .stExpanderContent {
        background-color: #f0f0f0 !important;
        color: black !important;
        position: relative;
        z-index: 10;
    }
    /* Стили toggle (checkbox) в светлой теме */
    div[role="switch"] > input[type="checkbox"] + div {
        background-color: #000ccc !important;
        border-color: #000999 !important;
        z-index: 10;
    }
    div[role="switch"] > input[type="checkbox"]:checked + div {
        background-color: #0d6efd !important;
        border-color: #0d6efd !important;
        z-index: 10;
    }
    </style>
    """, unsafe_allow_html=True)

with st.expander("Как пользоваться ботом?", expanded=True):
    st.write("Чтобы пользоваться ботом нужно написать /start, " \
    "затем выбрать действие, которое должен выполнить бот")

with st.expander("Что умеет бот?", expanded=True):
    st.write("Бот умеет генерировать и создавать qr-коды")

with st.expander("Как сохранить qr-код?", expanded=True):
    st.write('Чтобы сохранить qr-код нужно:\n')
    st.write('С компьютера:\n1. Нажать правой кнопкой мыши по картинке\n' \
    '2. Выбрать пункт "сохранить как"\n')
    st.write('С телефона:\n1. Нажать на картинку\n2. Нажать на 3 точки\n' \
    '3. Выбрать пункт "сохранить в галерею"')
