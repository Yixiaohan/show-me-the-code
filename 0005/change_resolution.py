import glob
from PIL import Image


def change_resolution(patterns):
    iphone_width, iphone_height = 760, 1334
    pictures = []
    for pattern in patterns:
        pictures.extend(glob.glob(pattern))
    print(pictures)
    for picture in pictures:
        img = Image.open(picture)
        min_width = img.size[0] if iphone_width > img.size[0] else iphone_width
        min_height = img.size[1] if iphone_height > img.size[1] else iphone_height
        dist = img.resize((min_width, min_height), Image.ANTIALIAS)
        dist.save("iphone6_" + picture)


if __name__ == '__main__':
    change_resolution(("*.jpg", "*.png"))
