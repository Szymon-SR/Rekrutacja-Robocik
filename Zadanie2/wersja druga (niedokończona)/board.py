input_board: list = [
    ['--', '--', 'bW', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', 'wr', '--', '--'],
    ['--', '--', '--', '--', '--', '--', 'bb', '--'],
    ['--', '--', '--', 'wq', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', 'bp', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', 'wp'],
    ['--', '--', '--', '--', 'wW', '--', '--', '--']
    ]

# Przykładowe szachownice
#
# Wygrana białych 1 (z treści zadania)
#
# ['--', '--', 'bW', '--', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', 'wr', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', '--', '--', 'wq', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', 'bp', '--', '--', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', 'wp'],
# ['--', '--', '--', '--', 'wW', '--', '--', '--']
#
# Wygrana białych 2:
#
# ['--', '--', 'bW', '--', '--', '--', '--', '--'],
# ['--', '--', '--', '--', 'wr', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', '--', '--', 'wq', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', 'bp', '--', '--', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', 'wp'],
# ['--', '--', '--', '--', 'wW', '--', '--', '--']
#
# Wygrana czarnych:
#
# ['--', '--', '--', 'bW', '--', '--', '--', 'br'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', '--', 'bb', '--', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', 'wp', '--', '--', '--', '--', '--', '--'],
# ['wp', '--', '--', '--', '--', 'wp', '--', 'wp'],
# ['--', '--', '--', '--', '--', 'wr', 'wW', '--']
#
# Brak wygranej:
#
# ['--', '--', '--', 'bW', '--', '--', '--', 'br'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', '--', 'bk', '--', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', '--', '--', '--', '--', '--', '--', '--'],
# ['--', 'wp', '--', '--', '--', '--', '--', '--'],
# ['wp', '--', '--', '--', '--', 'wp', '--', 'wp'],
# ['--', '--', '--', '--', '--', 'wr', 'wW', '--']
#
