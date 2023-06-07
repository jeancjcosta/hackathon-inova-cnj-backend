from ..services.movimento_service import MovimentosService
from ..services.statistics_service import StatisticsService
from ..services.dados_basicos_service import DadosBasicosService
from flask import jsonify


class ReportController:

    def __init__(self):
        pass

    @staticmethod
    def gargalos(request):
        codigo_assunto = request.args.get('codigoAssunto')
        codigo_classe = request.args.get('codigoClasse')
        threshold = request.args.get('threshold')
        if threshold is None:
            threshold = 0.5
        else:
            threshold = float(threshold)
        calcs = MovimentosService().get_avg_std_by_movimento_full(codigo_classe, codigo_assunto)
        calcs_all = DadosBasicosService().get_avg_std_processo_full(codigo_classe, codigo_assunto)
        statistics = StatisticsService()
        df_list = statistics.format_data_frame_by_codigonacional(calcs, 'codigoorgao')
        df_bolha = statistics.format_data_frame_by_zscore(calcs_all, 'codigoorgao')
        dict_return = {}
        columns = []
        bolha_series = []

        for df in df_list:
            dic = statistics.get_outliers(df, threshold=threshold, column_name='avg')
            column_dic = {}
            if len(dic['outliers']) > 0:
                column_dic['mean_geral'] = dic['mean']
                column_dic['std_geral'] = dic['std']
                column_dic['descricao'] = dic['descricao']
                column_dic['serventias'] = []
                for serventia in dic['outliers']:
                    serventia_dict = {}
                    serventia_dict['nome'] = serventia
                    serventia_dict['mean'] = dic['outliers'][serventia]['value']
                    serventia_dict['zscore'] = dic['outliers'][serventia]['zscore']
                    column_dic['serventias'].append(serventia_dict)
                columns.append(column_dic)

        bolha_dic_eficientes = {
            'name': 'Eficientes',
            'color': "#90EE90",
            'data': []
        }
        bolha_dic_medianos = {
            'name': 'Próximos da Média',
            'color': "#FFD700",
            'data': []
        }
        bolha_dic_lentos = {
            'name': 'Lento nos Movimentos',
            'color': "#DC143C",
            'data': []
        }

        for serventia in df_bolha.index:
            dic_serventia = {
                    'name': serventia,
                    'value': int(df_bolha.at[serventia, 'count'])
                }
            if df_bolha.at[serventia, 'zscore'] < -threshold:
                bolha_dic_eficientes['data'].append(dic_serventia)
            elif -threshold < df_bolha.at[serventia, 'zscore'] < threshold:
                bolha_dic_medianos['data'].append(dic_serventia)
            else:
                bolha_dic_lentos['data'].append(dic_serventia)
        bolha_series.append(bolha_dic_eficientes)
        bolha_series.append(bolha_dic_medianos)
        bolha_series.append(bolha_dic_lentos)

        dict_return['columns'] = columns
        dict_return['bolhas'] = bolha_series
        return jsonify(dict_return)

    @staticmethod
    def gargalos_serventia(request):
        codigo_serventia = request.args.get('codigoServentia')
        codigo_assunto = request.args.get('codigoAssunto')
        codigo_classe = request.args.get('codigoClasse')
        threshold = request.args.get('threshold')
        if threshold is None:
            threshold = 0.5
        else:
            threshold = float(threshold)
        calcs = MovimentosService().get_avg_std_by_movimento(codigo_serventia, codigo_classe, codigo_assunto)
        statistics = StatisticsService()
        df_list = statistics.format_data_frame_by_codigonacional(calcs, 'codigoorgao')
        dict_list = {
            'columns': [],
            'speedometer': []
        }
        for df in df_list:
            dict = statistics.get_outliers(df, threshold=threshold, column_name='avg')
            dict_aux = {}
            if int(codigo_serventia) in dict['outliers']:
                dict_aux['codmovimento'] = dict['codmovimento']
                dict_aux['descricao'] = dict['descricao']
                dict_aux['avg_geral'] = dict['mean']
                dict_aux['avg_serventia'] = dict['outliers'][int(codigo_serventia)]['value']
                dict_aux['std_geral'] = dict['std']
                dict_aux['zscore'] = dict['outliers'][int(codigo_serventia)]['zscore']
                dict_list['columns'].append(dict_aux)
            dict2 = statistics.get_all_desempenho(df, column_name='avg')
            dict_aux2 = {}
            if int(codigo_serventia) in dict2['serventias']:
                dict_aux2['codmovimento'] = dict2['codmovimento']
                dict_aux2['descricao'] = dict2['descricao']
                dict_aux2['avg_geral'] = dict2['mean']
                dict_aux2['avg_serventia'] = dict2['serventias'][int(codigo_serventia)]['value']
                dict_aux2['std_geral'] = dict2['std']
                dict_aux2['zscore'] = dict2['serventias'][int(codigo_serventia)]['zscore']
                dict_list['speedometer'].append(dict_aux2)
        return jsonify(dict_list)

    @staticmethod
    def expected_process_duration(request):
        codigo_serventia = request.args.get('codigoServentia')
        codigo_assunto = request.args.get('codigoAssunto')
        codigo_classe = request.args.get('codigoClasse')

        calc = DadosBasicosService().get_avg_std_processo(codigo_serventia, codigo_classe, codigo_assunto)

        return jsonify(calc[0])

    @staticmethod
    def performance_statistics(request):
        codigo_serventia = request.args.get('codigoServentia')

        return jsonify(0)
