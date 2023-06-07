import pandas as pd
import numpy as np


class StatisticsService:

    def __init__(self):
        pass

    def get_outliers(self, df, threshold=2, direcao=1, column_name=None):
        mean = np.mean(df[column_name])
        std = np.std(df[column_name])

        dic = {
            "codmovimento": str(df['codigonacional'].iloc[0]),
            "descricao": str(df['dsc_mov'].iloc[0]),
            "mean": mean,
            "std": std,
            "outliers": {}
        }

        for y in df.index:
            if std > 0:
                z_score = (df.at[y, column_name] - mean)/std
            else:
                z_score = 0
            if direcao*z_score > threshold:
                dic['outliers'][y] = {}
                dic['outliers'][y]['value'] = df.at[y, column_name]
                dic['outliers'][y]['zscore'] = z_score

        return dic

    def get_all_desempenho(self, df, direcao=1, column_name=None):
        mean = np.mean(df[column_name])
        std = np.std(df[column_name])

        dic = {
            "codmovimento": str(df['codigonacional'].iloc[0]),
            "descricao": str(df['dsc_mov'].iloc[0]),
            "mean": mean,
            "std": std,
            "serventias": {}
        }

        for y in df.index:
            if std > 0:
                z_score = (df.at[y, column_name] - mean)/std
            else:
                z_score = 0
            dic['serventias'][y] = {}
            dic['serventias'][y]['value'] = df.at[y, column_name]
            dic['serventias'][y]['zscore'] = z_score
        return dic

    def format_data_frame_by_codigonacional(self, df, column_name):
        df = df.set_index(column_name)
        cod_nacional = df['codigonacional'].unique()
        df_list = []

        for i in cod_nacional:
            df_list.append(df[(df['codigonacional'] == i)])

        return df_list

    def format_data_frame_by_zscore(self, df, column_name):
        df = df.set_index(column_name)
        mean = np.mean(df['avg'])
        std = np.std(df['avg'])
        df['zscore'] = (df['avg'] - mean)/std

        return df

