import tkinter
from config import *
from Snake.app import Snake, Food


def game_over():
    canvas.delete(tkinter.ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('consolas', 70),
                       text="GAME OVER", fill="red",
                       tags="gameover")
    snake.direction = 'space'

score = 0
window = tkinter.Tk()
window.resizable(False, False)
canvas = tkinter.Canvas(window, height=SIDE, width=SIDE, bg='black')
label = tkinter.Label(window, text=f'Score: {score}', font=('consolas', 40))
snake = Snake(window, canvas)
food = Food(canvas)
label.pack()
canvas.pack()
window.bind('<KeyPress>', snake.turn)
snake.move(food)
window.mainloop()