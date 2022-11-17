import pandas as pd

df = pd.read_csv('full_padron.csv')
# print(df)


# 1 - Total de personas
print(f"Cantidad de personas totales: {len(df)}")

# 2- Cantida de personas por provincia


# 3- Cantidad de personas con cierto nombre
nombre = 'DAISY maria'
new_df = df.loc[df['NOMBRE'] == nombre.upper()]
new_df = new_df.reset_index()
print(f"Personas que coinciden con este nombre: {new_df.index.stop}")


# 4 - Cantidad de personas con cierto apellido... Lista.
apellido = 'JIMENEZ'
new_df = df.loc[(df['APELLIDO_1'] == apellido.upper()) |
                (df['APELLIDO_2'] == apellido.upper())]
new_df = new_df.reset_index()
print(f"Hay: {new_df.index.stop} personas con ese apellido.")


# 5- Consultas por numero de cedula... LISTA.
cedula = 102400349
new_df = df.loc[df['CÉDULA'] == cedula]
print(new_df[['NOMBRE', 'APELLIDO_1', 'APELLIDO_2']])
