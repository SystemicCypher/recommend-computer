from pyswip import Prolog
from os import system
from time import sleep


prolog = Prolog()
prolog.consult("computer-KB.pl")

choices = []
choices.append(input("What is your intended use for the computer?\n1) Gaming\n2) Workstation\n"))#Selects whether a gaming gpu is selected
if int(choices[-1]) == 1:
    choices.append(input("Do you want raytracing?\nY/N\n"))#Selects raytracing or not for GPU

else:
    choices.append(input("Do you need good computer graphics or the ability to process matrices?\nY/N\n"))#Will include the work GPUs
    
choices.append(input("Do you need your computer to boot quickly and have fast access to files?\nY/N\n"))#Selects SSDs or either

choices.append(input("Do you save large files? (Photos, videos, etc.)\nY/N\n")) #Splits b/w below 2tb

choices.append(input("Do you need to multitask or handle multiple large files\nY/N\n"))# splits b/w 16 and less or 16 and more

choices.append(input("Do you work with image rendering?\nY/N\n"))#Splits between 6 and more or 6 and less cores

#budget = input("What is your budget?\n")

selection = {
    'gfx' : [],
    'store' : [],
    'mem' : [],
    'proc' : []
}
system('clear')

print("Selecting...")
sleep(2)
system('clear')

if int(choices[0]) == 1:
    if choices[1] == 'Y':
        gfx = prolog.query("graphics(gaming, ray, X, Y, Z)")
    else:
        gfx = prolog.query("graphics(gaming, normal, X, Y, Z)")
else:
    if choices[1] == 'Y':
        gfx = prolog.query("graphics(work, W, X, Y, Z)")
    else:
        gfx = prolog.query("graphics(V, W, X, Y, 350)")

print("Suggested Graphics Cards:")
for g in gfx:
    selection['gfx'].append(g)
    print(g['X'] + " " + g['Y'])
sleep(1)
print("\nSuggested Storage:")
if choices[2] == 'Y':
    store = prolog.query("storage(ssd, X, Y)")
    for s in store:
        if choices[3] == 'Y':
            if s['X']  >= 2048:
                selection['store'].append(s)
                print('ssd '+ str(s['X']) + " gb")
        else:
            if s['X'] <= 2048:
                selection['store'].append(s)
                print('ssd '  + str(s['X']) + " gb")
        
else:
    store = prolog.query("storage(W, X, Y)")
    for s in store:
        if choices[3] == 'Y':
            if s['X']  >= 2048:
                selection['store'].append(s)
                print(s['W'] +' '+ str(s['X']) + " gb")
        else:
            if s['X'] <= 2048:
                selection['store'].append(s)
                print(s['W'] + ' '  + str(s['X']) + " gb")
sleep(1)      
print("\nSuggested Memory:")
mem = prolog.query("memory(X, Y)")
for m in mem:
    if choices[4] == 'Y':
        if m['X'] >= 16:
            selection['mem'].append(m)
            print(str(m['X']) + " gb" )
    else:
        if m['X'] <= 16:
            selection['mem'].append(m)
            print(str(m['X']) + " gb")
sleep(1)
print("\nSuggested Processors:")
proc = prolog.query("processor(X, Y, Z, W, V)")
for p in proc:
    if choices[5] == 'Y':
        if p['Z'] >= 8:
            selection['proc'].append(p)
            print(p['X'] + " " + p['Y'].replace('m', ' ') + " : " + str(p['Z']) + " threads and " + str(p['W']) + "mhz" )
    else:
        if p['Z'] <= 8:
            selection['proc'].append(p)
            print(p['X'] + " " + p['Y'].replace('m', ' ') + " : " + str(p['Z']) + " threads and " + str(p['W']) + " mhz" )

#print(selection)