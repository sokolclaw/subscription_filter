import imaplib

class MailServer():

    def __init__(self):

        self.mail_servers = {
            'Mail.ru' : 'imap.mail.ru',
            'Яндекс.Почта': 'imap.yandex.ru',
            'Outlook': 'outlook.office365.com',
            'Exchange': 'mail.contoso.com',
            'Gmail': 'imap.gmail.com',
            'iCloud': 'imap.mail.me.com'
        }

        self.name = input('name: ')
        self.mail_password = input('password: ')

    def _choose_server(self):
        try:
            self.mail = input('Which mail? ')
            return self.mail_servers[self.mail]
        except (KeyError):
            print('Ошибка. Повторите ввод почтового сервиса')

    def autorize(self):
        self.imap = imaplib.IMAP4_SSL(self._choose_server())
        self.imap.login(self.name, self.mail_password)

if __name__ == '__main__':
    ms = MailServer()
    try:
        ms.autorize()
    except ValueError:
        print('Неверный логин или пароль')
    except NameError:
        print('Неправильное имя сервера')
    except (imaplib.IMAP4.error, ConnectionRefusedError):
        print('Нет доступа к почте. ' + 
        'Убедитесь, что даны разрешения на подключение сервиса к почтовому ящику, ' +
        'а также проверьте корректность логина и пароля')
