import array

def count(teksti):
    teksti=teksti.lower()
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


def reverse(teksti):
    r_string=teksti[len(teksti)::-1]
    
    return r_string.strip()

def palindrome(teksti):
    teksti=teksti.lower()
    r_teksti=reverse(teksti).lower()

    if(teksti==r_teksti):
        return True
    else:
        return False
