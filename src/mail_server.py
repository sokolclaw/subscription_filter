import imaplib
import logging

from settings import config

logging.basicConfig(filename=config.filename, level=logging.INFO)

class MailServer():
    
    def __init__(self):
        self.servers = config
        self.name = input('Логин: ')
        self.mail_password = input('Пароль: ')
        self.mail = input('Какая почта?  ')
        self.save_account = input('Сохранить данные аккаунта? yes/no ')


    def autorize(self):
        try:
            self.imap = self._choose_server()
            self.imap.login(self.name, self.mail_password)
            return self.imap
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

    def _choose_server(self):
        try:
            mail = self.servers.mail_servers[self.mail]
            return imaplib.IMAP4_SSL(mail)
        except (KeyError):
            logging.exception('Неправильный ввод почтового сервиса')
            print('Ошибка. Повторите ввод почтового сервиса')

ms = MailServer()

   