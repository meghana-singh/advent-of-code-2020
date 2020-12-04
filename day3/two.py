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
    tree_count_1 = mapper.get_trees(1,1)
    tree_count_2 = mapper.get_trees(3,1)
    tree_count_3 = mapper.get_trees(5,1)
    tree_count_4 = mapper.get_trees(7,1)
    tree_count_5 = mapper.get_trees(1,2)

    print(tree_count_1, tree_count_2, tree_count_3, tree_count_4, tree_count_5)
    print(tree_count_1 * tree_count_2 * tree_count_3 * tree_count_4 * tree_count_5)