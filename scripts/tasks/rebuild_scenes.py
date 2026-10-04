import sys
from pathlib import Path
from ndspy import lz10

from tasks.extract_scenes import SCENE_FILES

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from libsummon.text import extract_text


def rebuild_scenes():
    for scene, offset in SCENE_FILES.items():

        scene_path = Path(f"decompressed/{scene}.rts")
        scene_data = scene_path.read_bytes()
        out_path = Path(f"translated/data/scnrts/{scene}.rtz")

        lz10.compressToFile(scene_data, out_path)
        print(f"{scene}.rtz updated!")

        


