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
    def transelt():
        pass
    def antierror():
        pass
    def test():
        pass
list_Rus=loe_failist("Rus.txt")
list_Ing=loe_failist("Ing.txt")
print(list_Rus)
print(list_Ing)
while True:
    v=input("Перевод-1, Новое слово-2, Исправить ошибку-3, Проверка знаний-4, выход-5 ==>")
    if v=="1":
        transelt()
    elif v=="2":
        rus_sona=input("введи слово на рус==>")
        ing_sona=input("введи слово на анг==>")
        list_Rus=salvesta_fali("Rus.txt",rus_sona)
        list_Ing=salvesta_fali("Ing.txt",ing_sona)
        print(list_Rus)
        print(list_Ing)
    elif v=="3":
        antierror()
    elif v=="4":
        test()
    elif v=="5":
            break
