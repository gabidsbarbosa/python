from email.message import EmailMessage
from app import password
import ssl
import smtplib

email_sender = ''
email_passaword = password

email_receiver = ''

subject = 'poema No fim de tudo dormir, de Álvaro de Campos'
body = """
No fim de tudo dormir.
No fim de quê?
No fim do que tudo parece ser...,
Este pequeno universo provinciano entre os astros,
Esta aldeola do espaço,
E não só do espaço visível, mas até do espaço total.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_passaword)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
