from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import mail_info
import json

# Create your views here.
def send_email(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        try:
            from_email = "eledenhelper@gmail.com"
            password = "kcgu zmff bmxi xlxe"

            subject = "Confirmación de Pago Exitoso"

            message = """
Asunto: Confirmación de Pago Exitoso

Estimado/a [Nombre del Cliente],

Nos complace informarte que hemos recibido con éxito tu pago para patrocinar un animal. Agradecemos tu confianza en El Eden.



Si tienes alguna pregunta o inquietud relacionada con tu pago, no dudes en ponerte en contacto con nuestro equipo de soporte a través de eledenhelper@gmail.com.

Agradecemos tu negocio y esperamos seguir sirviéndote en el futuro.

Saludos cordiales,

El-eden
eledenhelper@gmail.com
eledenapi.com
"""


            
            to_email = data['email']

            mail_structure = MIMEMultipart('alternative')
            mail_structure['From'] = from_email
            mail_structure['To'] = to_email
            mail_structure['Subject'] = subject

            mail_structure.attach(MIMEText(message, 'plain'))

            server_smtp = 'smtp.gmail.com'  
            port_smtp = 587  

            server = smtplib.SMTP(server_smtp, port_smtp)
            server.starttls()

            server.login(from_email,password)
            server.sendmail(from_email, to_email, mail_structure.as_string())

            server.quit()

            new_mail_info = mail_info.objects.create(user_id=data['username'],subject=subject,message=message)
            new_mail_info.save()

            return JsonResponse({"status": "Correo enviado exitosamente"})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error al decodificar JSON en la solicitud'}, status=400)
    else:
        return JsonResponse({'error': 'Método de solicitud no permitido'}, status=405)



def button(request):
    return render(request, 'button.html')

