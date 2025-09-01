from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2
import os


#click on open and select  video and click on click button and wait for seconds

url_path = ""

def open():
    global url_path
    video_path = filedialog.askopenfilename()
    for item in video_path:
        url_path += item



def click():
    # Read the video from specified path
    if url_path != "":
        cam = cv2.VideoCapture(url_path)

        try:

            # creating a folder named data
            if not os.path.exists('data'):
                os.makedirs('data')

        # if not created then raise error
        except OSError:
            print('Error: Creating directory of data')

        # frame
        currentframe = 0
        run = True
        while run:

            # reading from frame
            ret, frame = cam.read()

            if ret:
                if url_entry.get() == "":
                    name = './data/frame' + str(currentframe) + '.jpg'
                else:
                    name = './data/' + url_entry.get() + str(currentframe) + '.jpg'

                # if video is still left continue creating images
                # print('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1

            else:
                # messagebox.showinfo(title="win", str="please click on show button to see the all images")
                # run = False
                break

        messagebox.showinfo(title="Succes", message="Please click on show button to see all images")
        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()
    else:
        messagebox.showerror(message="Open your file please!")



def show_photo():
    if not os.path.exists("data"):
        messagebox.showerror(message="This file not exists !")
    os.startfile("data")




window = Tk()

window.config(width=600, height=600)

window.title("Extract Images App")

canvas = Canvas(width=600, height=600)


photo = PhotoImage(file="Assets/photo3.png")


canvas.create_image(300, 300, image=photo)

GREY = "#F1F1FF"
BLUE = "#22F9FF"

url_entry = Entry(width=35, font=("Ariel", 15, "normal"), bg=GREY)
url_entry.place(x=34, y=306)

# url_entry.insert(0, string="write any name here")


open_image = PhotoImage(file='Assets/open.png')

open_button = Button(image=open_image, highlightthickness=0, borderwidth=0, command=open)
open_button.place(x=492, y=306)


click_image = PhotoImage(file='Assets/click.png')
show_image = PhotoImage(file="Assets/show.png")


click_button = Button(image=click_image, highlightthickness=0, borderwidth=0, command=click)
click_button.place(y=416, x=264)

show_button = Button(image=show_image, highlightthickness=0, borderwidth=0, command=show_photo)
show_button.place(y=470, x=264)


canvas.place(x=0, y=0)
window.mainloop()