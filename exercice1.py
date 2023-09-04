import cv2
import numpy as np

# Charger une image binaire de ce format
IMG_HEIGHT = 480
IMG_WIDTH = 640
CHANNEL = 1 # Grayscale

with open("resources/thermal_img_640x480_16bits_grayscale.bin", 'rb') as file:
    buffer = file.read()

# Astuce une image est une matrice (numpy est une librairie interressante quand il est question de matrice)
# https://numpy.org/doc/stable/reference/arrays.ndarray.html

# Conversion du buffer en un tableau numpy de type uint16 (entier non signé sur 16 bits)
thermal_data = np.frombuffer(buffer, dtype=np.uint16)

# Redimensionnement du tableau pour obtenir une matrice de 640x480
thermal_img = thermal_data.reshape(IMG_HEIGHT, IMG_WIDTH)

# Faites une normalisation MIN/MAX sur 8 bits de l'image (utiliser opencv)
normalized_img = cv2.normalize(thermal_img, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Enregistrer l'image normalisée au format png
cv2.imwrite('normalized_image.png', normalized_img)