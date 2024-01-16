def dienas_mekletajs (sis_gads, sis_menesis, sis_datums, si_diena, dz_gads, dz_menesis, dz_datums):
    menesu_dienu_skaits = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #Skaitām, cik dienas ir pagājušas
    #Pārbaude, vai šogad jau ir bijusi dzimšanas diena
    

    pagajusas_dienas = 0
    pagajusie_gadi = sis_gads-dz_gads

    if vai_datums_pagajis(sis_menesis, sis_datums, dz_menesis, dz_datums) == False:
        pagajusie_gadi = pagajusie_gadi-1


def vai_datums_pagajis(sis_menesis, sis_datums, dz_menesis, dz_datums)
    if sis_menesis>dz_menesis:
        return True
    if sis_menesis<dz_menesis:
        return False 
    if sis_datums<dz_datums:
        return False
        return True

    pagajusas_dienas = pagajusie_gadi*365

    garie_gadi = 0
    parbaudes_gads_sakums = dz_gads
    if vai_datums_pagajis(dz_menesis, dz_datums, 2, 29) == True:
        parbaudes_gads_sakums = parbaudes_gads_sakums+1
    

    parbaudes_gads_beigas = sis_gads
    if vai_datums_pagajis(sis_menesis, sis_datums, 2, 29) == False:
        parbaudes_gads_beigas = sis_gads-1

    for gads in range(dz_gads, sis_gads, 1):
        if gads % 4 == 0:
            garie_gadi = garie_gadi+1
        if gads % 100 == 0 and gads % 400 !=0:
            garie_gadi = garie_gadi-1

#cik menesi kops pedejas dzimsanas dienas
    if sis_menesis>dz_menesis:
        pilni_menesi = sis_menesis-dz_menesis
    else: 
        pilni_menesi = sis_menesis+12-dz_menesis

    if vai_datums_pagajis(1, sis_datums, 1, dz_datums) == False
        pilni_menesi -= 1

    dienas_menesos = 0 


    menesis = dz_menesis
    while menesis != sis_menesis:
        if menesis == 13:
            menesis=1
        dienas_menesos += menesu_dienu_skaits[menesis]
        menesis +=1

    pagajusas_dienas += dienas_menesos

    if sis_datums>dz_datums:
        pagajusas_dienas += sis_datums-dz_datums
    else:
        pagajusas_dienas = sis_datums + menesu_dienu_skaits[sis_menesis-1] - dz_datums

print("KOPŠ DZIMŠANAS IR PAGĀJUŠAS")

    dienu_atlikums = pagajusas_dienas % 7

dz_diena = si_diena-dienu_atlikums
if dz_diena <=0:
    dz_diena


return "OK"
