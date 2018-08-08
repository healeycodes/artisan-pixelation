import argparse
from PIL import Image

parser = argparse.ArgumentParser(
    description='Create artisanal pixelated images.')
# image
parser.add_argument('img', help='A required image path.')
# resolution
parser.add_argument('--width', nargs='?', type=int, default=22)
# how much of the original to destroy - higher is more destruction
parser.add_argument('--density', nargs='?', type=int, default=3)
# parse args
args = parser.parse_args()
img = Image.open(args.img)
width = args.width
density = args.density

# setup chunk size and block mapping
chunk_size = int(img.size[0] / width)
# set height relative to width for non-square images
height = int(img.size[1] / img.size[0] * width)
# ensure we keep as much entropy as possible
if height % density != 0:
    height += density - height % density

# create final image object
pixelated_img = Image.new(
    'RGB', (width // density * chunk_size, height // density * chunk_size))

# split source image into chunks
chunks = []
for i in range(0, height, density):  # for each row
    row = []
    for j in range(0, width, density):  # for each column
        left = j * chunk_size
        upper = i * chunk_size
        right = left + chunk_size
        lower = upper + chunk_size
        row.append(img.crop((left, upper, right, lower)))
    chunks.append(row)

# place chunks into final image object
y = 0
for row in chunks:
    x = 0
    for image in row:
        pixelated_img.paste(image, (x, y))
        x += chunk_size
    y += chunk_size

# show final image
pixelated_img.show()


def show_side_by_side(scale=1):

    # scale pixelated image
    pixelated_img = pixelated_img.resize(
        map(lambda x: x * scale, pixelated_img.size), Image.ANTIALIAS)

    # scale source image
    shrunk_img = img.resize(pixelated_img.size, Image.ANTIALIAS)

    # show images side by side
    width_sum = sum([pixelated_img.size[0], shrunk_img.size[0]])
    height_max = max([pixelated_img.size[1], shrunk_img.size[1]])
    combined_img = Image.new('RGB', (width_sum, height_max))
    combined_img.paste(shrunk_img, [0, 0])
    combined_img.paste(pixelated_img, [shrunk_img.size[0], 0])
    combined_img.show()
