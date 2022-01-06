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
        menu_text = "CON What would you want to check \n"
        menu_text += "1. My Account \n"
        menu_text += "2. My phone number \n"
        menu_text += "3. My branch"

    elif text =="1":
        menu_text = "CON Choose the account information that you want to view \n"
        menu_text += "1. My Account balance\n"
        menu_text += "2. My Account number \n"

    elif text =="2":
        menu_text = "END Your phone number is "+phoneNumber

    elif text =="1*1":
        menu_text = "END Your account number is ACOO10SWO2101."

    elif text =="1*2":
            menu_text = "END Your BALANCE  is KES 120/-"

    return HttpResponse(menu_text, content_type = 'text/plain')
 