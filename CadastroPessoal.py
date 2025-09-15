import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd




st.set_page_config(page_title="IntegraSGP", layout = "wide")

# ====== Barra Superior ======

def top_menu():
    st.markdown(
        """
        <style>
        .top-bar {
            background-color: #1B3E74;
            padding: 10px 25px;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
        }
        .top-bar h2 {
            margin: 0;
            font-size: 20px;
            font-weight: bold;
        }
        .top-bar a {
            text-decoration: none;
            margin-left: 20px;
            color: white;
            font-weight: 500;
        }
        .top-bar a:hover {
            color: #FFD700;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="top-bar">
            <h2>GOV.BR</h2>
            <div>
                <a href="#">COMUNICA BR</a>
                <a href="#">ACESSO À INFORMAÇÃO</a>
                <a href="#">PARTICIPE</a>
                <a href="#">LEGISLAÇÃO</a>
                <a href="#">ÓRGÃOS DO GOVERNO</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Chamar no topo
top_menu()

    #Criando abas

#aba0, aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs(["**IntegraSGP**", "**Informações Funcionais**", "**Carreira e desenvolvimento**", "**Saúde e Bem-estar**", "**Gestão da força de trabalho**", "**Remuneração e benefícios**", "**Tabelas**", "**Relatórios**"])


#CONTEÚDO ABA0

#********************************************************************************************************************
  
#MENU LATERAL

with st.sidebar:
    st.markdown("""
        <h2 style='text-align: center; font-size: 22px; font-weight: bold;'>
            Menu
        </h2>
        """,
        unsafe_allow_html=True
    )
    escolha = option_menu(
    None,
    [
        "Início",
        "Servidores",
        "Carreira e desenvolvimento",
        "Saúde e Bem-estar",
        "Gestão da força de trabalho",
        "Remuneração e benefícios",
        "Tabelas",
        "Relatórios",
        ],
    icons=[
        "display",
        "person",
        "book",
        "heart",
        "file-person",
        "cash-coin",
        "table",
        "copy"
        ],
    default_index=0,
    styles={
            "container": {"padding": "0.5rem", "background-color": "#ffffff"},
            "icon": {"color": "#1B3E74", "font-size": "1.1rem"},
            "nav-link": {
                "font-size": "0.95rem",
                "padding": "0.35rem 0.5rem",
                "margin": "0.15rem 0",
            },
            "nav-link-selected": {"background-color": "rgba(24,80,153,.60)", "font-weight": "700"},
        }
    )
    
#************************************************************************************************************

# ========== COMPONENTE: FILTROS (definido ANTES do uso) ==========

def filtros_info_funcionais():
        st.subheader("Consulta servidores")
        
        # CSS do card
        st.markdown("""
        <style>
        .card-filtro {
            background: #eef3f6;         /* cinza-azulado leve */
            border: 1px solid #d8dee4;
            border-radius: 12px;
            padding: 16px 16px 8px 16px;
            margin-bottom: 12px;
        }
        .card-filtro label p {           /* deixa os labels mais fortes */
            font-weight: 600 !important;
            margin-bottom: 4px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        # CARD + FORM: isto é o que realmente desenha a “tela de filtro”

        with st.container():
            st.markdown('<div class="card-filtro">', unsafe_allow_html=True)

            with st.form("form_filtros_funcionais"):
                c1, c2, c3, c4, c5 = st.columns(5)
                with c1:
                    nome = st.text_input("Nome:")
                    cargo_funcao = st.selectbox("Cargo/Função Comissionada:", ["-- Selecione --","CGE I","CA I","CCT V"])
                with c2:
                    cpf = st.text_input("CPF:")
                    funcao = st.selectbox("Função:", ["-- Selecione --","Superintendente","Coordenador","Analista"])
                with c3:
                    uorg = st.selectbox("UORG:", ["-- Selecione --","SGP","SRM","SFG"])
                    grupo = st.selectbox("Grupo Gestão:", ["-- Selecione --","Titular UORG","Gerência","Coordenação"])
                with c4:
                    vinculo = st.selectbox("Vínculo:", ["-- Selecione --","Efetivo","Comissionado","Terceirizado"])
                    participante_pgd = st.selectbox("Participante PGD:", ["-- Selecione --","Sim","Não"])
                with c5:
                    cargo = st.selectbox("Cargo:", ["-- Selecione --","Especialista","Analista","Técnico"])
                    modalidade = st.selectbox("Modalidade:", ["-- Selecione --","Teletrabalho Parcial","Integral","Presencial"])
                
        
                enviar = st.form_submit_button("Filtrar")
                
                
            st.markdown('</div>', unsafe_allow_html=True)

            return enviar, {
                "nome": nome.strip(),
                "cpf": "".join(filter(str.isdigit, cpf)),
                "uorg": uorg if uorg != "-- Selecione --" else "",
                "vinculo": vinculo if vinculo != "-- Selecione --" else "",
                "cargo": cargo if cargo != "-- Selecione --" else "",
            }

        
                
#*********************************************************************************************************************

# ========== PÁGINAS ==========


#CONTEÚDO PAGINA_HOME

def page_home():
    st.header("IntegraSGP")
    st.text("IntegraSGP: v.1.0.1")
    with st.container():
        st.image("integra.jpg", use_container_width=True)
    
#*********************************************************************************************************************    

#CONTEÚDO PAGINA_INFOS_servidores

def page_info_servidores():
    st.header("Cadastro de Servidores")
    
    #linha divisória
    st.write("---")

    ###################
    # 1) Tabela "persistente" no app
    if "serv_df" not in st.session_state:
        st.session_state.serv_df = pd.DataFrame({
            "Nome":["Ana Silva","Bruno Costa","Carla Nunes"],
            "CPF":["11111111111","22222222222","33333333333"],
            "UORG":["SGP","SFG","SGP"],
            "Vínculo":["Efetivo","Comissionado","Efetivo"],
            "Cargo":["Analista","Especialista","Técnico"],
            "Cargo/Função comissionada":["CGE IV","CA I","CCT III"],
            "Função":["Superintendente","Assessor","Coordenador"],
            "Grupo Gestão":["Titular uorg","Coordenação","Gerência"],
            "Participante PGD":["Sim","Não","Sim"],
            "Modalidade PGD":["Parcial","Integral","Presencial"],
            "Ações":["Editar/Ver/Salvar","Editar/Ver/Salvar","Editar/Ver/Salvar"],
        })


    # 2) Formulário de inclusão
    st.subheader("Incluir servidor")
    with st.expander("Incluir servidor", expanded=False):
        nome  = st.text_input("**NOME**",  key="in_nome")
        cpf   = st.text_input("**CPF**",   key="in_cpf")
        email = st.text_input("**E-MAIL INSTITUCIONAL**", key="in_email")
        matricula = st.text_input("**Matrícula siape**", key="in_matricula")
        uorg  = st.text_input("**Unidade Organizacional**", key="in_uorg")
        vinc  = st.text_input("**VÍNCULO (ex: efetivo, comissionado, quadro específico)**", key="in_vinc")
        cargo = st.text_input("**CARGO (ex: Especialista, Analista, Técnico)**", key="in_cargo")
        cargof = st.text_input("**CARGO/FUNÇÃO COMISSIONADA (ex: CGE I, CA I, CGE IV, CCT V)**", key="in_cargof")
        func  = st.text_input("**FUNÇÃO (ex: Superintendente de gestão de pessoas)**", key="in_func")
        lot   = st.text_input("**LOTAÇÃO**", key="in_lot")
        grupo = st.text_input("**GRUPO GESTÃO (ex: titular uorg, gerência, coordenação)**", key="in_grupo")
        pgd   = st.text_input("**Participante do PGD/Modalidade**", key="in_pgd")

        if st.button("Incluir", type="primary"):
            # validações básicas
            if not nome or not cpf:
                st.warning("Preencha pelo menos **Nome** e **CPF**.")
            elif (st.session_state.serv_df["CPF"] == cpf).any():
                st.error("Já existe um servidor com esse **CPF**.")
            else:
                novo = {
                    "Nome": nome,
                    "CPF": cpf,
                    "UORG": uorg or "",
                    "Vínculo": vinc or "",
                    "Cargo": cargo or "",
                    "Cargo/Função comissionada": cargof or "",
                    "Função": func or "",
                    "Grupo Gestão": grupo or "",
                    "Participante PGD": pgd or "",
                    "Modalidade PGD": "",  # preencha se tiver no formulário
                }
                st.session_state.serv_df = pd.concat(
                    [st.session_state.serv_df, pd.DataFrame([novo])],
                    ignore_index=True
                )
               
                
                ########################################
                st.session_state.serv_df.to_csv("servidores.csv", index=False, encoding="utf-8")

                                 # inclui/valida...
                

                ############################################

                                
                st.success(f"Servidor **{nome}** incluído.")
                

                # limpa campos
                for k in [
                    "in_nome","in_cpf","in_email","in_matricula","in_uorg","in_vinc",
                    "in_cargo","in_cargof","in_func","in_lot","in_grupo","in_pgd"
                ]:
                    st.session_state[k] = ""
                    
                
    

    st.write("---")

    # 3) Filtros
    clicou, filtros = filtros_info_funcionais()

    # 4) Aplica filtros sobre a TABELA PERSISTIDA
    df = st.session_state.serv_df.copy()
    q = df.copy()
    if clicou:
        if filtros["nome"]:
            q = q[q["Nome"].str.contains(filtros["nome"], case=False, na=False)]
        if filtros["cpf"]:
            q = q[q["CPF"].str.contains(filtros["cpf"], na=False)]
        if filtros["uorg"]:
            q = q[q["UORG"] == filtros["uorg"]]
        if filtros["vinculo"]:
            q = q[q["Vínculo"] == filtros["vinculo"]]
        if filtros["cargo"]:
            q = q[q["Cargo"] == filtros["cargo"]]
        st.success(f"{len(q)} registro(s) encontrado(s).")

    # 5) Exibe a tabela final (já com a inclusão)
    st.dataframe(q, use_container_width=True)

    ####################
    
        
    #linha divisória
    st.write("---")



    
  

    

#*********************************************************************************************************

#CONTEÚDO PAGINA_CARREIRA

def page_carreira():
    st.header("Carreira e desenvolvimento")
    st.write("Conteúdo da página…")

#*********************************************************************************************************

#CONTEÚDO PAGINA_SAUDE

def page_saude():
    st.header("Saúde e Bem-estar")
    #linha divisória
    st.write("---")

    st.radio("Escolha uma opção:", ["Planos de saúde", "SIASS", "Ambulatório"])

    #linha divisória
    st.write("---")
      
    




#*********************************************************************************************************

def page_gestao_forca():
    st.header("Gestão da força de trabalho")
     #linha divisória
    st.write("---")

    st.radio("Escolha uma opção:", ["Movimentação interna e externa", "Dimensionamento da força de trabalho (DFT)", "Terceirização", "Estágio"])

    #linha divisória
    st.write("---")

   



#*********************************************************************************************************

def page_remuneracao():
    st.header("Remuneração e benefícios")
    
    #linha divisória
    st.write("---")

     #submenu aba5

    st.radio("Escolha uma opção:", ["Aposentadoria e pensão", "benefícios"])

    #linha divisória
    st.write("---")
        
#*********************************************************************************************************

def page_tabelas():
    st.header("Tabelas")
       
    #linha divisória
    st.write("---")    


    with st.expander("Tabelas básicas e cadastrais"):
        submenuTABCAD = st.radio("Escolha uma opção:", ["Nacionalidade", "Naturalidade", "Formação Acadêmica"])
    with st.expander("Tabelas institucionais"):
        submenuTABINST = st.radio("Escolha uma opção:", ["Servidores", "Cargos", "Cargos/funções comissionadas", "Unidades Organizacionais", "Órgãos", "Tipo de movimentação", "Tipo de servidor", "Regime jurídico", "Desligamento"])
 


#*********************************************************************************************************

def page_relatorios():
    st.header("Relatórios")
    st.write("Conteúdo da página…")



#*********************************************************************************************************

#ROTEADORES

ROUTES = {
    "Início": page_home,
    "Servidores": page_info_servidores,
    "Carreira e desenvolvimento": page_carreira,
    "Saúde e Bem-estar": page_saude,
    "Gestão da força de trabalho": page_gestao_forca,
    "Remuneração e benefícios": page_remuneracao,
    "Tabelas": page_tabelas,
    "Relatórios": page_relatorios,
}

ROUTES[escolha]()  # renderiza a página selecionada









