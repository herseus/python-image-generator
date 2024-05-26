from PIL import Image, ImageDraw, ImageFont # type: ignore

content = "Bar"
font = "path-to-font"
outputPath = "path-to-output"
outputFile = "icon.png"

try:
    image = Image.new('RGBA', (80, 80), (211, 141, 95, 255))
    d = ImageDraw.Draw(image)
    # d.rectangle([(0, 1600), (2000, 2400)], (255, 127, 42, 255))
    fnt = ImageFont.truetype(font, 40)
    d.text((5,15), content, font=fnt, fill=(0,0,0,255))
    print("Generating " + outputFile)
    image.save(outputPath + outputFile)
except:
    pass
