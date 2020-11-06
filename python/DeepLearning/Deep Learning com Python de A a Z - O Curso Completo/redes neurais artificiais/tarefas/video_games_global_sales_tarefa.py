import pandas as pd
from tensorflow.keras.layers import Dense, Dropout, Activation, Input # atualizado: tensorflow==2.0.0-beta1
from tensorflow.keras.models import Model # atualizado: tensorflow==2.0.0-beta1

base = pd.read_csv('games.csv')
base = base.drop('Other_Sales', axis = 1)
base = base.drop('Developer', axis = 1)

# Como faremos a previsão somente do Global_Sales, precisamos excluir as
# vendas na América do Norte, Europa e Japão
base = base.drop('NA_Sales', axis = 1)
base = base.drop('EU_Sales', axis = 1)
base = base.drop('JP_Sales', axis = 1)

# Apagamos os registros com valores faltantes
base = base.dropna(axis = 0)

# Retiramos da base de dados vendas com valores menores do que 1
base = base.loc[base['Global_Sales'] > 1]

base['i#Name'].value_counts()
nome_jogos = base['i#Name']
base = base.drop('i#Name', axis = 1)

# Aqui mudamos os índices dos atributos previsores e também do valor a ser previsto
previsores = base.iloc[:, [0,1,2,3,5,6,7,8,9]].values
valor_vendas = base.iloc[:, 4].values

# Transformação dos atributos categóricos
from sklearn.preprocessing import OneHotEncoder #atualizado
from sklearn.compose import ColumnTransformer #atualizado

onehotencorder = ColumnTransformer(transformers=[("OneHot", OneHotEncoder(), [0,2,3,8])],remainder='passthrough') #atualizado
previsores = onehotencorder.fit_transform(previsores).toarray() #atualizado

# A camada de entrada possui 99 neurônios na entrada, pois equivale a
# quantidade de atributos previsores após o pré-processamento
# A quantidade 50 é relativo a fórumula: (entradas (99) + saída (1)) / 2
# Definida somente uma camada de entrada pois estamos trabalhando somente com o valor total
camada_entrada = Input(shape=(99,))
ativacao = Activation(activation = 'sigmoid')
camada_oculta1 = Dense(units = 50, activation=ativacao)(camada_entrada)
camada_oculta2 = Dense(units = 50, activation=ativacao)(camada_oculta1)
camada_saida = Dense(units = 1, activation='linear')(camada_oculta2)

regressor = Model(inputs = camada_entrada, outputs=[camada_saida])
regressor.compile(optimizer='adam', loss='mean_squared_error')
regressor.fit(previsores, valor_vendas, epochs = 5000, batch_size=100)
previsoes = regressor.predict(previsores)
