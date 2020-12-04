class TreeMapper():
    def __init__(self, num_rows, row_width, rows):
        self.num_rows = num_rows
        self.row_width = row_width
        self.rows = rows

    def repeat(self, row):
        return ''.join(row * self.times)

    def get_trees(self, right, down):
        self.times = (self.num_rows * right)/self.row_width + 1
        tree_map = list(map(self.repeat, self.rows))
        tree_count = 0
        index = right
        i=down
        while(i < len(tree_map)):
            if tree_map[i][index] == '#':
                tree_count = tree_count + 1
            index = index + right
            i=i+down
        return tree_count

if __name__ == '__main__':
    with open('input.txt') as f:
        rows = f.read().splitlines()
    mapper = TreeMapper(len(rows), len(rows[0]), rows)
    tree_count = mapper.get_trees(3,1)
    print(tree_count)
