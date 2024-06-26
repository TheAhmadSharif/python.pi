from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "\n".join(str(x) for x in range(10))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
