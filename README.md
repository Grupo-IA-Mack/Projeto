# Projeto

# Projeto Match

## Integrantes
- Murilo Kenichiro Senaga, 10395789
- Kenny Jun Takahashi, 10396373
- João Pedro Mota Paes Rodrigues de Almeida, 10395291
- Lucas Kenzo Kawamoto 10396359
- Lucas Pinheiro, 10391001

## Problema a ser Resolvido
O projeto tem como objetivo ajudar pessoas a encontrarem outras com gostos musicais semelhantes, utilizando os dados fornecidos pela Spotify API. A principal necessidade a ser atendida é facilitar a conexão entre usuários com base em seus hábitos musicais, gerando "matches" que permitam a descoberta de novas amizades ou comunidades com gostos musicais em comum.

## Dados
Os dados utilizados serão extraídos da Spotify Web API, que oferece uma vasta gama de informações sobre:
- Playlists do usuário
- Artistas favoritos
- Características de áudio das faixas (tempo, valência, energia, acústica e popularidade)
- Histórico de músicas mais tocadas

## Ferramentas e Métodos

### Coleta de Dados via Spotify API
Utilizando a Spotify Web API, serão coletadas informações sobre playlists, faixas, artistas e características de áudio. A API permite a extração de informações no formato JSON, que será convertido em formato tabular para análise com Pandas.

### Pré-processamento dos Dados
Serão utilizadas bibliotecas como Pandas e NumPy para processar e organizar os dados em colunas categóricas e numéricas, para extrair métricas relevantes dos hábitos musicais dos usuários.

### Similaridade de Perfis
Será utilizada a biblioteca scikit-learn para calcular a similaridade entre perfis musicais utilizando métricas de distância, como distância Euclidiana. Essas medidas de similaridade serão usadas para comparar as características das faixas ou hábitos musicais dos diferentes usuários, sem necessidade de treinamento de modelos.

### Implementação com Docker
Toda a aplicação será containerizada utilizando Docker, com um Dockerfile configurando o ambiente Python, incluindo as bibliotecas necessárias, como Pandas, scikit-learn, NumPy, Flask e o cliente da API do Spotify.

### Apresentação dos Resultados
Será utilizada a ferramenta Flask para criar a interface web, que exibirá os "matches" de usuários com gostos musicais semelhantes. A interface apresentará os perfis de outros usuários, indicando a proximidade dos gostos musicais e destacando os percentuais de similaridade.

