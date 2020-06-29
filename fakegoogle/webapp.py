from flask import Blueprint, render_template, request


blueprint = Blueprint('fakegoogle', __name__)


@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/fakesearch')
def result_page():
    return render_template('fakesearch.html', query=request.query_string.decode('utf-8'))


@blueprint.route('/rendeer')
def rendeer():
    term = request.args.get('term')
    correction = request.args.get('correction')    
    return render_template('render_page.html', term=term, correction=correction)