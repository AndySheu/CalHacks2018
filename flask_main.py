from flask import Flask, request, render_template
import summarize
app = Flask(__name__)

@app.route('/summarizeText', methods=['Post'])
def search():
    term = request.form['input_text']
    return summarize.main(term)

@app.route('/summarizePDF', methods = ['Post'])
def summarize():
	pdf_file = request.form['pdf_upload']
	file_type = request.form['file_type']
	return summarize.pdf(pdf_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file', methods=['Post'])
def save(fi, ty):
    file = open('a.' + ty, 'w')
    file.write(fi)
    file.close()
    return summarize.main('a.' + ty)

if __name__ == '__main__':
    app.run()

