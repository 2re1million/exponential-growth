import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
np.set_printoptions(suppress=True)

#Ingress 
st.title('Renters Rente [BETA]')
st.write('Verdens åttende underverk')

# Kladd
#st.write("""
#If you invest a sum of money at 10 per cent for five years, you will multiply your wealth by 1.6 times.

#If you invest your capital at that rate for 10 times as long (50 years), you will not multiply your wealth by 16 times.

#You will multiply it by more than 117 times.
#	""") 

### Sett månedlig inntekt:
mI = st.number_input(label='Månedlig sparing på:', value=1599)
### Sett månedlig Rente / avkastning - antatt snitt
rente = st.number_input(label='Gjennomsnittlig årlig rente på:', value=7.88)
### Antall år
ÅR = st.number_input(label='Antall år med sparing:', key=int, value=18)


########## Prosjekt Rente
r = ((rente / 100)+1)
#r = (r1 + 1)
# Antall år:
n = ÅR

############## Prosjekt Inflasjon #### KLADD
åInf = 0.025
# Årlig inntekt:
åI = ((mI-åInf) * 12)
#15.991 - 18.296. (2.306 14.42%) 
#print((mI-åInf) * 12)

############# Prosjekt Eksponensiellvekst:
ev = åI*r**n

def column_generator(n):
    columns = []
    for i in range(n):
        columns.append(i + 1)
    return columns

columns = column_generator(n)

å = {'AntallÅr': columns}
df = pd.DataFrame(data=å)

for i in range(len(columns)):
    df[i + 1] = åI * r ** (df['AntallÅr'] - i)
    df[i + 1] = df[i + 1].round(1)

###### BUGG:  Se nærmere på denne  19200 (fjerne nuller på annen måte)

df[df <= 19200.0] = 0

df['Sammenlagt'] = df.sum(axis=1)

tot = df['Sammenlagt'].iloc[-1]

###### Prosjekt Antall år column 
df['AntallÅr'] = range(len(df))
df['AntallÅr'] = df['AntallÅr'] + 1

print("So far so good")

###### Porjsket calculations 
st.write("Med en årlig sparing på:", int(åI/12),"kr i MND", "og med en gj.snitt rente på", rente,"% vil totalbeløpet til syvende og sist bli", tot.round(0).astype(int), "kr", "etter", ÅR, "år")
st.write("Det er", (tot-(1599*12)*ÅR).round(0).astype(int), "kr mer enn å spare på sparekonto.")

###### Prosjekt grafer
st.line_chart(data=df.Sammenlagt,use_container_width=1,)


