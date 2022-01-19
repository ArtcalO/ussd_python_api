montant = 0
code = ""
def menu_niveau1():
    menu_text = "Choisissez: \n"
    menu_text += "1.De l'agent: \n"
    menu_text += "2.Approuver la transaction: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau2():
    menu_text = "Entrer le code d'agent: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau3():
    menu_text = "Entrer le code PIN: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau4():
    menu_text = "Entrer le montant: \n"
    menu_text += "0. Retour"
    return menu_text

def menu_niveau5():
    menu_text = "Delai d'expiration de la transaction ou aucune transaction n'est lancée"
    return menu_text


def menu_niveau6():
    menu_text = f"Confirmation de retrait {montant} \n \
                par Niyungeko Carmel\n \
                 {code},frais: 450 Fbu. Choisissez : \n"
    menu_text += "1.Oui"
    menu_text += "2.Non"
    return menu_text

def menu_lumicash():
    menu_text = "Lumicash- Choisissez \n"
    menu_text += "1. Transfert\n"
    menu_text += "2. Retirer \n"
    menu_text += "3. Achat des unités \n"
    menu_text += "4. Payer les factures \n"
    menu_text += "5. Payer le marchand \n"
    menu_text += "6. Service bancaires \n"
    menu_text += "7. OBR \n"
    menu_text += "8. Mairie \n"
    menu_text += "9. Engrais \n"
    menu_text += "10. Service \n"

    return menu_text


def handler_menu_lumicash():
    print(menu_lumicash())
    text = input("")
    if text == '2':
        handler_niveau1()

def handler_niveau1():
    print(menu_niveau1())
    text=input("")
    if text=='1':
        handler_niveau2()
    elif text == '2':
      	handler_niveau3()
    elif text == '0':
        handler_menu_lumicash()

def handler_niveau2():
    print(menu_niveau2())
    text=input("")
    if text!='0':
        code=text
        handler_niveau4()
    elif text == '0':
        handler_menu_lumicash()

def handler_niveau3():
    print(menu_niveau3())
    text=input("")
    if text!='0':
        code=text
        handler_niveau5()
    elif text == '0':
        handler_menu_lumicash()

def handler_niveau4():
    print(menu_niveau4())
    text=input("")
    if text!='0':
        montant=text
        handler_niveau6()
    elif text == '0':
        handler_menu_lumicash()

def handler_niveau5():
    print(menu_niveau5())

def handler_niveau6():
    print(menu_niveau6())
    text=input("")
    if text =='1':
        print("Retrait avec success !")
    elif text == '2':
        print("Echec de retrait !")

def main():
    text = input("Entrer le code ussd :")
    if(text == "*163#"):
        handler_menu_lumicash()
    else:
        print("code invalide")

main()