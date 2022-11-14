from flask import Flask, render_template

from controllers.teachers_controller import teachers_blueprint
from controllers.carers_controller import carers_blueprint


app = Flask(__name__)

app.register_blueprint(teachers_blueprint)
app.register_blueprint(carers_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()