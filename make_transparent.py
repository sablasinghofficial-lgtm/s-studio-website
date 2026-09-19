from PIL import Image, ImageEnhance

# Open the image
img = Image.open('logo.png').convert('RGBA')
datas = img.getdata()

newData = []
for item in datas:
    r, g, b, a = item
    # Calculate brightness (luminance)
    lum = (r * 0.299 + g * 0.587 + b * 0.114)
    # The background is dark. Let's make dark pixels transparent smoothly.
    # If lum is close to 0, alpha is 0. If lum is high, alpha is 255.
    # We can map alpha directly to luminance to give a perfect 'screen' effect natively in the PNG.
    # Since the logo is golden, the colors should be kept, just alpha scaled by luminance.
    # To keep the gold color rich, we shouldn't just set alpha to luminance, we should scale the RGB up so when multiplied by alpha it looks right.
    # Or simple threshold:
    if lum < 25:
        newData.append((0, 0, 0, 0))
    else:
        # Smooth anti-aliasing
        alpha = int(min(255, (lum - 25) * 3))
        newData.append((r, g, b, alpha))

img.putdata(newData)
img.save('logo_transparent.png', 'PNG')
print("Made transparent logo")
