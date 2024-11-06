# Projeto Mood

## Integrantes
- Murilo Kenichiro Senaga, 10395789
- Kenny Jun Takahashi, 10396373
- João Pedro Mota Paes Rodrigues de Almeida, 10395291
- Lucas Kenzo Kawamoto, 10396359
- Lucas Pinheiro, 10391001

### Introdução  
Este projeto visa criar um classificador de humor musical utilizando características de áudio das músicas de um artista, extraídas da Spotify Web API. Com o aumento do consumo de streaming, os usuários buscam novas maneiras de explorar músicas baseadas em suas emoções ou preferências de humor. Nosso objetivo é fornecer uma ferramenta que permita a classificação das músicas de um artista com base em valência (felicidade) e energia. Essa ferramenta utiliza algoritmos de aprendizado de máquina, auxiliando o usuário a identificar músicas que correspondem ao seu estado emocional. Além disso, a interface permite a visualização interativa dos resultados, proporcionando insights sobre as variações emocionais das músicas do artista.

### Referencial Teórico  
A classificação de humor em músicas envolve a aplicação de aprendizado de máquina a dados tabulares, onde características de áudio (valência e energia) são usadas como variáveis para categorizar o humor das músicas. Diferentes algoritmos de classificação, como k-nearest neighbors, árvore de decisão, Naive Bayes, e SVM, são aplicados para analisar e prever o humor das faixas. A Spotify API fornece uma grande fonte de dados, oferecendo atributos que descrevem o humor e a energia das músicas, permitindo um bom treinamento e comparação entre diferentes classificadores.

### Metodologia  

**Coleta de Dados:** A Spotify Web API foi utilizada para coletar dados de músicas de um artista específico. As características extraídas incluem valência e energia, que são usadas para a classificação do humor, além do ID e nome da música.

**Pré-processamento:** Os dados coletados são tratados para eliminar valores nulos e garantir a consistência das características de áudio. A valência e a energia são usadas como os principais atributos para a classificação do humor.

**Classificação de Humor:** Inicialmente, um modelo baseado em regras é usado para categorizar as músicas em "Alegre", "Calmo", "Energético" e "Triste". Além disso, diversos algoritmos de aprendizado de máquina, como K-Nearest Neighbors, árvore de decisão, Naive Bayes e SVM, são aplicados para treinar classificadores usando os dados de valência e energia, permitindo comparar a precisão entre diferentes métodos.

**Visualização e Interface:** A aplicação foi desenvolvida com Streamlit, permitindo ao usuário inserir o nome de um artista e visualizar a distribuição de humor das músicas desse artista. Gráficos interativos são gerados para ilustrar as distribuições de humor e a relação entre valência e energia.

### Resultados  
A aplicação classifica as músicas em diferentes categorias de humor com base nas características de valência e energia fornecidas pela Spotify API. Além do modelo baseado em regras, foram aplicados algoritmos de aprendizado de máquina, e os resultados de classificação foram comparados usando métricas como precisão e relatórios de classificação. As visualizações resultantes demonstram padrões de humor para cada artista pesquisado, possibilitando ao usuário explorar os dados de maneira interativa e obter insights sobre as preferências emocionais das músicas.

### Conclusão  
Este projeto demonstrou a viabilidade de uma ferramenta de classificação de humor para músicas, utilizando tanto um modelo baseado em regras quanto classificadores de aprendizado de máquina. A interface construída permite uma exploração intuitiva e personalizada das músicas de um artista específico.
