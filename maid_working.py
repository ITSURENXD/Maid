import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import threading
from time import sleep

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
            self.popup_window.after(5, self.next_image)
        else:
            self.popup_window.destroy()
            exit()

    def set_transparent_background(self, image):
        # Process the image and make the desired color transparent
        transparent_color = (255, 255, 255, 255)  # Change the color here if necessary
        image = image.convert("RGBA")
        data = image.getdata()
        new_data = []
        for item in data:
            if item[:3] == transparent_color[:3]:
                new_data.append((0, 0, 0, 0))
            else:
                new_data.append(item)
        image.putdata(new_data)
        return image


def create_popup_window():
    root = tk.Tk()
    root.withdraw()

    # Create the popup window
    popup = PopupWindow(root)

    # Update the window position after it's drawn
    popup.popup_window.update_idletasks()
    width = popup.popup_window.winfo_width()
    height = popup.popup_window.winfo_height()

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position for the bottom right corner
    x_pos = screen_width - width
    y_pos = screen_height - height

    # Move the window to the bottom right corner
    popup.popup_window.geometry(f"+{x_pos}+{y_pos}")

    root.mainloop()


# Example usage
def sounder():
    sleep(1)
    playsound("Resources\\notif.wav")

t1 = threading.Thread(target=create_popup_window,args=())
t2 = threading.Thread(target=sounder,args=());

t1.start()
t2.start()
t1.join()
t2.join()
#create_popup_window()
