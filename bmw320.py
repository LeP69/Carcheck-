import streamlit as st
import base64

st.set_page_config(
    page_title="BMW 320i coupé Msport 2007 - leboncoin",
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

img10_b64 = get_base64_img("photo10.jpg")
img11_b64 = get_base64_img("photo11.jpg")
img12_b64 = get_base64_img("photo12.jpg")

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
        background-color: #6B7280; display: inline-block;
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
st.markdown('<div class="breadcrumb">Accueil > Voitures > Nord-Pas-de-Calais > Pas-de-Calais > Saint-Omer 62500 > BMW 320i coupé Msport 2007 (moteur changé)</div>', unsafe_allow_html=True)

col_left, col_right = st.columns([2.2, 1])

with col_left:
    # --- GALERIE HTML ---
    st.markdown(f"""
        <div class="gallery-wrapper">
            <div class="main-photo-box">
                <img src="{img10_b64}" alt="Photo 10">
            </div>
            <div class="side-photos-box">
                <div class="side-photo-item"><img src="{img11_b64}" alt="Photo 11"></div>
                <div class="side-photo-item"><img src="{img12_b64}" alt="Photo 12"></div>
            </div>
        </div>
        <div class="price-box">
            <div class="ad-title">BMW 320i coupé Msport 2007 (moteur changé)</div>
            <div class="ad-sub">Saint-Omer · 2007 · 197500 km · Essence · Rapport d’historique disponible</div>
            <div class="ad-price">11 500 €</div>
            <div style="font-size: 13px; text-decoration: underline; font-weight: 600; margin-bottom: 6px;">📑 Simuler mon financement</div>
            <div style="font-size: 11px; color: #9CA3AF;">le mois dernier à 15:55</div>
            <div style="margin-top: 10px; background: #E0F2FE; color: #0369A1; display: inline-block; padding: 4px 8px; border-radius: 6px; font-size: 12px; font-weight: 600;">📍 Pack Sérénité : dès 139 €</div>
        </div>
    """, unsafe_allow_html=True)

    # Liens financement sous la carte
    st.markdown("""
        <div style="display: flex; gap: 30px; margin-top: 20px; font-size: 13px; font-weight: 600; color: #003B63;">
            <div>🪙 Voir le financement</div>
            <div>📄 Simulez votre prêt avec COFIDIS</div>
        </div>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

    # --- LES + DE L'ANNONCE ---
    st.markdown("### Les + de cette annonce")
    st.markdown("""
        <div style="display: flex; gap: 30px; margin-top: 15px;">
            <div class="plus-item">
                <div class="plus-icon-box">🚗</div>
                <div class="plus-text">Crit'Air 2</div>
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
        ("📋 Marque", "BMW", "📋 Modèle", "Série 3"),
        ("📅 Année modèle", "2007", "🏎️ Kilométrage", "197500 km"),
        ("⛽ Énergie", "Essence", "🕹️ Boîte de vitesse", "Manuelle"),
        ("🚗 Nombre de portes", "2", "👥 Nombre de place(s)", "4")
    ]

    infos_extra = [
        ("🗓️ Date de fin de validité du contrôle technique", "2027", "🚦 Date de première mise en circulation", "06/2007"),
        ("✨ État du véhicule", "Bon état général", "🚙 Type de véhicule", "Coupé"),
        ("🛋️ Sellerie", "Tout cuir", "🛠️ Historique et entretien", "Carnet d'entretien disponible, Factures disponibles, Réparations utiles déjà faites, État du contrôle technique valide"),
        ("🎨 Couleur", "Noir", "🌱 Crit'Air", "2"),
        ("⚡ Puissance fiscale", "9 Cv", "🐎 Puissance DIN", "170 Ch"),
        ("🪪 Permis", "Avec permis", "", "")
    ]

    if "show_all_bmw" not in st.session_state:
        st.session_state.show_all_bmw = False

    display_infos = infos_base + (infos_extra if st.session_state.show_all_bmw else [])

    for label1, val1, label2, val2 in display_infos:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="info-label">{label1}</div><div class="info-val">{val1}</div>', unsafe_allow_html=True)
        with c2:
            if label2:
                st.markdown(f'<div class="info-label">{label2}</div><div class="info-val">{val2}</div>', unsafe_allow_html=True)

    if not st.session_state.show_all_bmw:
        if st.button("Voir plus de critères"):
            st.session_state.show_all_bmw = True
            st.rerun()
    else:
        if st.button("Voir moins"):
            st.session_state.show_all_bmw = False
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
    st.write("Bonjour, suite à l’évolution des besoins familiaux, je mets en vente à regret ma BMW série 3 E92 coupé 320i M Sport.")
    st.write("Je vais essayer d’être le plus complet possible dans sa description :")
    st.write("")
    st.write("Il s’agit d’un modèle d’origine Belge nommé 320i « M Sport » (En France la version équivalente est « Sport Design »)")
    st.write("J’ai acheté ce véhicule en octobre 2019 à 177500 km, à un revendeur en France (reprise de concession Belge). J’en suis donc le second conducteur.")
    st.write("Le 1er propriétaire a toujours fait suivre son véhicule dans la même concession, celle de l’achat neuf en Belgique. (carnet de bord fourni)")
    st.write("")
    st.write("AUJOURD’HUI le véhicule totalise 197 500 km au compteur. Mais le moteur a quant à lui désormais environ 137 000 km.")
    st.write("En effet, le moteur nous a lâché suite apparemment à un défaut de graissage (arbres à cames rayés). Il a donc été remplacé (par un professionnel).")
    st.write("Factures à l’appui (Moteur 134000km) + Main d’œuvre (remplacement moteur, Vidange et fluides, Embrayage neuf) pour 4279 €.")
    st.write("Le véhicule a été soigneusement entretenu depuis son acquisition et de nombreux frais ont été réalisés. J’en oublie certainement…")
    st.write("")
    st.write("Fin 2019/2020 :")
    st.write("- sonde à Oxygène")
    st.write("- bougies")
    st.write("- Capteur basse pression")
    st.write("- Plaquette de freins")
    st.write("- Bobines d’allumage")
    st.write("")
    st.write("Fin 2022 :")
    st.write("- Roulement arrière droit")
    st.write("- 2 amortisseurs arrière + kit de protection amortisseurs")
    st.write("- 2 bras de suspensions avant")
    st.write("- Moyeu roue arrière droit")
    st.write("- Pompe à vide + joint torique")
    st.write("")
    st.write("Les 4 pneus sont récents eux aussi ainsi qu’un lave phare et 3 des 4 optiques phares arrière on été remplacés (origine) car les barres led ne fonctionnaient plus.")
    st.write("L’air bag Takara a été remplacé suite à la campagne de rappel chez BMW.")
    st.write("")
    st.write("Le véhicule sera bien sûr passé au CT pour la vente quand le processus de vente sera engagé.")
    st.write("")
    st.write("Le véhicule est globalement d’origine hormis quelques toute petites améliorations esthétiques. Covering black shadow contours de fenêtres (retirable selon les goûts).")
    st.write("")
    st.write("Voici les données/options principales à la livraison du véhicule neuf:")
    st.write("- Puissance : 15kw/170cv")
    st.write("- Couleur : Noir Saphir métallisé")
    st.write("- Sellerie/Tapisserie : Cuir Dakota/ D1 rouge corail LCD1")
    st.write("- Date de 1ère circulation : 25/06/2007")
    st.write("Edition et forfait :")
    st.write("- Forfait M Sport")
    st.write("- Suspension Sport M")
    st.write("- Volant M cuir")
    st.write("- Forfait aérodynamique M")
    st.write("Confort/ équipement :")
    st.write("- Forfait fumeur")
    st.write("- Siéges avant sport")
    st.write("- Siéges avant chauffants")
    st.write("- Garnitures intérieures Aluminium brossé fin")
    st.write("- Système navigation pro + chargeur 6 cd")
    st.write("- Système d’aide au stationnement « park distance control »")
    st.write("- Capteur de pluie")
    st.write("- Climatisation automatique")
    st.write("- Régulateur de vitesse")
    st.write("- Système de nettoyage des phares")
    st.write("- Eclairage xenon")
    st.write("- Touche multifonctions sur volant")
    st.write("- Jantes Alliage BMW M Araignée avec rayons 193, 18 pouces")
    st.write("- Ligne d’ombre haute brillance Shadow line (covering actuel retirable au besoin type black Shadow)")
    st.write("- Pavillon/ciel de toit anthracite")
    st.write("- Verrouillage automatique éloignement du véhicule/ verrouillage au démarrage")
    st.write("- Fonction Start and stop")
    st.write("...")
    st.write("Le prix proposé pour le véhicule est 11500€, discutable dans la limite du raisonnable mais DEVANT LE VEHICULE SEULEMENT.")
    st.write("")
    st.write("Merci d’avance de ne pas me proposer d’échange, ni d’offres farfelues.")
    st.write("")
    st.write("Si vous êtes intéressé, je peux vous envoyer davantage de photos sans soucis.")
    st.write("")
    st.write("Véhicule soigné et en très bel état, visible près de Saint-Omer (62500)")
    st.write("")
    st.write("Bien cordialement et au plaisir")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # --- SIMULATION FINANCEMENT CETELEM ---
    st.markdown('<div class="sponsor-badge">Sponsorisé</div>', unsafe_allow_html=True)
    st.markdown('<div class="cetelem-legal-notice">Un crédit vous engage et doit être remboursé. Vérifiez vos capacités de remboursement avant de vous engager.</div>', unsafe_allow_html=True)
    st.markdown('<div class="cetelem-title">Simuler un financement avec <span class="cetelem-logo-text">cetelem</span></div>', unsafe_allow_html=True)

    st.text_input("Montant du financement", value="11 500 €", key="montant_financement_bmw")
    
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
    st.markdown("<div style='font-size:15px; font-weight:700; color:#111827; margin-bottom:12px;'>Saint-Omer (62500)</div>", unsafe_allow_html=True)

    st.markdown("""
        <iframe width="100%" height="320" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" 
        src="https://www.openstreetmap.org/export/embed.html?bbox=2.2400%2C50.7300%2C2.2900%2C50.7600&amp;layer=mapnik&amp;marker=50.7450%2C2.2530" 
        style="border-radius:12px; border: 1px solid #E5E7EB;"></iframe>
        <hr class="section-divider">
    """, unsafe_allow_html=True)

    # --- VENDU PAR ---
    st.markdown("### Vendu par")

    col_v1, col_v2 = st.columns([3, 1])
    with col_v1:
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 14px;">
                <div class="vendeur-avatar" style="width: 56px; height: 56px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 20px;">k</div>
                <div>
                    <div style="font-weight: 900; font-size: 18px; color: #111827;">kam</div>
                    <div style="font-size: 13px; color: #6B7280;">23 annonces</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col_v2:
        st.markdown('<div class="btn-suivre" style="text-align: center; margin-top: 10px;">Suivre</div>', unsafe_allow_html=True)

    st.markdown("""
        <div style="font-size: 13px; color: #4B5563; margin-top: 12px; display: flex; flex-direction: column; gap: 4px;">
            <div>📅 Membre depuis août 2013</div>
            <div>⏱️ Dernière activité il y a 2 heures</div>
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
                <div class="vendeur-avatar" style="display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 18px;">k</div>
                <div>
                    <div style="font-weight: 800; font-size: 16px;">kam</div>
                    <div style="font-size: 12px; color: #6B7280;">23 annonces</div>
                </div>
            </div>
            <div style="background: #FFF7ED; color: #C2410C; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; display: inline-block;">💬 Réactif</div>
            <div style="font-size: 12px; color: #6B7280; margin: 8px 0 15px 0;">⏱️ Dernière activité il y a 2 heures</div>
            <div class="btn-reserver">⚡ Réserver</div>
            <div class="btn-msg">Envoyer un message</div>
            <div style="font-size: 12px; text-align: center; color: #4B5563; margin-bottom: 8px;">📞 Voir le numéro</div>
            <div style="font-size: 12px; text-align: center; color: #4B5563;">🔒 Paiement sécurisé 💳 <b>VISA</b></div>
        </div>
    """, unsafe_allow_html=True)