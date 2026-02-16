import sys
from random import randint
from math import floor, ceil

from PIL import Image

dark = Image.open(sys.argv[1])
light = Image.open(sys.argv[2])

def contrastify(pixel, color):
	if pixel[3] > 0:
		return color
	else:
		return (0, 0, 0, 0)

pixel_count = dark.width * dark.height

dark_count = floor(pixel_count / 2)
light_count = ceil(pixel_count / 2)

for y in range(0, dark.height):
	for x in range(0, dark.width):
		c = (x, y)

		v = (0, 0, 0, 0)

		d = randint(0, pixel_count)

		if d < dark_count:
			v = contrastify(dark.getpixel(c), (7, 7, 9, 255))
			dark_count -= 1
		elif d < dark_count + light_count:
			v = contrastify(light.getpixel(c), (251, 251, 251, 255))
			light_count -= 1

		dark.putpixel(c, v)

		pixel_count -= 1

dark.save(sys.argv[3])
