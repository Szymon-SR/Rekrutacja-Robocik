from board import input_board
from move_translator import finishing_move


def get_all_tiles() -> list:
    """Zwraca oznaczenia wszystkich występujących na szachownicy miejsc, miejsa
    są liczbą dwucyfrową gdzie pierwsza cyfra to numer rzęcu a druga cyfra to
    numer kolumny. (na przykład: 4, 57)
    """
    all_tiles = []
    for i in range(8):
        for j in range(8):
            all_tiles.append(i*10 + j)

    return all_tiles


def get_empty_tiles(board: list) -> list:
    """Zapisuje każde niezajęte pole na planszy i zwraca wszystkie w liście"""
    empty_tiles = []
    for r, row in enumerate(board):
        for t, tile in enumerate(row):
            if tile == '--':
                tile_number: int = r*10 + t
                empty_tiles.append(tile_number)

    return empty_tiles


def get_not_own_tiles(board: list, is_white: bool) -> list:
    """Zwraca w liście pola puste, lub takie na których jest figura przeciwnika,
    w zależności od tego czy jest ruch białych czy czarnych"""
    not_own_tiles = []

    if is_white:
        opponent_color = 'b'
    else:
        opponent_color = 'w'

    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == '--' or tile[0] == opponent_color:
                s: int = i*10 + j
                not_own_tiles.append(s)

    return not_own_tiles


def rook_moves(board: list, rook_pos: int, white_turn: bool) -> list:
    """Zwraca listę możliwych ruchów wieży (o określonej pozycji)
    na wolne pola, lub pola gdzie może zbić"""
    moves = []
    position_changes = [-10, -1, 1, 10]

    for change in position_changes:
        move = rook_pos
        while True:

            move = move + change

            # dodajemy wszystkie wolne pola po kolei
            if move in get_empty_tiles(board):
                moves.append(move)

            # jeśli natrafimy na figurę przeciwnika, możemy ją zbić ale nie możemy
            # ruszać się dalej (nie możemy dodawać kolejnych pól)
            elif move in get_not_own_tiles(board, white_turn):
                moves.append(move)
                break

            # jeśli natrafimy na swoją figurę, nie możemy iść w tę stronę
            else:
                break

    return moves


def knight_moves(board: list, knight_pos: int, white_turn: bool) -> list:
    """Zwraca listę możliwych ruchów skoczka (o określonej pozycji)
    na wolne pola, lub pola gdzie może zbić"""

    k = knight_pos
    moves = []
    all_moves = [k - 21, k - 19, k - 8, k + 12, k + 21, k + 19, k + 8, k - 12]

    for move in all_moves:
        if move in get_not_own_tiles(board, white_turn):
            moves.append(move)

    return moves


def bishop_moves(board: list, bishop_pos: int, white_turn: bool) -> list:
    """Zwraca listę możliwych ruchów gońca (o określonej pozycji)
    na wolne pola, lub pola gdzie może zbić"""
    moves = []
    position_changes = [-11, -9, 9, 11]

    for change in position_changes:
        move = bishop_pos
        while True:

            move = move + change

            # dodajemy wszystkie wolne pola po kolei
            if move in get_empty_tiles(board):
                moves.append(move)

            # jeśli natrafimy na figurę przeciwnika, możemy ją zbić ale nie możemy
            # ruszać się dalej (nie możemy dodawać kolejnych pól)
            elif move in get_not_own_tiles(board, white_turn):
                moves.append(move)
                break

            else:
                break

    return moves


def queen_moves(board: list, queen_pos: int, white_turn: bool) -> list:
    """Zwraca listę możliwych ruchów hetmana o określonej pozycji, czyli ruchy
    które mógłby wykonać goniec i ruchy które mogłaby wykonać wieża """
    moves = []
    rook = rook_moves(board, queen_pos, white_turn)
    bishop = bishop_moves(board, queen_pos, white_turn)

    for number in rook:
        moves.append(number)

    for number in bishop:
        moves.append(number)

    return moves


def pawn_moves(board: list, pawn_pos: int, white_turn: bool) -> list:
    """Zwraca listę możliwych ruchów piona o określonej pozycji"""
    moves = []

    # Tworzymy listę wszystkich pól na których piony zaczynają, mogą się z nich
    # poruszyć o dwa pola zamiast jednego
    if white_turn:
        starting_positions = [60 + i for i in range(8)]

        move = pawn_pos - 10
        if move in get_empty_tiles(board):
            moves.append(move)

            if pawn_pos in starting_positions:
                double_move = pawn_pos - 20
                moves.append(double_move)

    else:
        starting_positions = [10 + i for i in range(8)]

        move = pawn_pos + 10
        if move in get_empty_tiles(board):
            moves.append(move)

            if pawn_pos in starting_positions:
                double_move = pawn_pos - 20
                moves.append(double_move)

    return moves


def pawn_attacks(pawn_pos: int, white_turn: bool) -> list:
    """Zwraca listę pól atakowanych przez piona"""
    attacks = []

    # pion atakuje pola: biały pole o numerze mniejszym o 9 i o 11 w
    # stosunku do obecnej pozycji piona, a czarny o numerze większym o 9 i 11

    if white_turn:
        multiplier = -1
    else:
        multiplier = 1

    x = pawn_pos + (9 * multiplier)
    y = pawn_pos + (11 * multiplier)
    if x in get_all_tiles():
        attacks.append(x)
    if y in get_all_tiles():
        attacks.append(y)

    return attacks


def king_moves(board: list, king_pos: int, white_turn: bool) -> list:
    """Zwraca listę możliwych ruchów króla (o określonej pozycji)
    na wolne pola, lub pola gdzie może zbić"""

    k = king_pos
    moves = []
    all_moves = [k - 11, k - 10, k - 9, k - 1, k + 1, k + 9, k + 10, k + 11]

    for move in all_moves:
        if move in get_not_own_tiles(board, white_turn):
            moves.append(move)

    return moves


def find_king(board: list, white_turn: bool) -> int:
    """Zwraca pozycję króla danego koloru, w postaci liczby całkowitej"""

    if white_turn:
        opponents_king = 'bW'
    else:
        opponents_king = 'wW'

    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == opponents_king:
                king_pos: int = i*10 + j

                return king_pos


def get_all_locations(board: list, white_turn: bool):
    """Zwraca słownik który każdej występującej na danej szachownicy figurze
    danego koloru przyporządkowuje liczbę oznaczającą pole na którym stoi
    """
    all_locations = {}

    if white_turn:
        color_letter = 'w'
    else:
        color_letter = 'b'

    for r, row in enumerate(board):
        for t, tile in enumerate(row):
            tile_number: int = r * 10 + t
            if tile[0] == color_letter:
                all_locations[tile_number] = tile

    return all_locations


def is_check(board: list, positions: dict, white_turn: bool) -> bool:
    """Zwraca wartość boolowską True jeśli w danej sytuacji występuje szach,
    False jeśli nie występuje."""

    attacked_tiles = []

    if white_turn:
        color_letter = 'w'
    else:
        color_letter = 'b'

    for position, figure in positions.items():
        if figure == f'{color_letter}p':
            attacked_tiles += pawn_attacks(position, white_turn)
        if figure == f'{color_letter}r':
            attacked_tiles += rook_moves(board, position, white_turn)
        if figure == f'{color_letter}k':
            attacked_tiles += knight_moves(board, position, white_turn)
        if figure == f'{color_letter}b':
            attacked_tiles += bishop_moves(board, position, white_turn)
        if figure == f'{color_letter}q':
            attacked_tiles += queen_moves(board, position, white_turn)
        if figure == f'{color_letter}W':
            attacked_tiles += king_moves(board, position, white_turn)

    opponents_king_pos = find_king(board, white_turn)

    if opponents_king_pos in attacked_tiles:
        return True
    else:
        return False


def check_all_moves(board: list, white_turn: bool):
    """Sprawdzamy czy występuje szach (w wersji docelowej szach mat) dla każdego
    z możliwych do wykonania ruchów"""

    if is_check(board, get_all_locations(board, white_turn), True):
        return 'Już występuje szach (mat) dla białego, nie można wykonywać ruchu'

    if is_check(board, get_all_locations(board, white_turn), False):
        return 'Już występuje szach (mat) dla czarnego, nie można wykonywać ruchu'

    positions = get_all_locations(board, white_turn)

    for position, figure in positions.items():

        def pick_function(figure_type: str):
            """Zwraca odpowiednią funkcję która będzie użyta, w zależnośći od
            rodzaju figury"""

            switcher = {
                'p': pawn_moves(board, position, white_turn),
                'r': rook_moves(board, position, white_turn),
                'k': knight_moves(board, position, white_turn),
                'b': bishop_moves(board, position, white_turn),
                'q': queen_moves(board, position, white_turn),
                'W': king_moves(board, position, white_turn)
            }

            func = switcher.get(figure_type)
            return func

        figure_letter = figure[1]
        moves = pick_function(figure_letter)

        for move in moves:
            positions = get_all_locations(board, True)

            del positions[position]
            positions[move] = figure

            if is_check(board, positions, white_turn):
                if white_turn:
                    return f'Biały może wygrać ({finishing_move(position, move)})'
                else:
                    return f'Czarny może wygrać ({finishing_move(position, move)})'


print(check_all_moves(input_board, True))
