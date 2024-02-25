import os, glob

ordner_pfad = r"C:\Users\soere\OneDrive\Bilder\Screenshots"

bilder_liste = glob.glob(os.path.join(ordner_pfad, '*.png'))
print("Elemente gefunden: " + str(len(bilder_liste)))



