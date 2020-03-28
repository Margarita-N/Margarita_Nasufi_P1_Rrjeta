def count(teksti):
    shkronjat_zanore=('a','e','i','o','u','y')
    shkronjat_bashketingellore=('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z')

    zanoret=0
    bashketingelloret=0
    for shkronja in teksti:
        if shkronja in shkronjat_zanore:
            zanoret=zanoret+1
        elif shkronja in shkronjat_bashketingellore:
            bashketingelloret=bashketingelloret+1
        else:
            continue

    rezultati='Numri i zanoreve eshte:'+str(zanoret)+'\nNumri i bashketingelloreve eshte:'+str(bashketingelloret)

    return rezultati