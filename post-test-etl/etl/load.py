import pandas
import os

def make_dir(path):
    os.makedirs(path, exist_ok=True)

def create_csv(path, data):
    for d in data.keys():
        df = pandas.DataFrame(data[d])
        df.to_csv(f'{path}/{d}.csv', index=False)
        print(f'{d}.csv created on folder {path}')