# Trie en fonction des extensions
# Auteur : Nono
# Date : 15/01/2024

from pathlib import Path

for f in Path(r"C:\Users\HP\Downloads").glob("*.png"):
    print(f.name)
dirs = {".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".pdf": "Documents",
        '.mp3': 'Musiques',
        ".avi": "Videos",
        ".wav": "Musiques",
        ".cbz": "Scan",
        ".mkv": "Videos",
        ".pnj": "Images"}

tri_dir = Path(r"C:\Users\HP\Downloads")
tri_dir.mkdir(exist_ok=True)

files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    # Si aucune correspondance n'est trouvée pour l'extension, on place les fichiers dans un dossier Autres
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
