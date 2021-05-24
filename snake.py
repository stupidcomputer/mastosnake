import random

class Snake:
    def __init__(self, bx=5, by=5):
        self.snake = [
            (2, 2),
            (2, 1),
            (2, 0)
        ]
        self.gamestate = "playing"
        self.boarddimensions = (bx, by)
        self.directions = [
            (-1, 0, "left"),
            (0, -1, "down"),
            (1, 0, "right"),
            (0, 1, "up")
        ]
        self.apple = (random.randrange(0, self.boarddimensions[0]),
            random.randrange(0, self.boarddimensions[0]))
    def moveset(self):
        tmp = []
        for i, j, text in self.directions:
            tmp.append(
                (self.snake[0][0] + i,
                self.snake[0][1] + j,
                text)
            )

        for i, j, text in tmp:
            if (i, j) == self.snake[1]:
                tmp.remove((i, j, text))

        for i, j, text in tmp:
                if i < 0 or i > self.boarddimensions[0] - 1:
                    tmp.remove((i, j, text))
                    break
                if j < 0 or j > self.boarddimensions[1] - 1:
                    tmp.remove((i, j, text))
                    break
        return tmp
    def nodir(self):
        tmp = []
        for i, j, _ in self.moveset():
            tmp.append((i, j))
        return tmp
    def move(self, direction):
        for i in self.directions:
            if direction == i[2]:
                considered = (self.snake[0][0] + i[0],
                    self.snake[0][1] + i[1])
                if considered in self.snake:
                    self.gamestate = "gameover"
                if considered in self.nodir():
                    self.snake.insert(0, considered)
                if self.apple != considered:
                    self.snake.pop()
                else:
                    c = (random.randrange(0, self.boarddimensions[0] - 1), random.randrange(0, self.boarddimensions[1] - 1))
                    while c in self.snake:
                        c = (random.randrange(0, self.boarddimensions[0] - 1), random.randrange(0, self.boarddimensions[1] - 1))
                    self.apple = c

    def render(self):
        tmp = []
        for j in range(self.boarddimensions[0] - 1, -1, -1):
            tmp.append([])
            current = tmp[-1]
            for i in range(0, self.boarddimensions[1]):
                if (i, j) in self.snake:
                    if (i, j) == self.snake[0]:
                        current.append('X')
                    else:
                        current.append('x')
                elif (i, j) == self.apple:
                    current.append('a')
                else:
                    current.append('_')
        return tmp

