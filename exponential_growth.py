import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
np.set_printoptions(suppress=True)
pd.show_versions()

#Ingress 
st.title('Renters Rente [BETA]')
st.write('Verdens åttende underverk')

# Kladd
#st.write("""
#If you invest a sum of money at 10 per cent for five years, you will multiply your wealth by 1.6 times.

#If you invest your capital at that rate for 10 times as long (50 years), you will not multiply your wealth by 16 times.

#You will multiply it by more than 117 times.
#	""") 

## Oppsparte midler 
S = st.number_input(label='Oppsparte middler :*** Not working', key=int, value=10000)
### Sett månedlig inntekt:
mI = st.number_input(label='Månedlig sparing på:', value=1599)
### Sett månedlig Rente / avkastning - antatt snitt
rente = st.number_input(label='Gjennomsnittlig årlig rente på:', value=7.88)
### Antall år
n = st.number_input(label='Antall år med sparing:', key=int, value=18)


########## Prosjekt Rente
r = ((rente / 100)+1)

############## Prosjekt Inflasjon #### KLADD
åInf = 0.025
#mInf = mI * åInf
#mI = mI - mInf
# Årlig inntekt:
åI = mI * 12
#15.991 - 18.296. (2.306 14.42%) 
#print((mI-åInf) * 12)
#sparepenger infl.
inflS = S * åInf
#S = S - inflS

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

df[df < (df[1].iloc[0])] = 0

first = df[1].iloc[0]
list1 = df[1]
list2 = []

for i in list1:
  if i <= first:
    list2.append(first + (S * r))
  else:
    list2.append(i + (S *r))
df[1] = list2

df['Sammenlagt'] = df.sum(axis=1)

tot = df['Sammenlagt'].iloc[-1]

åInf = 0.025
inflTot = tot * åInf
tot = tot - inflTot


###### Prosjekt Antall år column 
df['AntallÅr'] = range(len(df))
df['AntallÅr'] = df['AntallÅr'] + 1
df.index += 1 

#oppsp = S*r**n 
#total = df['Sammenlagt'].iloc[-1] + oppsp

print("So far so good")

###### Projsekt calculations 
st.write("Etter ",n,"år, vil pengene vokse til ",tot.round(0).astype(int),"kr.")

#st.write(f"Med ett første innskudd på: {S}kr og deretter en månedlig sparing på {mI}kr. Har pengene vokst til {tot}kr etter {n}år med en rente på {r}%.")
#st.write("Det er", (tot-(1599*12)*ÅR).round(0).astype(int), "kr mer enn å spare på sparekonto.")
#st.write(""" Med en årlig sparing på:", int(åI/12),"kr i MND", "og med en gj.snitt rente på", rente,"% vil totalbeløpet til syvende og sist bli", tot.round(0).astype(int), "kr", "etter", ÅR, "år" """)
#st.write("Det er", (tot-(1599*12)*ÅR).round(0).astype(int), "kr mer enn å spare på sparekonto.")
#st.write("Med oppsparte midler og fast innsatt beløp er TOTALEN", total.round(0).astype(int), "kr ")


###### Prosjekt grafer
st.line_chart(data=df.Sammenlagt, use_container_width=1,)


print(df)

