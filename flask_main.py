from flask import Flask, request, render_template
import summarize
app = Flask(__name__)

@app.route('/summarizeText', methods=['Post'])
def search():
    term = request.form['input_text']
    return summarize.main(term)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarizePDF', methods = ['Post'])
def save():
	fi = request.form['pdf_upload']
	ty = request.form['file_type']

    file = open('a.' + ty, 'w')
    file.write(fi)
    file.close()
    return summarize.main('a.' + ty)

if __name__ == '__main__':
    app.run()

