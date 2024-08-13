import sys
sys.path.append("../RAG_SERVICE")

from encoder import Encoder
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import clickhouse_connect
import typing as tp

client = clickhouse_connect.get_client(host='127.0.0.1', username='default', password='1234')
app = FastAPI()


class RequestModel(BaseModel):
    list_text_question: list
    list_text_answer: list


class RequestModel_get(BaseModel):
    arr: list
    k_neighbors: int


class ResponseModel(BaseModel):
    response: str


class ResponseListModel(BaseModel):
    list_text: list


def find_top_set(responses, k):
    outputs = []
    answers = []
    for i in responses:
        if i[1] not in answers:
            answers.append(i[1])
            outputs.append(i)
            if len(outputs) == k:
                break
    return outputs


encoder = Encoder("intfloat/multilingual-e5-small")  # download_model_e5-small-v2


@app.get("/")
async def home():
    return {"error": "Work"}


@app.post("/save/", response_model=ResponseModel)
async def encode(request_body: RequestModel):
    try:
        real_text = request_body.list_text_question
        answer = request_body.list_text_answer
        encoded_text = encoder.encode(real_text)
        client.insert('ann_index_example', list(zip(real_text, encoded_text, answer)))
        return {"response": "save"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/get_neighbors/", response_model=ResponseListModel)
async def give_neighbors(request_body: RequestModel_get):
    # try:
        real_text = request_body.arr
        k = request_body.k_neighbors
        encoded_text = encoder.encode(real_text)
        output_res = []
        # можно улучшить-ускорить
        for i in encoded_text:
            encoded_text_str = ", ".join(map(str, i))
            query = f"""
            SELECT
                Name,
                Name_2,
                score
            FROM
                (
                SELECT
                    Name,
                    Name_2,
                    L2Distance(embedding, [{encoded_text_str}]) AS score
                FROM ann_index_example
                ORDER BY score ASC
                LIMIT {k}
                )
            """
            results = client.query(query).result_rows
            output_res.append(find_top_set(results, k))

        return {"list_text": output_res}  # output_res
    # except Exception as e:
    #    return {"error": [str(e)]}
# сделаю @app.post("/get_NN/", response_model=ResponseModel) для получения ближайшей к запросу строки
# uvicorn RAG_project_clickhouse.main:app --reload
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8001)
# http://localhost:8001/docs - чтобы войти в пульт управление