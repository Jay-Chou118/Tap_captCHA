import cv2
import pytesseract
from PIL import Image

print("hello?")
image_path = r"D:\Python_worksapce\fdu\Tap_CHA\Test_for_login\captCHA_img\001.jpg"  # 替换为图片的实际路径
image = Image.open(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用二值化（可以尝试不同的二值化方法）
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# 也可以尝试自适应二值化：
# binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 放大图片（例如放大2倍）
binary = cv2.resize(binary, (binary.shape[1] * 2, binary.shape[0] * 2))

# 保存处理后的图片以供调试
cv2.imwrite('processed_image.jpg', binary)

# 使用 pytesseract 进行 OCR 识别
text = pytesseract.image_to_string(Image.fromarray(binary), lang='chi_sim')

text = pytesseract.image_to_string(image, lang='chi_sim')


print(text)