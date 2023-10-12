from tkinter import *
import socket

ESP_IP = "192.168.100.191"

ESP_PORT = 8266

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def key_pressed(c):
    print("Tecla presionada: ", c.char)
    s.send(c.char.encode())
def key_released(c):
    print("Tecla liberada: ", c.char)
    s.send(c.char.encode())


root = Tk()
root.title("Control de Carro")

frame = Frame(root)

lbl_title = Label(frame, text="Control de Carro ROBOT")
lbl_title.grid(row=0, column=0, pady=10, padx=10)

frame.bind ("<KeyPress>", key_pressed)
frame.bind ("<KeyRelease>", key_released)

s.connect((ESP_IP, ESP_PORT))

frame.pack()
frame.focus_set()

root.mainloop()