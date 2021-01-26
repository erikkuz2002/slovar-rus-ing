def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def salvesta_fali(f,text):
    fail=open(f,"a",encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas

def uued_sonad():
    rus_sona=input("введи слово на рус==>")
    ing_sona=input("введи слово на анг==>")
    list_Rus=salvesta_fali("Rus.txt",rus_sona)
    list_Ing=salvesta_fali("Ing.txt",ing_sona)
    print(list_Rus)
    print(list_Ing)
    return list_Rus, list_Ing

def transelt(list_Rus,list_Ing):
    slovo=input("введите слово для перевода==>")
    if slovo in list_Rus:
        ind=list_Rus.index(slovo)
        print(f"{slovo}-{list_Ing[ind]}")
    elif slovo in list_Ing:
        ind=list_Ing.index(slovo)
        print(f"{slovo}-{list_Rus[ind]}")
    else:
        print(f"{slovo.upper()} Сожелению нет таких слов в анг. и рус. может добавить слово")
        v=input("желаете добавить слово в словарь")
        if v.lower()=="да": uued_sonad()

def antierror():
    v=input("какую хотите исправит рус-1, анг-2")
    if =="1":
        ruseerror=in
        
    else:
        ingeerror


    slovoerror=input("какую слово хотите исправит")

def test():
    pass

list_Rus=loe_failist("Rus.txt")
list_Ing=loe_failist("Ing.txt")
print(list_Rus)
print(list_Ing)
while True:
    v=input("Перевод-1, Новое слово-2, Исправить ошибку-3, Проверка знаний-4, выход-5 ==>")
    if v=="1":
        transelt(list_Rus,list_Ing)
    elif v=="2":
        list_Rus, list_Ing=uued_sonad()
    elif v=="3":
        antierror()
    elif v=="4":
        test()
    elif v=="5":
            break
