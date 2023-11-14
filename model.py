from typing import Optional, List
from sqlmodel import SQLModel ,or_, Field, create_engine, Session, select, Relationship
from sqlalchemy import func

db = SQLModel()

def configure(app):
    app.db = db



class Person(SQLModel, table=True):
	"""docstring for Person  -  tabela para usuarios do sistema"""
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	password:str
	registration:str
	types:str  # do usuario, master ou comum
	todos:List['Todo']=Relationship()





class Todo(SQLModel, table=True):
	"""
	docstring for Todo   -   tabela para as acoes do sistema,
	adicionar valor
	devolver valor 
	"""
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str
	observation: str
	nature:str
	value:str
	date:str
	status:str
	person_id: int = Field(foreign_key='person.id')
	

class User(SQLModel, table=True):
	"""docstring for User  -  tabela para cotistas"""
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	cpf:str
	email:str
	birth:str
	telephone:str
	cell:str
	status:str
	code:str
	adresses:List['Address']=Relationship()
	accounts:List['Account']=Relationship()
	quotas:List['Quota']=Relationship()

class Address(SQLModel, table=True):
	"""docstring for Address"""
	id: Optional[int] = Field(default=None, primary_key=True)
	street:str
	number:str 
	city:str
	state:str
	cep:str
	user_id: int = Field(foreign_key='user.id')


class Account(SQLModel, table=True):
	"""docstring for Account"""
	id: Optional[int] = Field(default=None, primary_key=True)
	bank:str
	agency:str
	number_account:str
	user_id: int = Field(foreign_key='user.id')


class Quota(SQLModel, table=True):
	"""docstring for Quota"""
	id: Optional[int] = Field(default=None, primary_key=True)
	code:str
	date:str
	grouping:str #para agrupar tipo 'z a b' 
	status:str
	old:str
	user_id: int = Field(foreign_key='user.id')


engine = create_engine('sqlite:///db.db')

SQLModel.metadata.create_all(engine)

def create_shareholder(
	name:str, 
	email: str, 
	cpf: str, 
	birth: str, 
	telephone: str, 
	cell: str, 
	
	):
	with Session(engine) as session:
		session.add(User(name=name, email=email, cpf=cpf, birth=birth, telephone=telephone, cell=cell, status = "ativo" , code = "123"))
		session.commit()


def push_shareholder(
	name:str, 
	email: str, 
	cpf: str, 
	birth: str, 
	telephone: str, 
	cell: str, 
	code: str, 
	street: str, 
	number: str, 
	cep: str, 
	city: str, 
	state: str, 
	
	):
	with Session(engine) as session:
		user = User(name=name, email=email, cpf=cpf, birth=birth, telephone=telephone, cell=cell, code = code, status = "ativo" )
		session.add(user)

		session.commit()
		session.refresh(user)
		adress = Address(street = street, number = number, cep = cep,city=city,state=state, user_id=user.id)
		
		session.add(adress)
		session.commit()

def push_quote(
	code:str,
	grouping:str,
	user:str,
	date:str

	
	):
	with Session(engine) as session:
		print(user)
		query = select(User ).where(User.code==user ) 
		us = session.exec(query).first()
		print(us)
		"""
		quote = Quota(code=code,date=date, grouping=grouping, user_id = user)
		session.add(quote)

		session.commit()
		session.refresh(user)
		adress = Address(street = street, number = number, cep = cep,city=city,state=state, user_id=user.id)
		
		session.add(adress)
		session.commit()
		"""



def update_shareholder(
	name:str, 
	email: str, 
	cpf: str, 
	birth: str, 
	telephone: str, 
	cell: str, 
	id
	
	):
	with Session(engine) as session:
		
		user = session.get(User, id)
		if name:
			user.name = name
		if email:
			user.email = email
		if cpf:
			user.cpf = cpf
		if birth:
			user.birth = birth
		if telephone:
			user.telephone = telephone
		if cell:
			user.cell = cell
		session.commit()
		


def list_users_shareholder(filters:str ):
	with Session(engine) as session:
		query = select(User)
		if filters:
			query = query.where( or_(User.name.contains(filters),User.cpf.contains(filters)) )

		
		data = session.exec(query).all()
		return data

def view_user_shareholder(id:str):
	with Session(engine) as session:
		query = select(User)
		query = query.where(User.id == id )

		data = session.exec(query).first()
		return data

"""

def read_norm_list(description:str=None , tags:str=None, page:str = None):
	with Session(engine) as session:	
		query= select(
			Norm_iten_sub,
			Norm_iten.title,
			Norm_iten.iten,
			).join(Norm_iten)

		if description:
			query = query.where( Norm_iten_sub.description.contains(description))
		if tags and tags != []:
			
			query = query.where( or_(Norm_iten_sub.tag == x for x in tags))
		
		if page:
			index = 10
			query = query.offset(page).limit(index)

		else:
			index = 10
			query = query.limit(index)

			

		data = session.exec(query).all()
"""












"""
Tabelas

Person
Para administração do sistema
Em diferentes níveis de acesso e edição

Id
Nome
Matrícula ou código
Senha
Tipo -> comum ou master


Todo -> tarefas
Serve para listar as ações no sistema 
Id 
Nome
Observação
Natureza -> adição de valor, devolver valor
Valor
Person-> id.person
Data
Status -> ok, pendente, autorizado, apagado





User

Id
Nome
Nascimento 
Telefone
Celular
Status -> ativo, inativo 

Endereço -> externo
Conta -> externo




Cotas
Serve para listar todas as cotas

Id
Código
Data
User -> id.user
Agrupamento - none, tipoa, tipob, tipoz




Regras
Calcular allicotas
Corte
Porcentagem
Data aplicação
"""