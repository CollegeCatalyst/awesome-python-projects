from PIL import Image
from tkinter.filedialog import *
import argparse

def compressImage(filename):
    img = Image.open(filename)
    myHeight, myWidth = img.size
    img = img.resize((myHeight,myWidth), Image.ANTIALIAS)
    img.save("compressed-"+filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("img",type = str)

    args = parser.parse_args()
    compressImage(args.img)