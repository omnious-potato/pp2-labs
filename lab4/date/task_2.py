from datetime import datetime, timedelta

def yestertomoday():
    now = datetime.now()
    #return now - timedelta(days=1), now, now + timedelta(days=1)
    print(f"""
          Yesteday was: {now - timedelta(days=1)}
          Today is: {now}
          Tommorow will be: {now + timedelta(days=1)}
    """)


yestertomoday()