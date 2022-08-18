from flask import Flask
from flask import request

app = Flask(__name__)

import requests

headers = {
    "authority": "www.the-village.ru",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    # handle the POST request
    if request.method == 'POST':
        url = request.form.get('url')
        response = requests.request("GET", url, headers=headers)
        return response.text

    # otherwise handle the GET request
    return '''
    <p>Вставьте ссылку вида <i>https://www.the-village.ru/city/situation/estoniya-poyasnila-komu-k-nim-mozhno</i></p>
           <form method="POST">
               <label>Ссылка: </label><br>
               <input type="url" name="url" size="100"><br>
               <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')