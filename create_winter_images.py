from PIL import Image, ImageEnhance, ImageFilter
import os

# Папка жолы
folder = r"c:\Users\User\Desktop\TARX"

# Өңдейтін суреттер
images = [
    ("river.png", "winter_river.png"),
    ("mountain_cave.png", "winter_mountain_cave.png"),
    ("steppe.png", "winter_steppe.png")
]

for original, winter in images:
    try:
        # Суретті ашу
        img_path = os.path.join(folder, original)
        img = Image.open(img_path)
        
        # Жарықтықты арттыру (ашық күн эффекті)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.2)
        
        # Контрастты арттыру
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.15)
        
        # Көк реңк қосу (суық атмосфера)
        pixels = img.load()
        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))[:3]
                # Көк реңкті күшейту, қызыл реңкті азайту
                r = int(r * 0.95)
                b = int(min(255, b * 1.1))
                img.putpixel((x, y), (r, g, b))
        
        # Сақтау
        output_path = os.path.join(folder, winter)
        img.save(output_path)
        print(f"Saved: {winter}")
        
    except Exception as e:
        print(f"Error with {original}: {e}")

print("\nAll images processed!")
