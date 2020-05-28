from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

permanent_fee = 0.36
day_minute_fee = 0.09
night_minute_fee = 0

def classify_by_phone_number(records):
    total_list = []
    total_call_price = {}
    for record in records:
        datetime_end = datetime.fromtimestamp(record['end'])
        datetime_start = datetime.fromtimestamp(record['start'])
        
        if datetime_start.hour < 6 and datetime_end.hour < 6:
            total_call = datetime_end - datetime_start
            total_minutes = total_call.total_seconds() // 60
            total_price = permanent_fee + (total_minutes * night_minute_fee)

        elif datetime_start.hour < 6 and 6 <= datetime_end.hour < 22:
            split_time = datetime(
                year=datetime_start.year,
                month=datetime_start.month,
                day=datetime_start.day,
                hour=6
            )
            night_call = split_time - datetime_start
            day_call = datetime_end - split_time
            total_price = permanent_fee
            total_price += night_minute_fee * (night_call.total_seconds() // 60)
            total_price += day_minute_fee * (day_call.total_seconds() // 60 )

        elif datetime_start.hour >= 6 and datetime_end.hour < 22:
            total_call = datetime_end - datetime_start
            total_minutes = total_call.total_seconds() // 60
            total_price = permanent_fee + (total_minutes * day_minute_fee) 

        elif 6 <= datetime_start.hour < 22 and datetime_end.hour >= 22:
            split_time = datetime(
                year=datetime_start.year,
                month=datetime_start.month,
                day=datetime_start.day,
                hour=22
            )
            day_call = split_time - datetime_start
            night_call = datetime_end - split_time
            total_price = permanent_fee
            total_price += night_minute_fee * (night_call.total_seconds() // 60)
            total_price += day_minute_fee * (day_call.total_seconds() // 60)

        elif datetime_start.hour >= 22 and datetime_end.hour >= 22:
            total_call = datetime_end - datetime_start
            total_minutes = total_call.total_seconds() // 60
            total_price = permanent_fee + (total_minutes * night_minute_fee)


        if record['source'] in total_call_price.keys():
            total_call_price[record['source']] += total_price
        
        else:
            total_call_price[record['source']] = total_price
    
    for key, value in total_call_price.items():
        total_list.append({'source': key, 'total': round(value, 2)})

    total_list = sorted(total_list, key=lambda item: item['total'], reverse=True)

    return total_list




