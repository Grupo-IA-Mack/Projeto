## Estrutura do Código

### **main.py**
- **Autenticação com a Spotify API**: Realiza a autenticação usando o `CLIENT_ID` e `CLIENT_SECRET` armazenados no arquivo `.env`.
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
## link do vídeo: 
https://youtu.be/9i6xHCKojpA

## Procedimentos de instalação

### Pré-requisitos

- **Python 3.9** ou superior instalado.
- Conta de desenvolvedor na [API do Spotify](https://developer.spotify.com/) para obter as credenciais `CLIENT_ID` e `CLIENT_SECRET`.
- **Opcional**: Docker instalado, caso prefira executar a aplicação em um container.

### Obtendo as Credenciais da API do Spotify

1. Acesse o [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Faça login com sua conta do Spotify.
3. Crie um novo aplicativo e dê um nome e descrição.
4. Após a criação, você terá acesso ao `CLIENT_ID` e `CLIENT_SECRET` na página do aplicativo.

### Instalação sem Docker

#### 1. Clonar o Repositório
Clone o repositório do projeto para sua máquina local ou faça o download dos arquivos do projeto.
```bash
git clone https://github.com/Grupo-IA-Mack/Projeto.git
```

### 2. Navegar até o Diretório do Projeto
```bash
cd Projeto/Projeto Mood
```

### 3. Criar um Ambiente Virtual (Opcional, mas Recomendado)
```bash
python -m venv venv
```

Ativar o ambiente virtual:

- No Windows:
  ```bash
  venv\Scripts\activate
  ```

- No macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 5. Configurar as Credenciais da API do Spotify
Crie um arquivo `.env` na raiz do projeto (se ainda não existir) e insira suas credenciais:
```bash
echo "CLIENT_ID='seu_client_id'" > .env
echo "CLIENT_SECRET='seu_client_secret'" >> .env
```

### 6. Executar a Aplicação
```bash
streamlit run main.py
```

### 7. Acessar a Aplicação
Abra seu navegador e acesse:
```
http://localhost:8501
```

## Instalação e Execução com Docker

### 1. Clonar o Repositório
```bash
git clone https://github.com/Grupo-IA-Mack/Projeto.git
```

### 2. Navegar até o Diretório do Projeto
```bash
cd Projeto/Projeto Mood
```

### 3. Configurar as Credenciais da API do Spotify
Edite o arquivo `.env` e insira suas credenciais:
```bash
echo "CLIENT_ID='seu_client_id'" > .env
echo "CLIENT_SECRET='seu_client_secret'" >> .env
```

### 4. Construir a Imagem Docker
```bash
docker build -t mood-app .
```

### 5. Executar o Container
```bash
docker run -p 8501:8501 mood-app
```

### 6. Acessar a Aplicação
Abra seu navegador e acesse:
```
http://localhost:8501

