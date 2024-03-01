import cv2, os, glob
import numpy as np
from PIL import Image

global RGBdBild # Durchschnittlicher RGB über alle Bilder
global MAximwarhier

def Ordnerauslesen(Bildpfad):
    bilder_liste = glob.glob(os.path.join(Bildpfad, '*.jpg'))
    print(f'Es wurden {str(len(bilder_liste))} Bilder in dem Ordner gefunden')
    #ydalleBild = HelligkeitjedesBilder(bilder_liste)
    #print(f'Durchschnittliche Helligkeit aller Bilder: {ydalleBild}')
    Bilderzusammenfügen(bilder_liste, Image.open(bilder_liste[0]).size)
def HelligkeitjedesBilder(ListeBilder):
    for Bild in ListeBilder:
        img = Image.open(Bild)
        data = np.array(img)
        RGBdBild = np.mean(data, axis=(0, 1))
        print(RGBdBild)
        # Rote Werte
        data[:, :, 0] = np.where(data[:, :, 0] < RGBdBild[0], data[:, :, 0] - (data[:, :, 0] - RGBdBild[0]) ,
                                 np.where(data[:, :, 0] > RGBdBild[0],
                                          data[:, :, 0] + (data[:, :, 0] - RGBdBild[0]), data[:, :, 0]))

        # Grüne Werte
        data[:, :, 1] = np.where(data[:, :, 1] < RGBdBild[1], data[:, :, 1] - (data[:, :, 1] - RGBdBild[1]),
                                 np.where(data[:, :, 1] > RGBdBild[1],
                                          data[:, :, 1] + (data[:, :, 1] - RGBdBild[1]), data[:, :, 1]))

        # Blaue Werte
        data[:, :, 2] = np.where(data[:, :, 2] < RGBdBild[2], data[:, :, 2] - (data[:, :, 2] - RGBdBild[2]),
                                 np.where(data[:, :, 2] > RGBdBild[2],
                                          data[:, :, 2] + (data[:, :, 2] - RGBdBild[2]), data[:, :, 2]))
        Image.fromarray(data.astype(np.uint8)).save("extrahierte_bilder/manipuliertes_bild.jpg")
def Bilderzusammenfügen(ListeBilder, imgsize):
    i = 0
    endbild = np.zeros((imgsize[1], imgsize[0], 3), dtype=np.uint8)
    for Bild in ListeBilder:
        img = Image.open(Bild)
        data = np.array(img)

        if i == 0:
            endbild = data[:,:]
        else:
            endbild = (endbild[:,:] + data[:,:]) // 2
            print(endbild[0][0][0])
        i +=1
    Image.fromarray(endbild.astype(np.uint8)).save("Ausgansbild.jpg")
    print("Test")
Ordnerauslesen('extrahierte_bilder')
