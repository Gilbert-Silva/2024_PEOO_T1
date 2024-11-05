from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterservicoUI import ManterServicoUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI

import streamlit as st

class IndexUI:
    def main():
        if "cliente_id" in st.session_state:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia", "Abrir Conta", "Entrar no Sistema"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
        if op == "Entrar no Sistema": LoginUI.main()
        
IndexUI.main()
