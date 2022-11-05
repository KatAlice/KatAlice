matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]


def search_in_matrix(matrix, value):
    for i, v in enumerate(matrix):
        if value in v:
            return {'row': i, 'col': v.index(value)}
    return print({'row': -1, 'col': -1})


print(search_in_matrix(matrix, 128))
