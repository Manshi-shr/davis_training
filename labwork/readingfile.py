import requests

url = "https://raw.githubusercontent.com/Manshi-shr/davis_training/refs/heads/main/Classwork/numpy/arangemethod.py"

response = requests.get(url)

text = response.text

print(text)