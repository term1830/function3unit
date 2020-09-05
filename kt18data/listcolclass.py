#change test
import pandas as pd
from pandas import DataFrame

'''attempt at class, test list and dataframe are inside
this creates a new dataframe and also locks the df and 
list into the class, also creates a new dataframe 
'''
test_list = [2,5,1,76,8,2,3,7,2]

class Lsc():
    def __init__(self, df, listt):
        self.df = df
        self.listt = listt
        series1 = pd.Series(listt)
        df['newcol'] = series1


if __name__ == "__main__":
    df = DataFrame({"col":["T","A","F","H","E","B"]})
    df.head()

    breakpoint()
