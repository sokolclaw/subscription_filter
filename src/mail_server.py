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
        self._search_mail_uid()

        '''Поиск и сбор писем в почте'''
    def _take_folders(self):
        self.mail_folders = self.imap.list()
        self.folders_list = []

        if self.mail_folders[0] != 'OK':
            logging.exception('imap.list != \'OK\', не удалось выгрузить папки')
            raise Exception('Нет доступа к папкам')
        
        for folder in self.mail_folders[1]:
            self.cut_folder = str(folder).split('" ')
            self.folders_list.append(self.cut_folder[1][:-1])
        
        return self.folders_list

    def _search_mail_uid(self):
        taken_folders = self._take_folders()
        mail_uid = []
        
        for folder in taken_folders:
            sum_mail = self.imap.select(folder)
            if sum_mail[1] == [b'0']:
                print(f'В папке {folder} нет писем')
                continue
            numbers = str(self.imap.uid('search', "ALL")[1][0]).split('\'')[1].split(' ')
            [mail_uid.append(number) for number in numbers]

        return mail_uid
        


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
