from datetime import datetime

def days_since_1996():
    start_date = datetime(1996, 1, 1)
    current_date = datetime.now()
    delta = current_date - start_date
    print(f"Number of days since 1996: {delta.days}")

# call the function
days_since_1996()