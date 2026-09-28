import cv2, numpy as np

def konvolusi(f, w, tepi="replicate"):
    """Konvolusi f dengan kernel w, ditulis eksplisit agar mekanikanya terlihat.
    Untuk pemakaian nyata gunakan cv2.filter2D yang jauh lebih cepat."""
    m, n = w.shape
    a, b = m // 2, n // 2
    # Langkah 1: putar kernel 180 derajat -> inilah yang membedakan
    # konvolusi dari korelasi
    w_putar = np.flipud(np.fliplr(w))
    # Langkah 2: lebarkan citra supaya tepi punya tetangga
    mode = {"zero": "constant", "replicate": "edge", "reflect": "reflect"}[tepi]
    f_pad = np.pad(f.astype(np.float64), ((a, a), (b, b)), mode=mode)
    # Langkah 3: geser jendela ke seluruh posisi
    g = np.zeros(f.shape, dtype=np.float64)
    for x in range(f.shape[0]):
        for y in range(f.shape[1]):
            jendela = f_pad[x:x + m, y:y + n] # ambil ketetanggaan
            g[x, y] = np.sum(jendela * w_putar) # jumlah hasil kali
    return g

def ke_uint8(g):
    """Bulatkan setengah ke atas lalu potong ke rentang yang sah."""
    return np.clip(np.floor(g + 0.5), 0, 255).astype(np.uint8)

f = np.array([[10, 10, 10, 10, 10],
              [10, 50, 50, 50, 10],
              [10, 50, 150, 50, 10],
              [20, 40, 40, 40, 20],
              [20, 20, 20, 20, 20]], dtype=np.float64)
w = np.ones((3, 3), np.float64) / 9.0

print(np.round(konvolusi(f, w, tepi="zero"), 2))
# Versi OpenCV. Perhatikan: filter2D menghitung KORELASI,
# jadi untuk kernel tak simetris kernelnya perlu dibalik lebih dulu.
hasil_cv = cv2.filter2D(f, -1, cv2.flip(w, -1), borderType=cv2.BORDER_REPLICATE)