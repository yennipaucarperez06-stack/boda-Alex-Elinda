import os
from PIL import Image

def convert_images():
    extensions = ('.png', '.jpg', '.jpeg')
    files = [f for f in os.listdir('.') if f.lower().endswith(extensions)]
    
    print(f"Encontradas {len(files)} imagenes para convertir.")
    
    for file in files:
        try:
            filename, ext = os.path.splitext(file)
            output_file = f"{filename}.webp"
            
            # Skip if webp already exists and is newer
            if os.path.exists(output_file):
                continue
                
            print(f"Convirtiendo {file} a {output_file}...")
            with Image.open(file) as img:
                img.save(output_file, 'webp', quality=80)
            print(f"OK: {output_file}")
        except Exception as e:
            print(f"Error convirtiendo {file}: {e}")

if __name__ == "__main__":
    convert_images()
