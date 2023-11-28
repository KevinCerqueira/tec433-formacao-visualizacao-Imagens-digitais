from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def read_image(image_path):
    image = Image.open(image_path).convert('L')  # Convertendo para escala de cinza
    return np.array(image)

def plot_normalized_histogram(image_array):
    # Calculando o histograma da imagem
    hist, bins = np.histogram(image_array, bins=256, range=(0, 256))
    
    # Normalizando o histograma
    hist_normalized = hist / hist.sum()

    # Plotando o histograma normalizado
    plt.bar(bins[:-1], hist_normalized, width=1)
    plt.title("Histograma Normalizado")
    plt.xlabel("Níveis de Intensidade")
    plt.ylabel("Probabilidade")
    plt.show()

if __name__ == "__main__":
    image_path = "images/white-noise-1024x701.jpg"  # Caminho para a imagem de ruído branco
    image_array = read_image(image_path)
    plot_normalized_histogram(image_array)
