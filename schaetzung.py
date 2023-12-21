import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import numpy as np
from db import aktuellData,up_Predict


def regression():

    df = pd.DataFrame(aktuellData(),columns=['Treiber','2019', '2020', '2021', '2022', '2023','2024','2025','2026','2027','2028'])
    print("vor regression",df)
    prognoseDF=df
    years = ['2019', '2020', '2021', '2022', '2023']
    data = prognoseDF[years].values.T  

    model = LinearRegression()

    
    for i in range(prognoseDF.shape[0]):
        # 2019-2023 yıllarına ait verileri kullanarak modeli eğit
        X = np.array(list(range(len(years)))).reshape(-1, 1)
        y = data[:, i]
        model.fit(X, y)

        # 2024-2028 yıllarına ait tahminler
        future_years = np.array(list(range(len(years), len(years) + 5))).reshape(-1, 1)
        predictions = model.predict(future_years)

        # Tahminleri DataFrame'e ekle
        prognoseDF.loc[i, '2024':'2028'] = predictions.astype('int64')

    print("reg",prognoseDF)

    for i in range(8):
        up_Predict(prognoseDF.iloc[i,0],prognoseDF.iloc[i,6],prognoseDF.iloc[i,7],prognoseDF.iloc[i,8],prognoseDF.iloc[i,9],prognoseDF.iloc[i,10])



def polynomial_regression():

    # AktuellData fonksiyonunuzun uygun bir şekilde tanımlandığını varsayalım
    df = pd.DataFrame(aktuellData(), columns=['Treiber', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028'])

    prognoseDF = df
    years = ['2019', '2020', '2021', '2022', '2023']
    data = prognoseDF[years].values.T  

    for i in range(prognoseDF.shape[0]):
        # 2019-2023 yıllarına ait verileri kullanarak modeli eğit
        X = np.array(list(range(len(years)))).reshape(-1, 1)
        y = data[:, i]

        # Polinom özelliklerini ekleyerek X matrisini genişlet
        degree = 2  # İsterseniz bu dereceyi istediğiniz gibi ayarlayabilirsiniz
        poly = PolynomialFeatures(degree=degree)
        X_poly = poly.fit_transform(X)

        model = LinearRegression()
        model.fit(X_poly, y)

        # 2024-2028 yıllarına ait tahminler
        future_years = np.array(list(range(len(years), len(years) + 5))).reshape(-1, 1)
        future_years_poly = poly.transform(future_years)
        predictions = model.predict(future_years_poly)

        # Tahminleri DataFrame'e ekle
        prognoseDF.loc[i, '2024':'2028'] = predictions.astype('int64')

    print("Poly",prognoseDF)


def exponential_smoothing():

    # AktuellData fonksiyonunuzun uygun bir şekilde tanımlandığını varsayalım
    df = pd.DataFrame(aktuellData(), columns=['Treiber', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028'])

    prognoseDF = df
    years = ['2019', '2020', '2021', '2022', '2023']
    
    for i in range(prognoseDF.shape[0]):
        # 2019-2023 yıllarına ait verileri kullanarak modeli eğit
        data = prognoseDF.loc[i, years].values.astype(float)

        # 'multiplicative' mevsimsel özellikler ile Exponential Smoothing modeli
        model = ExponentialSmoothing(data, seasonal='additive', seasonal_periods=len(years), initialization_method=None)



        fit_model = model.fit()

        # 2024-2028 yıllarına ait tahminler
        predictions = fit_model.forecast(steps=5)

        # Tahminleri DataFrame'e ekle
        prognoseDF.loc[i, '2024':'2028'] = predictions.astype('int64')

    print("ETS",prognoseDF)

regression()
polynomial_regression()
#exponential_smoothing()


