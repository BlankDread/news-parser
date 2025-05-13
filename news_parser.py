import requests
from bs4 import BeautifulSoup


def get_bbc_news():
    # URL сайта для парсинга
    url = "https://www.bbc.com"

    # Отправляем GET запрос
    response = requests.get(url)

    # Проверяем, успешен ли запрос
    if response.status_code != 200:
        print("Ошибка при получении данных!")
        return

    # Парсим HTML содержимое страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем все заголовки новостей (например, можем использовать 'h2', 'h1' или другой тег)
    headlines = soup.find_all(['h2', 'h3', 'h1'])  # В зависимости от структуры

    # Выводим заголовки
    print("Последние новости с BBC:\n")
    for idx, headline in enumerate(headlines[:10], 1):  # Выводим только 10 первых заголовков
        print(f"{idx}. {headline.get_text(strip=True)}")


if __name__ == "__main__":
    get_bbc_news()
