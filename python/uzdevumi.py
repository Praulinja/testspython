def tests(parametrs):
    a = parametrs #darbibas ar parametriem
    return a #funkcijas rezultats

#print(tests("saule"))


def pirmais(par1, par2):
    reizinajums = par1*par2 
    summa = par1+par2
    if reizinajums<1000 : 
       return reizinajums
    else:
        return summa
#print("The result is", pirmais(40, 30) ) 

def otrais(): #def otrais(sakums = 0, beigas = 10, solis = 1)
    esosais = 0 
    ieprieksejais = 0
    for i in range(10): #range(sakums, beigas, solis)
        ieprieksejais = esosais 
        esosais = i 
        summa = ieprieksejais + esosais
        print("Current Number", esosais, "Previous Number", ieprieksejais, "Sum:", summa)
    return
#otrais()

def tresais(teksts):
    print("Sakotnejais teksts ir", teksts)
    print("Tikai pāra indeksa burti:")
    for i in teksts:
