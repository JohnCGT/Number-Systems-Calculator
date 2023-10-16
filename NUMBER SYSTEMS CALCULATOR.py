import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Calculator")
root.geometry("290x300")
bg = PhotoImage(file = "E:\\Programming Project\\Python\\CALCULATOR GUI\\background2.png")
my_label = Label(root, image = bg)
my_label.place(x=0, y=0, relwidth =1, relheight = 1)

for x in range(7):
    root.grid_rowconfigure(x, weight=1)
    root.grid_columnconfigure(x, weight=1)


calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluation_of_calculation():
    global calculation
    try:
        calculation = str((eval(calculation)))
        decimal_count = calculation.count(".0")
        if decimal_count == 1:
            calculation = str(int(eval(calculation)))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        else:
            calculation = str((eval(calculation)))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def backspace():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def binary():
    global calculation
    a3 = calculation.count("2")
    b3 = calculation.count("3")
    c3 = calculation.count("4")
    d3 = calculation.count("5")
    e3 = calculation.count("6")
    f3 = calculation.count("7")
    g3 = calculation.count("8")
    h3 = calculation.count("9")

    a = calculation.count("a")
    a2 = calculation.count("A")
    b = calculation.count("b")
    b2 = calculation.count("B")
    c = calculation.count("c")
    c2 = calculation.count("C")
    d = calculation.count("d")
    d2 = calculation.count("D")
    e = calculation.count("e")
    e2 = calculation.count("E")
    f = calculation.count("f")
    f2 = calculation.count("F")
    g = calculation.count("g")
    g2 = calculation.count("G")
    h = calculation.count("h")
    h2 = calculation.count("H")

    if a > 0 or b > 0 or c > 0 or d > 0 or e > 0 or f > 0 or g > 0 or h>0 or c2>0 or a2>0 or b2>0 or d2>0 or e2>0 or f2>0 or g2>0 or h2>0:
        clear_field()
        text_result.insert(1.0, "Error")

    elif a3 > 0 or b3 > 0 or c3 > 0 or d3 > 0 or e3 > 0 or f3 > 0 or  g3 > 0 or h>0:
        clear_field()
        text_result.insert(1.0, "Error")
    else:
        num = list(int(x) for x in calculation)
        num.reverse()
        fruits = []
           
    for biT in range(len(num)):
        product = (2 ** biT) * (num[biT])
                
        fruits.append(product)
                
        fruits.reverse()
        calculation = str(sum(fruits))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

def decimal_to_binary():
    global calculation
    calculation = int(calculation)
    binary_list = []

    while calculation >= 1:
        remainder = calculation%2
        calculation = calculation/2
        binary_list.append(int(remainder))

    binary_list.reverse()

    highest_binary_number_on_a_certain_list = all(binarydigit == 0 for binarydigit in binary_list)

    if highest_binary_number_on_a_certain_list:
        binary_list.insert(0, 1)
        awit = ''.join(map(str,binary_list))
        calculation = awit
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    else:
        awit = ''.join(map(str,binary_list))
        calculation = awit
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

def hexadecimal():
    global calculation
    a = calculation.count("a")
    a2 = calculation.count("A")
    b = calculation.count("b")
    b2 = calculation.count("B")
    c = calculation.count("c")
    c2 = calculation.count("C")
    d = calculation.count("d")
    d2 = calculation.count("D")
    e = calculation.count("e")
    e2 = calculation.count("E")
    f = calculation.count("f")
    f2 = calculation.count("F")
    g = calculation.count("g")
    g2 = calculation.count("G")
    h = calculation.count("h")
    h2 = calculation.count("H")

    if a > 0 or b > 0 or c > 0 or d > 0 or e > 0 or f > 0 or g > 0 or h>0 or c2>0 or a2>0 or b2>0 or d2>0 or e2>0 or f2>0 or g2>0 or h2>0:
        clear_field()
        text_result.insert(1.0, "Error")
    else:
        hexadecimal_values = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
        calculation = int(calculation)
        decimal_num_into_hexadecimal = []

        while (calculation != 0):
            remainder = calculation % 16
            decimal_num_into_hexadecimal.append(remainder)
            calculation //= 16

        decimal_num_into_hexadecimal.reverse()

        hexadecimal_equivalent = [str(hexadecimal_values[x]) for x in decimal_num_into_hexadecimal]
        execution_of_numbers = ''.join(map(str,hexadecimal_equivalent))
        calculation = execution_of_numbers
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
       

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=6, sticky="nsew")

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1, sticky="nsew")

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2, sticky="nsew")

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3, sticky="nsew")

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1, sticky="nsew")

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2, sticky="nsew")

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3, sticky="nsew")

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1, sticky="nsew")

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2, sticky="nsew")

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3, sticky="nsew")

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2, sticky="nsew")

btn_addition = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_addition.grid(row=2, column=4, sticky="nsew")

btn_subtraction = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_subtraction.grid(row=3, column=4, sticky="nsew")

btn_multiplication = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multiplication.grid(row=4, column=4, sticky="nsew")

btn_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_division.grid(row=5, column=4, sticky="nsew")

btn_parenthesis = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_parenthesis.grid(row=5, column=1, sticky="nsew")

btn_parenthesis2 = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_parenthesis2.grid(row=5, column=3, sticky="nsew")

btn_equals = tk.Button(root, text ="=", command=evaluation_of_calculation, width=5, font=("Arial, 14"))
btn_equals.grid(row=6, column=1, sticky="nsew")

btn_clear = tk.Button(root, text ="Clear", command=clear_field, width=5, font=("Arial, 14"))
btn_clear.grid(row=6, column=2, sticky="nsew")

btn_backspace = tk.Button(root, text ="Del", command=backspace, width=5, font=("Arial, 14"))
btn_backspace.grid(row=6, column=3, sticky="nsew")

btn_decimal = tk.Button(root, text ="Dec", command=binary, width=5, font=("Arial, 14"))
btn_decimal.grid(row=6, column=4, sticky="nsew")

btn_binary = tk.Button(root, text ="Bin", command=decimal_to_binary, width=5, font=("Arial, 14"))
btn_binary.grid(row=7, column=1, sticky="nsew")

btn_hexadecimal = tk.Button(root, text ="Hex", command=hexadecimal, width=5, font=("Arial, 14"))
btn_hexadecimal.grid(row=7, column=2, sticky="nsew")


root.mainloop()