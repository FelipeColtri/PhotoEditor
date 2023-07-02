#!/usr/bin/env python

from PIL import Image, ImageFilter
import argparse

# Função de rotacionar a imagem 
def image_rotate(image, angle):
    return image.rotate(angle)

# Função de espelhar a imagem na horizontal  
def image_flip_horizontal(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

# Função de espelhar a imagem na vertical 
def image_flip_vertical(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)

# Função de transpor a imagem [muda entre paisagem e retrato]
def image_transpose(image):
    return image.transpose(Image.TRANSPOSE)

# Função de transpor na e espelhar ao mesmo tempo 
def image_transverse(image):
    return image.transpose(Image.TRANSVERSE)

# Função de inverter a cor da imagem
def image_invert(image):
    return Image.eval(image, lambda x: 255 - x)

# Função de descolorir para tons de cinza a imagem 
def image_grayscale(image):
    return image.convert("L")

def image_filter_blur(image):
    return image.filter(ImageFilter.BLUR)

def image_filter_contour(image):
    return image.filter(ImageFilter.CONTOUR)

def image_filter_emboss(image):
    return image.filter(ImageFilter.EMBOSS)

def main():
    # Configurando o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Photo Editor v0.1.')
    parser.add_argument('imagem', type=str, help='Caminho da imagem')
    parser.add_argument('-r', '--rotate', type=float, default=0.0, help='Ângulo de rotação em graus (sentido anti-horário)')
    parser.add_argument('-fh', '--flip_horizontal', action='store_true', help='Espelhar a imagem na horizontal')
    parser.add_argument('-fv', '--flip_vertical', action='store_true', help='Espelhar a imagem na vertical')
    parser.add_argument('-tp', '--transpose', action='store_true', help='Transpõe a imagem')
    parser.add_argument('-tv', '--transverse', action='store_true', help='Transpõe e espelha a imagem')
    parser.add_argument('-i', '--inverter', action='store_true', help='Inverter as cores da imagem')
    parser.add_argument('-g', '--gray_scale', action='store_true', help='Converte a imagem em tons de cinza')
    parser.add_argument('-blur', '--filter_blur', action='store_true', help='Filtro BLUR')
    parser.add_argument('-contour', '--filter_contour', action='store_true', help='Filtro CONTOUR')
    parser.add_argument('-emboss', '--filter_emboss', action='store_true', help='Filtro EMBOSS')
    
    # Obtendo os argumentos da linha de comando
    args = parser.parse_args()

    # Abrindo a imagem
    image = Image.open(args.imagem)

    # Realizando as operações conforme os argumentos fornecidos
    if args.rotate:
        image = image_rotate(image, args.rotate)
    if args.flip_horizontal:
        image = image_flip_horizontal(image)
    if args.flip_vertical:
        image = image_flip_vertical(image)
    if args.transpose:
        image = image_transpose(image)
    if args.transverse:
        image = image_transverse(image)
    if args.inverter:
        image = image_invert(image)
    if args.gray_scale:
        image = image_grayscale(image)
    if args.filter_blur:
        image = image_filter_blur(image)
    if args.filter_contour:
        image = image_filter_contour(image)
    if args.filter_emboss:
        image = image_filter_emboss(image)

    # Salvando a imagem processada
    new_image = "new_" + args.imagem
    image.save(new_image)
 
    # Informa mensagem ao usuário 
    print(f'Imagem salva como "{new_image}".')
    
    # Abre o visualizador de imagem 
    image.show()

if __name__ == '__main__':
    main()

