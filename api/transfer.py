montant = 0
code = ""
def menu_niveau1():
    menu_text = "Choisissez: \n"
    menu_text += "1.Revendeur: \n"
    menu_text += "2.End_user: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau2():
    menu_text = "Entrer le numero de telephone: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau3():
    menu_text = "Entrer le montant: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau4():
    menu_text = "Entrer le code PIN: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau5():
    menu_text = f"Confirmation de transfert {montant} \n \
                vers Niyungeko Carmel, 68 46 18 41 \n . Choisissez : \n"
    menu_text += "1.Oui"
    menu_text += "2.Non"
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
    if text == '1':
        handler_niveau1()

def handler_niveau1():
    print(menu_niveau1())
    text=input("")
    if text=='1':
        handler_niveau2()
    elif text == '2':
      	handler_niveau2()
    elif text == '0':
        handler_menu_ussd()


def handler_niveau2():
    print(menu_niveau2())
    text=input("")
    if text!='0':
        handler_niveau3()
    elif text == '0':
        handler_menu_ussd()

def handler_niveau3():
    print(menu_niveau3())
    text=input("")
    if text!='0':
        montant=text
        handler_niveau4()
    elif text == '0':
        handler_menu_ussd()

def handler_niveau4():
    print(menu_niveau4())
    text=input("")
    if text!='0':
        handler_niveau5()
    elif text == '0':
        handler_menu_ussd()

def handler_niveau5():
    print(menu_niveau5())
    text=input("")
    if text =='1':
        print("Transfert avec success !")
    elif text == '2':
        print("Echec de transfert !")

def main():
    text = input("Entrer le code ussd :")
    if(text == "*800#"):
        handler_menu_ussd()
    else:
        print("code invalide")

main()