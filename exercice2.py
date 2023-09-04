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

# En se basant sur l'analyse des histogrammes, on suppose identifier ces plages pour la couleur du chateau

mask_r_1 = cv2.inRange(cropped_img[:, :, 0], 50, 150)
mask_g_1 = cv2.inRange(cropped_img[:, :, 1], 50, 85)
mask_b_1 = cv2.inRange(cropped_img[:, :, 2], 100, 130)

mask_r_2 = cv2.inRange(cropped_img[:, :, 0], 150, 255)
mask_g_2 = cv2.inRange(cropped_img[:, :, 1], 0, 255)
mask_b_2 = cv2.inRange(cropped_img[:, :, 2], 0, 255)

# On combine les masques pour obtenir la couleur du chateau
combined_mask_1 = cv2.bitwise_and(mask_r_1, mask_g_1)
combined_mask_1 = cv2.bitwise_and(combined_mask_1, mask_b_1)

combined_mask_2 = cv2.bitwise_and(mask_r_2, mask_g_2)
combined_mask_2 = cv2.bitwise_and(combined_mask_2, mask_b_2)


combined_mask = cv2.bitwise_or(combined_mask_1, combined_mask_2)
segmented_img = cv2.bitwise_and(cropped_img, cropped_img, mask=combined_mask)

cv2.imshow('Segmentation du Chateau', segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Enregistrez vos resultats
cv2.imwrite("cropped_image.png", cv2.cvtColor(cropped_img, cv2.COLOR_RGB2BGR))  # Conversion de nouveau en BGR pour l'enregistrement
cv2.imwrite("segmented_image.png", segmented_img)
