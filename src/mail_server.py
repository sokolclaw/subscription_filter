import imaplib
import logging

from settings import config

logging.basicConfig(filename=config.filename, level=logging.INFO)

class MailServer():
    
    def __init__(self):

        self.servers = config
        self.name = input('Логин: ')
        self.mail_password = input('Пароль: ')

    def _choose_server(self):
        try:
            self.mail = input('Какая почта?  ')
            return self.servers.mail_servers[self.mail]
        except (KeyError):
            logging.exception('Неправильный ввод почтового сервиса')
            print('Ошибка. Повторите ввод почтового сервиса')

    def autorize(self):
        self.imap = imaplib.IMAP4_SSL(self._choose_server())
        self.imap.login(self.name, self.mail_password)
        print(self.imap.select('INBOX'))

if __name__ == '__main__':
    ms = MailServer()
    try:
        ms.autorize()
    except ValueError:
        logging.exception('Неверный логин или пароль')
        print('Неверный логин или пароль')
    except NameError:
        logging.exception('Неправильное имя сервера')
        print('Неправильный ввод названия почтового сервиса')
    except (imaplib.IMAP4.error, ConnectionRefusedError, TypeError):
        logging.exception('Нет доступа к почте')
        print('''Нет доступа к почте. Убедитесь, что даны разрешения на подключение
        сервиса к почтовому ящику,а также проверьте корректность логина и пароля''')
