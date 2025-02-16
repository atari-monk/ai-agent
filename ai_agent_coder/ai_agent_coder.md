# AI Agent Coder #1

## Prompt

- Generate ai agent in python and chatgpt instance in chrome.
- Role of this agent is coding.
- This coder is responsible for component with has many files.
- His task is to anlayze classes on SOLID.

## Chat

### **Tworzenie Agenta AI do Analizy SOLID w Pythonie**  

Ten agent AI będzie:  
- Analizować pliki kodu Pythona.  
- Sprawdzać zgodność klas z zasadami SOLID.  
- Proponować ulepszenia.  

---

## **Krok 1: Tworzenie Agenta AI w Pythonie**  

Poniższy kod:  
✅ Otwiera plik Pythona.  
✅ Wysyła kod do ChatGPT.  
✅ Analizuje zgodność z SOLID i zwraca sugestie.  

```python
import openai
import os

# Ustawienie klucza API OpenAI (zamień na swój)
openai.api_key = "twój-klucz-api"

def analyze_code(file_path):
    """Odczytuje plik Python i analizuje go pod kątem SOLID."""
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    prompt = f"""
    Przeanalizuj poniższy kod pod kątem zasad SOLID (SRP, OCP, LSP, ISP, DIP).
    Wskaż naruszenia i zaproponuj poprawki.

    Kod:
    {code}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "Jesteś ekspertem od inżynierii oprogramowania."},
                  {"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

# Przykładowe użycie
file_to_analyze = "ścieżka/do/pliku.py"
print(analyze_code(file_to_analyze))
```

---

## **Krok 2: Automatyzacja ChatGPT w Przeglądarce Chrome (Opcjonalne)**  
Jeśli chcesz, aby agent AI używał **ChatGPT w przeglądarce Chrome**, skorzystaj z **Selenium**.  

### **1️⃣ Instalacja wymaganych pakietów**  
Uruchom w terminalu:  
```sh
pip install selenium webdriver-manager
```

### **2️⃣ Skrypt do automatyzacji Chrome**  

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def chat_with_chatgpt(prompt):
    """Automatycznie wysyła wiadomość do ChatGPT w przeglądarce Chrome."""
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Otwórz ChatGPT w Chrome
    driver.get("https://chat.openai.com")
    
    time.sleep(5)  # Poczekaj na załadowanie strony

    # Znajdź pole tekstowe czatu
    input_box = driver.find_element("xpath", "//textarea")
    
    input_box.send_keys(prompt)
    input_box.send_keys(Keys.RETURN)
    
    time.sleep(10)  # Poczekaj na odpowiedź

    # Pobierz ostatnią wiadomość z czatu
    response_elements = driver.find_elements("xpath", "//div[contains(@class, 'message')]")
    
    if response_elements:
        response = response_elements[-1].text  # Pobierz najnowszą odpowiedź
    else:
        response = "Brak odpowiedzi."

    driver.quit()
    return response

# Przykładowe użycie
prompt = "Przeanalizuj poniższy kod pod kątem zasad SOLID:\n<twój kod>"
print(chat_with_chatgpt(prompt))
```

---

## **Jak to działa?**
1️⃣ **Pythonowy agent AI** czyta plik i analizuje kod za pomocą OpenAI API.  
2️⃣ **Automatyzacja przeglądarki** pozwala na interakcję z ChatGPT w Chrome.  

Jeśli masz pytania lub chcesz coś poprawić – daj znać! 🚀