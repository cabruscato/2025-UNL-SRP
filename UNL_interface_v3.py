import numpy as np
from tkinter import *

def HfO2_thickness_predict_v3(n, p):
    """Predicts doped:HfO₂ thin film thickness based on fit parameter values derived from hyperbolic regression models.
    Assumptions
        laser energy = 195 mJ
        growth temperature = 890°C (optimal)
    Args
        n: integer, number of pulsed laser shots
        p: float, O₂ growth pressure [mTorr]  
    Returns
        d: float, thin film thickness [nm]  
    """   
    alpha = 38.25
    beta = 12.09
    gamma = 417.2
    a = alpha * p
    b = a / (beta * p + gamma)
    d = (b / a) * np.sqrt(n * (n + 2*a))

    return d

def calculate_thickness():
    input_shots = shotsEntry.get()
    input_press = pressEntry.get()
    if input_shots:
        try:
            float(input_shots)
        except ValueError:
            readout.config(text='invalid laser shots')
            return
    else:
        readout.config(text='missing laser shots')
        return
    
    if float(input_shots) < 0:
        readout.config(text='invalid laser shots')
        return
    
    if input_press:
        try:
            float(input_press)
        except ValueError:
            readout.config(text='invalid O₂ pressure')
            return
    else:
        readout.config(text='missing O₂ pressure')
        return    
    
    if float(input_press) <= 0:
        readout.config(text='invalid O₂ pressure')
        return
    
    thickness_tmp = HfO2_thickness_predict_v3(float(input_shots), float(input_press))
    thickness = str(round(thickness_tmp, 2)) + ' nm'
    readout.config(text=thickness)

def submit(event):
    button.invoke()
    
root = Tk()

root.title('Doped:HfO₂ Thin Film Thickness Calculator')
root.config(bg='#d00000', padx=20, pady=10)

unl_logo_file = r"C:\Users\abrus\Active Academics\UNL2025_SRP\Quantum Materials Project\GUI_calculator\UNL_icon.png"
icon = PhotoImage(file=unl_logo_file)
root.iconphoto(True, icon)

title = Label(root, text='Film Thickness Estimator', font=('Times New Roman', 24, 'bold'), fg='white', bg='#d00000')

shotsLabel = Label(root, text='# of laser shots:', font=('Times New Roman', 16), fg='white', bg='#d00000')
shotsEntry = Entry(root, font=('Times New Roman', 16), width=15)
shots_unitsLabel = Label(root, text='shots', font=('Times New Roman', 16), fg='white', bg='#d00000')

pressLabel = Label(root, text='O₂ growth pressure:', font=('Times New Roman', 16), fg='white', bg='#d00000')
pressEntry = Entry(root, font=('Times New Roman', 16), width=15)
pressEntry.insert(0, '70')
press_unitsLabel = Label(root, text='mTorr', font=('Times New Roman', 16), fg='white', bg='#d00000')

tempLabel = Label(root, text='Growth temperature:', font=('Times New Roman', 16), fg='white', bg='#d00000')
tempEntry = Entry(root, font=('Times New Roman', 16), width=15)
tempEntry.insert(0, '890')
tempEntry.config(cursor='arrow', state=DISABLED)
temp_unitsLabel = Label(root, text='°C', font=('Times New Roman', 16), fg='white', bg='#d00000')

nrgLabel = Label(root, text='Laser energy:', font=('Times New Roman', 16), fg='white', bg='#d00000')
nrgEntry = Entry(root, font=('Times New Roman', 16), width=15)
nrgEntry.insert(0, '195')
nrgEntry.config(cursor='arrow', state=DISABLED)
nrg_unitsLabel = Label(root, text='mJ', font=('Times New Roman', 16), fg='white', bg='#d00000')

button = Button(root, text='Calculate', font=('Times New Roman', 20, 'bold'), fg='white', bg='#d00000', bd=4, relief=RAISED, 
                cursor='exchange', activebackground='black', activeforeground='#d00000', command=calculate_thickness)

readout = Label(root, font=('Times New Roman', 22, 'bold'), fg='white', bg='#d00000', bd=2, relief=SUNKEN, height=2, width=20)

CI_footnote = Label(root, text='95% CI: ± 1.11 nm', font=('Times New Roman', 16, 'italic'), fg='white', bg='#d00000')

title.grid(row=0, column=0, columnspan=3, pady=8, padx=4, sticky='n')

shotsLabel.grid(row=1, column=0, padx=2, pady=4, sticky='e')
shotsEntry.grid(row=1, column=1, pady=4)
shots_unitsLabel.grid(row=1, column=2, padx=2, pady=4, sticky='w')

pressLabel.grid(row=2, column=0, padx=2, pady=4, sticky='e')
pressEntry.grid(row=2, column=1, pady=4)
press_unitsLabel.grid(row=2, column=2, padx=2, pady=4, sticky='w')

tempLabel.grid(row=3, column=0, padx=2, pady=4, sticky='e')
tempEntry.grid(row=3, column=1, pady=4)
temp_unitsLabel.grid(row=3, column=2, padx=2, pady=4, sticky='w')

nrgLabel.grid(row=4, column=0, padx=2, pady=4, sticky='e')
nrgEntry.grid(row=4, column=1, pady=4)
nrg_unitsLabel.grid(row=4, column=2, padx=2, pady=4, sticky='w')

button.grid(row=5, column=0, columnspan=3, pady=16)
readout.grid(row=6, column=0, columnspan=3, pady=4)
CI_footnote.grid(row=7, column=0, columnspan=3, pady=0, sticky='n')

root.bind('<Return>', submit)

root.mainloop()
