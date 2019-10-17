from flask import Flask, request, render_template
from salcal import calculate


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = False

    @app.route('/', methods=['GET'])
    def get_web_app():
        if request.method == "GET":
            render = render_template("index.html",
                                     title='Salary Calculator')
            return render

    @app.route('/', methods=['POST'])
    def post_web_app():
        if request.method == "POST":
            # Get the hourly rate and pay period from the form
            hourly_rate = request.form['hourly-rate']
            pay_period = request.form['pay-period']
            try:
                hourly_rate = float(hourly_rate)
                # Calculate the salary based on form selection
                salary = calculate.salary_calc(pay_period, hourly_rate)

                # Convert the case on the pay period to post for results
                pay_period = pay_period.lower()
                render = render_template("index.html",
                                         salary=salary,
                                         pay_period=pay_period,
                                         hourly_rate=hourly_rate)
                return render
            except ValueError:
                return render_template("index.html",
                                       error="Invalid Entry.",
                                       error_state=True)

    return app
