import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


num = ''.join(random.sample('\
    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 4))


def random_col():
    return (random.randint(50, 150),
            random.randint(100, 200), random.randint(100, 200))


def make(strs, width=400, height=200):
    im = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('verdana.ttf', width // 4)
    font_width, font_height = font.getsize(strs)
    strs_len = len(strs)
    x = (width - font_width) // 2
    y = (height - font_height) // 2
    total_dex = 0
    for c in strs:
        draw.text((x, y), c, random_col(), font)
        temp = random.randint(-20, 30)
        total_dex += temp
        draw = ImageDraw.Draw(im)
        x += font_width / strs_len
    im = im.rotate(total_dex)
    draw = ImageDraw.Draw(im)
    draw.line([
        (random.randint(0, width // 4), random.randint(0, height // 4)),
        (random.randint(width // 4 * 3, width), random.randint(height // 4 * 3, height))],
        fill=random_col(), width=width // 80)
    draw.line([
        (random.randint(0, width // 4), random.randint(height // 4 * 3, height)),
        (random.randint(width // 4 * 3, width), random.randint(0, height // 4))],
        fill=random_col(), width=width // 60)
    draw.line([
        (random.randint(width // 4 * 3, width),
         random.randint(height // 4 * 3, height)),
        (random.randint(width // 3 * 2, width), random.randint(0, height // 3))],
        fill=random_col(), width=width // 60)
    for x in range(width):
        for y in range(height):
            col = im.getpixel((x, y))
            if col == (255, 255, 255) or col == (0, 0, 0):
                draw.point((x, y), fill=random_col())
    im = im.filter(ImageFilter.BLUR)
    im.save('out.jpg')


if __name__ == '__main__':
    make(num)
