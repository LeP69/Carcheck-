import streamlit as st
import base64

st.set_page_config(
    page_title="Renault Clio 3 GPL 2010 - leboncoin",
    page_icon="🧡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fonction pour convertir les photos locales en base64
def get_base64_img(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return f"data:image/jpeg;base64,{base64.b64encode(data).decode()}"
    except Exception:
        return ""

img7_b64 = get_base64_img("photo7.jpg")
img8_b64 = get_base64_img("photo8.jpg")
img9_b64 = get_base64_img("photo9.jpg")

# --- CSS EXACT LEBONCOIN ---
st.markdown("""
<style>
    /* Reset & fond blanc */
    .stApp { background-color: #FFFFFF !important; }
    
    header[data-testid="stHeader"] { display: none; }
    
    .block-container { 
        padding-top: 0rem !important; 
        padding-bottom: 2rem !important;
        max-width: 1150px !important; 
    }

    /* EN-TÊTE LEBONCOIN */
    .lbc-header-container {
        width: 100%;
        border-bottom: 1px solid #E5E7EB;
        padding: 12px 0 8px 0;
        margin-bottom: 16px;
    }
    .lbc-top-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
    }
    .lbc-logo {
        font-size: 28px;
        font-weight: 900;
        color: #EC5A13;
        letter-spacing: -1.5px;
        font-family: sans-serif;
    }
    .btn-deposer {
        background-color: #EC5A13;
        color: white;
        font-weight: 700;
        padding: 8px 16px;
        border-radius: 14px;
        font-size: 14px;
        display: flex;
        align-items: center;
        gap: 6px;
        white-space: nowrap;
    }
    .search-box {
        background: #F3F4F6;
        border-radius: 14px;
        display: flex;
        align-items: center;
        padding: 4px 6px 4px 14px;
        flex: 1;
        max-width: 400px;
    }
    .search-input-fake {
        font-size: 14px;
        color: #6B7280;
        flex: 1;
    }
    .search-btn-icon {
        background-color: #EC5A13;
        color: white;
        width: 32px;
        height: 32px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
    }
    .header-icons {
        display: flex;
        gap: 20px;
        align-items: center;
    }
    .icon-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-size: 11px;
        color: #111827;
        font-weight: 500;
    }
    .icon-item span { font-size: 18px; margin-bottom: 2px; }

    /* Barre de sous-catégories */
    .lbc-subnav {
        display: flex;
        gap: 16px;
        font-size: 13px;
        color: #374151;
        margin-top: 14px;
        font-weight: 500;
    }
    .lbc-subnav span.bold { font-weight: 700; }
    .lbc-subnav span.dot { color: #9CA3AF; }

    /* Fil d'ariane */
    .breadcrumb { font-size: 12px; color: #6B7280; margin-bottom: 16px; }

    /* Galerie compacte */
    .gallery-wrapper {
        display: flex;
        gap: 6px;
        height: 340px;
        width: 100%;
        border-radius: 12px;
        overflow: hidden;
    }
    .main-photo-box { flex: 1.2; height: 100%; }
    .main-photo-box img { width: 100%; height: 100%; object-fit: cover; }
    .side-photos-box { flex: 1; display: flex; flex-direction: column; gap: 6px; height: 100%; }
    .side-photo-item { height: 167px; }
    .side-photo-item img { width: 100%; height: 100%; object-fit: cover; }

    /* Carte de prix sous la photo */
    .price-box {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border: 1px solid #F3F4F6;
        margin-top: -70px;
        margin-left: 15px;
        position: relative;
        z-index: 99;
        width: 82%;
    }
    .ad-title { font-size: 22px; font-weight: 800; color: #111827; }
    .ad-sub { font-size: 13px; color: #6B7280; margin: 4px 0 12px 0; }
    .ad-price { font-size: 24px; font-weight: 900; color: #111827; margin-bottom: 8px; }

    /* Ligne de séparation fine */
    .section-divider {
        border: none;
        border-top: 1px solid #E5E7EB;
        margin: 24px 0;
    }

    /* "Les + de cette annonce" icônes */
    .plus-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
    }
    .plus-icon-box {
        width: 50px;
        height: 50px;
        background-color: #F3F4F6;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }
    .plus-text { font-size: 12px; color: #111827; text-align: center; }

    /* Informations clés */
    .info-label { font-size: 12px; color: #6B7280; margin-bottom: 2px; }
    .info-val { font-size: 14px; font-weight: 800; color: #111827; margin-bottom: 14px; }

    /* Masquer le style du bouton Streamlit pour en faire un lien texte souligné */
    div.stButton > button {
        background: none !important;
        border: none !important;
        padding: 0 !important;
        color: #111827 !important;
        text-decoration: underline !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        box-shadow: none !important;
        cursor: pointer !important;
    }
    div.stButton > button:hover {
        color: #EC5A13 !important;
        background: none !important;
    }

    /* Carte Vendeur Droite */
    .vendeur-card {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    .vendeur-avatar {
        width: 48px; height: 48px; border-radius: 50%;
        background-color: #EAB308; display: inline-block;
    }
    .btn-reserver {
        background-color: #EC5A13; color: white; text-align: center;
        padding: 12px; border-radius: 20px; font-weight: bold; margin: 15px 0 8px 0;
    }
    .btn-msg {
        background-color: #003B63; color: white; text-align: center;
        padding: 12px; border-radius: 20px; font-weight: bold; margin-bottom: 12px;
    }

    /* Style Cetelem & Financement */
    .sponsor-badge {
        border: 1px solid #9CA3AF;
        color: #374151;
        font-size: 11px;
        padding: 1px 6px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .cetelem-legal-notice {
        font-size: 12px;
        color: #6B7280;
        margin-bottom: 12px;
    }
    .cetelem-title {
        font-size: 18px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 20px;
    }
    .cetelem-logo-text {
        color: #00875A;
        font-weight: 900;
    }
    .btn-cetelem {
        border: 1.5px solid #003B63;
        color: #003B63;
        background: white;
        border-radius: 20px;
        padding: 8px 20px;
        font-weight: 700;
        font-size: 14px;
        display: inline-block;
        margin: 15px 0;
        cursor: pointer;
    }
    .cetelem-footnote {
        font-size: 10px;
        color: #9CA3AF;
        line-height: 1.4;
        margin-top: 10px;
    }

    /* Badges Profil Vendeur */
    .vendeur-badges-container {
        display: flex;
        gap: 20px;
        margin: 15px 0;
    }
    .vendeur-badge-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-size: 11px;
        color: #374151;
        text-align: center;
    }
    .vendeur-badge-circle {
        width: 44px;
        height: 44px;
        background-color: #FDE8E8;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        margin-bottom: 6px;
    }
    .btn-suivre {
        border: 1px solid #003B63;
        color: #003B63;
        border-radius: 18px;
        padding: 6px 18px;
        font-weight: 700;
        font-size: 13px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# --- EN-TÊTE EXACT LEBONCOIN ---
st.markdown("""
<div class="lbc-header-container">
    <div class="lbc-top-row">
        <div class="lbc-logo">leboncoin</div>
        <div class="btn-deposer">➕ Déposer une annonce</div>
        <div class="search-box">
            <div class="search-input-fake">Rechercher sur leboncoin</div>
            <div class="search-btn-icon">🔍</div>
        </div>
        <div class="header-icons">
            <div class="icon-item"><span>🔔</span>Mes recherches</div>
            <div class="icon-item"><span>🤍</span>Favoris</div>
            <div class="icon-item"><span>💬</span>Messages</div>
            <div class="icon-item"><span>👤</span>Se connecter</div>
        </div>
    </div>
    <div class="lbc-subnav">
        <span>Immobilier</span> <span class="dot">•</span>
        <span>Véhicules</span> <span class="dot">•</span>
        <span>Matériel pro</span> <span class="dot">•</span>
        <span>Emploi</span> <span class="dot">•</span>
        <span>Mode</span> <span class="dot">•</span>
        <span>Maison & Jardin</span> <span class="dot">•</span>
        <span>Famille</span> <span class="dot">•</span>
        <span>Électronique</span> <span class="dot">•</span>
        <span>Loisirs</span> <span class="dot">•</span>
        <span>Autres</span> <span class="dot">•</span>
        <span class="bold">Bons plans !</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- FIL D'ARIANE ---
st.markdown('<div class="breadcrumb">Accueil > Voitures > Rhône-Alpes > Loire > Saint-Étienne 42000 > Clio 3 GPL</div>', unsafe_allow_html=True)

col_left, col_right = st.columns([2.2, 1])

with col_left:
    # --- GALERIE HTML ---
    st.markdown(f"""
        <div class="gallery-wrapper">
            <div class="main-photo-box">
                <img src="{img7_b64}" alt="Photo 7">
            </div>
            <div class="side-photos-box">
                <div class="side-photo-item"><img src="{img8_b64}" alt="Photo 8"></div>
                <div class="side-photo-item"><img src="{img9_b64}" alt="Photo 9"></div>
            </div>
        </div>
        <div class="price-box">
            <div class="ad-title">Clio 3 GPL</div>
            <div class="ad-sub">Saint-Étienne · 2010 · 105000 km · Essence · Rapport d’historique disponible</div>
            <div class="ad-price">3 990 €</div>
            <div style="font-size: 13px; text-decoration: underline; font-weight: 600; margin-bottom: 6px;">📑 Simuler mon financement</div>
            <div style="font-size: 11px; color: #9CA3AF;">aujourd'hui à 13:11</div>
            <div style="margin-top: 10px; background: #E0F2FE; color: #0369A1; display: inline-block; padding: 4px 8px; border-radius: 6px; font-size: 12px; font-weight: 600;">📍 Pack Sérénité : dès 139 €</div>
        </div>
    """, unsafe_allow_html=True)

    # Liens financement sous la carte
    st.markdown("""
        <div style="display: flex; gap: 30px; margin-top: 20px; font-size: 13px; font-weight: 600; color: #003B63;">
            <div>🪙 Voir le financement</div>
            <div>📄 Voir le PDF (gratuit)</div>
        </div>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

    # --- LES + DE L'ANNONCE ---
    st.markdown("### Les + de cette annonce")
    st.markdown("""
        <div style="display: flex; gap: 30px; margin-top: 15px;">
            <div class="plus-item">
                <div class="plus-icon-box">🚗</div>
                <div class="plus-text">Crit'Air 1</div>
            </div>
        </div>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

    # --- PACK SÉRÉNITÉ ---
    st.markdown("""
        <div class="serenite-title">
            <span style="background: #EC5A13; color: white; border-radius: 4px; padding: 2px 6px; font-size: 16px;">p</span> Pack Sérénité
        </div>
        <div style="font-size: 14px; color: #374151; margin-top: 6px;">Achetez ce véhicule sur leboncoin en toute confiance grâce au Pack Sérénité*</div>
        <div class="serenite-list" style="margin-top: 8px; font-size: 13px; color: #374151; line-height: 1.6;">
            🔒 <b>Réservation du véhicule</b><br>
            💳 <b>Paiement sécurisé</b><br>
            🛠️ <b>Garantie Panne Mécanique** dès 139 €</b>
        </div>
        <div style="font-size: 13px; font-weight: 700; text-decoration: underline; margin-top: 10px; color: #111827;">En savoir plus</div>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

    # --- INFORMATIONS CLÉS ---
    st.markdown("### Les informations clés")

    infos_base = [
        ("📋 Marque", "RENAULT", "📋 Modèle", "Clio"),
        ("📅 Année modèle", "2010", "🏎️ Kilométrage", "105000 km"),
        ("⛽ Énergie", "Essence", "🕹️ Boîte de vitesse", "Manuelle"),
        ("🚗 Nombre de portes", "3", "👥 Nombre de place(s)", "5")
    ]

    infos_extra = [
        ("🗓️ Date de fin de validité du contrôle technique", "2028", "🚦 Date de première mise en circulation", "09/2010"),
        ("✨ État du véhicule", "Excellent état (proche du neuf)", "🚙 Type de véhicule", "Berline"),
        ("🛠️ Historique et entretien", "Carnet d'entretien disponible, Véhicule non fumeur, Factures disponibles, Réparations utiles déjà faites, État du contrôle technique valide", "🎨 Couleur", "Rouge"),
        ("🌱 Crit'Air", "1", "⚡ Puissance fiscale", "4 Cv"),
        ("🐎 Puissance DIN", "75 Ch", "🪪 Permis", "Avec permis")
    ]

    if "show_all_clio" not in st.session_state:
        st.session_state.show_all_clio = False

    display_infos = infos_base + (infos_extra if st.session_state.show_all_clio else [])

    for label1, val1, label2, val2 in display_infos:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="info-label">{label1}</div><div class="info-val">{val1}</div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="info-label">{label2}</div><div class="info-val">{val2}</div>', unsafe_allow_html=True)

    if not st.session_state.show_all_clio:
        if st.button("Voir plus de critères"):
            st.session_state.show_all_clio = True
            st.rerun()
    else:
        if st.button("Voir moins"):
            st.session_state.show_all_clio = False
            st.rerun()

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # --- HISTORIQUE DU VÉHICULE AUTOVIZA ---
    st.markdown("### Historique du véhicule Autoviza ®")
    st.markdown("""
        <div style="font-size: 13px; color: #4B5563; margin-bottom: 15px;">
            Le rapport d'historique vous fournit des données sur l'historique du véhicule, certifiées par un tiers de manière neutre et indépendante.
        </div>
        <div style="font-size: 13px; color: #111827; font-weight: 600; display: flex; flex-direction: column; gap: 8px; margin-bottom: 15px;">
            <div>📋 Contrôle de l'existence du véhicule</div>
            <div>📊 Relevés kilométriques</div>
            <div>👥 Nombre de propriétaires</div>
        </div>
        <div style="font-size: 13px; font-weight: 700; text-decoration: underline; color: #003B63; margin-bottom: 10px;">Voir le rapport d'historique</div>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

    # --- DESCRIPTION ---
    st.markdown("### Description")
    st.write("Je vends ma Renault Clio 3 GPL de 2010, une citadine économique et écologique avec 105 000 km au compteur.")
    st.write("Quatre pneus neuf, ballet d'essuie-glaces changer, il n'y a rien à signaler véhicule en très bon état !")
    st.write("( Pas de climatisation )")
    st.write("")
    st.write("- Marque : Renault")
    st.write("- Modèle : Clio 3")
    st.write("- Année : 2010")
    st.write("- Kilométrage : 105 000 km")
    st.write("- Carburant : GPL et essence")
    st.write("- Motorisation : 75 Ch")
    st.write("- Puissance fiscale : 4 Cv")
    st.write("- Boîte de vitesses : Manuelle")
    st.write("- Type de véhicule : Berline")
    st.write("- Nombre de portes : 3")
    st.write("- Nombre de sièges : 5")
    st.write("- Couleur : Rouge")
    st.write("- Crit'air : 1")
    st.write("N'hésitez pas à me contacter pour plus d'informations ou pour convenir d'un essai !")
    st.write("")
    st.write("mots clefs : 207 peugeot citroen c3 swift 107 c1")
    st.write("")
    st.write("Carte grise de l'ancien propriétaire non faite, non-gage ok mais à faire à votre nom.")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # --- SIMULATION FINANCEMENT CETELEM ---
    st.markdown('<div class="sponsor-badge">Sponsorisé</div>', unsafe_allow_html=True)
    st.markdown('<div class="cetelem-legal-notice">Un crédit vous engage et doit être remboursé. Vérifiez vos capacités de remboursement avant de vous engager.</div>', unsafe_allow_html=True)
    st.markdown('<div class="cetelem-title">Simuler un financement avec <span class="cetelem-logo-text">cetelem</span></div>', unsafe_allow_html=True)

    st.text_input("Montant du financement", value="3 990 €", key="montant_financement_clio")
    
    col_duree1, col_duree2 = st.columns([3, 1])
    with col_duree1:
        st.markdown("<div style='font-size:13px; color:#374151; font-weight:600;'>Durée du financement</div>", unsafe_allow_html=True)
    with col_duree2:
        st.markdown("<div style='text-align:right; font-weight:800; color:#003B63; font-size:15px;'>24 mois</div>", unsafe_allow_html=True)

    duree = st.slider("Durée slider", min_value=6, max_value=84, value=24, label_visibility="collapsed")

    st.markdown('<div class="btn-cetelem">Simuler ma mensualité</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="cetelem-footnote">
            Cetelem est une marque de BNP Paribas Personal Finance, Société Anonyme au capital de : 634 574 115 €. Siège social : 1 Boulevard Haussmann - 75009 Paris France. RCS : Paris n° 542 097 902. N° ORIAS : 07 023 128 (www.orias.fr).
        </div>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

    # --- LOCALISATION CARTE IFRAME DIRECTE ---
    st.markdown("### Localisation")
    st.markdown("<div style='font-size:15px; font-weight:700; color:#111827; margin-bottom:12px;'>Saint-Étienne (42000)</div>", unsafe_allow_html=True)

    st.markdown("""
        <iframe width="100%" height="320" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" 
        src="https://www.openstreetmap.org/export/embed.html?bbox=4.3600%2C45.4150%2C4.4300%2C45.4600&amp;layer=mapnik&amp;marker=45.4397%2C4.3872" 
        style="border-radius:12px; border: 1px solid #E5E7EB;"></iframe>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

    # --- VENDU PAR ---
    st.markdown("### Vendu par")

    col_v1, col_v2 = st.columns([3, 1])
    with col_v1:
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 14px;">
                <div class="vendeur-avatar" style="width: 56px; height: 56px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 20px;">M</div>
                <div>
                    <div style="font-weight: 900; font-size: 18px; color: #111827;">Marir</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col_v2:
        st.markdown('<div class="btn-suivre" style="text-align: center; margin-top: 10px;">Suivre</div>', unsafe_allow_html=True)

    st.markdown("""
        <div style="font-size: 13px; color: #4B5563; margin-top: 12px; display: flex; flex-direction: column; gap: 4px;">
            <div>📅 Membre depuis mai 2026</div>
            <div>⏱️ Dernière activité il y a 3 heures</div>
        </div>

        <div class="vendeur-badges-container">
            <div class="vendeur-badge-item">
                <div class="vendeur-badge-circle">💬</div>
                <div>Réactif</div>
            </div>
            <div class="vendeur-badge-item">
                <div class="vendeur-badge-circle">📱</div>
                <div>Numéro<br>vérifié</div>
            </div>
        </div>

        <hr class="section-divider">

        <div style="display: flex; gap: 24px; font-size: 13px; font-weight: 700; color: #111827;">
            <div style="cursor: pointer;">🚩 Signaler l'annonce</div>
            <div style="cursor: pointer;">ℹ️ Vos droits et obligations</div>
        </div>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

with col_right:
    # --- BLOC VENDEUR FIXE DROITE ---
    st.markdown("""
        <div class="vendeur-card">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                <div class="vendeur-avatar" style="display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 18px;">M</div>
                <div style="font-weight: 800; font-size: 16px;">Marir</div>
            </div>
            <div style="background: #FFF7ED; color: #C2410C; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; display: inline-block;">💬 Réactif</div>
            <div style="font-size: 12px; color: #6B7280; margin: 8px 0 15px 0;">⏱️ Dernière activité il y a 3 heures</div>
            <div class="btn-reserver">⚡ Réserver</div>
            <div class="btn-msg">Envoyer un message</div>
            <div style="font-size: 12px; text-align: center; color: #4B5563; margin-bottom: 8px;">📞 Voir le numéro</div>
            <div style="font-size: 12px; text-align: center; color: #4B5563;">🔒 Paiement sécurisé 💳 <b>VISA</b></div>
        </div>
    """, unsafe_allow_html=True)