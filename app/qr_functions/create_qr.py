import qrcode

def generate_qrcode(data, filename):
	img = qrcode.make(data)
	img.save(f"./qrcodes/{filename}")

#generate_qrcode("https://instagram.com", "ig_com.png")
