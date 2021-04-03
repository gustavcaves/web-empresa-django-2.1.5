from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.mail import EmailMessage # Sirve para crear la estructura de un mensaje e incluye un método para enviarlo
from .forms import ContactForm 

# Create your views here.

def contact(request):
    # print("Tipo de metodo: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo Mensaje de Contacto",
                "De {} <{}>\n\nEscribió\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["django@hectorprofe.net"],
                reply_to=[email]
            )
            try:
                email.send()
                # Todo bien, redireccionaos al Ok
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido biel, redireccionaos al Fail
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})