import streamlit as st



st.set_page_config(page_title="IntegraSGP")


#Criando abas

aba1, aba2, aba3, aba4, aba5 = st.tabs(["Informações funcionais", "Capacitação", "Saúde e Desempenho", "Planejamento e gestão da força de trabalho", "Remuneração e benefícios"])


#CONTEÚDO ABA1

with aba1:
    st.header("Módulo de Informações funcionais")

    #submenu aba1

    submenuaba1 = st.radio("Escolha uma opção", ["Cadastro", "Cargo comissionado", "Movimentação", "Desligamento"])


        
    if submenuaba1 == "Cadastro":
        st.subheader("Cadastro")

       #criando as colunas

        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("Consultar")
        with col2:
            st.button("Incluir")
        with col3:
            st.button("Alterar")
                
        
        consulta = st.text_input("Consulta")
        nome = st.text_input("Nome")
        cpf = st.number_input("CPF")
        Matrícula_siape = st.number_input("Matrícula siape")
        situação = st.text_input("situação")
        cargo_efetivo = st.text_input("Cargo efetivo")
        função = st.text_input("Função")
        lotação = st.text_input("Lotação")






#Conteúdo aba2

with aba2:
    st.header("Módulo de capacitação")


#Conteúdo aba3

with aba3:
    st.header("Módulo de saúde e desempenho")


#Conteúdo aba4

with aba4:
    st.header("Módulo de planejamento e Gestão da força de trabalho")


