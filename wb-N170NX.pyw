# This program does the necessary weight and balance calculations for an aircraft I built
from tkinter import *

def wbCalc():
    pilot=getdouble(p.get())
    fuel=getdouble(f.get())*6
    bags=getdouble(b.get())
    ew = 589.2
    totalwt=pilot+fuel+bags+ew
    moment = 34152.3 + bags * 102 + fuel * 46.45 + pilot * 78
    CG=moment/totalwt

    result=Tk()
    result.title("Results")
    Label(result, text="-------N170NX Weight and Balance results-------").grid(row=1,column=0)
    Label(result, text="Pilot weight: %s" % pilot).grid(row=2,column=0)
    Label(result, text="Fuel weight: %s" % fuel).grid()
    Label(result, text="Baggage weight: %s" % bags).grid()
    Label(result, text="Total Weight: %s lbs. (Maximum gross weight is 950 lbs.)"%totalwt).grid()
    Label(result, text="Calculated CG: %05.2f inches from datum. (Between 60.5-66.5 is acceptable.)"%CG).grid()
    result.mainloop()

if __name__ == '__main__':
    root=Tk()
    root.title('N170NX W&B Calculator')
    Label(root, text="Weight and Balance Calculator for N170NX").grid(row=0)

    p=float()
    Label(root, text="Pilot Weight (lbs.)").grid(row=1)
    p=Entry(root, textvariable=p)
    p.grid(row=1,column=1)

    f=float()
    Label(root, text="Fuel (gallons)").grid(row=2)
    f=Entry(root)
    f.grid(row=2,column=1)

    b=float()
    Label(root, text="Baggage (lbs.)").grid(row=3)
    b=Entry(root)
    b.grid(row=3,column=1)
    Button(root, text="Calculate",command=wbCalc).grid(row=5,column=1)
    root.mainloop()
