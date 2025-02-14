import streamlit as st
from io import BytesIO
from PIL import Image
import base64

# Definir a classe Usuario
class Usuario:
    def __init__(self, nome, foto):
        self.nome = nome
        self.foto = foto
    
    def obter_foto_base64(self):
        return base64.b64encode(self.foto.read()).decode('utf-8')

# Função principal da página Streamlit
def main():
    st.title('Cadastro de Usuário')
    
    # Entrada de dados do usuário
    nome = st.text_input("Digite o nome do usuário")
    foto_upload = st.file_uploader("Faça o upload da foto", type=["png", "jpg", "jpeg"])

    if nome and foto_upload:
        # Criar objeto Usuario
        usuario = Usuario(nome, foto_upload)
        
        # Converter a foto para Base64
        foto_base64 = usuario.obter_foto_base64()
        
        # Exibir nome e imagem
        st.write(f"Nome: {usuario.nome}")
        st.image(foto_upload, caption="Foto do Usuário", use_column_width=True)
        
        # Exibir a string Base64 da foto
        st.text_area("String Base64 da foto:", foto_base64, height=200)

if __name__ == "__main__":
    main()
