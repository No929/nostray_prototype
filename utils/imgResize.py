import os
import random
from PIL import Image

from nostray_prototype import settings

def pImgResize(filename):
    image = Image.open(filename)
    image.thumbnail((640,360),Image.ANTIALIAS)
    url = 'post_img/%Y/%m' + image.name
    name = settings.MEDIA_URL + url

    if os.path.exists(name):
        fname, ext = os.path.splitext(image.name)
        fname = fname[0:4] + str(random.randint(0,10000))
        image.name = fname + ext
        url = 'post_img/%Y/%m' + image.name
        name = settings.MEDIA_URL + url

        image.save(name, 'jpg')

        return url
    else:
        image = None

        return None