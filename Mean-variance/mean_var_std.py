import numpy as np


def calculate(lista):
  if len(lista) != 9:
    raise ValueError("List must contain nine numbers.")

  # Convert the input list to a NumPy array and reshape
  lista_array = np.array(lista).reshape((3, 3))

  media = [
      lista_array.mean(axis=0).tolist(),
      lista_array.mean(axis=1).tolist(),
      np.mean(lista_array).tolist()
  ]

  varianza = [
      lista_array.var(axis=0).tolist(),
      lista_array.var(axis=1).tolist(),
      np.var(lista_array).tolist()
  ]

  desviacion_estandar = [
      lista_array.std(axis=0).tolist(),
      lista_array.std(axis=1).tolist(),
      np.std(lista_array).tolist()
  ]

  maximo = [
      lista_array.max(axis=0).tolist(),
      lista_array.max(axis=1).tolist(),
      np.max(lista_array).tolist()
  ]

  minimo = [
      lista_array.min(axis=0).tolist(),
      lista_array.min(axis=1).tolist(),
      np.min(lista_array).tolist()
  ]

  suma = [
      lista_array.sum(axis=0).tolist(),
      lista_array.sum(axis=1).tolist(),
      np.sum(lista_array).tolist()
  ]

  return {
      "mean": media,
      "variance": varianza,
      "standard deviation": desviacion_estandar,
      "max": maximo,
      "min": minimo,
      "sum": suma
  }


