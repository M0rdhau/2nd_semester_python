from sys import version_info
from circle import circle

if version_info.major == 2:  # python2
    import Tkinter as tkinter
elif version_info.major == 3:  # python3
    import tkinter as tkinter

def main():
    window = tkinter.Tk()
    window.title("Homework 1")
    window.geometry('500x200')

    lbl = tkinter.Label(window, text="Circlinator5000", font=("Arial Bold", 18))
    lbl.grid(column=0, row=0)

    tkinter.Label(window, text='Input', font=("Monospace", 15)).grid(column=0, row=1)
    txt = tkinter.Entry(window, width=10)
    txt.grid(column=1, row=1)
    txt.focus()

    #Static text
    tkinter.Label(window, text='Radius', font=("Monospace", 15)).grid(column=0, row=3)
    tkinter.Label(window, text='Area', font=("Monospace", 15)).grid(column=0, row=4)
    tkinter.Label(window, text='Circumference', font=("Monospace", 15)).grid(column=0, row=5)

    #Dynamic text - changes every time you click a button
    radiustext = tkinter.StringVar()
    areatext = tkinter.StringVar()
    circumferencetext = tkinter.StringVar()
    radiustext.set(0)
    areatext.set(0)
    circumferencetext.set(0)
    tkinter.Label(window, textvariable=radiustext, font=("Monospace", 15)).grid(column=1, row=3)
    tkinter.Label(window, textvariable=areatext, font=("Monospace", 15)).grid(column=1, row=4)
    tkinter.Label(window, textvariable=circumferencetext, font=("Monospace", 15)).grid(column=1, row=5)

    def clicked():
        if txt.get() != "":
            radius = int(txt.get())
        else:
            return
        calculated = circle.circlinate(radius)
        area = calculated[0]
        circumference = calculated[1]
        radiustext.set(str(radius))
        areatext.set("{:.3f}".format(area))
        circumferencetext.set("{:.3f}".format(circumference))


    # add a button in the application
    btn = tkinter.Button(window, text="Circlinate", command=clicked)
    btn.grid(column=1, row=2)

    window.mainloop()


if __name__ == '__main__':
    main()