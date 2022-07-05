import pandas as pd
import glob


def split_art():
    f = glob.glob('files/*.xlsx')
    files = f
    df = [pd.read_excel(f, header=0) for f in files]
    art = pd.concat(df, keys=glob.glob('files/*xlsx'))
    names_cols = list(art.columns)
    art = art.rename(columns={names_cols[0]: 'Артикул'})
    art[['Art1', 'Art2', 'Art3']] = art['Артикул'].str.split('-', n=2, expand=True)
    art.info()
    art.to_excel('log/new.xlsx')
    print('Готово')


split_art()
