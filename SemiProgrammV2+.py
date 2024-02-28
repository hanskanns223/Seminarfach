import cv2, os, glob
import numpy as np
from PIL import Image

global RGBdBild # Durchschnittlicher RGB über alle Bilder


def Ordnerauslesen(Bildpfad):
    bilder_liste = glob.glob(os.path.join(Bildpfad, '*.jpg'))
    print(f'Es wurden {str(len(bilder_liste))} Bilder in dem Ordner gefunden')
    ydalleBild = HelligkeitjedesBilder(bilder_liste)
    print(f'Durchschnittliche Helligkeit aller Bilder: {ydalleBild}')

def HelligkeitjedesBilder(ListeBilder):
    RGBdBild= []
    for Bild in ListeBilder:
        img = Image.open(Bild)
        data = np.array(img)
        for RGB in data[:,:]:
            RGBdBild[0] = RGB[0] + sum(RGBdBild[0])/(len(RGBdBild[1])+1)
            RGBdBild[1] = RGB[1] + sum(RGBdBild[1]) / (len(RGBdBild[1]) + 1)




Ordnerauslesen('extrahierteBilder')