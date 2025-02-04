from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
app = Flask(__name__)

def fetch_content(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

    # Wait for the page to load completely
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(15)  # Pauses execution for 2 seconds
    # Fetch the page source
    content = driver.page_source
    driver.quit()
    return content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load-url', methods=['POST'])
def load_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    try:
        content = fetch_content(url)
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)








# import requests
# from bs4 import BeautifulSoup
# import html5lib
# from markdownify import markdownify as md

# url = "https://edition.cnn.com/2025/01/27/tech/lucie-ai-chatbot-france-scli-intl/index.html"
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html5lib')

# # Remove navigation links and other irrelevant sections
# for nav in soup.find_all(['nav', 'footer', 'header', 'aside']):
#     nav.decompose()

# # Extract only HTML content (excluding script and style tags)
# for script in soup(["script", "style"]):
#     script.decompose()

# html_content = soup.prettify()
# markdown_content = md(html_content)

# # Remove extra whitespace
# markdown_content = '\n'.join([line.strip() for line in markdown_content.splitlines() if line.strip()])

# # Save the Markdown content as 'valendata.md'
# with open('valendata.md', 'w', encoding='utf-8') as file:
#     file.write(markdown_content)

# print("Markdown content saved to 'valendata.md'.")
