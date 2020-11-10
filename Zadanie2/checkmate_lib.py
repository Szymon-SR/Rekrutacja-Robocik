import chess
import io

input_board: list = [
    ['--', '--', '--', 'bW', '--', '--', '--', 'br'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', 'bb', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', 'wp', '--', '--', '--', '--', '--', '--'],
    ['wp', '--', '--', '--', '--', 'wp', '--', 'wp'],
    ['--', '--', '--', '--', '--', 'wr', 'wW', '--']
    ]


def board_to_fen(board: list, color: str) -> str:
    """Zamienia szachownicę w formie listy na notację Forsytha-Edwardsa (FEN)
    która jest zrozumiała dla biblioteki chess"""

    with io.StringIO() as s:
        for row in board:
            empty: int = 0
            for cell in row:
                c = cell[0]
                if c in ('w', 'b'):  # Warunek spełniony gdy pole nie jest puste
                    if empty > 0:
                        s.write(str(empty))
                        empty = 0

                    # Zamieniamy oznaczenia skoczka i króla na zgodne z FEN
                    if cell[1] == 'k':
                        s.write('N' if c == 'w' else 'n')

                    elif cell[1] == 'W':
                        s.write('K' if c == 'w' else 'k')

                    # Zamieniamy białe figury na duże litery zgodnie z FEN
                    else:
                        s.write(cell[1].upper() if c == 'w' else cell[1].lower())
                else:
                    empty += 1
            if empty > 0:
                s.write(str(empty))
            s.write('/')

        # Usuwamy ostatni '/' bo nie powinien występować w notacji
        s.seek(s.tell() - 1)

        # Dodajemy literę która oznacza kolor gracza który ma aktualnie ruch (w/b)
        s.write(' ' + color)

        return s.getvalue()


def main(color: str) -> bool:
    """Wywołujemy board_to_fen, dla wszystkich możliwych dla podanego koloru
    bierek ruchu sprawdzamy czy po wykonaniu tego ruchu występuje sytuacja matowa.
    Wyświetlamy wygrywające ruchy i zwracamy True jeśli jest możliwość mata, lub
    False jeśli jej nie ma."""

    # uzyskujemy notację FEN
    fen: str = board_to_fen(input_board, color)
    print('\nNotacja: ' + fen)

    # ustawiamy szachownicę odpowiadającej naszej FEN
    board = chess.Board()
    board.set_fen(fen)

    # zapisujemy do moves wszystkie możliwe do wykonania ruchy
    moves = board.legal_moves
    can_win: bool = False

    for move in moves:
        # Wykonujemy ruch
        move = str(move)
        current_move = chess.Move.from_uci(move)
        board.push(current_move)
        
        if board.is_checkmate():
            can_win = True
            if color == 'w':
                print(f'Biały może wygrać ({move})')
            else:
                print(f'Czarny może wygrać ({move})')

        # pop - musimy cofnąć ruch, w przeciwnym razie plansza wyglądała by inaczej
        board.pop()

    # Jeśli can_win jest nadal fałszem, aktualny kolor nie ma możliwości wygranej
    if not can_win:
        if color == 'w':
            print(f'Biały NIE może wygrać')
        else:
            print(f'Czarny NIE może wygrać')

    return can_win


# Wywołujemy funkcję dla koloru białego, jeśli zwracana jest wartość fałsz
# (czyli biały nie ma możliwośći wygrania), wywołujemy dla koloru czarnego
if not main('w'):
    main('b')
