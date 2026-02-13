import tkinter as tk

# Initialize window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game state
current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]

# Create canvas for the game grid
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Draw the grid lines
def draw_grid():
    canvas.create_line(100, 0, 100, 300, width=2)
    canvas.create_line(200, 0, 200, 300, width=2)
    canvas.create_line(0, 100, 300, 100, width=2)
    canvas.create_line(0, 200, 300, 200, width=2)

draw_grid()

# Status label
status_label = tk.Label(root, text="Player X's Turn", font=('Arial', 14))
status_label.pack()

# Handle drawing X or O
def draw_symbol(x, y, player):
    x_center = x * 100 + 50
    y_center = y * 100 + 50
    if player == 'X':
        canvas.create_line(x_center - 25, y_center - 25, x_center + 25, y_center + 25, width=2)
        canvas.create_line(x_center + 25, y_center - 25, x_center - 25, y_center + 25, width=2)
    else:
        canvas.create_oval(x_center - 25, y_center - 25, x_center + 25, y_center + 25, width=2)

# Check for win
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# Check for draw
def check_draw():
    return all(cell != '' for row in board for cell in row)

# Handle click
def click(event):
    global current_player

    x = event.x // 100
    y = event.y // 100

    if board[y][x] == '':
        board[y][x] = current_player
        draw_symbol(x, y, current_player)

        if check_winner():
            status_label.config(text=f"Player {current_player} wins!")
            canvas.unbind("<Button-1>")
        elif check_draw():
            status_label.config(text="It's a Draw!")
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            status_label.config(text=f"Player {current_player}'s Turn")

# Reset the game
def reset_game():
    global board, current_player
    board = [['' for _ in range(3)] for _ in range(3)]
    canvas.delete("all")
    draw_grid()
    current_player = 'X'
    status_label.config(text="Player X's Turn")
    canvas.bind("<Button-1>", click)

# Bind click event
canvas.bind("<Button-1>", click)

# Add reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack()

# Run the application
root.mainloop()
