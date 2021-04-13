if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))

    l = []
    for i in range(0, x+1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                if i + j + k != n:
                    l.append([i, j, k])

    print(l)

    # A better way to do it using print function and nested for loops
    #print([[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n ])