
class Movimento:

    def __init__(self, millis_insercao=None, numero=None, identificador_movimento=None,
                 tipo_responsavel_movimento=None, codigo_nacional=None, data_hora=None):
        self.millis_insercao = millis_insercao
        self.numero = numero
        self.identificador_movimento = identificador_movimento
        self.tipo_responsavel_movimento = tipo_responsavel_movimento
        self.codigo_nacional = codigo_nacional
        self.data_hora = data_hora

    def get_millis_insercao(self):
        return self.millis_insercao

    def get_numero(self):
        return self.numero

    def get_identificador_movimento(self):
        return self.identificador_movimento

    def get_tipo_responsavel_movimento(self):
        return self.tipo_responsavel_movimento

    def get_codigo_nacional(self):
        return self.codigo_nacional

    def get_data_hora(self):
        return self.data_hora
