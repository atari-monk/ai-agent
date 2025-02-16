from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def chat_with_chatgpt(prompt):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://chat.openai.com")
    
    time.sleep(5)

    input_box = driver.find_element("xpath", "//textarea")
    
    input_box.send_keys(prompt)
    input_box.send_keys(Keys.RETURN)
    
    time.sleep(10)

    response_elements = driver.find_elements("xpath", "//div[contains(@class, 'message')]")
    
    if response_elements:
        response = response_elements[-1].text
    else:
        response = "Brak odpowiedzi."

    driver.quit()
    return response

prompt = "Przeanalizuj poniższy kod pod kątem zasad SOLID:\n<twój kod>"
print(chat_with_chatgpt(prompt))
