from snake2 import Snake

snake = Snake()
while True:
    for i in snake.render():
        print(i)
    print(snake.gamestate)
    snake.move(input("choose a move: "))
    if snake.gamestate == 'gameover':
        exit(0)

