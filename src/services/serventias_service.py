from ..dao.serventias_dao import ServentiasDAO


class ServentiasService:

    def __init__(self):
        pass

    def get_serventias(self):
        serventias_dao = ServentiasDAO()
        dict = {}
        serventias = serventias_dao.get_serventias_list()
        filhos = self.get_filhos(serventias)
        for row in serventias:
            dict[row[0]] = {
                "seq_orgao": row[0] if row[0] is not None else None,
                "nomedavara": row[1] if row[1] is not None else None,
                "seq_orgao_pai": row[2] if row[2] is not None else None,
                "tip_orgao": row[3] if row[3] is not None else None,
                "seq_cidade": row[4] if row[4] is not None else None,
                "dsc_cidade": row[5] if row[5] is not None else None,
                "sig_uf": row[6] if row[6] is not None else None,
                "cod_ibge": row[7] if row[7] is not None else None,
                "dsc_tip_orgao": row[8] if row[8] is not None else None,
                "tip_esfera_justica": row[9] if row[9] is not None else None,
                "int_ordem_orgao": row[10] if row[10] is not None else None,
                "dsc_orgao": row[11] if row[11] is not None else None,
                "cod_filhos": filhos[row[0]] if row[0] in filhos else None
            }
        formated_data = []
        for row in serventias:
            if row[2] is None and row[0] is not None:
                if dict[row[0]]['cod_filhos'] is not None:
                    item = {
                        'id': row[0],
                        'label': row[1],
                        'children': self.generate_tree(row[0], dict)
                    }
                else:
                    item = {
                        'id': row[0],
                        'label': row[1]
                    }
                formated_data.append(item)

        del serventias_dao
        return formated_data

    def get_filhos(self, serventias):
        filhos = {}
        for row in serventias:
            if row[2] in filhos:
                filhos[row[2]].append(row[0])
            else:
                filhos[row[2]] = [row[0]]

        return filhos

    def generate_tree(self, id, serv_dict):
        filhos_formatados = []
        for item in serv_dict[id]['cod_filhos']:
            if serv_dict[item]['cod_filhos'] is not None:
                dict = {
                    'id': item,
                    'label': serv_dict[item]['nomedavara'],
                    'children': self.generate_tree(item, serv_dict)
                }
            else:
                dict = {
                    'id': item,
                    'label': serv_dict[item]['nomedavara']
                }
            filhos_formatados.append(dict)
        return filhos_formatados
