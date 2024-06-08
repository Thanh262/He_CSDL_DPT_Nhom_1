import cv2
import numpy as np
from skimage.feature import hog

def perform_search(image):
    # xử lý ảnh
    img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    hog_features = hog(img, block_norm='L2-Hys', pixels_per_cell=(16, 16))
    
    # so sánh hog feature với thmubnail
    
    # tìm kiếm
    
    # trả về list các video
    
    return []