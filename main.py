from email.utils import collapse_rfc2231_value
from tkinter import *
from cell import Cell
import settings, utils

root = Tk()
# override settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg= 'black', #change later to black
    width=settings.WIDTH,
    height=utils.height_prct(25),
)
top_frame.place(x=0, y=0)       # setting the axis for the top frame

left_frame = Frame(
    root,
    bg= 'black',  #change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75),
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg="black",      # change to black
    width= utils.width_prct(75),
    height=utils.height_prct(75),
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25),
)

for x in range(5):
    for y in range(5):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=y, 
            row=x
        )

# run the window
root.mainloop()