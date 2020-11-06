import pandas as pd
import seaborn as sns

notas = pd.read_csv("C:/Users/Administrador/Documents/Python/notebooks/aula0/ml-latest-small/ratings.csv")

notas.columns = ['usuario id', 'filmeId','nota','momento']

notas.nota.plot(kind="hist")

notas.nota.describe()

sns.boxplot(notas.nota)

filmes = pd.read_csv("C:/Users/Administrador/Documents/Python/notebooks/aula0/ml-latest-small/movies.csv")
filmes.columns = ["filmeId","titulo","genero"]


notas.query("filmeId==1").nota.mean()

media_por_filme = notas.groupby("filmeId").mean()['nota']

sns.boxplot(media_por_filme)

sns.distplot(media_por_filme)

import matplotlib.pyplot as plt

movies = pd.read_csv("C:/Users/Administrador/Documents/Python/notebooks/tmdb-movie-metadata/tmdb_5000_movies.csv")
movies.head()

teste = movies["original_language"].value_counts().to_frame().reset_index()
teste.columns = ["original_language","total"]
teste.head()

sns.barplot(x="original_language",y="total",data=teste)

sns.catplot(x="original_language",kind="count",data=movies)

plt.pie(teste['total'],labels=teste['original_language'])

