import math
from ctb import place

OUR_RANGE = 5
# cube
for i in range(OUR_RANGE):
	place(i, 0, 0)
	place(0, i, 0)
	place(0, 0, i)
	place(0, i, OUR_RANGE-1)
	place(i, 0, OUR_RANGE-1)
	place(i, OUR_RANGE-1, 0)
	place(0, OUR_RANGE-1, i)
	place(OUR_RANGE-1, i, 0)
	place(OUR_RANGE-1, 0, i)
	place(OUR_RANGE-1, OUR_RANGE-1, i)
	place(i, OUR_RANGE-1, OUR_RANGE-1)
	place(OUR_RANGE-1, i, OUR_RANGE-1)

# square
for i in range(OUR_RANGE):
	place(i, 0, 0)
	place(0, i, 0)
	place(i, OUR_RANGE - 1, 0)
	place(OUR_RANGE - 1, i, 0)

# circle
BLOCKS = 40

for position in range(BLOCKS):
  radians = 2 * math.pi * position / BLOCKS
  x = OUR_RANGE * math.cos(radians)
  y = OUR_RANGE * math.sin(radians)
  place(x, y, 0)
