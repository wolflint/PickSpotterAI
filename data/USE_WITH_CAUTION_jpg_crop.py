#!/usr/bin/env python3

import sys
from PIL import Image

# Process all input files so we only incur Python startup overhead once
for filename in sys.argv[1:]:
   print(f'Processing: {filename}')
   img = Image.open(filename)
   print(img.size)
   h, w = img.size
   img = img.crop((0, 0, w, h - 400))
   img.save(filename)
