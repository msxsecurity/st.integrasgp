import streamlit as st



st.set_page_config(page_title="IntegraSGP")
st.set_page_config(layout="wide")



    #Criando abas

aba0, aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs(["IntegraSGP", "Informações Funcionais", "Capacitação", "Saúde e Desempenho", "Planejamento e gestão da força de trabalho", "Remuneração e benefícios", "Tabelas"])

#linha divisória
st.write("---")

#CONTEÚDO ABA0

with aba0:
    st.header("Página inicial")
    #linha divisória
    
    st.subheader("IntegraSGP: v.1.0.0")


#CONTEÚDO ABA1

with aba1:
    st.header("Módulo de Informações funcionais")

    #submenu aba1

    submenuaba1 = st.radio("Escolha uma opção", ["Cadastro", "Cargo comissionado", "Movimentação", "Desligamento"])

    #linha divisória
    st.write("---")
        
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

        #linha divisória                
        st.write("---")
                        
        consulta = st.text_input("Consulta")
        
        #linha divisória
        st.write("---")

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


#Conteúdo aba5

with aba5:
    st.header("Módulo de remuneração e benefícios")


#Conteúdo aba6

with aba6:
    st.header("Tabelas")
