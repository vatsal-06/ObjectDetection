# Object Detection using OpenCV in Python by Vatsal Gupta, XII-E (Group I)

# Start of Project

# Import libraries
from tkinter import *


# Define a Class for Tkinterr
class App:

    def __init__(self, main):  # Define self object
        self.root = main
        self.root.geometry("500x230")  # State Geometry
        self.root.title('Object Detection')  # State Title

        # Add Title
        title = Label(self.root, text="Object Detection", background='#efc595', foreground="#ce3012",
                      font=("retroica", 25), bd=5, relief=RIDGE)
        title.pack(side=TOP, fill=X)

        # Define Functions for commands for Buttons

        def video():
            exec(open("/Users/vatsalgupta/Desktop/ObjectDetection/Subfiles/Video.py").read())

        def webcam():
            exec(open("/Users/vatsalgupta/Desktop/ObjectDetection/Subfiles/webcam.py").read())

        def face_detect():
            exec(open("/Users/vatsalgupta/Desktop/ObjectDetection/Subfiles/Face_Detection.py").read())

        def exit_app():
            quit()

        # Add Buttons

        video_button = Button(text="Video", command=video, bg='#efc595', bd=1, foreground="#ce3012")
        video_button.place(x=150, y=80, width=80, height=40)

        webcam_button = Button(text="Webcam", command=webcam, bg='#efc595', bd=1, foreground="#ce3012")
        webcam_button.place(x=250, y=80, width=80, height=40)

        face_detect_button = Button(text="Face Detection", command=face_detect, bg='#efc595', bd=1,
                                    foreground="#ce3012")
        face_detect_button.place(x=180, y=130, width=120, height=40)

        exit_button = Button(text="Exit", command=exit_app, bg='#efc595', bd=1, foreground="#ce3012")
        exit_button.place(x=200, y=180, width=80, height=40)


# Close Window & End the Loop
root = Tk()
obj = App(root)
root.mainloop()

# End of Program
