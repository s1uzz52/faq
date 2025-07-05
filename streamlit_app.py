import streamlit as st

st.set_page_config(
    page_title="FAQ",
    layout="centered",
)

st.markdown("""
<style>
body {
    background-color: #222;
    color: #eee;
}
.stApp {
    background-color: #222;
}
.stHeading {
  color: #eee;
}
.stExpanderHeader {
  background-color: #333;
  color: #eee;
  z-index: 10; /* Важно: устанавливаем z-index */
}
.stExpanderContent {
  background-color: #333;
  color: #eee;
  z-index: 10; /* Важно: устанавливаем z-index */
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
