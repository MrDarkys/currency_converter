from converte_wallet import Converter

c = Converter()

# справка по валютам
spravka = """
USD - доллар
EUR - евро
TJS — сомони
RUB — рубли
KZT — тенге
AZN — манат
GEL — лари
AMD — драм
CNY — юань
THB — бат
IDR — рупия
MYR — ринггит
PKR — рупия (пакистанская)
INR — рупия (индийская)
BRL — реал (бразильский)
TRY — лира (турецкая)
EGP — фунт (египетский)
UAH — гривна
UZS — сум
VND — донг
PHP — песо (филиппинский)
KGS — сом
"""
    
# сам конвертер
def convert(sum, reg1, reg2):
    value = c.convert(sum, reg1, reg2)
    result = f"ИТОГ: {value}"
    return result

print("Привет и добро пожаловать в конвертер валют!!!\n")

while True:
    try:
        question = input("Нужна помощь в валютах? (Д/Н): ")
        if question.upper() == "Д" or question.upper() == "Y":
            print(spravka)
        else:
            try:
                summa = int(input("Введите сумму для конвертации: "))
            except:
                print("Сумма должна быть числом!\n")
                
            reg1 = input("\nВведите вашу валюту (RUB/TJS/KZT и тд.): ")
            reg2 = input("\nВведите валюту для конвертации (RUB/TJS/KZT и тд.): ")

            try:
                res = convert(summa, reg1, reg2)
                print("\n", res, "\n")
            except:
                print("\nОшибка в типах данных которые вы ввели!\n")
    except:
        print("\n\nПока!")
        break