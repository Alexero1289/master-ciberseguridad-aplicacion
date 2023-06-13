import requests

def search(objeto: str):
    url = f"https://api.wallapop.com/api/v3/general/search?filters_source=search_box&keywords={objeto}&longitude=-3.69196&latitude=40.41956"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers = user_agent)
    results = r.json()["search_objects"]
    for r in results:
        print(f'{r["price"]}€ -  {r["title"]}')

search (¨consulta¨)
