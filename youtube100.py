f = open('100.txt')
line = f.readline()
while line:
	text = line
	line = f.readline()
	from PIL import Image, ImageDraw, ImageFont
	img = Image.new('RGB', (1920, 1080), color = (0,128,0))
	d = ImageDraw.Draw(img)
	fnt = ImageFont.truetype('/Library/Fonts/ヒラギノ角ゴシック W6.ttc', 40)
	size = d.textsize(text.strip(), font=fnt)
	d.rectangle((30,1010, 30 + size[0], 1010 + size[1]), fill='black')
	d.text((30,1010), text.strip(), font=fnt, fill=(255,255,255,128))
	img.save(text.strip() + '.jpg')
f.close()