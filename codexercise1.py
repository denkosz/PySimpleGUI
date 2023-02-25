



import PySimpleGUI as sG

label1 = sG.Text("Enter feet: ")
input1 = sG.Input(key="input")

label2 = sG.Text("Enter inches: ")
input2 = sG.Input(key="input2")

convert_button = sG.Button("Convert", key="btn_convert")
out_label = sG.Text(key="output")

window = sG.Window("Convertor", [[label1, input1],
                                 [label2, input2],
                                 [convert_button, out_label]])

while True:
    event, value = window.read()
    feet_meter = float(value["input"])
    inches_meter = float(value["input2"])
    total = feet_meter * 0.3048 + inches_meter * 0.025
    window["output"].update(value=total)

