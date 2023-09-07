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
    for i in range(0, len(teksts), 2):
        print (teksts[i])
    return
#tresais("mergaite")


def ceturtais(teksts, n):
    print("Teksts", teksts)
    print("Nonemot pirmos", n, "burtus sanāk:", teksts[n:]) #n novietojums nosaka kurus burtus nonems ja pirms kola pedejos, ja pec pirmos
    return

#ceturtais("mergaite", 4) #4 norada cik burtus nonem


def piektais(saraksts):
    print("Dotais saraksts", saraksts)
    #if saraksts[0] == saraksts[-1]:
    print("Result is", saraksts[0]==saraksts[-1])
    return

skaitli1 = [10, 20, 30, 40, 10]
skaitli2 = [75, 65, 35, 75, 30]

piektais(skaitli1)