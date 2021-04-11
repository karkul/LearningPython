import numpy


def matrix_transpose(m):
    mt = numpy.array(m)
    num_rows, num_cols = mt.shape

    output = '['

    for col in range(0, num_cols):
        output += '['
        for row in range(0, num_rows):
            output += m[row][col]

            if row != num_rows - 1:
                output += ' '
        output += ']'
        if col != num_cols - 1:
            output += '\n'
    output += ']'

    print(output)


def matrix_flatten(m):
    mt = numpy.array(m)
    num_rows, num_cols = mt.shape

    output = '['
    for row in range(0, num_rows):
        for col in range(0, num_cols):
            output += m[row][col] + ' '
    output = output[:-1] + ']'

    print(output)


if __name__ == '__main__':
    num_rows, num_cols = map(int, input().split())

    matrix = []

    for row in range(0, num_rows):
        row_values = input()
        matrix.insert(row, row_values.split())

    matrix_transpose(matrix)
    matrix_flatten(matrix)