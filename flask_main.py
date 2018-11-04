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
    print(-1)
    fi = request.files['file']
    print(0)
    ty = request.form['file_type']
    print(1)
    file = open('a.' + ty, 'w')
    print(2)
    file.write(fi)
    print(3)
    file.close()
    print(4)
    a = summarize.main('a.' + ty)
    print(a)
    print('\n\n\n')
    return a

if __name__ == '__main__':
    app.run()

