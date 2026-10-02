import sys
from pathlib import Path
from ndspy import lz10

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from libsummon.text import extract_text

SCENE_FILES: dict[str, int] = {
    "scn000a": 14384,
	"scn000b": 16105,
	"scn001a": 23816,
	"scn001b": 28557,
	"scn002a": 35849,
	"scn002b": 24663,
	"scn003a0": 14167,
	"scn003a1": 36587,
	"scn003b": 17743,
	"scn004a": 33854,
	"scn004b": 16076,
	"scn005a": 34679,
	"scn005b": 17747,
	"scn006a": 37728,
	"scn006b": 15152,
	"scn007a": 33908,
	"scn007b": 15472,
	"scn008": 34340,
	"scn009a": 31688,
	"scn009b": 16084,
	"scn010": 26429,
	"scn011a": 24428,
	"scn011b": 17184,
	"scn012a": 37197,
	"scn012b": 15502,
	"scn013": 26838,
	"scn014": 12223,
	"scn015": 26013,
	"scn016": 22226,
	"scn017a": 10628,
	"scn017b": 11071,
	"scn017c": 26201,
	"scn018": 26111,
	"scn020": 12824,
	"scn021": 10826,
	"scn0suba": 28178,
	"scn0subc": 12652,
	"scn0subd": 13437,
	"scn0subf": 12544
}

def extract_scenes():
    for scene, offset in SCENE_FILES.items():
        # Decompress scene files into the decompressed folder
        scene_path = Path(f"extracted/data/scnrts/{scene}.rtz")
        scene_data = scene_path.read_bytes()
        out_path = Path(f"decompressed/{scene}.rts")
        lz10.decompressToFile(scene_data, out_path)

        


