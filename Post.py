import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class Mailer:
      def __init__(self, sender_mail, password):
            self.GMAIL_SMTP = "smtp.gmail.com"
            self.GMAIL_IMAP = "imap.gmail.com"
            self.sender_mail = sender_mail
            self.password = password

      def send_message(subject: str, recipients: list, body: str, header: str):
            """send message"""
            message = MIMEMultipart()
            message['From'] = self.sender_mail
            message['To'] = ', '.join(recipients)
            message['Subject'] = subject
            message.attach(MIMEText(body))

            ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
            # identify ourselves to smtp gmail client
            ms.ehlo()
            # secure our email with tls encryption
            ms.starttls()
            # re-identify ourselves as an encrypted connection
            ms.ehlo()
            ms.login(self.sender_mail, self.password)
            ms.sendmail(self.sender_mail, ms, message.as_string())
            ms.quit()

      def recieve_message(header: str):
            """recieve message"""
            mail = imaplib.IMAP4_SSL(self.GMAIL_SMTP)
            mail.login(self.sender_mail, self.password)
            mail.list()
            mail.select("inbox")

            criterion = ''
            if header:
                  criterion = f'HEADER Subject "{header}s"'
            else:
                  criterion = 'ALL'

            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
            mail.logout()

if __name__ == '__main__':
      mailer = Mailer('login@gmail.com', 'qwerty')
      mailer.send_message('Subject', ['vasya@email.com', 'petya@email.com'], 'Message', None)
      mailer.recieve_message(None)
      
