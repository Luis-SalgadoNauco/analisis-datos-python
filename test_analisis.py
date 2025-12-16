import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'x': np.random.randn(100),
    'y': np.random.randn(100)
}

df = pd.DataFrame(datos)

print("Estadísticas básicas:")
print(df.describe())

plt.scatter(df['x'], df['y'])
plt.title('Primer gráfico con Python')
plt.savefig('primer_grafico.png')
print("Gráfico guardado como primer_grafico.png")