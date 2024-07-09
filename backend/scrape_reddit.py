import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from tqdm import tqdm

PURPLE = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


def scrape_reddit():
    url = 'https://www.reddit.com/r/webdev/?rdt='
    posts = []
    bar_format = f"{PURPLE}{{l_bar}}{{bar}}{RESET}| {{n_fmt}}/{{total_fmt}} {{elapsed}} < {{remaining}}"
    with tqdm(total=18, desc=f"{GREEN}Reddit Scraping Progress{RESET}", unit="step", bar_format= bar_format, colour="RED", leave=True) as pbar:

    # with tqdm(total=19, desc=f"{GREEN}Reddit Scraping Progress{RESET}", unit="step", bar_format= bar_format, leave=True, colour="RED") as pbar:
            
        # Set up the options for Selenium
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        driver = webdriver.Chrome(options=options)
        pbar.update(1)

        # Use stealth to avoid detection
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        pbar.update(1)
        driver.get(url)
        pbar.update(1)
        time.sleep(5)
        pbar.update(1)

        # set relevant state
        last_height = driver.execute_script("return document.body.scrollHeight")
        pbar.update(1)
        total_posts = 0
        pbar.update(1)

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Wait for the page to load at each scroll

            try:
                titles = driver.find_elements(By.CSS_SELECTOR, '.block.font-semibold.text-neutral-content-strong.m-0.visited\\:text-neutral-content-weak.text-16.xs\\:text-18.mb-2xs.xs\\:mb-xs')
                contents = driver.find_elements(By.CSS_SELECTOR, '.md.feed-card-text-preview.text-ellipsis.line-clamp-3.xs\\:line-clamp-6.text-14')
                scroll_total = min(len(titles), len(contents))
                for i in range(scroll_total):
                    posts.append({
                        'title': titles[i].text,
                        'content': contents[i].text
                    })
                total_posts += scroll_total
            except Exception as error:
                print('Error during scraping:', error)

            # update state 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            # pbar.update(1)
            last_height = new_height
        pbar.update(10)
        driver.quit()
        pbar.update(1)

        driver.quit()

        import os
        current_directory = os.getcwd()
        file_path = current_directory + "/data/results.json"
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        else:
            existing_data = []
        existing_data.extend(posts)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

        pbar.update(1)
        return

