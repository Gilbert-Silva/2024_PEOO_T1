import streamlit as st
from views import View
from datetime import datetime
import time

class AbrirAgendaUI:
    def main():
        st.header("Abrir Agenda do Dia")
        AbrirAgendaUI.abrir_agenda()

    def abrir_agenda():
        data = st.text_input("Informe a data no formato *dd/mm/aaaa*", datetime.now().strftime("%d/%m/%Y"))
        hinicio = st.text_input("Informe o horário inicial no formato *HH\:MM*")
        hfim = st.text_input("Informe o horário final no formato *HH\:MM*")
        intervalo = st.text_input("Informe o intervalo entre os horários (minutos)")
        if st.button("Inserir Horários"):
            View.horario_abrir_agenda(data, hinicio, hfim, int(intervalo))
            st.success("Horário(s) inserido(s) com sucesso")
            time.sleep(2)
            st.rerun()
