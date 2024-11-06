from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterservicoUI import ManterServicoUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from views import View

import streamlit as st

class IndexUI:
    def main():
        View.cliente_admin()
        if "cliente_id" in st.session_state:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            if st.session_state["cliente_nome"] == "admin":
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
        else:
            IndexUI.menu_visitante()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Abrir Conta": AbrirContaUI.main()
        if op == "Entrar no Sistema": LoginUI.main()

    def menu_cliente():
        pass

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
        IndexUI.sair_do_sistema()
    
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()


        
IndexUI.main()
