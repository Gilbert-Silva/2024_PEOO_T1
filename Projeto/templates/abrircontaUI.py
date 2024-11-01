import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir conta no sistema")
        AbrirContaUI.inserir()

    def inserir():
        nome = st.text_input("Informe o nome do cliente")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Senha", type="password")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()
