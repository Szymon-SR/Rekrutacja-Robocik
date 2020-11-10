import random
from time import sleep
import socket
from typing import List

host: str = '192.168.0.105'
port: int = 12345


def starting_coordinates() -> None:
    """Wysyła startowe koordynaty do programu calculations.py"""

    cords: List[int] = [0, 0, 0]
    cords: str = str(cords)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(cords.encode('utf8'))
    s.close()


def finish() -> None:
    """Wysyła informację finish_message która kończy działanie calculations.py"""

    finish_message: str = 'finish'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(finish_message.encode('utf8'))
    s.close()


def main(t: float, n: int) -> None:
    """Wywołuje starting_coordinates(), wysyła n sygnałów z losowymi
    koordynatami co t sekund, wywołuje finish()
    """

    # Określamy wymiary basenu/przestrzeni w której porusza się łódź, losowane
    # koordynaty będą w tym zakresie. Przyjmujemy wartości w metrach
    pool_lenght: int = 150
    pool_width: int = 50
    pool_depth: int = 20

    starting_coordinates()

    sleep(t)

    # Losujemy i wysyłamy koordynaty n razy
    for i in range(n):
        x: int = random.randint(0, pool_lenght)
        y: int = random.randint(0, pool_width)
        z: int = random.randint(0, pool_depth)

        print(f'Obecne koordynaty: {x}, {y}, {z}')

        cords: List[int] = [x, y, z]

        # zamieniamy na typ string aby móc przesłać
        cords: str = str(cords)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(cords.encode('utf8'))

        sleep(t)

    s.close()
    finish()


# Pierwszy argument to liczba sekund między sygnałami, drugi to liczba sygnałów
main(3, 5)
