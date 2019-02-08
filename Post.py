import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mailer:
      def __init__(self, sender_mail: str, password: str,
                         smtp = GMAIL_SMTP, imap = GMAIL_IMAP,
                         port_name = '587', inbox = 'inbox'):
            self.smtp = smtp
            self.imap = imap
            self.port_name = port_name
            self.sender_mail = sender_mail
            self.password = password
            self.inbox = inbox

      def send_message(self, subject: str, recipients: list, body: str):
            """send message"""
            message = MIMEMultipart()
            message['From'] = self.sender_mail
            message['To'] = ', '.join(recipients)
            message['Subject'] = subject
            message.attach(MIMEText(body))

            ms = smtplib.SMTP(self.smtp, self.port_name)
            # identify ourselves to smtp gmail client
            ms.ehlo()
            # secure our email with tls encryption
            ms.starttls()
            # re-identify ourselves as an encrypted connection
            ms.ehlo()
            ms.login(self.sender_mail, self.password)
            ms.sendmail(self.sender_mail, ms, message.as_string())
            ms.quit()

      def recieve_message(self, header: str = ''):
            """recieve message"""
            mail = imaplib.IMAP4_SSL(self.smtp)
            mail.login(self.sender_mail, self.password)
            mail.list()
            mail.select(self.inbox)

            criterion = f'(HEADER Subject "{header or "ALL"}")'

            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            mail.logout()

            return email_message

if __name__ == '__main__':
      mailer = Mailer('login@gmail.com', 'qwerty',
                            'smtp.gmail.com','imap.gmail.com')
      mailer.send_message('Subject',
                          ['vasya@email.com', 'petya@email.com'], 'Message', None)
      mailer.recieve_message()
      
