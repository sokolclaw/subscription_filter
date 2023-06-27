import imaplib
import logging

from settings import config
from models import UserMailCredentials

logging.basicConfig(filename=config.filename, level=logging.INFO)

class MailServer():
    
    def __init__(self):
        self.servers = config
        self.mail = input('Какая почта?  ')
        self.saving = input('Сохраненные данные? yes/no ')
        self.name = input('Логин: ')
        if self.saving == 'yes':
            account = UserMailCredentials()  
            account.choose_email(self.mail)
            try:
                self.mail_password = account.take_password(self.name)
            except AttributeError:
                logging.exception('нет сохраненных аккаунтов в базе')
                print('нет сохраненных аккаунтов в базе')
        else:
            self.mail_password = input('Пароль: ')
            self.save_account = input('Сохранить данные аккаунта? yes/no ')
            if self.save_account == 'yes':
                account = UserMailCredentials()
                account.add_account(name=self.name, 
                    pas=self.mail_password, 
                    mail=self.mail)

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
        except AttributeError:
            logging.exception('нет сохраненных аккаунтов в базе')

    def _choose_server(self):
        try:
            mail = self.servers.mail_servers[self.mail]
            return imaplib.IMAP4_SSL(mail)
        except (KeyError):
            logging.exception('Неправильный ввод почтового сервиса')
            print('Ошибка. Повторите ввод почтового сервиса')


ms = MailServer()

   