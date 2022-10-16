from flask import Flask, flash, render_template, request


def create_app():

    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/sample', methods=('GET', 'POST'))
    def sample():
        if request.method == 'POST':
            using = ['flask', 'vue', 'mysql', 'aws']
            user_input = request.form['input']
            message = None

            if not user_input:
                message = 'Input is required'
            elif user_input not in using:
                message = 'Input is not used'
            else:
                message = 'Input is used'
            flash(message)

        return render_template('sample.html')

    return app
