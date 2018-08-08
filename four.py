import argparse
from PIL import Image

parser = argparse.ArgumentParser(
    description='Create artisanal pixelated images.')
# image
parser.add_argument('img', help='A required image path.')
# resolution
parser.add_argument('--resolution', nargs='?', type=int, default=22)
# parse args
args = parser.parse_args()
img = Image.open(args.img)
resolution = args.resolution


