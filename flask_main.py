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

@app.route('/file', methods=['Post'])
def save(fi, ty):
    file = open('a.' + ty, 'w')
    file.write(fi)
    file.close()
    return summarize.main('a.' + ty)

if __name__ == '__main__':
    app.run()

