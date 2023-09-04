import cv2
import numpy as np

img_path = "resources/chateau.png"

# Chargez l'image
img = cv2.imread(img_path)

# Affichez la taille de l'image
print(f"Dimensions de l'image : {img.shape[1]}x{img.shape[0]}")

# Conversion de l'image de BGR (OpenCV utilise BGR par défaut) en RGB pour l'analyse ultérieure
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Cropez l'image autour du chateau au dimension ci-dessous
x_top = 950
y_top = 450
height = 170
width = 450

x_bottom = x_top + width
y_bottom = y_top + height

cropped_img = img_rgb[y_top:y_bottom, x_top:x_bottom]

# Tracez un histogramme par bande spectrale RGB des valeurs pixels (installer matplolib pour les visualiser) avec numpy ou opencv
import matplotlib.pyplot as plt


colors = ('r', 'g', 'b')
for i, col in enumerate(colors):
    histogram, bin_edges = np.histogram(
        cropped_img[:, :, i], bins=256, range=(0, 255)
    )
    plt.plot(bin_edges[0:-1], histogram, color=col)
    plt.title("Histogramme pour la bande couleur {}".format(col))
    plt.xlabel('Valeur de pixel')
    plt.ylabel('Nombre de pixels')
    plt.show()

# Analysez les histogrammes pour segmenter le chateau avec un seuil

# Enregistrez vos resultats

