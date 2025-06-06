import requests
from bs4 import BeautifulSoup

def scrape_aliexpress(query, max_results=5):
    url = f"https://www.aliexpress.com/wholesale?SearchText={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    products = soup.select("a._3t7zg._2f4Ho")

    for item in products[:max_results]:
        title = item.get("title")
        link = "https:" + item.get("href")
        price_tag = item.select_one("div.mGXnE._37W_B")
        price = price_tag.text if price_tag else "N/A"

        results.append({
            "title": title,
            "link": link,
            "price": price
        })

    return results
