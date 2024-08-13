# Rag_service
- В main.py запускаем сервер на FastAPI
- Файл creat_table запускаем только при создании таблицы
- Файл save_datadase.py сохраняет в clickhouse данные ML_questions.csv
- Файл find_nearest_neighbors.py ищет вопрос в векторной базе данных
- Файл fined_nearest_n_test.py ищет список вопросов
- Файл save_emb.py сохраняет новый sample в БД
- ML_questions.csv - данные вопрос-ответ по ML/DL
# ClickHouse
1) Скачан docker desktop + создана БД ClickHouse: https://www.youtube.com/watch?v=W22Dp3rGkis
2) При создании ClickHouse в консоли Ubuntu пишем: docker run --name clickhouse -p 8123:8123 -e CLICKHOUSE_ADMIN_PASSWORD=1234 -d bitnami/clickhouse:latest
# Модель
Взята из https://huggingface.co/intfloat/e5-small-v2. Для простоты скачиваем из hf, можно скачать и локально работать быстрее. Есть доп вариации: e5-base, e5-large, e5-large-instruct