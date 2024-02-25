import cv2, os, glob
import numpy as np
from PIL import Image
global avgHelligkeit
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

def Helligkeitbestimmen(ListeBilder):
    Durchschnittshelligkeit = []
    for Bild in ListeBilder:
        helligkeit = Helligkeitbestimmen_numpy(Bild)
        Durchschnittshelligkeit.append(helligkeit)

    return sum(Durchschnittshelligkeit) / len(Durchschnittshelligkeit)

def Ordnerauslesen(Bildpfad):
    bilder_liste = glob.glob(os.path.join(Bildpfad, '*.jpg'))
    print(f'Es wurden {str(len(bilder_liste))} Bilder in dem Ordner gefunden')
    durchschnittliche_helligkeit = Helligkeitbestimmen(bilder_liste)
    print(f'Durchschnittliche Helligkeit aller Bilder: {durchschnittliche_helligkeit}')
def Hintergrundrausrechnen(durchschnittHelligkeit,y):
    if y < durchschnittHelligkeit and avgHelligkeit != 0:
        avgHelligkeit = (durchschnittHelligkeit + y) / 2
        y = 0
    else:
        avgHelligkeit = (durchschnittHelligkeit + y) / 2
        y = 255


VideoBilder(r"C:\Users\soere\OneDrive\Videos\SeminarfachProjektVideos\DJI_0017.MP4")
Ordnerauslesen('extrahierte_bilder')
