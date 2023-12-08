import smtplib as smtp
from email.mime.text import MIMEText
from email.header import Header

def send_message(concert, mail):
  login = 'okyxxxf@gmail.com'
  password = 'zkmd luus htjs lcjx'

  server = smtp.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(login, password)

  subject = 'Билет успешно забронирован!'
  text = 'Билет на концерт ' + concert.name + ' успешно забронирован на дату ' + concert.date.strftime("%Y-%m-%d")

  mime = MIMEText(text, 'plain', 'utf-8')
  mime['Subject'] = Header(subject, 'utf-8')

  server.sendmail(login, mail, mime.as_string())
