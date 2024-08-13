import sys
sys.path.append("../RAG_SERVICE")

import pandas as pd
import requests
from RAG_project_clickhouse.find_nearest_neighbors_function import find_NN
from tqdm import tqdm


df = pd.read_csv("C:/Users/Denchik/Desktop/ATOM/rag_service/data/filtering_data.csv")
url = 'http://127.0.0.1:8000/get_neighbors/'
question_1 = []
question_2 = []
question_3 = []
answer_1 = []
answer_2 = []
answer_3 = []
for i in tqdm(df.iterrows()):
    user_text = i[1]["user"]
    admin_text = i[1]["admin"]
    res = find_NN(user_text, 3)[0]
    question_1.append(res[0][0])
    question_2.append(res[1][0])
    question_3.append(res[2][0])
    answer_1.append(res[0][1])
    answer_2.append(res[1][1])
    answer_3.append(res[2][1])
    print(question_3[-1])

df_documents_questions = pd.DataFrame({"question_1": question_1, "question_2": question_2, "question_3": question_3, "answer_1": answer_1, "answer_2": answer_2, "answer_3": answer_3})
combined_df = pd.concat([df, df_documents_questions], axis=1)
combined_df.to_csv("df_documents_questions.csv")



