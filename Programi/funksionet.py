import array
import datetime
from random import random

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


def time():
    koha_obj=datetime.datetime.now()

    koha=str(koha_obj.hour)+":"+str(koha_obj.minute)+":"+str(koha_obj.second)

    return 'Koha e serverit eshte:'+koha

def game():
    lista_numrat=[]
    random_number=0
    nr_count=0
    while nr_count<5:
        random_number=int((random()*35)+1)
        lista_numrat.append(random_number)
        nr_count+=1

    return lista_numrat


def GCF(number1,number2):
    smaller_number=number1
    if number1<number2: smaller_number=number1
    elif number2<number1:smaller_number=number2

    gcf=1

    while smaller_number>0:
        if number1%smaller_number==0 and number2%smaller_number==0:
            gcf=smaller_number
            break
        smaller_number-=1
    
    return print(f'GCF per numrat {number1} dhe {number2} eshte:{gcf}')

def convert_cmToFeet(number):
    shndrrimi=round(number/30.48,3)
    return print(f'Shndrrimi i {number} centimetrave ne feet eshte:{shndrrimi}')

def convert_feetToCm(number):
    shndrrimi=round(number*30.48,3)
    return print(f'Shndrrimi i {number} feet ne centimetrave eshte:{shndrrimi}')

def convert_kmToMiles(number):
    shndrrimi=round()
    return

def convert_kmToMiles(number):
    shndrrimi=round(number/1.609,2)
    return print(f'Shndrrimi i {number} kilmetrave ne miles eshte:{shndrrimi}')

def convert_milesToKm(number):
    shndrrimi=round(number*1.609,2)
    return print(f'Shndrrimi i {number} miles ne kilometra eshte:{shndrrimi}')