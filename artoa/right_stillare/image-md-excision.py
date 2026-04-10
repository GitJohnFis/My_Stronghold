
from logging import info
from PIL import Image
from PIL.ExifTags import TAGS

def get_data(img_path):
    img = Image.open(img_path)
    exif_data = img._getexif()

    if not info:
         print("no metadata found")
         return

    for tag_id in info:
        name = TAGS.get(tag_id, tag_id)
        val = info.get(tag_id)
        print(f"{name}: {val}")

get_data("photo.jpeg")

def scrub(in_file, out_file):
    img = Image.open(in_file)
    px = list(img.get_flattened_data())

    safe = Image.new(img.mode, img.size)
    safe.putdata(px)
    safe.save(out_file)

scrub("photo.jpeg", "clean.jpg")
get_data("clean.jpg")