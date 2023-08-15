import tkinter as tk
from PIL import Image, ImageTk

image_folder = "Resources\\pngs\\"

class PopupWindow:
    def __init__(self, master):
        self.master = master
        self.current_image_index = 0

        self.popup_window = tk.Toplevel(master)
        self.popup_window.overrideredirect(True)
        self.popup_window.wm_attributes("-topmost", 1)
        self.popup_window.wm_attributes("-transparentcolor", "white")  # Set the transparent color

        self.label = tk.Label(self.popup_window, bg="white")
        self.label.pack()

        self.next_image()

    def next_image(self):
        if self.current_image_index < 28:
            image_path = image_folder+str(self.current_image_index+1)+".png"
            image = Image.open(image_path).convert("RGBA")
            self.set_transparent_background(image)
            photo = ImageTk.PhotoImage(image)
            self.label.configure(image=photo)
            self.label.image = photo
            self.current_image_index += 1
            self.popup_window.after(30, self.next_image)
        else:
            self.popup_window.destroy()
            exit()

    def set_transparent_background(self, image):
        # Set the transparent color in the image
        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, g, b, a = image.getpixel((x, y))
                if (r, g, b) == (255, 255, 255):  # Change the color here if necessary
                    image.putpixel((x, y), (0, 0, 0, 0))  # Make the color transparent


def create_popup_window():
    root = tk.Tk()
    root.withdraw()

    popup = PopupWindow(root)

    root.mainloop()


create_popup_window()
