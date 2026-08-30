import os
import streamlit as st

# --- CONFIGURATION PAGE (MODE LARGE) ---
st.set_page_config(
    page_title="CarCheck - Expertise Auto", page_icon="🟣", layout="wide"
)

# --- CSS PERSONNALISÉ (DESIGN EXACT DE LA MAQUETTE & PALETTE AUBERGINE) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    /* Suppression de la barre blanche supérieure et masquage des éléments natifs */
    header.stAppHeader {
        background-color: transparent !important;
        display: none !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp { background-color: #F8F9FC !important; font-family: 'Plus Jakarta Sans', sans-serif; color: #1E2229 !important; }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
        max-width: 100% !important;
    }

    /* Style du Header de la Navbar (Reprenant la disposition de la capture) */
    .top-nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #FFFFFF;
        padding: 10px 20px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        margin-bottom: 25px;
    }

    /* Hero Banner aux couleurs de la maquette (Dégradé aubergine/violet profond) */
    .hero-container {
        background: linear-gradient(135deg, #1F1421 0%, #3F2941 50%, #532C53 100%) !important;
        padding: 55px 40px !important;
        border-radius: 16px !important;
        margin-bottom: 25px !important;
        box-shadow: 0 15px 35px -10px rgba(31, 20, 33, 0.4);
        border: 1px solid #6B3E6B;
        text-align: center;
    }
    .hero-title {
        color: #FFFCFF !important;
        font-size: 38px !important;
        font-weight: 800 !important;
        text-align: center !important;
        margin-bottom: 15px !important;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        color: #C6B9CC !important;
        font-size: 16px !important;
        text-align: center !important;
        margin-bottom: 30px !important;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.5;
    }

    /* Barre de recherche personnalisée identique à la maquette */
    .custom-search-box {
        display: flex;
        align-items: center;
        background-color: #FFFFFF;
        border: 1px solid #C6B9CC;
        border-radius: 40px;
        padding: 6px 6px 6px 20px;
        max-width: 700px;
        margin: 0 auto;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    .custom-search-input {
        flex: 1;
        border: none !important;
        outline: none !important;
        font-size: 15px;
        color: #1D1420;
        background: transparent !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .custom-search-input::placeholder {
        color: #A999B0;
    }
    .custom-search-btn {
        background: linear-gradient(135deg, #532C53 0%, #7D4F7D 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 10px 28px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(83, 44, 83, 0.3);
    }
    .custom-search-btn:hover {
        background: linear-gradient(135deg, #3F2941 0%, #532C53 100%) !important;
    }

    /* Boutons de navigation du haut */
    div[data-testid="column"] button {
        background-color: transparent !important;
        color: #532C53 !important;
        border: none !important;
        box-shadow: none !important;
        font-weight: 600 !important;
        height: 40px !important;
        font-size: 14px !important;
        border-radius: 8px !important;
    }
    div[data-testid="column"] button:hover {
        background-color: #EFE8F0 !important;
        color: #1F1421 !important;
    }

    /* Cartes & Encadrés techniques (Intensité conservée) */
    .data-box {
        background-color: #FFFFFF;
        border: 1px solid #E9DCE8;
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 18px;
        box-shadow: 0 2px 8px rgba(31, 20, 33, 0.03);
    }
    .data-box-highlight {
        background: linear-gradient(135deg, #EFE8F0 0%, #FFFFFF 100%);
        border: 1px solid #C6B9CC;
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 18px;
    }
    .data-box-price {
        background: linear-gradient(135deg, #E4F0E7 0%, #FFFFFF 100%);
        border: 1px solid #3F8F5F;
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 18px;
    }
    .data-box-argus {
        background: linear-gradient(135deg, #EFE8F0 0%, #FFFFFF 100%);
        border: 1px solid #C6B9CC;
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 18px;
    }
    .data-label {
        color: #71607A;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }
    .data-value {
        color: #1D1420;
        font-size: 18px;
        font-weight: 700;
    }
    .data-value-big {
        color: #3F8F5F;
        font-size: 26px;
        font-weight: 800;
    }
    .data-value-argus {
        color: #532C53;
        font-size: 26px;
        font-weight: 800;
    }
    .data-value-model {
        color: #1D1420;
        font-size: 22px;
        font-weight: 800;
    }

    .photo-box-empty {
        background-color: #FFFFFF;
        border: 2px dashed #C6B9CC;
        border-radius: 14px;
        height: 270px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #71607A;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        padding: 15px;
    }
    
    .expert-card {
        background-color: #FFFFFF;
        border: 1px solid #E9DCE8;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 22px;
        color: #1D1420;
        box-shadow: 0 4px 12px rgba(31, 20, 33, 0.04);
        line-height: 1.6;
    }

    .mot-cle-important {
        font-weight: 700 !important;
        font-size: 13px !important;
        color: #1F1421 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)


def trouver_chemin_image(nom_base):
  extensions = ["", ".jpg", ".jpeg", ".png", ".JPG", ".PNG"]
  for ext in extensions:
    chemin_test = nom_base + ext
    if os.path.exists(chemin_test):
      return chemin_test
  return nom_base + ".jpg"

DONNEES_ANNONCES = {
    "polo": {
        "id_unique": "polo_2018",
        "modele": "Volkswagen Polo VI",
        "prix": "12 000 €",
        "cote_argus": "13 400 €",
        "annee": "2018",
        "km": "80 000 km",
        "carburant": "Essence",
        "puissance": "65 Ch",
        "critair": "2",
        "image_url": trouver_chemin_image("photo1"),
        "points_cles": [
            "Modèle 2018 affichant 80 000 km au compteur",
            "Véhicule propre présenté par le vendeur",
            "Entretien déclaré comme suivi",
            "Idéal pour un usage citadin"
        ],
        "blocants": [
            "Aucun blocage apparent d'après l'annonce du vendeur."
        ],
        "frais_majeurs": [
            "Aucun frais particulier mentionné par le vendeur."
        ],
        "avantages": [
            "Kilométrage modéré pour l'année",
            "Prix affiché attractif face à la cote Argus"
        ],
        "inconvenients": [
            "Motorisation de 65 ch limitée pour les longs trajets"
        ],
        "rapport_cache": {
            "plaque": "ET456ZX",
            "vin": "WVWZZZAWZJY123456",
            "origine": "France (Première immatriculation nationale)",
            "situation": "Non gagé (Certificat régulier)",
            "fvv": "Non signalé volé",
            "proprios": "1 seul propriétaire",
            "rappels": "Aucun rappel constructeur en cours pour ce numéro VIN.",
            "frise": [
                "04/2018 : Sortie d'usine et première immatriculation (Particulier - 0 km).",
                "01/2022 : Changement de titulaire (Même département).",
                "01/2026 : Dernier contrôle technique favorable enregistré."
            ],
            "ct": [
                "14/01/2026 : 79 500 km (OK)",
                "10/01/2024 : 61 000 km (OK)"
            ],
            "sinistres": "Aucun accident répertorié.",
            "options": "Finition Confortline - Climatisation automatique - Régulateur de vitesse - Radars de stationnement arrière.",
            "frais_estimes": "Prévoir une révision standard annuelle et purge des liquides (env. 250 €).",
            "nego": "Offre déjà positionnée sous la cote, marge de négociation limitée (potentiellement 300 à 500 € pour frais de carte grise)."
        }
    },
    "audi": {
        "id_unique": "audi_2004",
        "modele": "Audi A3",
        "prix": "1 000 €",
        "cote_argus": "1 500 €",
        "annee": "2004",
        "km": "320 000 km",
        "carburant": "Diesel",
        "puissance": "105 Ch",
        "critair": "3",
        "image_url": trouver_chemin_image("photo4"),
        "points_cles": [
            "Modèle 2004 avec kilométrage élevé (320 000 km)",
            "Prix de vente très bas",
            "Présentation basique d'occasion",
            "Idéal pour bricoleur ou pièces"
        ],
        "blocants": [
            "Contrôle technique à vérifier en détail (mentionné dans le rapport complet)."
        ],
        "frais_majeurs": [
            "Prévoir une révision mécanique globale au vu du kilométrage."
        ],
        "avantages": [
            "Prix d'acquisition très accessible"
        ],
        "inconvenients": [
            "Usure globale très prononcée due au kilométrage",
            "Incertitude sur la longévité mécanique à court terme"
        ],
        "rapport_cache": {
            "plaque": "AA-123-BB",
            "vin": "WAUZZZ8P44A123456",
            "origine": "France",
            "situation": "Non gagé",
            "fvv": "Non signalé volé",
            "proprios": "4 propriétaires successifs",
            "rappels": "Campagne airbag passager réalisée en 2018.",
            "frise": [
                "06/2004 : Sortie d'usine",
                "11/2012 : Changement de propriétaire (Choc arrière réparé)"
            ],
            "ct": [
                "12/05/2025 : 315 000 km (Défavorable)"
            ],
            "sinistres": "Choc arrière enregistré en 2012 avec réparation de longeron.",
            "options": "Finition Ambiente - Sellerie tissu - Jantes alliage - Climatisation manuelle.",
            "frais_estimes": "Embrayage et volant moteur à prévoir rapidement (estimé à 1 200 €).",
            "nego": "Négociation possible de 30 % vu l'état général et le contrôle technique défavorable."
        }
    },
    "clio": {
        "id_unique": "clio_2010",
        "modele": "Renault Clio 3 GPL",
        "prix": "3 990 €",
        "cote_argus": "8 980 €",
        "annee": "2010",
        "km": "105 000 km",
        "carburant": "Essence / GPL",
        "puissance": "75 Ch",
        "critair": "1",
        "image_url": trouver_chemin_image("photo7"),
        "points_cles": [
            "Modèle 2010 avec seulement 105 000 km au compteur",
            "Motorisation bicarburation Essence / GPL d'origine",
            "Vignette Crit'Air 1 avantageuse",
            "Mention dans l'annonce : Carte grise en retard"
        ],
        "blocants": [
            "Attention à la régularisation de la carte grise signalée par le vendeur."
        ],
        "frais_majeurs": [
            "Prévoir les démarches de mise à jour administrative de la carte grise et vérifier la validité du réservoir GPL."
        ],
        "avantages": [
            "Faible kilométrage pour une voiture de 2010",
            "Économies substantielles à l'usage grâce au GPL et vignette Crit'Air 1"
        ],
        "inconvenients": [
            "Démarches administratives supplémentaires à prévoir suite au retard de carte grise"
        ],
        "rapport_cache": {
            "plaque": "CL-987-IO",
            "vin": "VF1BR1H0541234567",
            "origine": "France",
            "situation": "🚨 Opposition administrative en cours",
            "fvv": "🚨 Véhicule signalé volé (Déclaration récente)",
            "proprios": "2 propriétaires",
            "rappels": "Vérification du détendeur GPL conseillée (rappel constructeur d'époque).",
            "frise": [
                "03/2010 : Première immatriculation",
                "12/2025 : Déclaration de vol enregistrée"
            ],
            "ct": [
                "10/01/2026 : 104 000 km (OK)"
            ],
            "sinistres": "Aucun accident majeur déclaré, mais véhicule signalé volé.",
            "options": "Finition Dynamique - Climatisation - Radio CD - Vitres électriques.",
            "frais_estimes": "Épreuve du réservoir GPL obligatoire tous les 10 ans (env. 600 € si non fait).",
            "nego": "Achat fortement déconseillé en l'état (situation administrative bloquante)."
        }
    },
    "bmw": {
        "id_unique": "bmw_2007",
        "modele": "BMW 320i coupé Msport",
        "prix": "11 500 €",
        "cote_argus": "13 874 €",
        "annee": "2007",
        "km": "197 500 km",
        "carburant": "Essence",
        "puissance": "170 Ch",
        "critair": "2",
        "image_url": trouver_chemin_image("photo10"),
        "points_cles": [
            "Modèle coupé 2007 avec 197 500 km",
            "Finition Pack Sport M esthétique",
            "Ligne sportive recherchée",
            "Prix positionné sous la cote Argus"
        ],
        "blocants": [
            "Aucun défaut structurel mentionné directement par le vendeur dans l'annonce."
        ],
        "frais_majeurs": [
            "Contrôle d'usure des trains roulants et des suspensions sport."
        ],
        "avantages": [
            "Style et prestance de la finition Pack M",
            "Tarif affiché inférieur à l'estimation Argus de référence"
        ],
        "inconvenients": [
            "Kilométrage avoisinant les 200 000 km nécessitant un suivi rigoureux"
        ],
        "rapport_cache": {
            "plaque": "BM-320-MS",
            "vin": "WBAWA71040A123456",
            "origine": "Allemagne (Importé en 2011)",
            "situation": "Non gagé (Véhicule VEI régularisé)",
            "fvv": "Non signalé volé",
            "proprios": "3 propriétaires",
            "rappels": "Rappel sur câblage ventilateur habitacle réalisé en concession.",
            "frise": [
                "05/2007 : Mise en circulation",
                "14/09/2015 : Sortie de route - Classé VEI (Véhicule Économiquement Irréparable)",
                "20/12/2015 : Réparations contrôlées par expert et levée de procédure"
            ],
            "ct": [
                "15/02/2026 : 196 000 km (OK)"
            ],
            "sinistres": "Sortie de route enregistrée en 2015 avec passage sur marbre et remplacement de longeron.",
            "options": "Pack M Sport - Jantes 18 pouces - Sièges sport cuir - Toit ouvrant - Châssis M.",
            "frais_estimes": "Suspensions et silentblocs fatigués (prévoir 800 € à moyen terme).",
            "nego": "Négocier de 1 000 € minimum en raison du passé VEI (accident de 2015) et de l'historique d'importation."
        }
    }
}

# --- SESSION STATE ---
if 'donnees_annonce' not in st.session_state:
    st.session_state.donnees_annonce = None
if 'vue_rapport' not in st.session_state:
    st.session_state.vue_rapport = False
if 'vue_guide' not in st.session_state:
    st.session_state.vue_guide = False
if 'vue_contact' not in st.session_state:
    st.session_state.vue_contact = False
if 'rapports_debloques' not in st.session_state:
    st.session_state.rapports_debloques = {}
if 'plaques_saisies' not in st.session_state:
    st.session_state.plaques_saisies = {}
if 'vins_saisies' not in st.session_state:
    st.session_state.vins_saisies = {}
if 'url_saisie' not in st.session_state:
    st.session_state.url_saisie = ""

def lancer_analyse_url(url_input):
    url_lower = url_input.lower() if url_input else ""
    if "clio" in url_lower or "renault" in url_lower or "gpl" in url_lower:
        st.session_state.donnees_annonce = DONNEES_ANNONCES["clio"]
    elif "bmw" in url_lower or "serie" in url_lower or "320i" in url_lower:
        st.session_state.donnees_annonce = DONNEES_ANNONCES["bmw"]
    elif "audi" in url_lower or "a3" in url_lower:
        st.session_state.donnees_annonce = DONNEES_ANNONCES["audi"]
    else:
        st.session_state.donnees_annonce = DONNEES_ANNONCES["polo"]
    st.session_state.vue_rapport = False
    st.session_state.vue_guide = False
    st.session_state.vue_contact = False

# Gestion des actions de soumission via paramètres URL (pour la barre de recherche intégrée)
query_params = st.query_params
if "action" in query_params and query_params["action"] == "analyser":
    url_recup = query_params.get("url", "")
    st.session_state.url_saisie = url_recup
    lancer_analyse_url(url_recup)
    st.query_params.clear()
    st.rerun()

# --- NAVBAR EXACTEMENT COMME SUR LA CAPTURE ---
col_logo, col_n1, col_n2, col_n3, col_n4, col_profile = st.columns([1.5, 0.9, 0.9, 0.9, 0.9, 1.3])

with col_logo:
    # CSS pour grossir le logo et masquer son fond blanc
    st.markdown("""
        <style>
        [data-testid="stImage"] img {
            width: 420px !important;
            mix-blend-mode: multiply;
        }
        </style>
    """, unsafe_allow_html=True)
    
    chemin_logo = trouver_chemin_image("logo")
    if os.path.exists(chemin_logo):
        st.image(chemin_logo)
    else:
        st.markdown("<h3 style='color: #532C53; margin: 0; padding-top: 5px;'>CarCheck</h3>", unsafe_allow_html=True)
with col_n1:
    if st.button("Accueil", use_container_width=True):
        st.session_state.vue_rapport = False
        st.session_state.vue_guide = False
        st.session_state.vue_contact = False
        st.rerun()
with col_n2:
    if st.button("Rapport", use_container_width=True):
        st.session_state.vue_rapport = True
        st.session_state.vue_guide = False
        st.session_state.vue_contact = False
        st.rerun()
with col_n3:
    if st.button("Guide", use_container_width=True):
        st.session_state.vue_guide = True
        st.session_state.vue_rapport = False
        st.session_state.vue_contact = False
        st.rerun()
with col_n4:
    if st.button("Contact", use_container_width=True):
        st.session_state.vue_contact = True
        st.session_state.vue_rapport = False
        st.session_state.vue_guide = False
        st.rerun()

# --- GESTION DES VUES ---
if st.session_state.vue_contact:
    st.markdown("##  Besoin d'un avis sur un véhicule ou d'aide ?")
    st.markdown("<div style='color: #71607A; font-size: 15px; margin-bottom: 30px;'>Une question sur un rapport d'historique, un doute sur une annonce ou un souci avec votre analyse ? Écrivez-nous directement, on vous répond rapidement sans jargon.</div>", unsafe_allow_html=True)

    if st.button("← Retour à l'accueil"):
        st.session_state.vue_contact = False
        st.rerun()

    col_form, col_info = st.columns([1.6, 1])

    with col_form:
        st.subheader("Envoyez-nous un message")
        with st.form("form_contact"):
            nom = st.text_input("Votre prénom / nom", placeholder="Ex : Thomas Martin")
            email = st.text_input("Votre e-mail pour qu'on puisse vous répondre", placeholder="Ex : thomas.martin@gmail.com")
            sujet = st.text_input("Sujet", placeholder="Ex : Question sur l'historique d'une Audi A3")
            message = st.text_area("Votre message", placeholder="Détaillez votre situation ou collez le lien de l'annonce si besoin...", height=150)
            
            submit_contact = st.form_submit_button("Envoyer ma demande", use_container_width=True)
            if submit_contact:
                if nom and email and message:
                    st.success(" C'est bien reçu ! On examine votre message et on revient vers vous par e-mail dans la journée.")
                else:
                    st.error(" Oups, il manque quelques infos : pensez à remplir votre nom, votre e-mail et votre message.")

    with col_info:
        st.subheader("En direct")
        st.markdown("** Par e-mail**\nsupport@carcheck.fr")
        st.markdown("**⏱ Temps de réponse moyen**\nMoins de 4 heures en journée")
        st.markdown("** Support technique**\nDisponible 7j/7 pour les soucis de déblocage de rapports")
        
        st.info(" **Un conseil avant d'acheter ?**\n\nPensez à jeter un œil à notre **Guide de l'acheteur**, il liste toutes les erreurs à éviter lors de l'achat d'une occasion entre particuliers.")

elif st.session_state.vue_guide:
    st.markdown("##  Le Guide de l'Acheteur d'Occasion")
    st.markdown("<div style='color: #71607A; font-size: 15px; margin-bottom: 35px;'>Maîtrisez toutes les étapes clés pour acheter en toute sécurité, éviter les arnaques et négocier comme un professionnel.</div>", unsafe_allow_html=True)

    if st.button("← Retour à l'accueil"):
        st.session_state.vue_guide = False
        st.rerun()

    st.markdown("### 1. Avant d'acheter : Décrypter l'annonce")
    st.markdown("""
        <div class="expert-card" style="padding: 28px; margin-bottom: 25px;">
            <div style="font-size: 15px; font-weight: bold; color: #532C53; margin-bottom: 12px;"> Les pièges majeurs à repérer dans le texte :</div>
            <ul style="margin: 0; padding-left: 20px; color: #71607A; font-size: 13px; line-height: 1.8;">
                <li>Mentions <span class="mot-cle-important">"Vendu dans l'état"</span> ou <span class="mot-cle-important">"Idéal export"</span> : Fuyez s'il s'agit d'un achat pour rouler tous les jours. Cela cache souvent des <span class="mot-cle-important">dysfonctionnements majeurs</span> ou un contrôle technique refusé.</li>
                <li><span class="mot-cle-important">Le prix anormalement bas</span> : Si une voiture coûte 10 000 € et est affichée à 6 000 €, posez-vous immédiatement des questions sur une éventuelle <span class="mot-cle-important">arnaque ou un passé lourd</span>.</li>
                <li><span class="mot-cle-important">Les photos floues ou sombres</span> : Elles masquent volontairement des défauts de carrosserie. Demandez toujours des <span class="mot-cle-important">photos nettes sous la lumière du jour</span>.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 2. Le rendez-vous et l'inspection visuelle")
    st.markdown("""
        <div class="expert-card" style="padding: 28px; margin-bottom: 25px;">
            <div style="font-size: 15px; font-weight: bold; color: #532C53; margin-bottom: 12px;"> La check-list impérative du parfait inspecteur :</div>
            <ul style="margin: 0; padding-left: 20px; color: #71607A; font-size: 13px; line-height: 1.8;">
                <li><span class="mot-cle-important">Privilégiez les moteurs froids</span> : Touchez le capot avant que le vendeur ne démarre. Un moteur chaud peut masquer des <span class="mot-cle-important">difficultés de démarrage</span>.</li>
                <li><span class="mot-cle-important">L'alignement de la carrosserie</span> : Inspectez les écarts entre les ailes et les portières. Des jours irréguliers trahissent un <span class="mot-cle-important">choc passé</span>.</li>
                <li><span class="mot-cle-important">L'usure de l'habitacle</span> : Si le vendeur annonce 80 000 km mais que le volant est complètement usé, méfiez-vous d'un <span class="mot-cle-important">recul de compteur</span>.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 3. Les documents administratifs indispensables")
    st.markdown("""
        <div class="expert-card" style="padding: 28px; margin-bottom: 25px;">
            <div style="font-size: 15px; font-weight: bold; color: #532C53; margin-bottom: 12px;"> Ne signez rien sans avoir vérifié ces pièces :</div>
            <ul style="margin: 0; padding-left: 20px; color: #71607A; font-size: 13px; line-height: 1.8;">
                <li><span class="mot-cle-important">La carte grise</span> : Le nom du propriétaire inscrit doit obligatoirement correspondre à la <span class="mot-cle-important">pièce d'identité</span> de la personne présente.</li>
                <li><span class="mot-cle-important">Le certificat de non-gage</span> : Il doit dater de <span class="mot-cle-important">moins de 15 jours</span> pour attester qu'aucune opposition ne bloque la vente.</li>
                <li><span class="mot-cle-important">Le contrôle technique</span> : Obligatoire de <span class="mot-cle-important">moins de 6 mois</span> pour les véhicules de plus de 4 ans. Lisez attentivement chaque ligne de défaut.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 4. Comment négocier efficacement le prix ?")
    st.markdown("""
        <div class="expert-card" style="padding: 28px; margin-bottom: 35px; border-left: 4px solid #3F8F5F;">
            <div style="font-size: 15px; font-weight: bold; color: #3F8F5F; margin-bottom: 12px;"> Les techniques de pro pour faire baisser l'addition :</div>
            <ul style="margin: 0; padding-left: 20px; color: #71607A; font-size: 13px; line-height: 1.8;">
                <li><span class="mot-cle-important">Appuyez-vous sur les faits</span> : Ne dites pas "c'est trop cher", chiffrez les défauts constatés (ex: "pneus usés à 70% = 300 € de frais immédiats").</li>
                <li><span class="mot-cle-important">Utilisez la cote Argus® officielle</span> : Montrez l'écart entre le prix demandé et la <span class="mot-cle-important">réalité du marché</span> pour justifier votre offre.</li>
                <li><span class="mot-cle-important">Restez ferme</span> : Ayez un paiement prêt (chèque de banque ou virement instantané) pour rassurer un vendeur sérieux et conclure rapidement.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.vue_rapport:
    st.markdown("## Rapport Historique & Administratif Officiel")
    
    d = st.session_state.donnees_annonce
    if d is not None:
        if st.button("← Retour à l'annonce"):
            st.session_state.vue_rapport = False
            st.rerun()
        modele_titre = d["modele"]
        annee_titre = d["annee"]
        id_vehicule = d["id_unique"]
    else:
        if st.button("← Retour à l'accueil"):
            st.session_state.vue_rapport = False
            st.rerun()
        modele_titre = "Véhicule Personnalisé"
        annee_titre = ""
        id_vehicule = "libre_utilisateur"

    est_debloque = st.session_state.rapports_debloques.get(id_vehicule, False)

    if not est_debloque:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #1F1421 0%, #3F2941 100%); border-radius: 16px; padding: 45px; color: #FFFFFF; text-align: center; box-shadow: 0 20px 40px rgba(31,20,33,0.25); width: 100%; margin: 40px auto; border: 1px solid #532C53;">
                <div style="font-size: 26px; font-weight: bold; margin-bottom: 12px; color: #FFFFFF;">🔒 Débloquer le Rapport Complet (4,99 €)</div>
                <div style="color: #C6B9CC; font-size: 15px; margin-bottom: 30px; line-height: 1.6;">Accédez instantanément à l'historique officiel, aux vices cachés, au passé accidenté et à la situation administrative de cette <b>{modele_titre}</b>.</div>
            </div>
        """, unsafe_allow_html=True)
        col_b1, col_b2, col_b3 = st.columns([1, 1.5, 1])
        with col_b2:
            if st.button("Payer 4,99 €", use_container_width=True):
                st.session_state.rapports_debloques[id_vehicule] = True
                st.rerun()
    else:
        rc = d["rapport_cache"] if d else {
            "plaque": "",
            "vin": "",
            "origine": "En attente de saisie...",
            "situation": "En attente de saisie de la plaque / VIN",
            "fvv": "En attente de vérification",
            "proprios": "En attente de saisie...",
            "rappels": "En attente de saisie du numéro VIN.",
            "frise": [
                "En attente de saisie de l'immatriculation ou du VIN pour charger l'historique."
            ],
            "ct": [
                "En attente de saisie pour afficher les rapports officiels."
            ],
            "sinistres": "En attente de saisie...",
            "options": "En attente de décodage VIN.",
            "frais_estimes": "En attente de l'analyse technique.",
            "nego": "En attente de l'analyse du dossier."
        }
        
        if id_vehicule not in st.session_state.plaques_saisies:
            st.session_state.plaques_saisies[id_vehicule] = rc.get("plaque", "")
        if id_vehicule not in st.session_state.vins_saisies:
            st.session_state.vins_saisies[id_vehicule] = rc.get("vin", "")

        st.markdown(f"### Fiche d'identification & Origine — {modele_titre} {annee_titre}")
        
        col_id1, col_id2, col_id3 = st.columns(3)
        with col_id1:
            st.markdown('<div class="data-label" style="margin-bottom: 6px;">Plaque d\'immatriculation <span style="color: #D89B3C; font-weight: normal;">(Obligatoire)</span></div>', unsafe_allow_html=True)
            st.session_state.plaques_saisies[id_vehicule] = st.text_input(
                "Plaque", 
                value=st.session_state.plaques_saisies[id_vehicule], 
                placeholder="Ex: AB-123-CD",
                label_visibility="collapsed",
                key=f"input_plaque_{id_vehicule}"
            )
        with col_id2:
            st.markdown('<div class="data-label" style="margin-bottom: 6px;">Numéro VIN <span style="color: #D89B3C; font-weight: normal;">(Obligatoire)</span></div>', unsafe_allow_html=True)
            st.session_state.vins_saisies[id_vehicule] = st.text_input(
                "VIN", 
                value=st.session_state.vins_saisies[id_vehicule], 
                placeholder="Ex: VF1XXXXXXXXXXXXXXXX",
                label_visibility="collapsed",
                key=f"input_vin_{id_vehicule}"
            )
        with col_id3:
            st.markdown(f'''
                <div class="data-box" style="margin-bottom: 0; height: 50px; display: flex; flex-direction: column; justify-content: center;">
                    <div class="data-label" style="margin-bottom: 2px;">Pays d'origine</div>
                    <div class="data-value" style="font-size: 14px;">{rc.get("origine", "En attente...")}</div>
                </div>
            ''', unsafe_allow_html=True)

        st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
        st.markdown("### 1. Situation Administrative & Juridique")
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            st.markdown(f'''
                <div class="data-box">
                    <div class="data-label">Situation administrative</div>
                    <div class="data-value" style="font-size: 15px;">{rc.get("situation", "En attente...")}</div>
                </div>
            ''', unsafe_allow_html=True)
        with col_s2:
            st.markdown(f'''
                <div class="data-box">
                    <div class="data-label">Fichier des véhicules volés (FVV)</div>
                    <div class="data-value" style="font-size: 15px;">{rc.get("fvv", "En attente...")}</div>
                </div>
            ''', unsafe_allow_html=True)
        with col_s3:
            st.markdown(f'''
                <div class="data-box">
                    <div class="data-label">Propriétaires précédents</div>
                    <div class="data-value" style="font-size: 15px;">{rc.get("proprios", "En attente...")}</div>
                </div>
            ''', unsafe_allow_html=True)

        st.markdown("### 2. Frise Chronologique & Historique")
        frise_items = "".join([f"<li style='margin-bottom: 8px;'>{item}</li>" for item in rc.get("frise", [])])
        st.markdown(f'''
            <div class="expert-card">
                <div style="font-size: 15px; font-weight: bold; color: #532C53; margin-bottom: 10px;">Évolution administrative :</div>
                <ul style="margin: 0; padding-left: 20px; color: #71607A; font-size: 14px;">{frise_items}</ul>
            </div>
        ''', unsafe_allow_html=True)

        st.markdown("### 3. Contrôles Techniques (UTAC-OTC)")
        ct_items = "".join([f"<div style='padding: 6px 0; font-size: 14px; color: #71607A; border-bottom: 1px solid #EFE8F0;'>{ct}</div>" for ct in rc.get("ct", [])])
        st.markdown(f'''
            <div class="expert-card">
                <div style="font-size: 15px; font-weight: bold; color: #532C53; margin-bottom: 10px;">Historique des visites :</div>
                {ct_items}
            </div>
        ''', unsafe_allow_html=True)

        st.markdown("### 4. Sinistres & Rappels Constructeur")
        st.markdown(f'''
            <div class="expert-card" style="border-left: 4px solid #3F8F5F; margin-bottom: 15px;">
                <div style="font-size: 15px; font-weight: bold; color: #3F8F5F; margin-bottom: 6px;">Bilan des dommages déclarés</div>
                <div style="color: #71607A; font-size: 14px;">{rc.get("sinistres", "En attente...")}</div>
            </div>
            <div class="expert-card" style="border-left: 4px solid #532C53;">
                <div style="font-size: 15px; font-weight: bold; color: #532C53; margin-bottom: 6px;">Rappels constructeur (Sécurité)</div>
                <div style="color: #71607A; font-size: 14px;">{rc.get("rappels", "En attente...")}</div>
            </div>
        ''', unsafe_allow_html=True)

        st.markdown("### 5. Équipements & Options d'Origine")
        st.markdown(f'''
            <div class="expert-card">
                <div style="font-size: 15px; font-weight: bold; color: #532C53; margin-bottom: 6px;">Spécifications usine décodées :</div>
                <div style="color: #71607A; font-size: 14px;">{rc.get("options", "En attente...")}</div>
            </div>
        ''', unsafe_allow_html=True)

        st.markdown("### 6. Estimation des Frais & Stratégie de Négociation")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.markdown(f'''
                <div class="expert-card" style="border-left: 4px solid #D89B3C; height: 100%;">
                    <div style="font-size: 15px; font-weight: bold; color: #D89B3C; margin-bottom: 8px;">Coûts de remise en état</div>
                    <div style="color: #71607A; font-size: 14px;">{rc.get("frais_estimes", "En attente...")}</div>
                </div>
            ''', unsafe_allow_html=True)
        with col_f2:
            st.markdown(f'''
                <div class="expert-card" style="border-left: 4px solid #532C53; height: 100%;">
                    <div style="font-size: 15px; font-weight: bold; color: #532C53; margin-bottom: 8px;">Conseil de négociation pro</div>
                    <div style="color: #71607A; font-size: 14px;">{rc.get("nego", "En attente...")}</div>
                </div>
            ''', unsafe_allow_html=True)

else:
    # --- ACCUEIL PRINCIPAL AVEC BANNIÈRE & BARRE DE RECHERCHE EXACTE ---
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">N'achetez plus jamais une mauvaise voiture.</div>
            <div class="hero-subtitle">CarCheck analyse l'historique, détecte les arnaques et compare chaque annonce à vos critères personnels pour vous garantir le meilleur achat.</div>
        </div>
    """, unsafe_allow_html=True)

# CSS pour supprimer le grand encadré et styliser le champ
    st.markdown("""
        <style>
        [data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
        }
        .stTextInput label { display: none !important; }
        
        /* Encadré aubergine uniquement autour de la zone de saisie */
        .stTextInput div[data-baseweb="input"] {
            border: 2px solid #532C53 !important;
            border-radius: 10px !important;
            background: #ffffff !important;
        }
        .stTextInput input {
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
        }
        
        /* Bouton Analyser aligné à l'intérieur à droite */
        [data-testid="stFormSubmitButton"] {
            display: flex;
            justify-content: flex-end;
            margin-top: 2px !important;
        }
        [data-testid="stFormSubmitButton"] button {
            background-color: #532C53 !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 8px 22px !important;
            font-weight: 600 !important;
            width: 100% !important;
        }
        [data-testid="stFormSubmitButton"] button:hover {
            background-color: #71607A !important;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.form(key='formulaire_recherche_design'):
        c_input, c_btn = st.columns([0.80, 0.20], vertical_alignment="center")
            
        with c_input:
            url_input = st.text_input(
                "Recherche",
                value=st.session_state.get('url_saisie', ''),
                placeholder="Plaque d'immatriculation, VIN ou lien d'annonce...",
                key="input_url_design"
            )
            
        with c_btn:
            submit_button = st.form_submit_button(label="Analyser")

    if submit_button:
        if url_input:
            st.session_state.url_saisie = url_input
            if 'lancer_analyse_url' in globals():
                lancer_analyse_url(url_input)
            st.rerun()
        else:
            st.warning("Veuillez saisir une plaque ou un lien.")

    # Badges de réassurance sous la barre (comme sur l'image)
    st.markdown("""
        <div style="display: flex; justify-content: center; gap: 40px; margin: 25px 0 45px 0; font-size: 13px; color: #71607A; font-weight: 600;">
            <div>✓ Historique certifié</div>
            <div>✓ Kilométrage vérifié</div>
            <div>✓ 0 frais cachés</div>
        </div>
    """, unsafe_allow_html=True)

    d = st.session_state.donnees_annonce

    # --- PARTIE 1 : SYNTHÈSE ---
    st.markdown("### 1. Synthèse du véhicule & Cote Argus®")
    col_img, col_main = st.columns([1, 2.5])

    with col_img:
        if d is not None and os.path.exists(d["image_url"]):
            st.image(d["image_url"], use_container_width=True)
        else:
            st.markdown('<div class="photo-box-empty">📸 Photos</div>', unsafe_allow_html=True)

    with col_main:
        modele_text = d["modele"] if d else "Marque & Modèle du véhicule"
        st.markdown(f'<div class="data-box-highlight"><div class="data-label">Modèle détecté</div><div class="data-value-model">{modele_text}</div></div>', unsafe_allow_html=True)

        prix_text = d["prix"] if d else "-- €"
        argus_text = d["cote_argus"] if d else "-- €"
        p_col1, p_col2 = st.columns(2)
        with p_col1:
            st.markdown(f'<div class="data-box-price"><div class="data-label" style="color: #3F8F5F;">Prix de l\'annonce</div><div class="data-value-big">{prix_text}</div></div>', unsafe_allow_html=True)
        with p_col2:
            st.markdown(f'<div class="data-box-argus"><div class="data-label" style="color: #532C53;">Cote Argus® Officielle</div><div class="data-value-argus">{argus_text}</div></div>', unsafe_allow_html=True)

        annee_val = d["annee"] if d else "----"
        km_val = d["km"] if d else "--"
        carb_val = d["carburant"] if d else "--"
        puis_val = d["puissance"] if d else "--"
        crit_val = d["critair"] if d else "--"

        d_col1, d_col2, d_col3, d_col4, d_col5 = st.columns(5)
        with d_col1: st.markdown(f'<div class="data-box"><div class="data-label">Année</div><div class="data-value">{annee_val}</div></div>', unsafe_allow_html=True)
        with d_col2: st.markdown(f'<div class="data-box"><div class="data-label">Kilométrage</div><div class="data-value">{km_val}</div></div>', unsafe_allow_html=True)
        with d_col3: st.markdown(f'<div class="data-box"><div class="data-label">Énergie</div><div class="data-value">{carb_val}</div></div>', unsafe_allow_html=True)
        with d_col4: st.markdown(f'<div class="data-box"><div class="data-label">Puissance</div><div class="data-value">{puis_val}</div></div>', unsafe_allow_html=True)
        with d_col5: st.markdown(f'<div class="data-box"><div class="data-label">Crit\'Air</div><div class="data-value">{crit_val}</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

    # --- PARTIE 2 : ANALYSE TECHNIQUE ---
    st.markdown("### 2. Analyse Technique Experte & Lecture de l'Annonce")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    
    with col_c1:
        points_cles_items = d["points_cles"] if d is not None else ["En attente d'analyse..."]
        html_points = "".join([f"<li style='margin-bottom: 10px; font-size: 13px;'>{p}</li>" for p in points_cles_items])
            
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FFFFFF 0%, #EFE8F0 100%); border: 1px solid #C6B9CC; border-radius: 16px; padding: 26px; color: #1D1420; box-shadow: 0 4px 15px rgba(31,20,33,0.04); height: 100%;">
                <div style="display: flex; align-items: center; margin-bottom: 16px;">
                    <div style="background: #EFE8F0; padding: 10px; border-radius: 10px; margin-right: 12px; color: #532C53; font-size: 18px;">📄</div>
                    <div style="font-size: 16px; font-weight: 700; color: #1F1421;">Résumé brut vendeur</div>
                </div>
                <ul style="margin: 0; padding-left: 18px; color: #71607A; line-height: 1.6;">{html_points}</ul>
            </div>
        """, unsafe_allow_html=True)

    with col_c2:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #FFFFFF 0%, #EFE8F0 100%); border: 1px solid #C6B9CC; border-radius: 16px; padding: 26px; color: #1D1420; box-shadow: 0 4px 15px rgba(31,20,33,0.04); height: 100%;">
                <div style="display: flex; align-items: center; margin-bottom: 16px;">
                    <div style="background: #EFE8F0; padding: 10px; border-radius: 10px; margin-right: 12px; color: #532C53; font-size: 18px;">⚖️</div>
                    <div style="font-size: 16px; font-weight: 700; color: #1F1421;">Méthode d'évaluation</div>
                </div>
                <div style="font-size: 13px; color: #71607A; line-height: 1.6; margin-bottom: 15px;">
                    Analyse croisée de 100+ critères techniques et historiques pour évaluer précisément la fiabilité et la valeur du véhicule sur le marché actuel.
                </div>
                <div style="font-size: 13px; font-weight: 700; color: #1F1421; margin-bottom: 8px;">Sources principales :</div>
                <ul style="margin: 0; padding-left: 18px; color: #71607A; font-size: 13px; line-height: 1.5;">
                    <li>Données constructeur</li>
                    <li>Tendances du marché</li>
                    <li>Base Argus® officielle</li>
                    <li>Retours de fiabilité</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col_c3:
        if d is not None:
            list_avantages = d["avantages"]
            list_vigilances = d["blocants"] + d["frais_majeurs"]
            avis_texte = "Bon rapport qualité/prix si l'entretien est suivi. Prévoir une enveloppe pour les frais d'usure courante."
        else:
            list_avantages = ["En attente..."]
            list_vigilances = ["En attente..."]
            avis_texte = "En attente d'analyse..."

        html_avantages = "".join(["<li style='margin-bottom: 6px; font-size: 13px;'>" + av + "</li>" for av in list_avantages])
        html_vigilances = "".join(["<li style='margin-bottom: 6px; font-size: 13px;'>" + vig + "</li>" for vig in list_vigilances])

        contenu_bilan = (
            '<div style="background: linear-gradient(135deg, #FFFFFF 0%, #EFE8F0 100%); border: 1px solid #C6B9CC; border-radius: 16px; padding: 26px; color: #1D1420; box-shadow: 0 4px 15px rgba(31,20,33,0.04); height: 100%;">'
            '<div style="display: flex; align-items: center; margin-bottom: 16px;">'
            '<div style="background: #EFE8F0; padding: 10px; border-radius: 10px; margin-right: 12px; color: #532C53; font-size: 18px;">🛡️</div>'
            '<div style="font-size: 16px; font-weight: 700; color: #1F1421;">Bilan & Avis du Pro</div>'
            '</div>'
            '<div style="color: #3F8F5F; font-weight: bold; font-size: 13px; margin-bottom: 4px;"> Points forts</div>'
            '<ul style="margin: 0 0 14px 0; padding-left: 18px; color: #71607A;">' + html_avantages + '</ul>'
            '<div style="color: #D89B3C; font-weight: bold; font-size: 13px; margin-bottom: 4px;"> Points de vigilance</div>'
            '<ul style="margin: 0 0 14px 0; padding-left: 18px; color: #71607A;">' + html_vigilances + '</ul>'
            '<div style="color: #1F1421; font-weight: bold; font-size: 13px; margin-bottom: 4px;"> Recommandation</div>'
            '<div style="font-size: 13px; color: #71607A; line-height: 1.5;">' + avis_texte + '</div>'
            '</div>'
        )

        st.markdown(contenu_bilan, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

    # --- PARTIE 3 : RAPPORT D'HISTORIQUE OFFICIEL ---
    st.markdown("### 3. Rapport d’Historique Officiel")
    st.markdown("<div style='color: #71607A; font-size: 14px; margin-bottom: 15px;'>Vérifications approfondies certifiées par nos partenaires officiels.</div>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background: linear-gradient(135deg, #1F1421 0%, #3F2941 100%); border: 1px solid #532C53; padding: 35px; border-radius: 16px; margin-top: 10px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 10px 25px rgba(31,20,33,0.25);">
            <div style="display: flex; align-items: center;">
                <div style="background: rgba(255, 255, 255, 0.15); padding: 14px; border-radius: 12px; margin-right: 20px; color: #FFFFFF; font-size: 24px; border: 1px solid rgba(255,255,255,0.3);">📄</div>
                <div>
                    <div style="color: #FFFFFF; font-size: 18px; font-weight: 700; margin-bottom: 6px;">Débloquer le Rapport Historique & Administratif Complet</div>
                    <div style="color: #C6B9CC; font-size: 13px; line-height: 1.5;">Accédez aux anciens contrôles techniques, aux sinistres, aux rappels constructeurs et à l'origine exacte.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_bspac, col_baction = st.columns([2, 1])
    with col_baction:
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        if st.button("Voir le rapport détaillé →", use_container_width=True):
            st.session_state.vue_rapport = True
            st.rerun()

    st.markdown("<hr style='margin-top: 45px; margin-bottom: 20px; border-color: #E9DCE8;'>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: #71607A; font-size: 12px;'>© 2026 CarCheck. Tous droits réservés. &nbsp;&nbsp;&nbsp;&nbsp; Mentions légales &nbsp;&nbsp;|&nbsp;&nbsp; CGU &nbsp;&nbsp;|&nbsp;&nbsp; Politique de confidentialité</div>", unsafe_allow_html=True)