import sqlalchemy as sqa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = sqa.Column(sqa.String(36), primary_key=True)
    first_name = sqa.Column(sqa.Text)
    last_name = sqa.Column(sqa.Text)
    gender = sqa.Column(sqa.Text)
    email = sqa.Column(sqa.Text)
    birthdate = sqa.Column(sqa.Text)
    height = sqa.Column(sqa.Float)


def connect_db():

    engine = sqa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data():

    print("Нужно Записать ваши данные")
    first_name = input("Введи своё имя: ")
    last_name = input("Теперь фамилию: ")
    gender = input("Введите свой пол (варианты: Male, Female) ")
    email = input("Ещё необходим адрес ел. почты: ")
    birthdate = input("Введите дату рождения в формате ГГГГ-ММ-ДД:")
    height = input("Укажите свой рост в метрах? (Для разделения целой и десятичной части используй точку)")
    user = User(
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )
    return user


def main():

    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Данные сохранены в базе данных!")


if __name__ == "__main__":
    main()