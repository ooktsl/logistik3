# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:42:06 2023



@author: Ömer Kutsal
"""

#import libs
import streamlit as st 

st.set_page_config(page_title="Logistikkostenprognose", page_icon="🚀", layout="wide")


from db import aktuellData, up_table
import pandas as pd
from streamlit_elements import elements, mui, dashboard

               
               
#footer
st.markdown(
    '<div style="position: fixed; bottom: 10px; right: 10px; padding: 10px; padding-right:40px">'
    'Logistikkostenprognose, v1.1-3, 2023-12-20'
    '</div>',
    unsafe_allow_html=True
)
st.markdown("""
    <style>
        img.right {
            float: right;
            margin: 0 0 0 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .sidebar-content {
            max-width: 300px; 
        }
    </style>
""", unsafe_allow_html=True)






#settings 
#col1, col2,col3,col4,col5 = st.columns(5) 
col1, col2, col3= st.columns((1,8,1),gap="small") 


with col1:
    st.image("./logo/i-wunder2.png", use_column_width='auto' )
with col2:
    st.markdown("<h1 style='text-align: center;'>Logistikkostenprognose</h1>", unsafe_allow_html=True)
with col3:
    st.image("./logo/fabianRogalla.png",use_column_width='auto')


# <div class="block-container st-emotion-cache-z5fcl4 ea3mdgi2" data-testid="block-container" ></div>
    


#load data
styles = {
    '2024': [{'selector': '', 'props': [('background-color', 'lightblue')]}],
    '2025': [{'selector': '', 'props': [('background-color', 'lightgreen')]}]
}


df = pd.DataFrame(aktuellData(),columns=['Treiber','2019', '2020', '2021', '2022', '2023','2024','2025','2026','2027','2028'])
df['Treiber']= ["Immobilien","Logistik DL","Material","others","Personal","Transport Ocean","Transport Road","Transport Shuttle"]
df = df.set_index('Treiber')


#sidebar
action=st.sidebar.selectbox('Entwicklung',('Prognose','Edit'))

if action == "Edit":
    st.sidebar.write("Edit Data:")
    name_to_edit = st.sidebar.selectbox("Select Treiber:",df.index.tolist())
    if name_to_edit in df.index.tolist():
        
        j2019 = st.sidebar.number_input("2019 Kosten:", value=int(df.loc[name_to_edit, '2019']), step=100)
        j2020 = st.sidebar.number_input("2020 Kosten:", value=int(df.loc[name_to_edit, '2020']), step=100)
        j2021 = st.sidebar.number_input("2021 Kosten:", value=int(df.loc[name_to_edit, '2021']), step=100)
        j2022 = st.sidebar.number_input("2022 Kosten:", value=int(df.loc[name_to_edit, '2022']), step=100)
        j2023 = st.sidebar.number_input("2023 Kosten:", value=int(df.loc[name_to_edit, '2023']), step=100)

        clicked=st.sidebar.button("Update Data")
        if clicked:
            up_table(name_to_edit,j2019,j2020,j2021,j2022,j2023)
            st.sidebar.success("Data updated successfully!")
            #st.experimental_set_query_params() 
            
        
    
#plausibilisierungOi= plausibilisierung.reset_index(drop=True)
   
df = pd.DataFrame(aktuellData(),columns=['Treiber','2019', '2020', '2021', '2022', '2023','2024','2025','2026','2027','2028'])
df['Treiber']= ["Immobilien","Logistik DL","Material","others","Personal","Transport Ocean","Transport Road","Transport Shuttle"]
df = df.set_index('Treiber')
#st.dataframe(df.iloc[:,0:10].style.format("{:,.0f} €",thousands=".").set_table_styles(styles))

def highlight_2024(s):
    return ['background-color: orange' if col in ('2024','2025','2026','2027','2028') else '' for col in s.index]
    
styled_df = df.iloc[:, 0:10].style.apply(highlight_2024, axis=1).format("{:,.0f} €", thousands=".").set_table_styles(styles)

col1, col2= st.columns((8,4),gap="small") 

with col1:
    st.write("Prognose") 
    st.dataframe(styled_df)


with col2:
    st.write("")
    st.write("")
    st.image("./logo/containers.png", use_column_width='auto',)

