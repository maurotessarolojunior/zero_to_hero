def alter(alt):

    n = len(alt)
    f=''
    for x in range(n):
        if (x%2) ==0:
            f+=alt[x].upper()
        else:
            f+=alt[x]  
    return(f)
        
alter('maurotessarolojunior')