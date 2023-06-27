from sqlalchemy import Column, Integer, String
from data_base import Base, engine, db_session

class UserMailCredentials(Base):
    __tablename__ = 'UserMailCredentials'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    mail_server = Column(String)

    def add_account(self, name, pas, mail):
        self.account = UserMailCredentials(username=name, password=pas, mail_server=mail)
        db_session.add(self.account)
        db_session.commit()

class MailUnsubExceptions(Base):
    __tablename__ = 'MailUnsubExceptions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    mail_from = Column(String)

    def add_accout(self, user_data):
        account = MailUnsubExceptions(user_data)
        db_session.add(account)
        db_session.commit()
    
class OperationHistory(Base):
    __tablename__ = 'OperationHistory'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    uid = Column(Integer)

    def add_accout(self, user_data):
        account = OperationHistory(user_data)
        db_session.add(account)
        db_session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)