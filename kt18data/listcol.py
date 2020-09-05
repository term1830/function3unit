#change test
from pandas import DataFrame

test_list = [2,5,1,76,8,2,3,7,2]

def lsc(dataframe, list):
    import pandas as pd
    series1 = pd.Series(list)
    dataframe['newcol'] = series1



if __name__ == "__main__":
    df = DataFrame({"col":["T","A","F","H","E","B"]})
    df.head()

    breakpoint()