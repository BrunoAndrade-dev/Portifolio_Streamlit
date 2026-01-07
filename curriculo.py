import streamlit as st 
from PIL import Image
import base64
import os

def abrirpdf (caminho_arquivo,  botao) : 
    try : 
        with open(caminho_arquivo, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = f'''
            <a href="data:application/pdf;base64,{base64_pdf}" 
               target="_blank" 
               style="text-decoration: none; background-color: #ff4b4b; color: white; 
                      padding: 10px 20px; border-radius: 8px; display: inline-block;">
               {botao}
            </a>
        '''
        st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Arquivo PDF não encontrado. Verifique se o nome está correto!")    

st.set_page_config(page_title = "Meu Portifólio" , layout = "wide")

with st.sidebar :
   st.title = "Aba de navegação"
   op = st.radio("Ir para" , ["Sobre mim" , "habilidades" , "Projetos" , "Contato"])

if op == "Sobre mim" : 
   st.header("📚​Vamos nos conhecer melhor!")
   col1 , col2  = st.columns([1,3] , gap = "small")
   st.divider()
   with col1 : 
      st.image("curriculo.jpeg" , width = 300)

   with col2 : 
      st.markdown("""
      ## Olá! Meu nome é **Bruno Raphael**

      Sou estudante do 5º período de Engenharia da Computação na Universidade Estadual do Maranhão (UEMA). Tenho paixão por análise de dados com Python e desenvolvimento de software com Java, buscando constantemente novos desafios e oportunidades de aprendizado.

      Desenvolvi projetos focados em análise de dados, abrangendo tratamento, visualização, extração de insights e criação de dashboards interativos utilizando o Streamlit. Atualmente, sou integrante do Laboratório de Engenharia Aplicada (LEA) da UEMA e do grupo SynapseLab, onde foco em soluções de dados aplicadas a problemas do mundo real.

      Estou animado para compartilhar meus conhecimentos e experiências através deste portfólio. Vamos juntos nessa jornada de aprendizado e crescimento profissional!

      Nas abas laterais, você encontrará detalhes sobre minhas habilidades, projetos e informações de contato. Fique à vontade para explorar!
      """)    
elif op == "habilidades" : 
   st.header ("🛠️​ Minhas Habilidades")
   aba1 , aba2 = st.columns([1,1], gap = "large")
   with aba1 : 
      st.markdown("### 📊 Análise de Dados")
        
      st.progress(100, text="Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit)")
      st.progress(100, text="Tratamento e limpeza de dados")
      st.progress(100, text="Visualização de dados")
      st.progress(100, text="Extração de insights")
      st.progress(95, text="Criação de dashboards interativos")
      st.progress(70, text="Excel básico")
      st.progress(60, text="SQL básico")

   with aba2 : 
      st.markdown ("""
      ### 💻 Desenvlvimento de Software """)  
      
      st.progress(75, text = "Java( POO, SpringBoot )")
      st.progress(100, text = "Git e Github")
      st.progress (95, text = "Lógica de Programação")
      st.progress(95 ,text = "Estrutura de Dados")
elif op == "Projetos" :   
   st.header ("🚀​ Meus Projetos")  
   st.write ("Aqui estão alguns dos meus projetos de análise de dados e desenvolvimento de software:") 
   proj1, proj2 = st.columns(2, gap = "large")
   with proj1 : 
      with st.container (border = True) : 
         st.subheader ("Análise de Dados Sociais com Python") 
         st.caption ("Projeto feito em conjunto com colegas do Laboratóro de Engenharia Aplicada (LEA) da UEMA.")

         st.caption ("Buscamos compreender a taxa de analfabetismo entre jovens a partir de 15 anos nos estados do Maranhão. Em primeiro plano, realizamos a coleta de dados no IPEADATA, seguida pela limpeza e tratamento.")

         st.caption ("Posteriormente, buscamos extrair insights relevantes por meio da criação de gráficos, que foram essenciais para a criação de um artigo científico, que pode ser visto clicando no botão abaixo.")

         if st.button ("Artigo Científico") : 
            abrirpdf ("artigo.pdf" , "Abrir")

         st.caption ("Além disso, desenvolvemos um dashboard interativo, permitindo a visualização dinâmica dos dados e insights extraídos. ")   

         if st.button ("Dashboard Interativo") :
            st.link_button("Acessar" , "https://sitearquivo.streamlit.app")

         st.caption ("Tecnologias utilizadas: Python (Pandas, NumPy, Matplotlib, Seaborn, Streamlit)" )

         st.caption("Durante esse projeto, adquiri habilidades valiosas em análise de dados, tratamento de dados e visualização, além de guiar uma oficina sobre análise de dados utilizando Python na Semana de Administração da UFMA (SEAD) 2024. É importante ressaltar que ganhamos o prémio de segundo melhor artigo cietífico e oficina ")  
         
         foto1 , foto2 , foto3 = st.columns(3)
         with foto1 : 
            st.image("ME.jpeg" , width = 300)         
         with foto2 :
            st.image("Certificacao.jpeg", width = 2000) 
         with foto3 :
            st.image("PremioALL.jpeg" , width= 300)    
   with proj2 :
      with st.container(border = True) : 
         st.subheader ("Machine Learning - Taxa de sobreviventes do Titanic")
         st.caption ("Projeto utilizando o método Random Forest para prever a taxa de sobrevivência dos passageiros do Titanic com base em características como idade, sexo, classe social...")      

         st.caption ("Depois do tratamento e limpeza dos dados, apliquei o algoritmo de Random Forest para criar um modelo preditivo. Avaliei o desempenho do modelo utilizando métricas como acurácia, precisão e recall.Com isso, consegui criar um dashboard interativo para visualizar os resultados.")

         if st.button("Dashboard Titanic") : 
            st.link_button("Acessar", "https://brunoandrade-dev-machine-lea-sourcefuncoes-auxiliaresapp-dndk9f.streamlit.app/")

         st.caption ("Tecnologias utilizadas: Python (Pandas, NumPy, Scikit-learn, Streamlit)")

         st.caption("Esse projeto me proporcionou uma compreensão prática de machine learning, desde o pré-processamento dos dados até a avaliação do modelo, além de aprimorar minhas habilidades em Python e análise de dados.")   