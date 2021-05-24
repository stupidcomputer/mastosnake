class Mastosnake:
    def __init__(self, tok, game):
        self.tok = tok
        self.game = game
    def returnStatus(self):
        statusstring = ""
        for j in range(self.game.boarddimensions[0] - 1, -1 -1):
            for i in range(0, self.game.boarddimensions[1]):
                if (i, j) in self.game.snake:
                    if (i, j) == self.game.snake:
                        statusstring += "X"
                    else:
                        statusstring += "x"
                elif (i, j) == self.apple:
                    statusstring += "a"
                else:
                    statusstring += " "
            statusstring += "\n"
        dataskel = {
            'status': statusstring,
            'poll': {
                'options': [],
                'expires_in': 60,
                'multiple': False
            }
        }
        for _, _, i in self.game.moveset():
            dataskel['poll']['options'].append(i)
        return dataskel
