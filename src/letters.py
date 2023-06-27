import email

import logging

class Letters:

    def __init__(self, server):
        self.imap = server

    def get_letters(self):
        try:
            self.taken_mailboxes = self._take_mailboxes()        
            for mailbox in self.taken_mailboxes:
                if not self._choose_mailbox(mailbox):
                    continue
                self.letters_id = self._get_uid_list()
                [self._taking_letter(num) for num in self.letters_id if num in self.numbers]
        except AttributeError:
            logging.exception('NoneType вместо папок')

    def _take_mailboxes(self):
        self.mailboxes = self.imap.list()
        self.mailboxes_list = []

        if self.mailboxes[0] != 'OK':
            logging.exception('imap.list != \'OK\', не удалось выгрузить папки')
            raise Exception('Нет доступа к папкам')
        
        for folder in self.mailboxes[1]:
            self.cut_folder = str(folder).split('" ')
            self.mailboxes_list.append(self.cut_folder[1][:-1])
        
        return self.mailboxes_list

    def _choose_mailbox(self, folder):
        self.sum_mail = self.imap.select(folder)
        if self.sum_mail[1] == [b'0']:
            # print(f'В папке {folder} нет писем')
            return False
        return True
    
    def _get_uid_list(self):
        self.numbers = str(self.imap.uid('search', 'ALL')[1][0]).split('\'')[1].split(' ')
        self.letters_uid = [number for number in self.numbers]
        return self.letters_uid
    
    def _taking_letter(self, num):
        res, msg = self.imap.uid('fetch', num, '(RFC822)')
        msg = email.message_from_bytes(msg[0][1])
        self.letter_from = msg['Return-path']
        self.unsubscribe = msg['List-Unsubscribe']
        return self.unsubscribe