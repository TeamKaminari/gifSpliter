from os import sep, path, mkdir
from PIL import Image, ImageSequence


def split(openimage, dirc):
    img = Image.open(openimage)
    fps = ImageSequence.Iterator(img)
    i = 0
    for frame in fps:
        frame.save('{}{}pic_{}.png'.format(dirc, sep, i))
        i += 1


def split_terminal(image, dirc):
    img = Image.open(image)
    fps = ImageSequence.Iterator(img)
    i = 0
    if not path.exists(dirc):
        mkdir(dirc)
    for frame in fps:
        frame.save('{}{}pic_{}.png'.format(dirc, sep, i))
        i += 1
