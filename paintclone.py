from tkinter import *
from tkinter import colorchooser  # Import colorchooser
from PIL import Image, ImageDraw
import PIL

WIDTH, HEIGHT = 500, 500
CENTER = WIDTH // 2
WHITE = (255, 255, 255)

class PaintGUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Paint clone by Saksham")

        self.brush_width = 15
        self.current_colour = "#000000"

        self.cnv = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg="white")
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint)

        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = ImageDraw.Draw(self.image)

        self.btn_frame = Frame(self.root)
        self.btn_frame.pack(fill=X)

        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)
        self.btn_frame.columnconfigure(3, weight=1)
        self.btn_frame.columnconfigure(4, weight=1)

        self.clear_btn = Button(self.btn_frame, text="Clear", command=self.clear)
        self.clear_btn.grid(row=1, column=0, sticky=W+E)

        self.save_btn = Button(self.btn_frame, text="Save", command=self.save)
        self.save_btn.grid(row=1, column=1, sticky=W+E)

        self.bplus_btn = Button(self.btn_frame, text="B+", command=self.brush_plus)
        self.bplus_btn.grid(row=1, column=2, sticky=W+E)

        self.bminus_btn = Button(self.btn_frame, text="B-", command=self.brush_minus)
        self.bminus_btn.grid(row=1, column=3, sticky=W+E)

        self.color_btn = Button(self.btn_frame, text="Change Color", command=self.change_color)
        self.color_btn.grid(row=1, column=4, sticky=W+E)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x - self.brush_width), (event.y - self.brush_width)
        x2, y2 = (event.x + self.brush_width), (event.y + self.brush_width)
        self.cnv.create_oval(x1, y1, x2, y2, fill=self.current_colour, outline=self.current_colour)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.current_colour)

    def clear(self):
        self.cnv.delete("all")
        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = ImageDraw.Draw(self.image)

    def save(self):
        file_name = "painting.png"
        
        self.image.save(file_name)

    def brush_plus(self):
        self.brush_width += 5

    def brush_minus(self):
        if self.brush_width > 1:
            self.brush_width -= 5

    def change_color(self):
        # Use the colorchooser to change the brush color
        color_choice = colorchooser.askcolor()[1]
        if color_choice:
            self.current_colour = color_choice

    def on_closing(self):
        self.root.destroy()

PaintGUI()


