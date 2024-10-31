#处理img文件夹中的文件命名格式
import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.startswith('image-'):
            number = filename.split('-')[1].replace('.jpg', '')  # 去掉.jpg后缀
            new_filename = f'image-{int(number):d}.jpg'  # 生成新的文件名，去除前导零
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)

# 调用函数，将'directory'替换为你的文件夹路径
rename_files(r'D:\Python_worksapce\fdu\Tap_CHA\Test_for_login\img')