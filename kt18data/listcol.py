#change test

def lsc(dataframe, list):
    import pandas as pd
    series1 = pd.Series(list)
    dataframe['newcol']=series1