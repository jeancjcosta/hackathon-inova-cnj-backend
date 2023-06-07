from ..dao.assuntos_dao import AssuntosDAO


class AssuntosService:

    def __init__(self):
        pass

    def get_assuntos(self):
        assuntos_dao = AssuntosDAO()
        dict = {}
        assunto_list = assuntos_dao.get_assuntos_list()
        for row in assunto_list:
            f = row[3].split(",") if row[3] is not None else None
            if f is not None:
                for i in range(0, len(f)):
                    try:
                        f[i] = int(f[i]) if int(f[i]) < 13000 else None
                    except:
                        f[i] = None
            dict[row[0]] = {
                "codigo": row[0] if row[0] is not None else None,
                "descricao": row[1],
                "pai": row[2] if row[2] is not None else None,
                "filhos": f
            }
        del assuntos_dao
        formated_data = []
        for row in assunto_list:
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

    def generate_tree(self, id, assunto_dict):
        filhos_formatados = []
        for item in assunto_dict[id]['filhos']:
            if item is not None:
                if assunto_dict[item]['filhos'] is not None:
                    dict = {
                        'id': item,
                        'label': assunto_dict[item]['descricao'],
                        'children': self.generate_tree(item, assunto_dict)
                    }
                else:
                    dict = {
                        'id': item,
                        'label': assunto_dict[item]['descricao']
                    }
                filhos_formatados.append(dict)
        return filhos_formatados