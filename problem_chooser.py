import os,subprocess,sys
from PIL import Image

if subprocess.call("./a.out") == 0:
    try:
        img  = Image.open("./photo1.png")
        img.show()
    except IOError:
        pass
