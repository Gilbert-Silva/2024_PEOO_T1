import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        Horarios = View.horario_listar()
        if len(Horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:  
            #for obj in Horarios: st.write(obj)
            dic = []
            #for obj in Horarios: dic.append(obj.__dict__)
            for obj in Horarios:
                cliente = View.cliente_listar_id(obj.id_cliente)
                servico = View.servico_listar_id(obj.id_servico)
                if cliente != None: cliente = cliente.nome
                if servico != None: servico = servico.descricao
                dic.append({"id" : obj.id, "data" : obj.data, "confirmado" : obj.confirmado, "cliente" : cliente , "serviço" : servico})
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes)
        servico = st.selectbox("Informe o serviço", servicos)
        if st.button("Inserir"):
            View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, cliente.id, servico.id)
            st.success("Horário inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            clientes = View.cliente_listar()
            servicos = View.servico_listar()
            op = st.selectbox("Atualização de horário", horarios)
            data = st.text_input("Informe a nova data e horário do serviço", op.data.strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova confirmação", op.confirmado)
            cliente = st.selectbox("Informe o novo cliente", clientes, op.id_cliente)
            servico = st.selectbox("Informe o novo serviço", servicos, op.id_servico)
            if st.button("Atualizar"):
                View.horario_atualizar(op.id, datetime.strptime(data, "%d/%m/%Y %H:%M"),  confirmado, cliente.id, servico.id)
                st.success("Horário atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de horário", horarios)
            if st.button("Excluir"):
                View.horario_excluir(op.id)
                st.success("Horário excluído com sucesso")
                time.sleep(2)
                st.rerun()
