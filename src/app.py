from mail_server import MailServer
from letters import Letters


def main():

    mail = input('Какая почта?  ')
    saving = input('Сохраненные данные? yes/no ')
    name = input('Логин: ')
    mail_password = input('Пароль: ')
    save_account = input('Сохранить данные аккаунта? yes/no ')

    ms = MailServer(mail, saving, name, mail_password, save_account)
    letters = Letters(ms.autorize())

    return letters.get_letters()


if __name__ == '__main__':
    main()

