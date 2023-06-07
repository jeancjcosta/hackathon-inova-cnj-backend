
class DadosBasicos:

    def __init__(self, millis_insercao=None, assunto=None, dsc_sistema=None, tamanho_processo=None, numero=None,
                 procel=None, data_ajuizamento=None, total_assuntos=None, classe_processual=None, nivel_sigilo=None,
                 codigo_orgao=None, competencia=None, codigo_localidade=None, sigla_tribunal=None, grau=None):
        self.millis_insercao = millis_insercao
        self.assunto = assunto
        self.dsc_sistema = dsc_sistema
        self.tamanho_processo = tamanho_processo
        self.numero = numero
        self.procel = procel
        self.data_ajuizamento = data_ajuizamento
        self.total_assuntos = total_assuntos
        self.classe_processual = classe_processual
        self.nivel_sigilo = nivel_sigilo
        self.codigo_orgao = codigo_orgao
        self.competencia = competencia
        self.codigo_localidade = codigo_localidade
        self.sigla_tribunal = sigla_tribunal
        self.grau = grau

    def get_millis_insercao(self):
        return self.millis_insercao

    def get_assuntos(self):
        return self.assunto

    def get_dsc_sistema(self):
        return self.dsc_sistema

    def get_tamanho_processo(self):
        return self.tamanho_processo

    def get_numero(self):
        return self.numero

    def get_procel(self):
        return self.procel

    def get_data_ajuizamento(self):
        return self.data_ajuizamento

    def get_total_assuntos(self):
        return self.total_assuntos

    def get_classe_processual(self):
        return self.classe_processual

    def get_nivel_sigilo(self):
        return self.nivel_sigilo

    def get_codigo_orgao(self):
        return self.codigo_orgao

    def get_competencia(self):
        return self.competencia

    def get_codigo_localidade(self):
        return self.codigo_localidade

    def get_sigla_tribunal(self):
        return self.sigla_tribunal

    def get_grau(self):
        return self.grau
