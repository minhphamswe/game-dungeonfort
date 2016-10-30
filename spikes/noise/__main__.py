from array import array
from io import BytesIO

from PIL import Image

def main():
  nx = 200
  ny = 100

  # Construct image buffer
  raw_buffer = bytearray()
  for j in range(ny, 0, -1):
    for i in range(nx):
      r = float(i)/float(nx)
      g = float(j)/float(ny)
      b = 0.2

      ir = int(255.99 * r)
      ig = int(255.99 * g)
      ib = int(255.99 * b)

      raw_buffer.append(ir)
      raw_buffer.append(ig)
      raw_buffer.append(ib)

  # Save image buffer to file
  image_buffer = bytes(raw_buffer)
  im = Image.frombytes('RGB', (nx, ny), image_buffer)
  im.save('./test_image.png', 'PNG')

main()
