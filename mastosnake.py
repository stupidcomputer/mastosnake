class Mastosnake:
    def __init__(self, game):
        self.game = game
    def returnStatus(self):
        statusstring = ""
        for j in range(self.game.boarddimensions[0] - 1, -1, -1):
            for i in range(0, self.game.boarddimensions[1]):
                if (i, j) in self.game.snake:
                    if (i, j) == self.game.snake[0]:
                        statusstring += '⬛'
                    else:
                        statusstring += '◾'
                elif (i, j) == self.game.apple:
                    statusstring += '🍎'
                else:
                    statusstring += '⬜'
            statusstring += '\n'
        statusstring += '\n'
        statusstring += self.game.gamestate
        statusstring += ' | score: '
        statusstring += str(len(self.game.snake))
        dataskel = {
            'status': statusstring,
            'poll': {
                'options': [],
                'expires_in': 100000,
                'multiple': False
            }
        }
        for _, _, i in self.game.moveset():
            dataskel['poll']['options'].append(i)
        return dataskel
    def updateState(self, data):
        tmp = []
        for i in data['options']:
            tmp.append((i['title'], i['votes_count']))
        tmp2 = (0, -1)
        for i in tmp:
            if i[1] > tmp2[1]:
                tmp2 = i
        self.game.move(tmp2[0])
