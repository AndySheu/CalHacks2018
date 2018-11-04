from flask import Flask, request, render_template
import main
app = Flask(__name__)

@app.route('/summarize_text', methods=['Post'])
def search():
	term = request.form['Search']
	return main(term)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

