import requests

if __name__ == "__main__":
    
    url = 'http://127.0.0.1:8001/save/'
    data = {'list_text_question': ["Что такое AI"], "list_text_answer": ["AI - это МИСИС"]}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Ошибка: {response.status_code}")