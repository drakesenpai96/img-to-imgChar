from PIL import Image, ImageDraw, ImageFont

import math


def gen_img(path_img, path_saida):
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

    charArray = list(chars)
    charLength = len(charArray)

    interval = charLength / 380

    scaleFactor = 1

    oneCharWidth = 10
    oneCharHeight = 28

    def getChar(inputInt):
        return charArray[math.floor(inputInt * interval)]

    text_file = open(fr'{path_saida}\output.txt', 'w')

    im = Image.open(path_img)

    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = im.size

    im = im.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth / oneCharHeight))), Image.NEAREST)

    width, height = im.size

    pix = im.load()

    outputImg = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0 ,0))
    d = ImageDraw.Draw(outputImg)

    for i in range(height):
        for j in range(width):
            
            r, g, b, a = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text((j * oneCharWidth, i * oneCharHeight), getChar(h), font=fnt, fill=(r, g, b))

        text_file.write('\n')

    outputImg.save(fr'{path_saida}\output.png')

gen_img(r'C:\Users\isaac.bittencourt\Downloads\img_test.jpg', r'C:\Users\isaac.bittencourt\Downloads')
