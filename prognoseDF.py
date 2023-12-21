import pandas as pd



prognoseDF=pd.DataFrame({
    '2019': [3900,1667, 1200,1500,2500,3000,2600,3000] ,  
    '2020':[4100,1806,1350,1650,2800,6000,3000,3200],
    '2021':[4500,1990,1624,1850,3000,6500,3300,3250],
    '2022':[4600,2200,1700,2000,3200,5500,3500,3500],
    '2023':[4800,2440,2000,2200,3500,3500,3600,4000],
    '2024':[0,0,0,0,0,0,0,0],
    '2025':[0,0,0,0,0,0,0,0],
    '2026':[0,0,0,0,0,0,0,0],
    '2027':[0,0,0,0,0,0,0,0],
    '2028':[0,0,0,0,0,0,0,0]
})



prognoseDF['Treiber']= ["Immobilien","Logistik DL","Material","others","Personal","Transport Ocean","Transport Road","Transport Shuttle"]
prognoseDF = prognoseDF.set_index('Treiber')


plausibilisierung=pd.DataFrame({
    'lokaler Trend': [1,2,3],
    'lokaler Anstieg ': [3 , 3,3] ,  
    'gloabaler Trend':[1,2,4],
    'gloabaler Anstieg':[1,2,3]
})