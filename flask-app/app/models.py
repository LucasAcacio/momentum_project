from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MonthlyCummulativeReturnCDI(db.Model):
    __tablename__= 'retorno_mensal_acumulado_cdi'
    data = db.Column(db.DateTime(), primary_key=True)
    retorno = db.Column(db.Float())
    
    def __init__(self, data, retorno):
        self.data = data
        self.retorno = retorno
        
class MonthlyCummulativeReturnIbovespa(db.Model):
    __tablename__= 'retorno_mensal_acumulado_ibovespa'
    data = db.Column(db.DateTime(), primary_key=True)
    retorno = db.Column(db.Float())
    
    def __init__(self, data, retorno):
        self.data = data
        self.retorno = retorno
        
class MonthlyCummulativeReturnMomentum(db.Model):
    __tablename__= 'retorno_mensal_acumulado_momentum'
    data = db.Column(db.DateTime(), primary_key=True)
    retorno = db.Column(db.Float())
    
    def __init__(self, data, retorno):
        self.data = data
        self.retorno = retorno
        
class MonthlyReturnMomentum(db.Model):
    __tablename__= 'retorno_mensal_momentum'
    data = db.Column(db.DateTime(), primary_key=True)
    cod0 = db.Column(db.Text())
    taxa0 = db.Column(db.Float())
    cod1 = db.Column(db.Text())
    taxa1 = db.Column(db.Float())
    cod2 = db.Column(db.Text())
    taxa2 = db.Column(db.Float())
    cod3 = db.Column(db.Text())
    taxa3 = db.Column(db.Float())
    cod4 = db.Column(db.Text())
    taxa4 = db.Column(db.Float())
    cod5 = db.Column(db.Text())
    taxa5 = db.Column(db.Float())
    cod6 = db.Column(db.Text())
    taxa6 = db.Column(db.Float())
    cod7 = db.Column(db.Text())
    taxa7 = db.Column(db.Float())
    cod8 = db.Column(db.Text())
    taxa8 = db.Column(db.Float())
    cod9 = db.Column(db.Text())
    taxa9 = db.Column(db.Float())
    
    def __init__(self, data, cod0, taxa0,cod1, taxa1,cod2, taxa2,cod3, taxa3,cod4, taxa4,cod5, taxa5,cod6, taxa6,cod7, taxa7,cod8, taxa8,cod9, taxa9):
        self.data = data
        self.cod0 = cod0
        self.taxa0 = taxa0
        self.cod1 = cod1
        self.taxa1 = taxa1
        self.cod2 = cod2
        self.taxa2 = taxa2
        self.cod3 = cod3
        self.taxa3 = taxa3
        self.cod4 = cod4
        self.taxa4 = taxa4
        self.cod5 = cod5
        self.taxa5 = taxa5
        self.cod6 = cod6
        self.taxa6 = taxa6
        self.cod7 = cod7
        self.taxa7 = taxa7
        self.cod8 = cod8
        self.taxa8 = taxa8
        self.cod9 = cod9
        self.taxa9 = taxa9