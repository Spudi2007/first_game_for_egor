from PIL import Image
imgname = '2'
while imgname != '1':
	imgname = input() + '.png'
	img = Image.open(imgname)
	img = img.convert("RGBA")
	datas = img.getdata()

	newData = []
	for item in datas:
	    # if (item[0] == 255 and item[1] == 255 and item[2] == 255) or (item[0] == 255 and item[1] == 30 and item[2] == 30) or (item[0] == 30 and item[1] == 30 and item[2] == 255) or (item[0] == 30 and item[1] == 255 and item[2] == 30):
	    #     newData.append((255, 255, 255, 0))
	    # else:
	    #     newData.append(item)
	    if item[3]:
	    	newData.append((255, 255, 255, 255))
	    else:
	    	newData.append(item)
	img.putdata(newData)
	img.save(imgname, "PNG")
