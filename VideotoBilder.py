import cv2
import os

# Video-Dateipfad angeben
video_path = r'C:\Users\soere\OneDrive\Videos\Valorant\Ass2.mp4'

# Ordner für die extrahierten Bilder erstellen
output_folder = 'extrahierte_bilder'
os.makedirs(output_folder, exist_ok=True)

# Video-Capture-Objekt erstellen
cap = cv2.VideoCapture(video_path)

# Überprüfen, ob das Video geöffnet wurde
if not cap.isOpened():
    print("Fehler beim Öffnen des Videos.")

count = 0
while cap.isOpened():
    # Frame für Frame lesen
    ret, frame = cap.read()

    # Überprüfen, ob das Ende des Videos erreicht ist
    if not ret:
        break

    # Frame im Ordner speichern
    frame_path = os.path.join(output_folder, f'frame_{count}.jpg')
    cv2.imwrite(frame_path, frame)

    count += 1
cap.release()
cv2.destroyAllWindows()

