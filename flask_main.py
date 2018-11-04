from flask import Flask, request
from main.py import main
app = Flask(__name__)

@app.route('/summarize_text', methods=['Post'])
def search():
	term = request.form['Search']
	return main(term)

if __name__ == '__main__':
    app.run(debug=True)