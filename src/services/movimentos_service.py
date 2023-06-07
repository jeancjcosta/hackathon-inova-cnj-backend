from ..dao.movimentos_dao import MovimentosDAO


class MovimentosService:

    def __init__(self):
        pass

    def get_movimnetos(self):
        movimnetos_dao = MovimentosDAO()
        dict = {}
        mov_list = movimnetos_dao.get_movimnetos_list()

        for row in mov_list:
            f = row[3].split(",") if row[3] is not None else None
            if f is not None:
                for i in range(0, len(f)):
                    try:
                        f[i] = int(f[i]) if int(f[i]) < 13000 else None
                    except:
                        f[i] = None

            dict[row[0]] = {
                "seq_orgao": row[0] if row[0] is not None else None,
                "descricao": row[1] if row[1] is not None else None,
                "pai": row[2] if row[2] is not None else None,
                "filhos": f
            }
        del movimnetos_dao
        formated_data = []
        for row in mov_list:
            if row[2] is None and row[0] is not None:
                if dict[row[0]]['filhos'] is not None:
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
        return formated_data

    def generate_tree(self, id, mov_dict):
        filhos_formatados = []
        for item in mov_dict[id]['filhos']:
            if item is not None:
                if mov_dict[item]['filhos'] is not None:
                    dict = {
                        'id': item,
                        'label': mov_dict[item]['descricao'],
                        'children': self.generate_tree(item, mov_dict)
                    }
                else:
                    dict = {
                        'id': item,
                        'label': mov_dict[item]['descricao']
                    }
                filhos_formatados.append(dict)
        return filhos_formatados