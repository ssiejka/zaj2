import pickle
import pathlib
from collections import OrderedDict

def load_animals(large_dataset=False):
    """
    :param bool large_dataset: Jeśli wartość to True zwraca 1E6 zwierząt, w
    przeciwnym razie 1E5. Test będzie odbywał się
    przy 1E6 zwierząt.
    :return: Lista zwierząt
    """
    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)

def przeliczenie_mas(mass,unit):
    if unit=='g':
        mass=mass/1000.0
    if unit=='mg':
        mass=mass/1e6
    if unit=='Mg':
        mass=mass*1000
    return mass

def porownanie(os1,os2):
    mass1,unit1=os1['mass']
    mass2,unit2=os2['mass']
    mass1=przeliczenie_mas(mass1,unit1)
    mass2=przeliczenie_mas(mass2,unit2)
    if(mass1>mass2):
        return 1
    elif(mass2>mass1):
        return 2
    else:
        return 0
    
    

def sortowanie(animal):
    typy={}
    c=0
    a={}
    b={}
    for i in range(0,len(animal)):
        klucz=animal[i]['genus']
        if animal[i]['genus'] in typy.keys():
            typy[klucz]+=1
            a[klucz].append(animal[i])
        else:
            typy[klucz]=1
            a[klucz]=[]
            a[klucz].append(animal[i])
            
    b=OrderedDict(sorted(a.items()))
    return (typy,b)
   

def filter_animals(animal_list):
    """
    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.
    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.
    Mususz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,
    Lista ta musi spełniać następujące warunki:
    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
    egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
* Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia
Wymaganie dla osób aspirujących na ocenę 5:
* Ilość pamięci zajmowanej przez program musi być stała względem
ilości elementów w liście zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
(można podejrzeć zawartość listy w interaktywnej sesji interpretera).
Do załadowania danych z listy możesz użyć metody `load_animals`.
:param animal_list:
    """
    zmiana_typu=False
    #animal_list=przeliczenie_mas(animal_list)
    typy,animal=sortowanie(animal_list)
    samiec={}
    samica={}
    wynik=[]
    a_klucz=''
    p_klucz=''
    for key in animal.keys():
        a_klucz=key
        if(a_klucz!=p_klucz):
            #Zapisz wyniki
            if(len(p_klucz)!=0):
                if(samica['name']>samiec['name']):
                    wynik.append(samiec)
                    wynik.append(samica)
                elif(samica['name']<samiec['name']):
                    wynik.append(samica)
                    wynik.append(samiec)
                else:
                    if(porownanie(samiec,samica)==1):
                        wynik.append(samica)
                        wynik.append(samiec)
                    else:
                        wynik.append(samiec)
                        wynik.append(samica)
            samica={}
            samiec={}
        for i in range(0,len(animal[key])):
            if(animal[key][i]['sex']=='male'):
                if(len(samiec)==0):
                    samiec=animal[key][i]
                else:
                    if(porownanie(animal[key][i],samiec)==2):
                        samiec=animal[key][i]
            if(animal[key][i]['sex']=='female'):
                if(len(samica)==0):
                    samica=animal[key][i]
                else:
                    if(porownanie(animal[key][i],samica)==2):
                        samica=animal[key][i]
        p_klucz=a_klucz

    if(samica['name']>samiec['name']):
        wynik.append(samiec)
        wynik.append(samica)
    elif(samica['name']<samiec['name']):
        wynik.append(samica)
        wynik.append(samiec)
    else:
        if(porownanie(samiec,samica)==1):
            wynik.append(samica)
            wynik.append(samiec)
        else:
            wynik.append(samiec)
            wynik.append(samica)
    return wynik
    
        
    
if __name__ == "__main__":
    animals = load_animals()

