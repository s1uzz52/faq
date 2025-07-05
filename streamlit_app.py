import streamlit as st

st.set_page_config(
    page_title="FAQ",
    layout="centered",
)

st.markdown("""
<style>
body {
    background-color: #222 !important; /* Темный фон */
    color: #eee !important; /* Светлый текст */
}
.stApp {
    background-color: #222 !important; /* Темный фон для всего приложения */
    
    z-index: 0;
}
.stHeading {
    color: #eee !important; /* Светлый цвет заголовка */
}
.stExpanderHeader {
    background-color: #333 !important; /* Темный фон заголовка блока */
    color: #eee !important;
    position: relative;
    z-index: 10;
}
.stExpanderContent {
    background-color: #333 !important; /* Темный фон контента блока */
    color: #eee !important;
    position: relative;
    z-index: 5;
}
</style>
""", unsafe_allow_html=True)


st.title("❓FAQ")
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
    '3. Выбрать пункт "сохранить как')
