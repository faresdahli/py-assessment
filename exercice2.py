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

# Analysez les histogrammes pour segmenter le chateau avec un seuil

# Enregistrez vos resultats

