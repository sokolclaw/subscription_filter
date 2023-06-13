import imaplib
    
mail_servers = {
    'Mail.ru' : 'imap.mail.ru',
    'Яндекс.Почта': 'imap.yandex.ru',
    'Outlook': 'outlook.office365.com',
    'Exchange': 'mail.contoso.com',
    'Gmail': 'imap.gmail.com',
    'iCloud': 'imap.mail.me.com'
}

name = input('name: ')
mail_password = input('password: ')
try:
    imap_server = mail_servers[input('Which mail? ')]
except (KeyError):
    print('Ошибка. Повторите ввод почтового сервиса')

if __name__ == '__main__':
    try:
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(name, mail_password)
    except ValueError:
        print('Неверный логин или пароль')
    except NameError:
        print('Неправильное имя сервера')
    except imaplib.IMAP4.error:
        print('Нет доступа к почте. ' + 
        'Убедитесь, что даны разрешения на подключение сервиса к почтовому ящику, ' +
        'а также корректность логина и пароля')

print(imap.select('INBOX'))