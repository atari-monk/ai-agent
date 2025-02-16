import openai
import os

openai.api_key = "twój-klucz-api"

def analyze_code(file_path):
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

file_to_analyze = "ścieżka/do/pliku.py"
print(analyze_code(file_to_analyze))