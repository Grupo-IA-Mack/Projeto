from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)

    if result.status_code != 200:
        st.error(f"Erro ao obter token: {result.status_code} - {result.text}")
        return None

    json_result = json.loads(result.content)
    token = json_result.get("access_token")
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=1"  

    query_url = f"{url}?{query}"  
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        st.error("Não foi possivel encontrar esse artista.")
        return None  
    
    return json_result[0]

def get_all_albums_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = get_auth_header(token)
    albums = []
    params = {"limit": 50, "include_groups": "album,single"}

    while url:
        result = get(url, headers=headers, params=params)
        json_result = json.loads(result.content)
        albums.extend(json_result["items"])
        url = json_result.get("next")

    return albums

def get_all_tracks_by_album(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    
    tracks = [{"id": track["id"], "name": track["name"]} for track in json_result]
    return tracks

def get_audio_features(token, track_ids):
    url = f"https://api.spotify.com/v1/audio-features"
    headers = get_auth_header(token)
    audio_features = []

    for i in range(0, len(track_ids), 100):
        batch_ids = track_ids[i:i+100]
        query = f"?ids={','.join(batch_ids)}"
        result = get(f"{url}{query}", headers=headers)

        if result.status_code != 200:
            st.error(f"Erro ao obter características de áudio: {result.status_code} - {result.text}")
            continue

        json_result = json.loads(result.content)
        if "audio_features" in json_result:
            audio_features.extend(json_result["audio_features"])

    return audio_features

def main():
    st.title("Projeto Mood")
    st.write("Classificador de humor das músicas de um artista")
    st.write("Esta ferramenta ajuda você a entender o humor das músicas de um artista específico. Basta inserir o nome do artista abaixo:")

    artist_name = st.text_input("Nome do artista:")
    if artist_name:
        token = get_token()
        result = search_for_artist(token, artist_name)
        if result is None:
            return

        artist_id = result["id"]
        albums = get_all_albums_by_artist(token, artist_id)

        track_data = []
        for album in albums:
            tracks = get_all_tracks_by_album(token, album["id"])
            track_data.extend(tracks)

        track_ids = [track["id"] for track in track_data][:2500]
        track_names = [track["name"] for track in track_data][:2500]

        audio_features = get_audio_features(token, track_ids)

        data = []
        for idx, features in enumerate(audio_features):
            if features is not None:
                valence = features['valence']
                energy = features['energy']
                track_id = track_ids[idx]
                track_name = track_names[idx]
                
                # Definindo o humor com base em Valence e Energy
                if valence > 0.5 and energy > 0.5:
                    mood = "Alegre"
                elif valence > 0.5 and energy <= 0.5:
                    mood = "Calmo"
                elif valence <= 0.5 and energy > 0.5:
                    mood = "Energético"
                else:
                    mood = "Triste"

                data.append([track_id, track_name, valence, energy, mood])

        df = pd.DataFrame(data, columns=['Track ID', 'Nome da Música', 'Valence', 'Energy', 'Humor'])
        st.write(df)

        # Preparação dos dados para o treinamento
        X = df[['Valence', 'Energy']]
        y = df['Humor']

        # Dividindo os dados
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Normalização dos dados
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Treinando o classificador KNN
        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train, y_train)
        y_pred_knn = knn.predict(X_test)

        # Treinando a árvore de decisão
        tree = DecisionTreeClassifier(random_state=42)
        tree.fit(X_train, y_train)
        y_pred_tree = tree.predict(X_test)

        # Treinando o classificador Naive Bayes
        nb = GaussianNB()
        nb.fit(X_train, y_train)
        y_pred_nb = nb.predict(X_test)

        # Treinando o classificador SVM
        svm = SVC(random_state=42)
        svm.fit(X_train, y_train)
        y_pred_svm = svm.predict(X_test)

        # Resultados
        st.subheader("Resultados do Classificador KNN")
        st.text(classification_report(y_test, y_pred_knn))
        st.write(f"Acurácia: {accuracy_score(y_test, y_pred_knn):.2f}")

        st.subheader("Resultados da Árvore de Decisão")
        st.text(classification_report(y_test, y_pred_tree))
        st.write(f"Acurácia: {accuracy_score(y_test, y_pred_tree):.2f}")

        st.subheader("Resultados do Naive Bayes")
        st.text(classification_report(y_test, y_pred_nb))
        st.write(f"Acurácia: {accuracy_score(y_test, y_pred_nb):.2f}")

        st.subheader("Resultados do SVM")
        st.text(classification_report(y_test, y_pred_svm))
        st.write(f"Acurácia: {accuracy_score(y_test, y_pred_svm):.2f}")

        # Visualizando os resultados
        st.subheader("Distribuição do Humor das Músicas")
        fig, ax = plt.subplots()
        mood_counts = y.value_counts()
        ax.bar(mood_counts.index, mood_counts.values)
        ax.set_xlabel('Mood')
        ax.set_ylabel('Number of Songs')
        ax.set_title('Mood Classification of Songs')
        st.pyplot(fig)

if __name__ == "__main__":
    main()