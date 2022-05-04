from models import db, MonthlyCummulativeReturnCDI, MonthlyCummulativeReturnIbovespa, MonthlyCummulativeReturnMomentum, MonthlyReturnMomentum
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

import json
import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = '****'

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/api/retorno_mensal_acumulado_cdi')
def retorno_mensal_acumulado_cdi():
    current_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not current_date and not end_date:
        end_date = datetime.datetime.now()
        end_date = datetime.datetime(end_date.year, end_date.month, 1)
        while not MonthlyCummulativeReturnCDI.query.filter_by(data=end_date).first():
            end_date = end_date - relativedelta(months=1)

        current_date = end_date - relativedelta(months=12)
    
    else:
        current_date = current_date.split('-')
        end_date = end_date.split('-')
        current_date = datetime.datetime(int(current_date[0]), int(current_date[1]), 1)
        end_date = datetime.datetime(int(end_date[0]), int(end_date[1]), 1)

    cummulative_retorno = 1

    response = []
    while current_date <= end_date:
        retorno = MonthlyCummulativeReturnCDI.query.filter_by(data=current_date).first().retorno 
        if retorno:
            cummulative_retorno = cummulative_retorno * retorno
            entry = {'data':f'{current_date.year}-{current_date.month}', 'retorno':(cummulative_retorno - 1) * 100}
            response.append(entry)
        current_date = current_date + relativedelta(months=1)
        
    response_json = json.dumps(response)
    return response_json

@app.route('/api/retorno_mensal_acumulado_ibovespa')
def retorno_mensal_acumulado_ibovespa():
    current_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not current_date and not end_date:
        end_date = datetime.datetime.now()
        end_date = datetime.datetime(end_date.year, end_date.month, 1)
        while not MonthlyCummulativeReturnCDI.query.filter_by(data=end_date).first():
            end_date = end_date - relativedelta(months=1)

        current_date = end_date - relativedelta(months=12)

    
    else:
        current_date = current_date.split('-')
        end_date = end_date.split('-')
        current_date = datetime.datetime(int(current_date[0]), int(current_date[1]), 1)
        end_date = datetime.datetime(int(end_date[0]), int(end_date[1]), 1)

    cummulative_retorno = 1

    response = []
    while current_date <= end_date:
        retorno = MonthlyCummulativeReturnIbovespa.query.filter_by(data=current_date).first().retorno 
        if retorno:
            cummulative_retorno = cummulative_retorno * retorno
            entry = {'data':f'{current_date.year}-{current_date.month}', 'retorno':(cummulative_retorno - 1) * 100}
            response.append(entry)
        current_date = current_date + relativedelta(months=1)
        
    response_json = json.dumps(response)
    return response_json

@app.route('/api/retorno_mensal_acumulado_momentum')
def retorno_mensal_acumulado_momentum():
    current_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not current_date and not end_date:
        end_date = datetime.datetime.now()
        end_date = datetime.datetime(end_date.year, end_date.month, 1)
        while not MonthlyCummulativeReturnCDI.query.filter_by(data=end_date).first():
            end_date = end_date - relativedelta(months=1)

        current_date = end_date - relativedelta(months=12)
    
    else:
        current_date = current_date.split('-')
        end_date = end_date.split('-')
        current_date = datetime.datetime(int(current_date[0]), int(current_date[1]), 1)
        end_date = datetime.datetime(int(end_date[0]), int(end_date[1]), 1)

    cummulative_retorno = 1

    response = []
    while current_date <= end_date:
        retorno = MonthlyCummulativeReturnMomentum.query.filter_by(data=current_date).first().retorno 
        if retorno:
            cummulative_retorno = cummulative_retorno * retorno
            entry = {'data':f'{current_date.year}-{current_date.month}', 'retorno':(cummulative_retorno - 1) * 100}
            response.append(entry)
        current_date = current_date + relativedelta(months=1)
        
    response_json = json.dumps(response)
    return response_json

@app.route('/api/retorno_mensal_momentum_list')
def retorno_mensal_momentum():
    req = request.args.get('start_date')
    if req:
        current_date = req.split('-')
        current_date = datetime.datetime(int(current_date[0]), int(current_date[1]), 1)
        entry = MonthlyReturnMomentum.query.filter_by(data=current_date).first()
    else:
        current_date = datetime.datetime.now()
        current_date = datetime.datetime(current_date.year, current_date.month, 1)
        entry = MonthlyReturnMomentum.query.filter_by(data=current_date).first()

    tries = 12
    while not entry and tries > 0:
        current_date = current_date - relativedelta(months=1)
        entry = MonthlyReturnMomentum.query.filter_by(data=current_date).first()
        tries = tries - 1
    
    if entry:
        response = [
            {
            'codigo': entry.cod0,
            'retorno':(entry.taxa0) * 100
            },
            {
            'codigo': entry.cod1,
            'retorno':(entry.taxa1) * 100
            },
            {
            'codigo': entry.cod2,
            'retorno':(entry.taxa2) * 100
            },
            {
            'codigo': entry.cod3,
            'retorno':(entry.taxa3) * 100
            },
            {
            'codigo': entry.cod4,
            'retorno':(entry.taxa4) * 100
            },
            {
            'codigo': entry.cod5,
            'retorno':(entry.taxa5) * 100
            },
            {
            'codigo': entry.cod6,
            'retorno':(entry.taxa6) * 100
            },
            {
            'codigo': entry.cod7,
            'retorno':(entry.taxa7) * 100
            },
            {
            'codigo': entry.cod8,
            'retorno':(entry.taxa8) * 100
            },
            {
            'codigo': entry.cod9,
            'retorno':(entry.taxa9) * 100
            },
        ]
    else:
        response = {}
    response_json = json.dumps(response)
    return response_json
