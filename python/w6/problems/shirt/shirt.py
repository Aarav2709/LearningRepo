import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_extensions = [".jpg", ".jpeg", ".png"]

input_file = sys.argv[1].lower()
output_file = sys.argv[2].lower()

input_ext = None
output_ext = None

for ext in valid_extensions:
    if input_file.endswith(ext):
        input_ext = ext
    if output_file.endswith(ext):
        output_ext = ext

if input_ext is None:
    sys.exit("Invalid input")
if output_ext is None:
    sys.exit("Invalid output")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")

input_image = ImageOps.fit(input_image, shirt.size)

input_image.paste(shirt, shirt)

input_image.save(sys.argv[2])
