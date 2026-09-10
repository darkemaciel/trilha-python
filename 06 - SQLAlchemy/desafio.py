from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'desafio.db')

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True, unique=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, unique=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Float)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    fornecedor = relationship("Fornecedor")

engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Inserindo fornecedores
try:
    with Session() as session: # Usando a sessão corretamente com o gerenciador de contexto
        fornecedores = [
            Fornecedor(nome="Fornecedor A", telefone="12345678", email="contato@test.com", endereco="Rua A"),
            Fornecedor(nome="Fornecedor B", telefone="32564777", email="contato1@test.com", endereco="Rua B"),
            Fornecedor(nome="Fornecedor C", telefone="52487145", email="contato2@test.com", endereco="Rua C"),
            Fornecedor(nome="Fornecedor D", telefone="41526356", email="contato3@test.com", endereco="Rua D"),
            Fornecedor(nome="Fornecedor E", telefone="45124565", email="contato4@test.com", endereco="Rua E"),
            Fornecedor(nome="Fornecedor F", telefone="21457888", email="contato5@test.com", endereco="Rua F")
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e: # Capturando exceções do SQLAlchemy
    print(f"Erro ao inserir fornecedores: {e}")


# Inserindo produtos
try:
    with Session() as session:
        produtos = [
            Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
            Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
            Produto(nome="Produto 3", descricao="Descrição do Produto 3", preco=300, fornecedor_id=3),
            Produto(nome="Produto 4", descricao="Descrição do Produto 4", preco=400, fornecedor_id=4),
            Produto(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5)
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e:
    print(f"Erro ao inserir produtos: {e}")


with Session() as session:
    resultado = session.query(
        Fornecedor.nome,
        func.sum(Produto.preco).label('total_preco')
    ).join(Produto, Fornecedor.id == Produto.fornecedor_id
    ).group_by(Fornecedor.nome).all()

    for nome, total_preco in resultado:
        print(f"Fornecedor: {nome}, Total Preço: {total_preco}")