from PIL import Image
from get_configs import *

def exportGif(export_name, clip):
    clipdir = Dir(clip)

    layer0 = get_layer(clipdir, 0)
    layer1 = get_layer(clipdir, 1)
    layer2 = get_layer(clipdir, 2)

    max_fps = get_length(clipdir)

    bgFrames = []

    def makeBackground(pos):
        bgFrames[pos] = Image.new('RGB', (320, 240), (255,255,255))
        return bgFrames[pos]

    class FRAME:
        def __init__(self, pos, background, oldFrame0, oldFrame1, oldFrame2):
            self.pos = pos
            self.background = background
            self.oldFrame0 = oldFrame0
            self.oldFrame1 = oldFrame1
            self.oldframe2 = oldFrame2
            pass

        def makeFrame(self):
            try:
                self.oldFrame0 = Image.open(clipdir + layer0[self.pos])
            except:
                self.oldFrame0 = Image.new('RGBA', (320, 240), (255, 0, 0, 0))
            try:
                self.oldFrame1 = Image.open(clipdir + layer1[self.pos])
            except:
                self.oldFrame1 = Image.new('RGBA', (320, 240), (255, 0, 0, 0))
            try:
                self.oldFrame2 = Image.open(clipdir + layer2[self.pos])
            except:
                self.oldFrame2 = Image.new('RGBA', (320, 240), (255, 0, 0, 0))
        
            self.background.paste(self.oldFrame0, (0,0), self.oldFrame0)
            self.background.paste(self.oldFrame1, (0,0), self.oldFrame1)
            self.background.paste(self.oldFrame2, (0,0), self.oldFrame2)

            return self.background 
            pass

    newFrames = []
    frame = []

    for i in range(max_fps):
        bgFrames.append(None)
        newFrames.append(None)
        frame.append(None)

    for c in range(max_fps):
        bgFrames[c] = makeBackground(c)
        newFrames[c] = FRAME(c, bgFrames[c], layer0[c], layer1[c], layer2[c])
        frame[c] = newFrames[c].makeFrame()


    frame[0].save("{}.gif".format(export_name), save_all=True, append_images=frame[1:], duration = 1000/get_fps(clipdir), loop=0)

if __name__ == '__main__':
    list = os.listdir(Dir(''))
    clip = list[0]

    exportGif('output.gif', clip)
    pass