def finishing_move(before_tile: int, after_tile: int) -> str:
    """Zmieniamy numer pola według moich oznaczeń liczbowych, na oznaczenia
    które występują na szachownicy i są nam potrzebne do outputu programu"""

    switcher = {
        0: 'a8',
        1: 'b8',
        2: 'c8',
        3: 'd8',
        4: 'e8',
        5: 'f8',
        6: 'g8',
        7: 'h8',
        10: 'a7',
        11: 'b7',
        12: 'c7',
        13: 'd7',
        14: 'e7',
        15: 'f7',
        16: 'g7',
        17: 'h7',
        20: 'a6',
        21: 'b6',
        22: 'c6',
        23: 'd6',
        24: 'e6',
        25: 'f6',
        26: 'g6',
        27: 'h6',
        30: 'a5',
        31: 'b5',
        32: 'c5',
        33: 'd5',
        34: 'e5',
        35: 'f5',
        36: 'g5',
        37: 'h5',
        40: 'a4',
        41: 'b4',
        42: 'c4',
        43: 'd4',
        44: 'e4',
        45: 'f4',
        46: 'g4',
        47: 'h4',
        50: 'a3',
        51: 'b3',
        52: 'c3',
        53: 'd3',
        54: 'e3',
        55: 'f3',
        56: 'g3',
        57: 'h3',
        60: 'a2',
        61: 'b2',
        62: 'c2',
        63: 'd2',
        64: 'e2',
        65: 'f2',
        66: 'g2',
        67: 'h2',
        70: 'a1',
        71: 'b1',
        72: 'c1',
        73: 'd1',
        74: 'e1',
        75: 'f1',
        76: 'g1',
        77: 'h1',
    }

    before = switcher.get(before_tile)
    after = switcher.get(after_tile)

    return f'{before} - {after}'
