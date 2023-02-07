import sys
import os
import pygame

from mapapi import get_map

MAP_FILE = "map.png"


class RequestException(Exception):
    pass


class SaveFileExeption(Exception):
    pass


def get_and_save_image(coordinates, map_type='map', add_params=None):
    response = get_map(coordinates, map_type, add_params=add_params)

    if not response:
        raise SaveFileExeption(f'Http статус: {response.status_code} ({response.reason})\n{response.url}')
        # Запишем полученное изображение в файл.
    map_file = MAP_FILE

    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        raise SaveFileExeption(f'"Ошибка записи временного файла: {ex}')


def main():
    coordinates = '151.21531815767764,-33.85673985210281'
    z = 17
    try:
        get_and_save_image(coordinates, map_type='sat', add_params={'z': z})
    except (RequestException, SaveFileExeption) as e:
        print(e)
        exit(0)
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    clock = pygame.time.Clock()
    fps = 60
    running = True

    screen.blit(pygame.image.load(MAP_FILE), (0, 0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_PAGEUP, pygame.K_KP_PLUS, pygame.K_PAGEDOWN, pygame.K_KP_MINUS):
                    if event.key in (pygame.K_PAGEUP, pygame.K_KP_PLUS):
                        print('+')
                        change = 1
                    else:
                        print('-')
                        change = -1
                    tmp_z = z + change
                    while tmp_z <= 25:
                        try:
                            get_and_save_image(coordinates, map_type='sat', add_params={'z': tmp_z})
                        except (RequestException, SaveFileExeption):
                            tmp_z += change

                        else:
                            z = tmp_z
                            break

                    print(z)
                    screen.blit(pygame.image.load(MAP_FILE), (0, 0))
                    pygame.display.flip()

        # pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(MAP_FILE)


if __name__ == '__main__':
    main()
