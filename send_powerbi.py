import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random

def data_generation(type):
    surr_id = random.randint(1, 3)
    type = random.randint(0,1024)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()

    return [surr_id, type, date, time]

def data_generation1(type):
    surr_id = random.randint(1, 3)
    type = random.randint(0,1)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()

    return [surr_id, type, date, time]

if __name__ == '__main__':

    REST_API_URL = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/24ecbae0-913f-4c9b-b5d2-71755c7fd42f/rows?key=9RdBUny3l7D8VtOG1voK5qjEj5XSM8MRLGbOSB%2Ff9A2CAddmx9%2BrXYh0hQ5pphgT1zkWU0tfd8xHHjhPKKxA2Q%3D%3D'
    REST_API_URL1 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/9721158a-2f42-458a-add8-35d8b0d74818/rows?key=91UQg%2FVkG%2F57ldpIDW8cc1rRL%2FodUS%2Fi6Qr20m%2FZKbjyLjmo0aR5jGWQUqf8i5fKnYxxecnLpjkqMe52Q7BwRA%3D%3D'
    REST_API_URL2 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/69f338f0-b7a0-4147-a453-5bba326a9b9f/rows?key=1w5QGMySWdH49DGN0KFI6qkFFHNyDY%2F86fxsSjUr%2BRNLlFjk8oO8XdDhd8yyPgYVrTBuShoMcnGjUTOV5NuCwA%3D%3D'
    REST_API_URL3 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/df56d87d-b949-49c5-b5a9-889e834b794d/rows?key=AMlc%2FZALtSg5FC0tuYMlFO3X64t4StOigxJkchRkVybEmvesZ0mlFkF80Dkap%2F2zBsKXBXaTcoACV2cPoPQI1A%3D%3D'
    REST_API_URL4 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/2486bc78-a76e-46cf-b6e6-3ccadf1f9167/rows?key=cywby3dLrazzajv2AphTbnwShlC%2FfBi9aZD1AupzZYsvjKSf0HqjNr2P%2BfsL1ATwOoAY0nfBsJ1v98CVh84Fvg%3D%3D'
    REST_API_URL5 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/65352694-a4f9-48a1-baf3-28d303d564da/rows?key=uJxOQ9v5DJrt2eJYNP13eN5AO182oe2j2kNQqhlSq7WpGl2LoYwAhCJwTl6Pd4rzwdN%2FhzKUvjWBQ7Z62D98Og%3D%3D'
    REST_API_URL6 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/5fd88df3-0f03-41ef-84c4-91a02e12597f/rows?key=w1ISaEKolu85iFrNJnrLYZuIr7FuBeU6IzXY7wdDOw%2BuJc39Po5HsbPbkUMeT8KrSZrGTeDD8sYZlTO0E5y3jQ%3D%3D'
    REST_API_URL7 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/8f1be508-477c-47e3-9b3e-bbcef7e9c944/rows?key=9U48C%2FP8Lx8IQSgdJJsSz67KN2brOre0uHMZM7j9CBf35zg09QPC3QmW%2F9zrKfxHd%2FQmf8Z3auTJJb5JghMxag%3D%3D'
    REST_API_URL8 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/11f51665-b0b1-4c40-9502-d5f250daeb32/rows?key=J%2FP6WpqU1ej1zOmE9H1l89Nih3TvP8G3Rq1PSOtlgEyIiB0WEodkcG9sRg%2BOShw5Ep3b7jSTHQe3hb6WQ6EHHQ%3D%3D'
    REST_API_URL9 = 'https://api.powerbi.com/beta/268cab5d-b46b-4ac0-9feb-47b66b171b88/datasets/dc8ecf00-3847-4508-b7f6-9443e5463259/rows?key=F7n%2FjTQCQjWGweac0umwgTjvBZhx3%2Bkk93tdm3hqSVoD0OFEY9LAmZy3PX3uzTebnO0tl7TueUVhJs8NjNmMdA%3D%3D'

    data_raw = []
    data_raw1 = []
    data_raw2 = []
    data_raw2 = []
    data_raw3 = []
    data_raw4 = []
    data_raw5 = []
    data_raw6 = []
    data_raw7 = []
    data_raw8 = []
    data_raw9 = []

    while True:
        for i in range(1):
            row = data_generation("distance1")
            data_raw.append(row)
            row1 = data_generation("distance2")
            data_raw1.append(row1)
            row2 = data_generation("distance3")
            data_raw2.append(row2)
            row3 = data_generation("temp")
            data_raw3.append(row3)
            row4 = data_generation("grayscale")
            data_raw4.append(row4)
            row5 = data_generation1("infrared")
            data_raw5.append(row5)
            row6 = data_generation1("tilt")
            data_raw6.append(row6)
            row7 = data_generation1("magetic")
            data_raw7.append(row7)
            row8 = data_generation1("vibration")
            data_raw8.append(row8)
            row9 = data_generation("ab_light")
            data_raw9.append(row9)

            print("Raw data1 - ", data_raw, data_raw1, data_raw2, data_raw3, data_raw4, data_raw5, data_raw6, data_raw7, data_raw8, data_raw9,)

        # set the header record
        HEADER = ["surr_id", "distance1", "date", "time"]
        HEADER1 = ["surr_id", "distance2", "date", "time"]
        HEADER2 = ["surr_id", "distance3", "date", "time"]
        HEADER3 = ["surr_id", "temp", "date", "time"]
        HEADER4 = ["surr_id", "grayscale", "date", "time"]
        HEADER5 = ["surr_id", "infrared", "date", "time"]
        HEADER6 = ["surr_id", "tilt", "date", "time"]
        HEADER7 = ["surr_id", "magetic", "date", "time"]
        HEADER8 = ["surr_id", "vibration", "date", "time"]
        HEADER9 = ["surr_id", "ab_light", "date", "time"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        data_df1 = pd.DataFrame(data_raw1, columns=HEADER1)
        data_json1 = bytes(data_df1.to_json(orient='records'), encoding='utf-8')
        data_df2 = pd.DataFrame(data_raw2, columns=HEADER2)
        data_json2 = bytes(data_df2.to_json(orient='records'), encoding='utf-8')
        data_df3 = pd.DataFrame(data_raw3, columns=HEADER3)
        data_json3 = bytes(data_df3.to_json(orient='records'), encoding='utf-8')
        data_df4 = pd.DataFrame(data_raw4, columns=HEADER4)
        data_json4 = bytes(data_df4.to_json(orient='records'), encoding='utf-8')
        data_df5 = pd.DataFrame(data_raw5, columns=HEADER5)
        data_json5 = bytes(data_df5.to_json(orient='records'), encoding='utf-8')
        data_df6 = pd.DataFrame(data_raw6, columns=HEADER6)
        data_json6 = bytes(data_df6.to_json(orient='records'), encoding='utf-8')
        data_df7 = pd.DataFrame(data_raw7, columns=HEADER7)
        data_json7 = bytes(data_df7.to_json(orient='records'), encoding='utf-8')
        data_df8 = pd.DataFrame(data_raw8, columns=HEADER8)
        data_json8 = bytes(data_df8.to_json(orient='records'), encoding='utf-8')
        data_df9 = pd.DataFrame(data_raw9, columns=HEADER9)
        data_json9 = bytes(data_df9.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset1", data_json, data_json1, data_json2, data_json3, data_json4, data_json5, data_json6, data_json7, data_json8, data_json9,)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)
        req = requests.post(REST_API_URL1, data_json1)
        req = requests.post(REST_API_URL2, data_json2)
        req = requests.post(REST_API_URL3, data_json3)
        req = requests.post(REST_API_URL4, data_json4)
        req = requests.post(REST_API_URL5, data_json5)
        req = requests.post(REST_API_URL6, data_json6)
        req = requests.post(REST_API_URL7, data_json7)
        req = requests.post(REST_API_URL8, data_json8)
        req = requests.post(REST_API_URL9, data_json9)
        print("Data posted in Power BI API")
        time.sleep(2)
