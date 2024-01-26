#Sources: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097 added code for a bounding box and also displaying the dominant color

import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans

cap = cv.VideoCapture(0)
rectangle = (650, 300, 600, 600)
while(1):
    # Take each frame
    _, frame = cap.read()

    x, y, w, h = rectangle
    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cropped = frame[y:y+h, x:x+w].reshape((-1, 3))

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(cropped)

    # Get the dominant color
    dominant_color = kmeans.cluster_centers_[0].astype(int)

    cv.putText(frame, f'Dominant Color: {dominant_color}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv.imshow('frame',frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()