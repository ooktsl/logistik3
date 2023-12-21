import streamlit as st
import sqlite3 



# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('kostenDB', type='sql')

with conn.session as g:
    g.execute('CREATE TABLE IF NOT EXISTS global (glabalVariable TEXT PRIMARY KEY,  j_2019 REAL, j_2020 REAL, j_2021 REAL, j_2022 REAL, j_2023 REAL, j_2024 REAL,j_2025 REAL,j_2026 REAL,j_2027 REAL,j_2028 REAL );')
    g.execute('Delete from global')

    zahlen = [("wci", 1400, 5900, 6300, 5300, 1600 ,0,0,0,0,0), 
            ("kraftstoff_diesel",1.285,1.134,1.41,1.97,1.733,0,0,0,0,0)
            ]
    
    for k in zahlen:
        g.execute(
            f'INSERT INTO global (glabalVariable, j_2019, j_2020, j_2021, j_2022, j_2023,j_2024,j_2025,j_2026,j_2027,j_2028) VALUES {tuple(k)};'
        )
    g.commit()



with conn.session as s:
    #s.execute('Drop Table IF EXISTS prognose')
    s.execute('CREATE TABLE IF NOT EXISTS prognose (treiber TEXT PRIMARY KEY, j_2019 REAL, j_2020 REAL, j_2021 REAL, j_2022 REAL, j_2023 REAL, j_2024 REAL,j_2025 REAL,j_2026 REAL,j_2027 REAL,j_2028 REAL );')
    
    try:
        status = conn.query('select * from prognose where treiber="Immobilien"')
        
    except:

        if True: #status["treiber"][0] == "Immobilien":
        
            zahlen = [("Immobilien", 3900, 4100, 4500, 4600, 4800,0,0,0,0,0), 
                        ("Logistik DL",1667,1806,1990,2200,2440,0,0,0,0,0),
                        ("Material",1200, 1350, 1624, 1700, 2000,0,0,0,0,0),
                        ("others", 1500, 1650, 1850, 2000, 2200,0,0,0,0,0),
                        ("Personal",2500, 2800, 3000, 3200, 3500,0,0,0,0,0),
                        ("Transport Ocean",3000, 6000, 6500, 5500, 3500,0,0,0,0,0),
                        ("Transport Road",2600, 3000, 3300, 3500, 3600,0,0,0,0,0),
                        ("Transport Shuttle", 3000, 3200, 3250, 3500, 4000,0,0,0,0,0)
                        ]
            for k in zahlen:
                s.execute(
                    f'INSERT INTO prognose (treiber, j_2019, j_2020, j_2021, j_2022, j_2023,j_2024,j_2025,j_2026,j_2027,j_2028) VALUES {tuple(k)};'
                )
            s.commit()
         


def updateDB(category,j2019,j2020,j2021,j2022,j2023):
    with conn.session as up:
            up.execute(f"""
                      UPDATE prognose 
                      SET j_2019 = {j2019}, j_2020 = {j2020}, j_2021 = {j2021}, j_2022 = {j2022}, j_2023 = {j2023}  
                          where treiber='{category}'
                    """)
            up.commit()
          


def up_table(category,j2019,j2020,j2021,j2022,j2023):
    conn = sqlite3.connect('kostenDB')
    print("############",conn)
    c = conn.cursor()
    c.execute(f' UPDATE prognose SET j_2019 = {j2019}, j_2020 = {j2020}, j_2021 = {j2021}, j_2022 = {j2022}, j_2023 = {j2023}  where treiber="{category}"' 
              )
    conn.commit()
    conn.close()

    #regression()

def up_Predict(category,j2024,j2025,j2026,j2027,j2028):
    conn = sqlite3.connect('kostenDB')    
    c = conn.cursor()
    c.execute(f' UPDATE prognose SET j_2024 = {j2024}, j_2025 = {j2025}, j_2026 = {j2026}, j_2027 = {j2027}, j_2028 = {j2028}  where treiber="{category}"' 
              )
    conn.commit()
    conn.close()


def aktuellData():
    conn = sqlite3.connect('kostenDB')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM prognose")
    data = cursor.fetchall()

    conn.close()
    return data