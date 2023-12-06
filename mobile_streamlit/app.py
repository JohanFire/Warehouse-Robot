# Importa la biblioteca Streamlit
import streamlit as st

# Define la función principal de la aplicación
def main():
    # Título de la página
    st.title("Mi Aplicación Streamlit")

    # Agrega un texto descriptivo
    st.write("Esta es una aplicación simple con dos botones.")

    # Botón 1
    if st.button("Botón 1"):
        st.write("¡Hiciste clic en el Botón 1!")

    # Botón 2
    if st.button("Botón 2"):
        st.write("¡Hiciste clic en el Botón 2!")

# Llama a la función principal
if __name__ == "__main__":
    main()