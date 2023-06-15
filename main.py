#!/usr/bin/env python

from PIL import Image
import argparse

def rotate_image(image, angle):
    rotated_image = image.rotate(angle)
    return rotated_image

def flip_image(image):
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_image

def invert_image(image):
    inverted_image = Image.eval(image, lambda x: 255 - x)
    return inverted_image

def main():
    # Configurando o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Processa uma imagem.')
    parser.add_argument('imagem', type=str, help='Caminho para a imagem')
    parser.add_argument('-r', '--rotacionar', type=float, default=0.0, help='Ângulo de rotação em graus (sentido anti-horário)')
    parser.add_argument('-e', '--espelhar', action='store_true', help='Espelhar a imagem')
    parser.add_argument('-i', '--inverter', action='store_true', help='Inverter as cores da imagem')
    
    # Obtendo os argumentos da linha de comando
    args = parser.parse_args()

    # Abrindo a imagem
    image = Image.open(args.imagem)

    # Realizando as operações conforme os argumentos fornecidos
    if args.rotacionar:
        image = rotate_image(image, args.rotacionar)
    if args.espelhar:
        image = flip_image(image)
    if args.inverter:
        image = invert_image(image)

    # Salvando a imagem processada
    image.save(f'new_{args.imagem}')
    print(f'Imagem processada e salva como "new_{args.imagem}".')

if __name__ == '__main__':
    main()

