from flask import Flask, request, render_template
import summarize
app = Flask(__name__)

@app.route('/summarizeText', methods=['Post'])
def search():
    term = request.form['input_text']
    return summarize.summarize(term)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

