# Orientada a Caractere
class Cabecalho_Charactere_Oriented:

    # Constantes
    FLAG_INICIO = "STX"
    FLAG_FINAL = "ETX"
    FLAG_INTERNA = "DLE"
    SPACE = " "

    #Atributos
    user_data = []
    transcricao = []
    indices_Flags = []

    def __init__(self):
        pass

    def montar_cabecalho(self):
        pass

    def desmontar_cabecalho(self):
        pass


if __name__ == "__main__":
    
    user_data = input("Entrada de Dados: ")

    print(f"Entradas: {user_data}")

