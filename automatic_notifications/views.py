from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import mail_info

# Create your views here.
def send_email(request):


    from_email = "eledenhelper@gmail.com"
    password = "kcgu zmff bmxi xlxe"

    subject = "prueba"
    message = "esta es una prueba de correo automatico"
    to_email = "roncancio.juan@correounivalle.edu.co"


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

    new_mail_info = mail_info.objects.create(user_id="1",subject=subject,message=message)
    new_mail_info.save()

    return JsonResponse({"status": "Correo enviado exitosamente"})



def button(request):
    return render(request, 'button.html')

