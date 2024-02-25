from PIL import Image
import numpy as np
Bild1 = []
Bild2 = []
im1 = Image.open('IMG_1462.JPG')
im2 = Image.open('IMG_1463.JPG')
pix = im1.load()
print(im1.size)
def ohneNumpy(im1):
    for x in range(im1.size[0]):
        for y in range(im1.size[1]):
            Y = 0.2126 * pix[x, y][0] + 0.7152 * pix[x, y][1] + 0.0722 * pix[x, y][2]
            Bild1.append(Y)
    print("Durschnitthellikeit:" + str(sum(Bild1) / len(Bild1)))

    pix2 = im2.load()
    for x in range(im2.size[0]):
        for y in range(im2.size[1]):
            Y = 0.2126 * pix2[x, y][0] + 0.7152 * pix2[x, y][1] + 0.0722 * pix2[x, y][2]
            Bild2.append(Y)
    print("Durschnitthellikeit:" + str(sum(Bild2) / len(Bild2)))

def Helligkeitbestimmen_numpy(Bild):
    img = Image.open(Bild)
    data = np.array(img)
    Y = 0.2126 * data[:, :, 0] + 0.7152 * data[:, :, 1] + 0.0722 * data[:, :, 2]
    return np.mean(Y)

def Helligkeitbestimmen(Bild):
    Durchschnittshelligkeit = []
    helligkeit = Helligkeitbestimmen_numpy(Bild)
    Durchschnittshelligkeit.append(helligkeit)

    return sum(Durchschnittshelligkeit) / len(Durchschnittshelligkeit)

print(Helligkeitbestimmen('IMG_1462.JPG'))