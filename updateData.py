import streamlit as st
from prognoseDF import prognoseDF, plausibilisierung 
import time
from db import conn,updateDB,up_table
from schaetzung import regression


pdfOi=prognoseDF

index={
    "Immobilien":0,
    "Logistik DL":1,
    "Material":2,
    "others":3,
    "Personal":4,
    "Transport Ocean":5,
    "Transport Road":6,
    "Transport Shuttle":7
}

def update_data(category,j2019,j2020,j2021,j2022,j2023):
    
    pdfOi.loc[category, '2019'] = j2019
    pdfOi.loc[category, '2020'] = j2020
    pdfOi.loc[category, '2021'] = j2021
    pdfOi.loc[category, '2022'] = j2022
    pdfOi.loc[category, '2023'] = j2023
    

    print("################################")
    print(category)
    print(index[category])
    
    up_table(category,j2019,j2020,j2021,j2022,j2023)

    
    
    regression()
    
    #st.experimental_set_query_params(page="localhost:8501/")
    #st.markdown("[You are being redirected to Prognose page...](http://localhost:8501/)")
    #st.markdown("<meta http-equiv='refresh' content='0;URL=http://localhost:8501/'>", unsafe_allow_html=True)
