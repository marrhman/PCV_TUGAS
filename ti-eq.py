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
#cv2.imshow("citra negatif", kontainer_negatif)

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
#cv2.imshow("citra log", kontainer_log)

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


cv2.waitKey(0)
cv2.destroyAllWindows()


