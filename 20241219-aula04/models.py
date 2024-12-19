from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Date, ForeignKey


from config import Base

# Toda classe que deve ser mapeada para uma tabela, obrigatoriamente deve herdar da classe Base
class User(Base):

    # O atributo __tablename__ serve para indicar o nome que a tabela mapeada terá no banco de dados. Se não indicarmos o valor, o nome da tabela será o nome da classe
    __tablename__ = "users"

    # Abaixo definimos os atributos da classe, que serão mapeados para colunas na tabela. A principal diferença nesse caso da versão 1.* para 2.* do SQLAlchemy, é que na versão 2.* podemos utilizar o type hint de maneira mais eficiente.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    # Alteramos o retorno do método __repr__, que é chamado quando o objeto é exibido pelo código
    def __repr__(self):
        return f"<User {self.email}>"


class Profile(Base):

    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=True)