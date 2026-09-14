import cv2, numpy as np

#Intro.py = berisi code read image, show image, filter color image, filter color video
#==FILTER GAMBAR==#
gambar = cv2.imread("image.jpg")
blue_channel = gambar[:,:,0]
green_channel = gambar[:,:,1]
red_channel = gambar[:,:,2]
black_channel = np.zeros_like(red_channel)

gambar_baru = cv2.merge([red_channel, green_channel, blue_channel])
cv2.imshow("Filter Warna Ketukar", gambar_baru)

cv2.waitKey(0)
cv2.destroyAllWindows()

#==FILTER VIDEO==#
video_cam = cv2.VideoCapture(0)
frame_order = 0
while True:
    safe_status, frame = video_cam.read() #status baca true/false, frame = array data video per frame
    print(safe_status)
    if not safe_status:
        break

    blue_channel = frame[:,:,0]
    green_channel = frame[:,:,1]
    red_channel = frame[:,:,2]
    black_channel = np.zeros_like(red_channel)

    filter_order = frame_order % 200
    if filter_order < 50:
        frame_baru = cv2.merge([blue_channel, black_channel, black_channel])
    elif filter_order < 100:
        frame_baru = cv2.merge([black_channel, green_channel, black_channel])
    elif filter_order < 150:
        frame_baru = cv2.merge([black_channel, black_channel, red_channel])
    else:
        frame_baru = cv2.merge([red_channel, green_channel, blue_channel])

    cv2.imshow("Filter Warna", frame_baru)
    frame_order += 1

    quit = cv2.waitKey(1) & 0xFF
    if quit == ord('q'):
        break

video_cam.release()
cv2.destroyAllWindows()