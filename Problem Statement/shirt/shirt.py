from PIL import Image,ImageOps
import sys
import os

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    extension = [".jpg", ".jpeg", ".png"]
    input_path = os.path.splitext(sys.argv[1])
    output_path = os.path.splitext(sys.argv[2])
    if output_path[1].lower() not in extension:
        sys.exit("Invalid output")
    elif input_path[1].lower() != output_path[1].lower():
        sys.exit("Input and output have different extensions")
    else:
        image_before = sys.argv[1]
        image_after = sys.argv[2]

try:
    shirt = Image.open("shirt.png")
    with Image.open(image_before) as input:
        input_cropped = ImageOps.fit(input, shirt.size)
        input_cropped.paste(shirt, mask=shirt)
        input_cropped.save(image_after)
except FileNotFoundError:
    sys.exit("Input does not exist")




