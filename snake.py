#!/bin/python

import random

class Game:
    """
    this class describes a 5x5 grid, with a snake and
    apple inside.

    coordinates are akin to a quadrant I cartesian plane, e.g.
        ^
       5| 
       4|
    y  3|
       2|
       1|
        +----->
         12345

           x
    """
    def __init__(self):
        self.snake = []
        self.apple = (0, 0)
        for i in range(3):
            self.snake.append((3, i + 1))
            self.snake.reverse()
        self.newapple()
    def newapple(self):
        candidate = (random.randint(1, 5), random.randint(1, 5))
        if candidate in self.snake:
            candidate = self.newapple()
        return candidate
    def subtracttuple(self, a, b):
        return (a[0] - b[0], a[1] - b[1])
    def addtuple(self, a, b):
        return (a[0] + b[0], a[1] + b[1])
    def returndirections(self):
        permute = []
        directions = []
        permute.append((self.snake[0][0], self.snake[0][0] + 1))
        permute.append((self.snake[0][0], self.snake[0][0] - 1))
        permute.append((self.snake[0][0], self.snake[0][1] + 1))
        permute.append((self.snake[0][0], self.snake[0][1] - 1))
        for i in permute:
            if not i[0] < 0 and \
                not i[0] > 5 and \
                not i[1] < 0 and \
                not i[1] > 5:
                directions.append(self.subtracttuple(i, self.snake[0]))
        return directions
    def cycle(self, direction):
        if direction in self.returndirections():
            self.snake.insert(0, self.addtuple(self.snake[0], direction))
            if not self.snake[0] == self.apple:
                self.snake.pop(-1)
                self.newapple()
            if self.snake[0] in self.snake[1:]:
                return 'game end'
        else:
            return 'invalid'
    def render(self): # very inefficent, fix later
        for y in range(5):
            line = []
            for x in range(5):
                if (x + 1, y + 1) in self.snake:
                    line.append("x")
                elif (x + 1, y + 1) == self.apple:
                    line.append("a")
                else:
                    line.append("-")
            print(' '.join(line))
