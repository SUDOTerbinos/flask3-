from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            return f"Hello, {name}!"
        else:
            return "Please provide a name."
    return '''
        <form method="post">
            Enter your name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
