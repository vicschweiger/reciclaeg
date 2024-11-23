from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coletor(db.Model):
    __tablename__ = 'coletores'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    logradouro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    colaboradores = db.relationship('Colaborador', backref='coletor', lazy=True)

    def __repr__(self):
        return f'<Coletor {self.nome}>'

class Colaborador(db.Model):
    __tablename__ = 'colaboradores'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(15), nullable=True)
    coletor_id = db.Column(db.Integer, db.ForeignKey('coletores.id'), nullable=True)

    def __repr__(self):
        return f'<Colaborador {self.nome}>'
