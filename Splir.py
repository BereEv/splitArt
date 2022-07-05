import pandas as pd
import glob


def split_art():
    df = [pd.read_excel(f, header=0) for f in glob.glob('files/*.xlsx')]
    art = pd.concat(df, keys=glob.glob('files/*xlsx'))
    names_cols = list(art.columns)
    art = art.rename(columns={names_cols[0]: 'Артикул'})
    art[['Art1', 'Art2', 'Art3']] = art['Артикул'].str.split('-', n=2, expand=True)
    art.to_excel('log/new.xlsx')


split_art()
