def salary_calc(pay_period, hourly_rate):
    rate = float(hourly_rate)
    pay_periods = {"Weekly": 40,
                   "Semi-monthly": 86.66,
                   "Biweekly": 80,
                   "Monthly": 160,
                   "Annual": 2080}

    if pay_period in pay_periods:
        salary = pay_periods.get(pay_period) * rate
        salary = '{:.2f}'.format(round(salary, 2))
        return salary

