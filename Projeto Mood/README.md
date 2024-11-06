# Estrutura do Código
  
### **main.py**  
- **Autenticação com a Spotify API**: Realiza a autenticação usando o CLIENT_ID e CLIENT_SECRET armazenados no arquivo `.env`.
- **Coleta de Dados de Áudio**: Extrai as características de valência e energia das músicas do artista selecionado.
- **Classificação de Humor**: Usa valência e energia para categorizar as músicas em quatro classes: "Alegre", "Calmo", "Energético" e "Triste".
- **Treinamento e Avaliação de Modelos**: Aplica algoritmos de aprendizado de máquina (K-Nearest Neighbors, Árvore de Decisão, Naive Bayes e SVM) para treinar e avaliar classificadores de humor.
- **Interface e Visualização**: Utiliza Streamlit para permitir a interação do usuário, exibindo resultados de classificação e gráficos que representam a distribuição de humor das músicas.

### **.env**
Arquivo de configuração para armazenar as credenciais do projeto, incluindo `CLIENT_ID` e `CLIENT_SECRET` e suas respectivas chaves para autenticação na Spotify API.

### **Dockerfile**
Arquivo para configuração do ambiente Docker. Ele configura a aplicação com:

- **Imagem base**: Usa Python 3.9 como imagem base.
- **Dependências**: Copia o arquivo `requirements.txt` e instala todas as dependências necessárias.
- **Exposição da porta**: Expõe a porta `8501` para que a aplicação Streamlit seja acessível.
- **Comando de execução**: Configura o comando para iniciar o Streamlit ao rodar o container.

### **requirements.txt**
Este arquivo lista todas as dependências do projeto, incluindo:

- `streamlit`: Para a criação da interface web interativa.
- `python-dotenv`: Para o gerenciamento seguro de variáveis de ambiente.
- `requests`: Para fazer chamadas HTTP à API do Spotify.
- `pandas`, `numpy`: Para manipulação e análise de dados.
- `matplotlib`: Para visualização de dados.
- `scikit-learn`: Para implementação e avaliação dos modelos de aprendizado de máquina.
