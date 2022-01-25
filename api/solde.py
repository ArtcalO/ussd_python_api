def menu_niveau1():
    menu_text = "Entrer le code PIN: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau2():
    menu_text = "votre solde est 10000 Fbu"
    menu_text += "0.Retour"
    return menu_text

def menu_ussd():
    menu_text = "ussd- Choisissez \n"
    menu_text += "1. Transfert\n"
    menu_text += "2. Solde \n"
    menu_text += "3. Code \n"

    return menu_text

def handler_menu_ussd():
    print(menu_ussd())
    text = input("")
    if text == '2':
        handler_niveau1()

def handler_niveau1():
    print(menu_niveau1())
    text = input("")
    if text!='0':
        print(menu_niveau2())
    elif text == '0':
        handler_menu_ussd()


def main():
    text = input("Entrer le code ussd :")
    if(text == "*800#"):
        handler_menu_ussd()
    else:
        print("code invalide")

main()