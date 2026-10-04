# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "ndspy",
# ]
# ///
import sys, subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tasks.rebuild_scenes import rebuild_scenes

PATCHED_NDS = "english.nds"

def main():


    print("Rebuilding Scene files...")
    rebuild_scenes()
    print("Done!")


    print("Rebuilding NDS...")
    json = Path("translated/sn1.json")

    result = subprocess.run(
        ["NitroPacker", "pack", "-p", json, "-r", PATCHED_NDS, "-c"],
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

    print(f"Patched NDS saved to {PATCHED_NDS}")

if __name__ == "__main__":
    main()