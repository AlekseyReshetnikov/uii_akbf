import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False) # Запускаем браузер
    page = await browser.newPage() # Создаем новую вкладку

    # Переходим на страницу для парсинга
    await page.goto('https://example.com')

    # Исполняем JavaScript для получения заголовка страницы
    title = await page.evaluate('() => document.title')
    print(f'Заголовок страницы: {title}')

    # Закрываем браузер
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

