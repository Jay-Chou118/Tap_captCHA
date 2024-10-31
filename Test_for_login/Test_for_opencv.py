import cv2

# 读取图片
img = cv2.imread(r'D:\Python_worksapce\fdu\Tap_CHA\Test_for_login\captCHA_img\007.jpg')

# 将图片转换为灰度
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 保存灰度图片
cv2.imwrite('output_gray.jpg', gray_img)