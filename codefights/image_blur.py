def box_blur(image):
    rows = len(image)
    columns = len(image[0])
    ans = []
    for i in range(1, rows - 1):
        row = []
        for j in range(1, columns - 1):
            row.append(sum([image[i + k][j + l]
                            for k in [-1, 0, 1] for l in [-1, 0, 1]]) // 9)
        ans.append(row)
    return ans


image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

print(box_blur(image))
