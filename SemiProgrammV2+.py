import cv2
import os
import glob
import numpy as np
from PIL import Image

def VideoBilder(Videopfad):
    video_path = Videopfad
    output_folder = 'extrahierte_bilder'
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Fehler beim Öffnen des Videos.")

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame_path = os.path.join(output_folder, f'frame_{count}.jpg')
        cv2.imwrite(frame_path, frame)

        count += 1
    cap.release()
    cv2.destroyAllWindows()

def Helligkeitbestimmen_numpy(Bild):
    img = Image.open(Bild)
    data = np.array(img)
    Y = 0.2126 * data[:, :, 0] + 0.7152 * data[:, :, 1] + 0.0722 * data[:, :, 2]
    return np.mean(Y)

def Hintergrundrausrechnen_numpy(durchschnittHelligkeit, bild):
    if durchschnittHelligkeit != 0:
        neuerDurchschnitt = (durchschnittHelligkeit + bild) / 2

        mask_unter_schwelle = bild < durchschnittHelligkeit * 0.5
        mask_ueber_schwelle = bild > durchschnittHelligkeit * 1.5

        bild[mask_unter_schwelle] = 0
        bild[mask_ueber_schwelle] = 255

        return neuerDurchschnitt, bild

    return durchschnittHelligkeit, bild

def Helligkeitbestimmen_und_rausrechnen(ListeBilder):
    Durchschnittshelligkeit = []
    for Bild in ListeBilder:
        helligkeit = Helligkeitbestimmen_numpy(Bild)
        Durchschnittshelligkeit.append(helligkeit)

    durchschnittHelligkeit = sum(Durchschnittshelligkeit) / len(Durchschnittshelligkeit)

    for i, Bild in enumerate(ListeBilder):
        img = Image.open(Bild)
        data = np.array(img)
        durchschnittHelligkeit, data = Hintergrundrausrechnen_numpy(durchschnittHelligkeit, data)

        neues_Bild = Image.fromarray(data)
        neues_Bild.save(f'angepasstes_bild_{i}.jpg')

# Beispielaufruf
Ordnerauslesen('extrahierte_bilder')
