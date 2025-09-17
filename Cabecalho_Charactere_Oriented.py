# Orientada a Caractere
class Cabecalho_Charactere_Oriented:

    # Constantes
    FLAG_INICIO = "STX"
    FLAG_FINAL = "ETX"
    FLAG_INTERNA = "DLE"
    SPACE = ' '
    COMMA = ','

    #Atributos
    user_data = []
    transcricao = ''
    indices_Flags = []

    def __init__(self, user_data):
        self.user_data = user_data
        
        self.character_stuffing(self.user_data)

    def montar_cabecalho(self):
        self.transcricao = self.FLAG_INICIO
        self.transcricao += self.SPACE
        self.transcricao += self.user_data
        self.transcricao += self.SPACE
        self.transcricao += self.FLAG_FINAL
        

    def desmontar_cabecalho(self):
        pass
    
    # TODO Fazer o Character_Stuffing
    def character_stuffing(self, user_data):
        string = self.converte_lista_em_string(user_data)
        if self.FLAG_INTERNA in string:
            print(string.split(self.SPACE))
        elif self.FLAG_FINAL in string:
            print(string.split(self.FLAG_FINAL))
        elif self.FLAG_INICIO in string:
            print(string.split(self.FLAG_INICIO))
        else:
            print("Não possui uma flag!\n")

    def to_string(self):
        return self.transcricao

    def converte_lista_em_string(self, lista):
        string = ''
        for valor in lista:
            string += str(valor)

        return string

if __name__ == "__main__":
    
    user_data = input("Entrada de Dados: ").upper()
    cabecalho = Cabecalho_Charactere_Oriented(user_data)

    cabecalho.montar_cabecalho()
    print(f"Transcrição: {cabecalho.to_string()}")
