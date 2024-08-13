import sys
sys.path.append("../RAG_DIGEST")

import pandas as pd
import clickhouse_connect
from encoder import Encoder
from tqdm import tqdm

# Подключение к ClickHouse
client = clickhouse_connect.get_client(host='127.0.0.1', username='default', password='1234')
encoder = Encoder("intfloat/multilingual-e5-small")  # download_model_e5-small-v2
# Чтение данных из csv
question_all = []
encoded_text_all = []
answer_all = []

excel_data = pd.read_csv("click_house_prj/ML_questions.csv")
for index, row in tqdm(excel_data.iterrows()):
    question = row['Вопрос']
    answer = row['Ответ на вопрос']
    question_all.append(question)
    emb_question = encoder.encode([question])[0]
    encoded_text_all.append(emb_question)
    answer_all.append(answer)
    # Пример кода для сохранения данных в ClickHouse
client.insert('ann_index_example', list(zip(question_all, encoded_text_all, answer_all)))
print("Данные успешно сохранены в ClickHouse.")