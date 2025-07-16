# --------------------------------------------------
# Class: CS 2742 PYTHON PROGRAMMING
# Term: SPRING 2024
# Instructor: Jianmin Wang
# Description: Auto Service GUI
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

class AutomotiveGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # creating the frame that will hold the options
        self.checkbutton_frame = tkinter.Frame(self.main_window)

        # creating the frame that will hold the buttons to either display the charge or quit the program
        self.optionbutton_frame = tkinter.Frame(self.main_window)

        # creating the variable for total cost of services, which will later be displayed in a message box
        self.total_cost = 0.00

        # creating the checkbutton widgets for each possible service
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # setting the checkbutton widgets IntVar objects to zero to later help determine which ones were selected
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # assigning each checkbutton widget a title and price that corresponds to each service
        self.cb1 = tkinter.Checkbutton(self.checkbutton_frame, text="Oil change - $30.00", variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.checkbutton_frame, text="Lube job - $20.00", variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.checkbutton_frame, text="Radiator flush - $40.00", variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.checkbutton_frame, text="Transmission flush - $100.00", variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.checkbutton_frame, text="Inspection $35.00", variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.checkbutton_frame, text="Muffler replacement - $200.00", variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.checkbutton_frame, text="Tire rotation - $20.00", variable=self.cb_var7)

        # packing each checkbutton widget into the correct frame
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # creating two buttons to either display the total charges selected or quit the program
        # if display charges is selected, then the show_charges function is called and a messagebox appears
        # if quit is selected, the window closes and the program ends
        self.display_button = tkinter.Button(self.optionbutton_frame, text="Display Charges", command=self.show_charges)
        self.quit_button = tkinter.Button(self.optionbutton_frame, text="Quit", command=self.main_window.destroy)

        # packing the buttons into their respective frame
        self.display_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.checkbutton_frame.pack()
        self.optionbutton_frame.pack()

        tkinter.mainloop()

    def show_charges(self):

        # creating the message that will eventually be displayed in the messagebox when display charges is selected
        self.message = "You selected: \n"

        # the following logic determines which checkbox widgets are selected and adds them to the message that will
        # appear in the messagebox.
        # for each checkbox widget selected, the price of the service gets added to the total cost
        if self.cb_var1.get() == 1:
            self.message = self.message + "Oil change - $30.00\n"
            self.total_cost += 30.00
        if self.cb_var2.get() == 1:
            self.message = self.message + "Lube job - $20.00\n"
            self.total_cost += 20.00
        if self.cb_var3.get() == 1:
            self.message = self.message + "Radiator flush - $40.00\n"
            self.total_cost += 40.00
        if self.cb_var4.get() == 1:
            self.message = self.message + "Transmission flush - $100.00\n"
            self.total_cost += 100.00
        if self.cb_var5.get() == 1:
            self.message = self.message + "Inspection - $35.00\n"
            self.total_cost += 35.00
        if self.cb_var6.get() == 1:
            self.message = self.message + "Muffler replacement - $200.00\n"
            self.total_cost += 200.00
        if self.cb_var7.get() == 1:
            self.message = self.message + "Tire rotation - $20.00\n"
            self.total_cost += 20.00

        # the messagebox displays all the services selected by the user as well as the total cost of everything
        tkinter.messagebox.showinfo("Selection", self.message + "\n" +
                                    "Total Cost: $" + str(self.total_cost))


if __name__ == '__main__':
    my_gui = AutomotiveGUI()



