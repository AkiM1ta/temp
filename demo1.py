import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def generate_captcha_string(number=4):
    source = tuple(string.ascii_letters + string.digits)
    return ''.join(random.sample(source, number))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


if __name__ == "__main__":
    res = generate_captcha_string()
    print(res)
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    # font = ImageFont.truetype('GreatVibes-Regular.otf', 36)
    font = ImageFont.truetype('BEBAS___.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), res, font=font, fill=rndColor2())
    # 模糊:
    # image = image.filter(ImageFilter.BLUR)
    image.save('code4.jpg', 'jpeg')
