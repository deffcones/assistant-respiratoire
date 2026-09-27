import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Assistant Technicien Respiratoire",
    page_icon="🫁",
    layout="wide"
)

# Style et en-tête
st.title("🫁 Assistant d'Analyse des Rapports Respiratoires")
st.markdown("""
Cette application vous permet d'importer vos rapports patients, d'obtenir une analyse structurée, 
d'identifier les problématiques clés et d'obtenir des recommandations d'amélioration.
""")

# Sidebar pour la configuration
st.sidebar.header("Paramètres du patient")
patient_id = st.sidebar.text_input("Identifiant / Nom du patient", "Patient #1042")
type_appareil = st.sidebar.selectbox(
    "Type de matériel / Examen",
    ["PPC (CPAP)", "VNI (Ventilation Non Invasive)", "Oxygénothérapie", "EFR / Spirométrie", "Polysomnographie / Oxymétrie"]
)

# 1. Intégrer des rapports
st.header("1. Intégration du rapport")
uploaded_file = st.file_uploader("Téléchargez le rapport (PDF, Texte ou Image)", type=["pdf", "txt", "png", "jpg"])
rapport_texte = st.text_area("Ou colciez/saisissez les données textuelles du rapport ici :", height=150)

if uploaded_file is not None:
    st.success("Rapport importé avec succès !")
    # Simulation de lecture du fichier
    if uploaded_file.type == "application/pdf":
        st.info("Fichier PDF détecté. Extraction des données en cours...")
    else:
        st.info("Fichier image/texte pris en compte.")

# Bouton d'analyse
if st.button("Lancer l'analyse complète", type="primary"):
    if uploaded_file is not None or rapport_texte.strip() != "":
        st.divider()
        
        # 2. Analyse des données
        st.header("2. Analyse des Données")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Observance estimée", value="85%", delta="+5% vs sem. dernière")
        with col2:
            st.metric(label="Fuites (P95)", value="28 L/min", delta="Élevé", delta_color="inverse")
        with col3:
            st.metric(label="IAH résiduel", value="4.2 /h", delta="Normal")

        # 3. Principaux problèmes
        st.header("3. Principaux Problèmes Identifiés")
        st.error("""
        * **Fuites excessives récurrentes** : Pic de fuite supérieur à 35 L/min en fin de nuit, risquant de compromettre l'efficacité de la Pression Positive Continue (PPC).
        * **Marque de fuite / Masque** : Instabilité potentielle du masque nasal ou besoin de revoir le dimensionnement/souflage.
        * **Observance limite sur le week-end** : Baisse de l'utilisation constatée les samedi et dimanche.
        """)

        # 4. Ce qu'il faudrait faire pour améliorer le cas
        st.header("4. Plan d'Action Recommandé")
        st.markdown("""
        1. **Vérification du matériel** : Planifier un appel ou une visite de contrôle pour vérifier le positionnement et le serrage du masque.
        2. **Test d'interface** : Envisager un changement de masque (passer d'un masque nasal à un masque narinaire ou facial si fuite buccale suspectée).
        3. **Éducation thérapeutique** : Renforcer l'accompagnement sur l'importance de l'observance quotidienne, y compris les week-ends.
        4. **Suivi distant** : Activer une surveillance rapprochée sur la plateforme de télésuivi pendant les 7 prochains jours.
        """)

    else:
        st.warning("Veuillez d'abord importer un rapport ou saisir du texte.")

# 5. Explications sur demande (Chat / Q&A personnalisé)
st.divider()
st.header("5. Comprendre et Poser vos questions")
user_question = st.text_input("Posez une question spécifique sur ce rapport (ex: 'À quoi correspond un IAH à 15 avec de fortes fuites ?' ou 'Qu'est-ce que le VEMS ?')")

if user_question:
    st.markdown(f"**Réponse à votre question :**")
    st.info(f"Analyse contextuelle liée à votre question ('{user_question}') : Dans le cadre de la prise en charge respiratoire, un IAH (Index d'Apnées-Hypopnées) supérieur à 5 sous ventilation indique un contrôle incomplet des évènements respiratoires, souvent aggravé par des fuites non intentionnelles qui faussent la détection des machines...")