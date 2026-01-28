from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import MensajeContacto

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        
        if nombre and email and asunto and mensaje:
            # 1. Guardar en Backend (Base de Datos)
            MensajeContacto.objects.create(
                nombre=nombre,
                email=email,
                asunto=asunto,
                mensaje=mensaje
            )
            
            # 2. Enviar por Correo Electrónico
            cuerpo_email = f"""
            Nuevo mensaje de contacto desde el sitio web de la Alcaldía de Suárez:
            
            Nombre: {nombre}
            Correo: {email}
            Asunto: {asunto}
            
            Mensaje:
            {mensaje}
            
            ---
            Este es un mensaje generado automáticamente.
            """
            
            try:
                send_mail(
                    subject=f"Portal Web: {asunto}",
                    message=cuerpo_email,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Si el correo falla, registramos el error pero no bloqueamos la experiencia del usuario
                # ya que el mensaje ya quedó guardado en la Base de Datos.
                print(f"Error enviando email: {e}")

            messages.success(request, 'Tu mensaje ha sido enviado correctamente y una copia ha sido enviada al correo institucional.')
            return redirect('contacto:index')
        else:
            messages.error(request, 'Por favor, completa todos los campos.')
            
    return render(request, 'contacto/index.html')
