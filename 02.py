from flask import Flask, request
from flask import make_response
import io
import csv
import random

app = Flask(__name__)

#-------------------------------------------------------------------------------

@app.route('/w2')
def w2():
    return '''
        <html>
            <body>
                <p>ID:</p>
                <form method="POST" action="/do_w2">
                    <p><input name="id" /></p>
                    <p><input type="submit" value="ดาวนโหลด csv" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/do_w2', methods=['POST'])
def do_w2():
    id = int(request.form['id'])

    si = io.StringIO()
    cw = csv.writer(si)
    random.seed(2)

    a = ['']
    a.extend([random.randint(0,999) for _ in range(26)])
    cw.writerow(a)
    for i in range(1000):
        if i == 586:
            cw.writerow([id % 1000])
        else:
            cw.writerow([random.randint(0,999)])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = f'attachment; filename={id}.csv'
    output.headers["Content-type"] = "text/csv"
    return output


#-------------------------------------------------------------------------------
@app.route('/')
def hello_world():
    return '''
        <html>
            <body>
                <p>ID:</p>
                <form method="POST" action="/calc">
                    <p><input name="id" /></p>
                    <p><input type="submit" value="ดาวนโหลด csv" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/calc', methods=['POST'])
def calc():
    id = int(request.form['id'])

    si = io.StringIO()
    cw = csv.writer(si)
    random.seed(10)
    cw.writerow(['price','discounted price'])
    for i in range(1000):
        if i == 486-2:
            cw.writerow([id % 1000])
        else:
            cw.writerow([random.randint(0,999)])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = f'attachment; filename={id}.csv'
    output.headers["Content-type"] = "text/csv"
    return output
