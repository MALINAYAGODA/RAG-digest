import clickhouse_connect

client = clickhouse_connect.get_client(host='127.0.0.1', username='default', password='1234')
client.command("SET allow_experimental_annoy_index = 1;")

# Создание таблицы
# L2Distance - Евклидово расстояние 
# cosineDistance - cos расстояние
client.command("""
CREATE TABLE ann_index_example
(
  Name String,
  embedding Array(Float32),
  INDEX ann_index_1 embedding TYPE annoy('L2Distance'),
  Name_2 String,
)
ENGINE = MergeTree
ORDER BY Name;
""")