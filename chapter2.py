from PIL import Image
from PIL import ImageFilter
image = Image.open('refal.jpg')
image.save('result.jpg')
cropped_image = image.crop((10, 10, 200, 100))
cropped_image.save('cropped_result.jpg')
resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')