def getNumberBlocks(blocks, rows):
    if rows < 1:
        print(blocks)
    else:
        blocks += rows+(rows-1)
        getNumberBlocks(blocks, rows-2)

def blocks(rows):
    if rows <= 0:
        return 0
    return rows + blocks(rows - 1)

getNumberBlocks(0, 6)
