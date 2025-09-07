import streamlit as st



st.set_page_config(page_title="IntegraSGP")
st.set_page_config(layout="wide")



    #Criando abas

aba0, aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs(["IntegraSGP", "Informações Funcionais", "Capacitação", "Saúde e Desempenho", "Planejamento e gestão da força de trabalho", "Remuneração e benefícios", "Tabelas", "Relatórios"])

#linha divisória
st.write("---")

#CONTEÚDO ABA0

with aba0:
    st.header("INTEGRASGP")
    st.text("IntegraSGP: v.1.0.0")
    
    with st.container():
        st.image("integra.jpg", use_container_width=True)
    


#CONTEÚDO ABA1

with aba1:
    st.header("Módulo de Informações funcionais")

    #submenu aba1

    submenuaba1 = st.radio("Escolha uma opção:", ["Cadastro", "Cargo comissionado", "Movimentação", "Desligamento"])

    #linha divisória
    st.write("---")
        
    if submenuaba1 == "Cadastro":
        st.subheader("Consulta")

        #criando as colunas

        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("Consultar")
        with col2:
            st.button("Incluir")
        with col3:
            st.button("Alterar")

                        
        consulta = st.text_input("Consulta")
        
        #linha divisória
        st.write("---")

        st.subheader("Dados do servidor")
        nome = st.text_input("NOME")
        cpf = st.number_input("CPF")
        email = st.text_input("E-MAIL INSTITUCIONAL")
        Matrícula_siape = st.number_input("Matrícula siape")
        Vinculo = st.text_input("VÍNCULO (ex: efetivo, comissionado, quadro específico)")
        cargo = st.text_input("CARGO (ex: Especialista, Analista, Técnico)")
        CargoFuncao = st.text_input("CARGO/FUNÇÃO COMISSIONADA (ex: CGE I, CA I, CGE IV, CCT V)")
        função = st.text_input("FUNÇÃO (ex: Superintendente de gestão de pessoas)")
        lotação = st.text_input("LOTAÇÃO")
        GrupoGestao = st.text_input("GRUPO GESTÃO (ex: titular uorg, gerência, coordenação)")

        #Campos para expansão

        with st.expander("Demais dados (FUNCIONAIS)"):
            OrgãoEmpresa = st.text_input("ÓRGÃO/EXMPRESA (ex: ANEEL, INFRAERO)")
            IngressoANEEL = st.text_input("INGRESSO NA ANEEL")
            DataServicoPublico = st.text_input("INGRESSO NO SERVIÇO PÚBLICO")
            pgd = st.text_input("MODALIDADE DE PGD")
            diretor = st.text_input("DIRETOR")

        with st.expander("Demais dados (PESSOAIS)"):
            identidade = st.text_input("IDENTIDADE")
            DataNascimento = st.text_input("DATA DE NASCIMENTO")
            EmailPessoal = st.text_input("E-MAIL PESSOAL")
            Telefone = st.text_input("TELEFONE")
            NomePai = st.text_input("NOME DO PAI")
            NomeMae = st.text_input("NOME DA MÃE")
            Endereço = st.text_input("ENDEREÇO")
            sexo = st.text_input("SEXO")
            RaçaCor = st.text_input("RAÇA/COR")
            pcd = st.text_input("PCD")
            

    if submenuaba1 == "Movimentação":
        st.subheader("Movimentações internas e externas")
        with st.expander("MOVIMENTAÇÃO INTERNA (ex: bim)"):
            teste = st.text_input("XXXX")
        with st.expander("CESSÃO/REQUISIÇÃO"):
            teste = st.text_input("teste")
        with st.expander("OUTROS ÓRGÃOS PARA A ANEEL (ex: cessão, requisição, movimentação força de trabalho)"):
            teste = st.text_input("YYYYY")


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

     #submenu aba6

    submenuaba6 = st.radio("Escolha uma opção", ["Servidores", "Cargos", "Cargos/funções comissionadas", "Lotação", "Órgãos", "Tipo de movimentação", "Tipo de servidor"])

    if submenuaba6 == "Tabelas":
        st.subheader("Cargos")

#Conteúdo aba7

with aba7:
    st.header("Relatórios")
