import random

def genNormal(von, bis):
    print(random.randint(von, bis))


def genEinschraenkend():
    vonbis = []
    einschraenkungen = []
    vonbis = input("Geben Sie die erste Zahl ein:")
    vonbis = input("Geben Sie die zweite Zahl ein:")
    einschränken = input("Wollen Sie Ihre Eingabe einschränken? yes? no?:")
    match einschränken:
        case "yes":
            while einschränken != "no":
                einschraenkungen = input("Geben Sie ihre Einschränkung ein:")
                einschränken = input("Wollen Sie Ihre Eingabe weiter einschränken? yes? no?:")
        case _:
            print("keine Einschränkung")
    
    print(random.choice([i for i in vonbis if i not in einschraenkungen]))


genEinschraenkend()