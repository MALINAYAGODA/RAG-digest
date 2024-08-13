from sentence_transformers import SentenceTransformer


class Encoder:
    def __init__(self, model_name):
      try:
          print('load')
          self.model = SentenceTransformer(model_name)
          print('load_model')
      except:
          raise ValueError("The model doesn't exist")

    def encode(self, text, batch_size=10):
        # Получение векторного представления текста
        vector_representations = []
        for i in range(0, len(text), batch_size):
            response = self.model.encode(text[i:i + batch_size])
            vector_representations.extend(response)
        # print(type(vector_representation))
        return vector_representations