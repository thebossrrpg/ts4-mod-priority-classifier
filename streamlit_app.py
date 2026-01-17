import streamlit as st
import sys
import os

# Adiciona src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# from web_scraper import extract_mod_content
# from llm_client import classify_with_llm  
# from notion_updater import update_notion_page

# Configuração da página
st.set_page_config(
    page_title="TS4 Mod Classifier",
    page_icon="🎮",
    layout="wide"
)

# CSS customizado
st.markdown("""
<style>
.big-font {font-size:20px !important; font-weight: bold;}
.success-box {padding: 20px; border-radius: 10px; background-color: #d4edda; border: 1px solid #c3e6cb;}
.info-box {padding: 15px; border-radius: 8px; background-color: #d1ecf1; border: 1px solid #bee5eb;}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎮 TS4 Mod Priority Classifier")
st.markdown("**Sistema automatizado de classificação de mods de The Sims 4**")
st.divider()

# Sidebar - Configurações
with st.sidebar:
    st.header("⚙️ Configurações")
    
    st.subheader("🤖 LLM API")
    llm_provider = st.selectbox(
        "Provedor LLM",
        ["Google Gemini (Grátis)", "OpenAI", "Anthropic"],
        help="Google Gemini é gratuito até 60 req/min"
    )
    
    if "Gemini" in llm_provider:
        model = "gemini-1.5-pro"
        api_label = "Google API Key"
        help_text = "Pegue em: https://makersuite.google.com/app/apikey"
    elif "OpenAI" in llm_provider:
        model = "gpt-4o"
        api_label = "OpenAI API Key" 
        help_text = "Pegue em: https://platform.openai.com/api-keys"
    else:
        model = "claude-3-opus-20240229"
        api_label = "Anthropic API Key"
        help_text = "Pegue em: https://console.anthropic.com/"
    
    llm_api_key = st.text_input(
        api_label,
        type="password",
        help=help_text
    )
    
    st.divider()
    
    st.subheader("📓 Notion")
    notion_api_key = st.text_input(
        "Notion API Key",
        type="password",
        help="Pegue em: https://www.notion.so/my-integrations"
    )
    
    st.info("💡 **Opcional:** Deixe em branco se quiser apenas classificar sem atualizar o Notion")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔗 Informações do Mod")
    mod_url = st.text_input(
        "URL da página do mod",
        placeholder="https://modthesims.info/d/...",
        help="Cole aqui a URL completa da página do mod"
    )
    
    notion_page_id = st.text_input(
        "Notion Page ID (opcional)",
        placeholder="abc123def456...",
        help="ID da página do Notion para atualizar"
    )

with col2:
    st.subheader("📊 Status")
    if llm_api_key:
        st.success("✅ LLM configurado")
    else:
        st.warning("⚠️ LLM não configurado")
    
    if notion_api_key:
        st.success("✅ Notion configurado")
    else:
        st.info("ℹ️ Notion opcional")

st.divider()

# Botão de classificação
if st.button("🚀 Classificar Mod", type="primary", use_container_width=True):
    if not mod_url:
        st.error("❌ Por favor, forneça a URL do mod")
    elif not llm_api_key:
        st.error("❌ Por favor, configure a API key do LLM")
    else:
        try:
            # Progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # 1. Extrair conteúdo
            status_text.text("🔍 [1/3] Extraindo conteúdo da página...")
            progress_bar.progress(33)
            mod_content = extract_mod_content(mod_url)
            
            # 2. Classificar
            status_text.text("🤖 [2/3] Classificando com LLM...")
            progress_bar.progress(66)
            os.environ['LLM_API_KEY'] = llm_api_key
            os.environ['LLM_MODEL'] = model
            classification = classify_with_llm(mod_content)
            
            # 3. Atualizar Notion (se fornecido)
            if notion_page_id and notion_api_key:
                status_text.text("📓 [3/3] Atualizando Notion...")
                progress_bar.progress(90)
                os.environ['NOTION_API_KEY'] = notion_api_key
                update_notion_page(notion_page_id, classification)
            
            progress_bar.progress(100)
            status_text.empty()
            progress_bar.empty()
            
            # Resultado
            st.success("✅ **Classificação concluída com sucesso!**")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Priority",
                    f"{classification['priority']}",
                    classification.get('priority_label', '')
                )
            
            with col2:
                if classification.get('sub_category'):
                    st.metric(
                        "Sub-categoria",
                        classification['sub_category'],
                        classification.get('sub_category_label', '')
                    )
            
            with col3:
                st.metric("Palavras Analisadas", mod_content.get('word_count', 0))
            
            st.subheader("📝 Justificativa")
            st.info(classification.get('notes_reason', 'N/A'))
            
            # Detalhes extras
            with st.expander("🔍 Ver detalhes do mod"):
                st.write("**Título:**", mod_content.get('title', 'N/A'))
                st.write("**Descrição:**", mod_content.get('description', 'N/A')[:300] + "...")
            
        except Exception as e:
            st.error(f"❌ **Erro:** {str(e)}")
            with st.expander("🐞 Ver detalhes do erro"):
                st.exception(e)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>👨‍💻 Desenvolvido com Streamlit | 
    <a href='https://github.com/thebossrrpg/ts4-mod-priority-classifier' target='_blank'>GitHub</a>
    </p>
</div>
""", unsafe_allow_html=True)
