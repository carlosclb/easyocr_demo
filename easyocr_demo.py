import easyocr

# 定义参数变量
options_api = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

reader = easyocr.Reader(['ch_sim', 'en'], model_storage_directory=r'C:\Users\demo\.EasyOCR\model', gpu=False)
result = reader.readtext('33.png')
for i in result:
    print(i[1])
