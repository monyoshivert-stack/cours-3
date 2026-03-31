import csv
from collections import Counter
import os

def count_services(file_path):
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        return

    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        # L'index 38 correspond à la colonne 'niveau_service' dans ce fichier spécifique
        # Bien que l'en-tête soit décalé, l'index 38 contient les données détaillées (ex: TABLETTE/Expert)
        service_idx = 38
        
        all_services = []
        for row in reader:
            if len(row) > service_idx:
                services_raw = row[service_idx]
                if services_raw:
                    # Extraction des services (format: NOM/NIVEAU)
                    parts = [s.strip() for s in services_raw.split(',') if '/' in s]
                    all_services.extend(parts)

    counts = Counter(all_services)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # Affichage des résultats
    print(f"{'Service / Niveau':<40} | {'Fréquence':<10}")
    print("-" * 53)
    for service, freq in sorted_counts:
        print(f"{service:<40} | {freq:<10}")

if __name__ == "__main__":
    csv_filename = "RAW_met_lieux_inclusion_numerique - RAW_met_lieux_inclusion_numerique.csv"
    count_services(csv_filename)
