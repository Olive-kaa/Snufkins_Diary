from flask import Flask, render_template

from controllers.hikers_controller import hikers_blueprint
from controllers.regions_controller import regions_blueprint
from controllers.munros_controller import munros_blueprint
from controllers.bagged_munros_controller import bagged_munros_blueprint


app = Flask(__name__)

app.register_blueprint(hikers_blueprint)
app.register_blueprint(regions_blueprint)

app.register_blueprint(munros_blueprint)
app.register_blueprint(bagged_munros_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()