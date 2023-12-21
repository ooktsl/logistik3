from statsmodels.tsa.arima.model import ARIMA



model = ARIMA([2500,3500,5000,4800,4600], order=(0,0,0))  
model_fit = model.fit()


tahminler = model_fit.predict(start='2024-01-01', end='2028-12-31', dynamic=True)

print(tahminler) 