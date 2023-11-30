import streamlit as st
from htmlTemplates import css

def handle_user_input(user_question):
    st.session_state.messages.append({"role": "user", "content": user_question})
    st.session_state.messages.append({"role": "assistant", "content": "Respuesta del chatbot"})

    for msg in st.session_state.messages:
        st.write(msg["content"], role=msg["role"])

def main():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.set_page_config(page_title="Mi Chatbot", page_icon=":tada:")
    st.write(css, unsafe_allow_html=True)
    st.sidebar.markdown(
        """
        ### Información:
        1. Este es un chatbot creado con Streamlit.
        2. Estamos usando contenedores 
        """
    )
    st.header("Bienvenido al chatbot")

    user_question = st.text_input("¿Qué vas a preguntar?")

    if user_question:
        handle_user_input(user_question)

if __name__ == "__main__":
    main()
