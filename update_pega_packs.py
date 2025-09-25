import zipfile
import shutil
from pathlib import Path

# Windows download path
zip_dir = Path.home() / "Downloads" / "pega_packs"
target_repo = Path.cwd()

for zip_file in zip_dir.glob("*.zip"):
    pack_name = zip_file.stem.replace("_", "/")
    print(f"🔁 Updating: {pack_name}")

    pack_path = target_repo / "packs" / pack_name
    if pack_path.exists():
        shutil.rmtree(pack_path)
    pack_path.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_file, 'r') as z:
        z.extractall(pack_path)

print("✅ All packs updated.")
