from flask import Flask, request, render_template
from flaskext.markdown import Markdown
from api import v2, v1
import docs
import demo
import errors
from logger import hits_logger

app = Flask(__name__, static_url_path='/src')
Markdown(app)

@app.route('/api/v2', methods=['GET'])
def api_v2():
    return(v2.base())

@app.route('/api/v2/day/<target>', methods=['GET'])
def day(target):
    return(v2.day(target))

@app.route('/api/v2/month/<target>', methods=['GET'])
def month(target):
    return(v2.month(target))

@app.route('/api/v2/year/<target>', methods=['GET'])
def year(target):
    return(v2.month(target))

@app.route('/api/v2/keyword/<target>', methods=['GET'])
def keyword(target):
    return(v2.keyword(target, request.args.to_dict()))

@app.route('/api/v1-alpha', methods=['GET'])
@app.route('/api/v1', methods=['GET'])
def api_v1():
    return(v1.main(request.args.to_dict()))

@app.route('/demo', methods=['GET'])
def demo_home():
    return(demo.index())

@app.route('/demo/day/<target>', methods=['GET'])
def server_day_search(target):
    return(demo.day_search(target))

@app.route('/demo/keyword/<target>', methods=['GET'])
def server_keyword_search(target):
    return(demo.keyword_search(target))

@app.route('/', methods=['GET'])
def website():
    return(docs.home())

@app.after_request
def hits(response):
    return(hits_logger.after_req(response))

@app.errorhandler(500)
def server_error(err):
    return(errors.err_400())

@app.errorhandler(404)
def not_found_err(err):
    return(errors.err_400())