def chessBoardCellColor(cell1, cell2):
    cell_1 = ord(cell1[0]) % 2 + int(cell1[1]) % 2
    cell_2 = ord(cell2[0]) % 2 + int(cell2[1]) % 2
    if (cell_1 == 2 and cell_2 == 0) or (cell_1 == 0 and cell_2 == 2):
        return True
    else:
        return (ord(cell1[0]) % 2 + ord(cell1[1]) % 2) == (ord(cell2[0]) % 2 + ord(cell2[1]) % 2)

print(chessBoardCellColor('B4', 'A3'))

def better_chessBoardCellColor(cell1, cell2):

    return (ord(cell1[0])+int(cell1[1])+ord(cell2[0])+int(cell2[1]))%2==0
