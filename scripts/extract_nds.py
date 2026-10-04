# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "ndspy",
# ]
# ///
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.tasks.extract_scenes import extract_scenes
from libsummon.text import extract_text

def main():


    if os.path.exists("extracted"):
        shutil.rmtree("extracted")
    print("Extracting NDS...")
    source_nds = Path("sn1.nds")
    if not source_nds.exists():
        sys.stderr.write(f"Source NDS not found: {source_nds}\n")
        sys.exit(1)
    result = subprocess.run(
        ["NitroPacker", "unpack", "-r", source_nds, "-o", "extracted", "-p", "sn1", "-d"],
        capture_output=True,
        text=True,
        shell=False,
    )
    if result.stdout:
        sys.stdout.write(result.stdout)
    if result.returncode != 0:
        sys.stderr.write(f"NitroPacker failed with return code {result.returncode}\n")
        if result.stderr:
            sys.stderr.write(f"stderr:\n{result.stderr}\n")
        sys.exit(result.returncode)

    # Copy extracted to translated
    if os.path.exists("translated"):
        shutil.rmtree("translated")
    shutil.copytree("extracted", "translated")
    print("Done!")

    if os.path.exists("decompressed"):
        shutil.rmtree("decompressed")
    os.makedirs("decompressed", exist_ok=True)

    print("Extracting all scene files...")
    extract_scenes()
    extract_text()
    print("Done!")


if __name__ == "__main__":
    main()
