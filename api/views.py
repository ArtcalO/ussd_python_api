from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

@api_view(['POST'])
def uss_callback(request):
    session_id = request.data.get("sessionId", None)
    serviceCode = request.data.get("serviceCode", None)
    phoneNumber = request.data.get("phoneNumber", None)
    text = request.data.get("text", None)

    #serve menus based on text
    if text == "":
        menu_text = "CON Kaze kuri HOGI \n"
        menu_text += "1. Ikonte yawe\n"
        menu_text += "2. Nomero yanje \n"
        menu_text += "3. Ubufasha"

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
            menu_text = "Ja kuri https://hogi.bi."

    return HttpResponse(menu_text, content_type = 'text/plain')
