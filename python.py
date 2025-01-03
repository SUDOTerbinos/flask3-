from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check_number():
    if request.method == 'POST':
        number = request.form.get('number')
        if number and number.isdigit():
            number = int(number)
            result = "even" if number % 2 == 0 else "odd"
            return f"The number {number} is {result}."
        else:
            return "Please enter a valid number."
    return '''
        <form method="post">
            Enter a number: <input type="text" name="number">
            <input type="submit" value="Check">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
