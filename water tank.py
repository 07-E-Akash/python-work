h=10
r=5
f=10
t=eval(input('enter the time'))
Vtank=3.14*r**2*h
Vwtr=f*t
if Vwtr < Vtank:
    print('under flow condition')
    ht = Vwtr/3.14*r**2
    hr = h-ht
    print(f'filled height (ht) and remaining height {hr}')
elif Vwtr == Vtank:
    print('tank full')
else:
    print('over flow condition')
    print('volume of' ,Vwtr-Vtank)
