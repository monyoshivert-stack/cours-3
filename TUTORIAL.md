# Tutoriel : Analyse et Cartographie de l'Inclusion Numérique

Ce guide explique comment reproduire l'analyse des données d'inclusion numérique de Bordeaux Métropole, de l'extraction des fréquences à la mise en ligne d'une carte interactive.

## 1. Préparation des données
Le fichier source est un CSV nommé `RAW_met_lieux_inclusion_numerique - RAW_met_lieux_inclusion_numerique.csv`.
Les colonnes clés pour l'analyse sont :
- **Index 38 (niveau_service)** : Contient les détails des prestations (ex: `TABLETTE/Expert`).
- **Latitude / Longitude** : Pour le positionnement géographique.

## 2. Analyse des services avec Python
Pour extraire la fréquence de chaque service, nous utilisons un script Python qui lit le CSV sans bibliothèques externes complexes.

### Utilisation du script `count_services.py` :
Exécutez la commande suivante dans votre terminal :
```bash
python3 count_services.py
```
Le script va :
1. Parcourir chaque ligne du CSV.
2. Découper la colonne `niveau_service` par les virgules.
3. Compter les occurrences de chaque couple `Service/Niveau`.
4. Afficher un tableau trié par popularité.

## 3. Analyse avec Google Sheets (Alternative)
Si vous préférez travailler dans un tableur, utilisez cette formule pour "aplatir" les services et compter les fréquences :
```excel
=QUERY(FLATTEN(ARRAYFORMULA(SPLIT(AM2:AM; ","))); "select Col1, count(Col1) where Col1 is not null group by Col1 order by count(Col1) desc")
```
*(Remplacez `AM2:AM` par votre colonne réelle).*

## 4. Création de la carte interactive (Leaflet)
La carte est construite dans `index.html` en utilisant la bibliothèque **Leaflet**.

### Points clés du code :
- **Fond de carte** : Utilisation de `CartoDB Positron` pour un rendu gris clair sobre.
- **Lecture du CSV** : Utilisation de `PapaParse` pour lire le fichier directement depuis le navigateur.
- **Icônes personnalisées** : Utilisation de `L.divIcon` pour remplacer les marqueurs par des emojis (💩).

### Personnalisation de l'icône :
Dans le fichier `index.html`, vous pouvez modifier l'emoji ou la taille ici :
```javascript
const poopIcon = L.divIcon({
    html: '<span style="font-size: 24px;">💩</span>',
    className: 'poop-icon',
    // ...
});
```

## 5. Déploiement sur GitHub Pages
Pour rendre la carte accessible publiquement :
1. Poussez vos fichiers (`index.html`, le CSV, etc.) sur la branche `main` de votre dépôt GitHub.
2. Allez dans les **Settings** de votre dépôt sur GitHub.
3. Dans le menu de gauche, cliquez sur **Pages**.
4. Sous **Build and deployment**, choisissez la source `Deploy from a branch`.
5. Sélectionnez `main` et cliquez sur **Save**.
6. Votre carte sera disponible à l'adresse : `https://[votre-pseudo].github.io/[nom-du-repo]/`

## 6. Prochaines étapes (Croisement de données)
Pour approfondir l'analyse :
1. Téléchargez les contours des **Quartiers Prioritaires (QPV)** sur data.gouv.fr.
2. Superposez-les sur la carte Leaflet en format GeoJSON.
3. Observez si les "💩" se situent bien dans les zones à forte fragilité numérique.

---
*Document créé le 31 mars 2026 pour accompagner l'étude sur l'inclusion numérique.*
