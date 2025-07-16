# --------------------------------------------------
# Class: CS 2742 PYTHON PROGRAMMING
# Term: SPRING 2024
# Instructor: Jianmin Wang
# Description: Info GUI
# Due: 04/15/2024
# Author: Ansley Bray
# Python version 3.0
#
# By turning in this code I pledge:
#   1. That I have completed the programming assignment independently
#   2. I have not copied the code from a student or any source
#   3. I have not given my code to any student
# ---------------------------------------------------
#


import tkinter
import tkinter.messagebox

class InfoGUI:
    def __init__(self):

        # creating the main window
        self.main_window = tkinter.Tk()

        # info_frame will display the address once the show info button is clicked
        self.info_frame = tkinter.Frame(self.main_window)

        # buttons_frame contains the show info and quit buttons
        self.buttons_frame = tkinter.Frame(self.main_window)

        # creating the show info and quit buttons
        # when the show info button is clicked, the show_info function is called and will display the address
        self.show_info_button = tkinter.Button(self.buttons_frame, text="Show Info", command=self.show_info)
        self.quit_button = tkinter.Button(self.buttons_frame, text="Quit", command=self.main_window.destroy)

        # positioning the buttons into the frames
        self.show_info_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.info_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()


    def show_info(self):
        # creating the labels that will contain the address information to be display
        self.name_label = tkinter.Label(self.info_frame, text="Ansley Bray")
        self.address_label1 = tkinter.Label(self.info_frame, text="405 Lofton Rd NW")
        self.address_label2 = tkinter.Label(self.info_frame, text="Atlanta, GA 30309")

        # packing the labels into the frame
        self.name_label.pack()
        self.address_label1.pack()
        self.address_label2.pack()


if __name__ == '__main__':
    my_gui = InfoGUI()