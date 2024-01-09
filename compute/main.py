import pandas as pd
import plotly.express as px

LEFT_NEW_CSV = 'new.csv'
RIGHT_OLD_CSV = 'old.csv'


def get_csv_data(new_dest, old_dest):
    new = pd.read_csv(new_dest)
    old = pd.read_csv(old_dest)


    return(new, old)

def joinem(new,old):

    joined = new.merge(old, on='refId', how='left')
    counted = joined[['refId', 'years_x']]['years_x'].value_counts()

    return(pd.DataFrame(counted))

def drawtheshit(df):

    fig = px.bar(df, x=df.index, y='count')
    fig.show()

    return

def main():

    new, old=get_csv_data(LEFT_NEW_CSV, RIGHT_OLD_CSV)
    counted = joinem(new,old)
    print(type(counted))
    print(counted)

    drawtheshit(counted)

    return

if __name__ == "__main__":
    main()
