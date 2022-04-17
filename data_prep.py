import os
import pandas as pd

df1 = pd.read_csv('Dataset-Unicauca-Version2-87Atts.csv')
df1.dropna(inplace=True)
df1.drop(columns=["Timestamp"], inplace=True)

hiprof = list(df1[df1['Flow.Bytes.s'] > (1024 * 8 * 2048)]['Source.IP'].value_counts().index)
med1prof = list(df1[(df1['Flow.Bytes.s'] < (1024 * 8 * 2048)) & (df1['Flow.Bytes.s'] > (1024 * 8 * 1024))][
                    'Source.IP'].value_counts().index)
med2prod = list(df1[(df1['Flow.Bytes.s'] < (1024 * 8 * 1024)) & (df1['Flow.Bytes.s'] > (1024 * 8 * 256))][
                    'Source.IP'].value_counts().index)
lowprof = list(df1[(df1['Flow.Bytes.s'] < (1024 * 8 * 256))]['Source.IP'].value_counts().index)


def labels(x):
    if hiprof.count(x):
        return 3
    elif med1prof.count(x):
        return 2
    elif med2prod.count(x):
        return 1
    else:
        return 0


df1['labels'] = df1['Source.IP'].apply(lambda x: labels(x))

prtin = df1[df1['Source.IP'].str.contains('10.200.7.') | (df1['Source.IP'].str.contains('192.168.'))][
    'ProtocolName'].value_counts().head(16).index

df1.drop(columns=["Label", "Source.IP", "Source.Port", "Destination.IP", "Destination.Port"], inplace=True)
df1.shape
df1.to_csv('Dataset-Unicauca-Version2-87Atts-Clean.csv', index=False)
