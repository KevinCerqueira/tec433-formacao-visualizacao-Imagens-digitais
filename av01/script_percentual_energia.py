from PIL import Image
import numpy as np
import os

def count_white_pixels(image_path):
    image = Image.open(image_path).convert('L')  # Convertendo para escala de cinza
    np_image = np.array(image)

    # Contando os pixels brancos
    white_pixels = np.sum(np_image == 255)
    total_pixels = np_image.shape[0] * np_image.shape[1]

    return white_pixels, total_pixels

def main():
    folder_path = "./images"  # Pasta contendo as imagens TIFF
    total_white_pixels = 0
    total_pixels = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".tif"):
            image_path = os.path.join(folder_path, filename)
            white_pixels, img_total_pixels = count_white_pixels(image_path)

            total_white_pixels += white_pixels
            total_pixels += img_total_pixels

            if img_total_pixels > 0:
                region_percentage = (white_pixels / img_total_pixels) * 100
                print(f"Imagem {filename}: {white_pixels} pixels brancos de um total de {img_total_pixels} pixels. Percentual: {region_percentage:.2f}%")
            else:
                print(f"Imagem {filename}: Nenhum pixel foi processado.")

    if total_pixels == 0:
        print("Nenhum pixel foi processado para todas as imagens. Verifique se o diretório das imagens está correto.")
        return

    overall_percentage = (total_white_pixels / total_pixels) * 100
    print(f"Percentual relativo da energia elétrica total para todas as regiões: {overall_percentage:.2f}%")

if __name__ == "__main__":
    main()
