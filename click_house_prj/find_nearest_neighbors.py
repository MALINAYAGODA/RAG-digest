import requests

if __name__ == "__main__":
    russian_names = ["Что такое Линейная регрессия"]  # What is Linear Regression?
    url = 'http://127.0.0.1:8001/get_neighbors/'
    data = {'arr': russian_names, 'k_neighbors': 5}

    response = requests.post(url, json=data)

    # print(response.json())
    if response.status_code == 200:
        for i in response.json()['list_text']:
            print('<->'*7)
            for j in i:
                print("Question:", j[0])
                print("Answer:", j[1])
                print('-'*7)
    else:
        print(f"Ошибка: {response.status_code}")