import os


class Helper:
    """
    implementa métodos estáticos úteis
    """

    @staticmethod
    def test():
        pass

    @staticmethod
    def get_leaf_paths():
        chosen_path = (os.getcwd())
        paths_found = []
        for root, dirs, files in os.walk(chosen_path + "/base", topdown=True):
            for name in files:
                if ".json" in name:
                    paths_found.append(root + "\\" + name)
        paths_found.sort()
        return paths_found

