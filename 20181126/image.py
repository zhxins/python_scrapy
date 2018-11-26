from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

image = Image.new('RGB', (150,30),'red')
image.save(open('test.png','wb'), 'png')