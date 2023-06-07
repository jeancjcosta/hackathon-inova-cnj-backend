from ..dao.classes_dao import ClassesDAO


class ClassesService:

    def __init__(self):
        pass

    def get_classes(self):
        classes_dao = ClassesDAO()
        dict = {}
        classe_list = classes_dao.get_classes_list()
        for row in classe_list:
            f = row[4].split(",") if row[4] is not None else None
            if f is not None:
                for i in range(0, len(f)):
                    try:
                        f[i] = int(f[i]) if int(f[i]) < 13000 else None
                    except:
                        f[i] = None
            dict[row[0]] = {
                "codigo": row[0] if row[0] is not None else None,
                "descricao": row[1],
                "pai": row[3] if row[3] is not None else None,
                "filhos": f
            }
        del classes_dao
        formated_data = []
        for row in classe_list:
            if row[3] is None and row[0] is not None:
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

    def generate_tree(self, id, classe_dict):
        filhos_formatados = []
        for item in classe_dict[id]['filhos']:
            if item is not None:
                if classe_dict[item]['filhos'] is not None:
                    dict = {
                        'id': item,
                        'label': classe_dict[item]['descricao'],
                        'children': self.generate_tree(item, classe_dict)
                    }
                else:
                    dict = {
                        'id': item,
                        'label': classe_dict[item]['descricao']
                    }
                filhos_formatados.append(dict)
        return filhos_formatados
