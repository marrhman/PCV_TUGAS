import cv2, numpy as np, math

#ti-eq.py = berisi penerapan transformasi intensitas dan ekualisasi histogram, 
# dilarang menggunakan func bawaan package.

gambar = cv2.imread("image.jpg", 0)  #nilai grayscale nya saja yg terbaca
print("Ukuran gambar: ", gambar.shape)
print("Tipe data gambar: ", gambar.dtype) 
cv2.imshow("gambar awal", gambar)

#transformasi titik (citra negatif)
kontainer_negatif = np.zeros_like(gambar)
for y in range(gambar.shape[0]):
    for x in range(gambar.shape[1]):
        asli_r = gambar[y, x]
        negatif_s = 255 - asli_r
        kontainer_negatif[y, x] = negatif_s
cv2.imshow("citra negatif", kontainer_negatif)

#transformasi log
kontainer_log = gambar.astype(np.float32)
c = 255 / math.log(256)
for y in range(gambar.shape[0]):
    for x in range(gambar.shape[1]):
        asli_r = int(gambar[y, x])
        log_s = c * math.log(1 + asli_r)
        kontainer_log[y, x] = log_s
kontainer_log = np.clip(kontainer_log, 0, 255)
kontainer_log = kontainer_log.astype(np.uint8)
cv2.imshow("citra log", kontainer_log)

#transformasi gamma
gamma = 0.5 #makin rendah makin terang (dibawah 1 untuk underexposed)
kontainer_gamma = gambar.astype(np.float32)
for y in range(gambar.shape[0]):
    for x in range(gambar.shape[1]):
        asli_r = int(gambar[y, x])
        gamma_s = 255 * (asli_r / 255) ** gamma
        kontainer_gamma[y, x] = gamma_s
kontainer_gamma = np.clip(kontainer_gamma, 0, 255)
kontainer_gamma = kontainer_gamma.astype(np.uint8)
cv2.imshow("citra gamma", kontainer_gamma)

#transformasi contrast stretching
#mencari rmin dan rmax
r_min=255 #dimulai dari terbesar, dibanding hingga terkecil
r_max=0 #dimulai dari terkecil untuk cari terbesar
for y in range(gambar.shape[0]):
    for x in range(gambar.shape[1]):
        r = int(gambar[y, x])
        if r > r_max:
            r_max = r
        if r < r_min:
            r_min = r
print("value tertinggi:", r_max)
print("value terendah:", r_min)
#proses transformasi
kontainer_contrast = gambar.astype(np.float32)
for y in range(gambar.shape[0]):
    for x in range(gambar.shape[1]):
        asli_r = int(gambar[y, x])
        stretch_s = ((asli_r - r_min) / (r_max - r_min)) * 255
        kontainer_contrast[y, x] = stretch_s
kontainer_contrast = np.clip(kontainer_contrast, 0, 255)
kontainer_contrast = kontainer_contrast.astype(np.uint8)
cv2.imshow("citra contrast", kontainer_contrast) #hasil serupa karena r_min dan r_max sudah memakai range 0-255

#transformas piecewise linear
r1, s1 = 80, 40
r2, s2 = 180, 220
kontainer_piecewise = gambar.astype(np.float32)
for y in range(gambar.shape[0]):
    for x in range(gambar.shape[1]):
        asli_r = int(gambar[y, x])
        if asli_r <= r1:
            piecewise_s = (s1 / r1) * asli_r
        elif asli_r <= r2:
            piecewise_s = ((s2 - s1) / (r2 - r1)) * (asli_r - r1) + s1
        else:
            piecewise_s = ((255 - s2) / (255 - r2)) * (asli_r - r2) + s2
        kontainer_piecewise[y, x] = piecewise_s
kontainer_piecewise = np.clip(kontainer_piecewise, 0, 255)
kontainer_piecewise = kontainer_piecewise.astype(np.uint8)
cv2.imshow("citra piecewise", kontainer_piecewise)

#transformasi threshold
threshold = 135
kontainer_threshold = gambar.astype(np.uint8)
for y in range(gambar.shape[0]):
    for x in range(gambar.shape[1]):
        asli_r = gambar[y, x]
        if asli_r < threshold:
            threshold_s = 0
        else:
            threshold_s = 255
        kontainer_threshold[y, x] = threshold_s
cv2.imshow("citra threshold", kontainer_threshold)

#ekualisasi histogram



cv2.waitKey(0)
cv2.destroyAllWindows()


