# Analyse de l'Inclusion Numérique - Bordeaux Métropole

Ce document récapitule les pistes d'analyse pour tester l'hypothèse d'une insuffisance des efforts de Bordeaux Métropole en matière d'inclusion numérique.

## 1. Colonnes les plus pertinentes du CSV
Pour l'analyse territoriale et qualitative, les colonnes suivantes sont essentielles :
- **`adresse_code_postal` / `adresse_commune`** : Pour la répartition géographique.
- **`latitude` / `longitude`** : Pour la cartographie précise (utilisée dans la carte interactive).
- **`public_cible`** : Pour vérifier si les publics fragiles sont visés.
- **`tarifs`** : Indicateur d'accessibilité financière.
- **`services` / `niveau_service`** : Détail des compétences enseignées (CAF, Impôts, etc.).
- **`modalites_accompagnement`** : Distingue l'accès libre de l'accompagnement humain.

## 2. Pistes de croisement de données
Pour démontrer une insuffisance, il est recommandé de croiser ce fichier avec :
- **Les Quartiers Prioritaires de la Ville (QPV)**.
- **Les données INSEE** : Taux de pauvreté, part des seniors (75+), niveau de diplôme par IRIS.
- **L'Indice de Fragilité Numérique** (disponible sur data.gouv.fr).
- **L'accessibilité TBM** : Proximité des transports en commun.

## 3. Fréquence des services (Extrait)
Le tableau ci-dessous montre la fréquence des services déclarés par les structures (généré le 31 mars 2026). Une forte présence de niveaux "Non" ou "Basique" peut soutenir l'hypothèse d'une offre limitée.

| Service / Niveau | Fréquence |
| :--- | :--- |
| IMPTROISD/Non | 108 |
| CODE/Non | 92 |
| SITEWEB/Non | 81 |
| EMPLOISTORE/Non | 61 |
| MOOC/Non | 57 |
| PAO/Non | 54 |
| MAILS/Expert | 53 |
| RETRAITE/Basique | 53 |
| RETRAITE/Non | 50 |
| INTERNET/Maîtrise | 49 |

## 4. Outils disponibles dans le dépôt
- **`index.html`** : Carte interactive (Leaflet) visualisant les lieux avec des icônes 💩 pour marquer l'insuffisance supposée.
- **`count_services.py`** : Script Python pour recalculer les statistiques de services à partir du CSV.

---
*Analyse générée dans le cadre de l'étude sur la politique d'inclusion numérique de Bordeaux Métropole.*
