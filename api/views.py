from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

class Lumicash():
    def main_menu_lumicash(text):
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

        if text == 1:
            Transfert.niveau1()
        return menu_text

class Transfert():
    def niveau1():
        menu_text = "Entrer le numero de telephone: \n"
        menu_text += "0. Retour \n"


        return menu_text



@api_view(['POST'])
def uss_callback(request):
    session_id = request.data.get("sessionId", None)
    serviceCode = request.data.get("serviceCode", None)
    phoneNumber = request.data.get("phoneNumber", None)
    text = request.data.get("text", None)

    #serve menus based on text
    if text == "*163#":
        menu_text = Lumicash.main_menu_lumicash(text)

    elif text =="1":
        menu_text = "CON Cagura ivyo ushaka kuraba \n"
        menu_text += "1. Ubutunzi bwanje\n"
        menu_text += "2. Nomero ya konti yanje \n"

    elif text =="2":
        menu_text = "END Inomero ya phone yawe : "+phoneNumber

    elif text =="1*1":
        menu_text = "END Ubutunzi bwanyu ni : 200 000 Fbu"

    elif text =="1*2":
            menu_text = "END Inomero ya konti yawe : HO-A10219-GI."

    elif text =="3":
            menu_text = "END Ja kuri https://hogi.bi."
    return HttpResponse(menu_text)


