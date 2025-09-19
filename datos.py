from flask import Flask
from flask import render_template
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)

#PRIMERA GRAFICA
def get_plot():
    dts = pd.read_csv("shopping_behavior_updated.csv")

    genero = dts[["Gender"]]
    monto = dts["Purchase Amount (USD)"]

    # Gráfico de barras
    sns.barplot(data=dts, x="Gender", y="Purchase Amount (USD)", hue="Gender", palette=["#92a8d1", "#f7cac9"])
    plt.title("Comparación monto de compra")
    return plt


#SEGUNDA GRAFICA
def get_plot2():
    dts = pd.read_csv("shopping_behavior_updated.csv")

    MetodoDePago = dts[["Payment Method"]]
    Edad = dts["Age"]

    # Gráfico de barras
    sns.violinplot(data=dts, x="Payment Method", y="Age", hue="Gender", split=True, palette=["#92a8d1", "#f7cac9"])
    plt.title("Metodos de pago por edad")
    return plt

#TERCERA GRAFICA
def get_plot3():
    dts = pd.read_csv("shopping_behavior_updated.csv")

    Precio = dts[["Purchase Amount (USD)"]]
    Calificacion = dts["Review Rating"]

    # Gráfico de barras
    sns.scatterplot(data=dts, x="Purchase Amount (USD)", y="Review Rating")
    sns.lineplot(x=dts["Purchase Amount (USD)"], y=dts["Review Rating"], color="blue")
    plt.title("Calficación en relación al precio")
    return plt

@app.route('/')
def home():
    plot = get_plot()
    plot.savefig(os.path.join("static","images","plot.jpg"))
    plt.close()
    plot2 = get_plot2()
    plot2.savefig(os.path.join("static","images","plot2.jpg"))
    plt.close()
    plot3 = get_plot3()
    plot3.savefig(os.path.join("static","images","plot3.jpg"))
    return render_template('index.html')


app.run(debug=True)