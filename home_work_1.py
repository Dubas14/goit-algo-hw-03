from datetime import datetime

def get_days_from_today(date):
        
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - input_date
        
        return delta.days



print(get_days_from_today("2024-06-25"))