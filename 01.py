# Create a CSV file with two columns

# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

app = Flask(__name__)

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
import io
import csv
from flask import make_response
import random

@app.route('/calc', methods=['POST'])
def calc():
    id = int(request.form['id'])

    si = io.StringIO()
    cw = csv.writer(si)
    random.seed(10)
    cw.writerow(['price','d_price'])
    for i in range(1000):
        if i == 486-2:
            cw.writerow([id % 1000])
        else:
            cw.writerow([random.randint(0,999)])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = f'attachment; filename={id}.csv'
    output.headers["Content-type"] = "text/csv"
    return output
