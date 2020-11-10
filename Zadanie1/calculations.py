import socket
import time as t
from typing import List

host: str = '192.168.0.105'
port: int = 12345


def sector_calculator(before: List, after: List) -> float:
    """Zwraca drogę pokonaną między punktami, policzoną z twierdzenia pitagorasa"""

    delta_x = abs(before[0] - after[0])
    delta_y = abs(before[1] - after[1])
    delta_z = abs(before[2] - after[2])

    delta_xy = (delta_x ** 2 + delta_y ** 2) ** 0.5
    result = (delta_z ** 2 + delta_xy ** 2) ** 0.5

    return result


def main():
    """Oblicza średnią prędkość między punktami na podstawie drogi obliczonej w
    funkcji sector_calculator() i czasu między otrzymaniem kolejnych sygnałów
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    previous_cords: List[int] = [0, 0, 0]
    previous_time = t.perf_counter()

    while True:
        conn, addr = s.accept()
        print(f'\nUzyskano połączenie od {addr}')

        cords = conn.recv(1024)
        cords = cords.decode('utf8')

        # Sprawdzenie czy nie została wysłana wiadomość zakańczająca działanie
        if cords == 'finish':
            print('Działanie programu zakończone.')
            break

        cords = eval(cords)
        print(f'Koordynaty: {cords}')

        # Obliczenie i wypisanie czasu między sygnałami
        time = t.perf_counter() - previous_time
        print(f'czas [s]: {time}')
        previous_time = t.perf_counter()

        # Wywołanie funkcji liczącej pokonaną drogę
        sector = sector_calculator(previous_cords, cords)
        print(f'odległość [m]: {sector}')

        # Obliczenie średniej wartości prędkości z wzoru v = s / t
        velocity = sector / time
        print(f'Średnia prędkość między koordynatami [m/s]: {velocity}')

        previous_cords = cords


main()
