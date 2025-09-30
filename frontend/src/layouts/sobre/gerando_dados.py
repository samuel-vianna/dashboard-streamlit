import streamlit as st

def AboutGenerateDataTab():
    # ------------------------------
    st.header("⚙️ Como gerar novos dados")
    st.write(
        """
        Você pode gerar novos dados diretamente pelo dashboard:

        1. Acesse a página **Gerar comentários** no menu lateral.  
        2. Defina os parâmetros desejados (quantidade de registros, variação de notas, etc).  
        3. Clique em **Gerar** para popular a base de dados.  
        4. Os gráficos e relatórios serão atualizados automaticamente.
        """
    )

    # ------------------------------
    st.subheader("Dados de filiais")
    st.write(
        """
        É possível cadastrar filiais diferentes diretamente pelo dashboard:

        1. Acesse a página **Filias** no menu lateral.  
        2. Defina o nome da nova filial.
        3. Clique em **Cadastrar filial** para criar a nova filial.
        """
    )


    st.success("✅ Pronto! Agora você já entende como o projeto funciona.")
