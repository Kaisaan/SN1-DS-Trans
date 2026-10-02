from pathlib import Path
def extract_text():     # scene: Path, offset: int
    scene = Path(f"decompressed/scn000a.rts")
    offset = 14384
    scene_data = scene.read_bytes()

    log = open("log.txt", "w", encoding="utf-8")

    num1 = 0
    array1 = []
    array2 = []
    array3 = []
    pos = offset

    while (pos < len(scene_data)):
        current = pos
        flag = False
        str_len = -1
        byte = scene_data[pos]

        match byte:

            case 46:
                pos += 5

            case 49:
                pos += 9
                
            case 52:
                pos += 13
                
            case 56:
                pos += 13
                
            case 64:
                pos += 5
                
            case 65:
                pos += 5
                
            case 72:
                pos += 5
                
            case 73:
                pos += 5
                
            case 75:
                pos += 5
                
            case 76:
                pos += 5
                
            case 77:
                pos += 5
                
            case 78:
                pos += 5
                
            case 79:
                pos += 5
                
            case 80:
                pos += 5
                
            case 81:
                pos += 5
                
            case 82:
                pos += 5
                
            case 83:
                pos += 5
                
            case 84:
                pos += 5
                
            case 85:
                pos += 5
                
            case 86:
                pos += 5
                
            case 88:
                pos += 5
                
            case 89:
                pos += 5
                
            case 90:
                pos += 5
                
            case 93:
                pos += 5
                
            case 94:
                pos += 5
                
            case 98:
                pos += 5
                
            case 99:
                pos += 5
                
            case 101:
                pos += 5
                

            case 104:
                pos += 14
                
            case 107:
                pos += 9
                
            case 108:
                pos += 9
                
            case 109:
                pos += 9
            
            case 110:
                if (scene_data[pos + 5] != 0):
                    pos += 5
                elif (scene_data[pos + 5] == 107):
                    pos += 14
                elif (scene_data[pos + 10] == 0):
                    pos += 17
                elif (scene_data[pos + 17] == 1):
                    pos += 20
                elif (scene_data[pos + 18] == 252):
                    if (scene_data[pos + 21] == 253):
                        pos += 26
                    else:
                        pos += 24
                elif (scene_data[pos + 19] == 252):
                    pos += 22
                else:
                    pos += 20
                
            case 111:
                pos = len(scene_data)
                

            case 51:
                flag = True
                str_len = scene_data[pos + 5]
                string = scene_data[pos + 6: pos + 6 + str_len].decode(encoding="shiftjis", errors="backslashreplace")
                string = string.replace("\n", "\\n")
                array2.append(string)
                log.write(f"{string}\n")
                array3.append(num1)
                pos += 5
                
            case _:
                print("bruh")

        num4 = pos - current
        data_file = scene_data[current:num4]
        array1.append(data_file)
        if flag:
            pos = pos + 1 + str_len

        num1 += 1
        