import os

def Dir(name):
    appdata = os.getenv('appdata')
    dir = appdata + '\\clipnote_studio\\notes\\' + name + '\\'
    return dir

def get_layer(dir, layer):

    layer0 = []
    layer1 = []
    layer2 = []

    for i in range(get_length(dir)):
        layer0.append(str(i) + ',0.png')
        layer1.append(str(i) + ',1.png')
        layer2.append(str(i) + ',2.png')
                
    if layer == 0:
        return layer0
    if layer == 1:
        return layer1
    if layer == 2:
        return layer2

def get_fps(dir):
    framerate = 12
    with open(dir + 'data.ini') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if 'framerate' in lines[i]:
            q1 = lines[i].find('"') + 1
            q2 = lines[i].find('"', q1)

            framerate = int((   lines[i] [q1:q2]    ))
    return framerate

def get_length(dir):
    length = 60
    with open(dir + 'data.ini') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if 'frame_max' in lines[i]:
            q1 = lines[i].find('"') + 1
            q2 = lines[i].find('"', q1)

            length = int((   lines[i] [q1:q2]    ))
    return length + 1

def get_thumb(dir):
    thumb = dir + 'thumb.png'
    return thumb

if __name__ == '__main__':

    list = os.listdir(Dir(''))

    clip = list[0]

    for i in get_layer(Dir(clip), 0):
        print(i)