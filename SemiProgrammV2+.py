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
    for Bild in ListeBilder:
        img = Image.open(Bild)
        data = np.array(img)
        RGBdBild = np.zeros(3)
        RGBdBild[0] = data[:,:,0].mean()
        RGBdBild[1] = data[:,:,1].mean()
        RGBdBild[2] = data[:, :, 2].mean()
        print(RGBdBild)
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                #Rote Werte:
                if data[i,j,0] < RGBdBild[0] and data[i,j,0] - (data[i,j,0] - RGBdBild[0])**2 >=0 :
                    data[i,j,0] = data[i,j,0] - (data[i,j,0] - RGBdBild[0])**2

                else:
                    if data[i,j,0] > RGBdBild[0] and data[i,j,0] + (data[i,j,0] - RGBdBild[0])**2 <=255 :
                        data[i,j,0] = data[i,j,0] - (data[i,j,0] - RGBdBild[0])**2
                # Grüne Werte:
                if data[i, j, 1] < RGBdBild[1] and data[i, j, 1] - (data[i, j, 1] - RGBdBild[1]) ** 2 >= 0:
                    data[i, j, 1] = data[i, j, 1] - (data[i, j,1] - RGBdBild[1]) ** 2

                else:
                    if data[i, j, 1] > RGBdBild[1] and data[i, j, 1] + (data[i, j, 1] - RGBdBild[1]) ** 2 <= 255:
                        data[i, j, 1] = data[i, j, 1] + (data[i, j, 1] - RGBdBild[1]) ** 2

                #Blaue Werte:
                if data[i, j, 2] < RGBdBild[2] and data[i, j, 2] - (data[i, j, 2] - RGBdBild[2]) ** 2 >= 0:
                    data[i, j, 2] = data[i, j, 2] - (data[i, j,2] - RGBdBild[2]) ** 2

                else:
                    if data[i, j, 2] > RGBdBild[2] and data[i, j, 2] + (data[i, j, 2] - RGBdBild[2]) ** 2 <= 255:
                        data[i, j, 2] = data[i, j, 2] + (data[i, j, 2] - RGBdBild[2]) ** 2
        Image.fromarray(data.astype(np.uint8)).save("manipuliertes_bild.jpg")
Ordnerauslesen('extrahierteBilder')