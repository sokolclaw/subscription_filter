
class Settings():
    
    def __init__(self):

        self.mail_servers = {
            'Mail.ru' : 'imap.mail.ru',
            'Яндекс.Почта': 'imap.yandex.ru',
            'Outlook': 'outlook.office365.com',
            'Exchange': 'mail.contoso.com',
            'Gmail': 'imap.gmail.com',
            'iCloud': 'imap.mail.me.com'
        }

        self.filename = 'mail.log'


config = Settings()