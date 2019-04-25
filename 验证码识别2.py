import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr
from PIL import Image
def img_to_text():
    text_list = []
    for img in ['app.png','d.png']:
        image = Image.open(img)
        result = tesserocr.image_to_text(image)
        text_list.append(result.strip())
    return text_list

if __name__ == '__main__':
    text = img_to_text()
    print(text)
















