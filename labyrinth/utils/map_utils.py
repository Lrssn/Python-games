import json

def loadmap(map_file):
    f = open('assets/maps/' + map_file)
    x = json.load(f)
    f.close()
    return x

def parsemap(map_string, sizex, sizey):
    final_map = []
    parsed_string = map_string.split(' ')
    for j in range(sizey):
        substring = []
        for i in range(sizex):
            substring.append(int(parsed_string[i+j*sizex]))
        final_map.append(substring)
    return final_map

def savemap(map_name, map_string, sizex, sizey):
    x = ''
    for i in range(sizey):
        for j in range(sizex):
            x += str(map_string[j][i].spriteids[0]) + " "
    
    y = json.dumps({"map_name":map_name, "sizex": sizex, "sizey":sizey, "layer0": x}, indent=4)
    f = open('assets/maps/' + map_name, "w")
    f.write(y)
    f.close()

