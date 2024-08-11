from os import path, mkdir
from PIL import Image, ImageSequence


def split(openimage, dirc):
    img = Image.open(openimage)
    fps = ImageSequence.Iterator(img)
    i = 0
    mydir = dirc
    if not path.exists(mydir):
        mkdir(mydir)
    for frame in fps:
        import os
        frame.save('{}{}pic_{}.png'.format(mydir, os.sep, i))
        i += 1
