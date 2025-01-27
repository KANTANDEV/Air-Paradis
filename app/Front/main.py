import streamlit as st

# Fonction d'analyse de sentiment simple pour tests
def analyze_sentiment(model, text):
    if model == "Modèle Simple":
        print("Modèle Simple")
        return "Positif"
    elif model == "Modèle Avancé":
        print("Modèle Avancé")
        return "Négatif"
    elif model == "Modèle BERT":
        print("Modèle BERT")
        return "Neutre"

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Air Paradis",
    page_icon="✈️",
    layout="centered"
)

# Titre et description
st.title("Air Paradis")
st.write("Analyse de sentiment")
st.write("Choisissez un modèle, entrez votre texte, et découvrez si le sentiment est positif ou négatif.")

# Sélection du modèle
model = st.selectbox(
    "Sélectionnez un modèle d'analyse de sentiment :",
    ["Modèle Simple", "Modèle Avancé", "Modèle BERT"]
)

# Zone de texte
text = st.text_area(
    "Entrez votre texte ici :",
    placeholder="Exemple : J'adore cette nouvelle fonctionnalité, c'est incroyable !"
)

# Bouton pour envoyer le texte
submitted = st.button("Analyser le sentiment")

# Résultat
if submitted:
    if text.strip():
        sentiment = analyze_sentiment(model, text)
        st.subheader("Résultat :")
        st.success(f"**{sentiment}**")
    else:
        st.warning("Veuillez entrer un texte avant d'analyser.")