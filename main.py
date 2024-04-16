from flask import Flask, render_template, request
from block import write_block, check_integrity

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        borrower = request.form.get('borrower') 
        lender = request.form.get('lender')
        amount = request.form.get('amount')

        write_block(borrower=borrower, lender=lender, amount=amount)

    return render_template('index.html')

@app.route('/checking')
def check():
    results = check_integrity()
    return render_template('index.html', checking_results=results)

if __name__ == "__main__":
    app.run(debug=True)
