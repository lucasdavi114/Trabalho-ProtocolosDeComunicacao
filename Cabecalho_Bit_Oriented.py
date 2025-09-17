# Orientada a Bit
# 01110111110101111111110100010
class Cabecalho_Bit_Oriented:

    # Constantes
    SPACE = " "
    FRAMING_FLAG = [0, 1, 1, 1, 1, 1, 1, 0]

    # Atributos
    user_data = []
    transmissao = []
    indices_flags = []
    
    # Construtor da classe inicia a entrada do usuário
    def __init__(self, user_data):
        self.user_data = user_data

    # Adiciona se necessário um bit flag 0 ao final de uma sequência de 5 1s, retorna um vetor com o bitStuffing realizado se for necessário
    def bit_stuffing(self):
        cont = 0
        bits = []
        tamanho = len(self.user_data)
        if tamanho < 5:
            return self.user_data
        for i in range(tamanho):
            bits.append(self.user_data[i])
            if self.user_data[i] == 1:
                cont += 1
            else:
                cont = 0
            if cont == 5:
                bits.append(0)
                cont = 0
                self.indices_flags.append(len(bits)-1)
        return bits
    
    # Monta o cabecalho com bitStuffing e as flags no inicio e final
    def monta_cabecalho(self):
        self.transmissao.extend(self.FRAMING_FLAG)
        self.transmissao.append(self.SPACE)
        self.user_data = self.bit_stuffing()
        self.transmissao.extend(self.user_data)
        self.transmissao.append(self.SPACE)
        self.transmissao.extend(self.FRAMING_FLAG)
    
    # Remove os bit_flags e o bitStuffing da mensagem do usuário
    def desmonta_cabecalho(self):
        num_flags = len(self.indices_flags)
        num_removidos = 0

        self.transmissao.clear()
        if num_flags:
            for indices in self.indices_flags:
                if num_removidos > 0:
                    indices -= num_removidos
                del self.user_data[indices]
                num_removidos += 1
        self.transmissao.extend(self.user_data)
        self.indices_flags.clear()

    # Uma saída padrão no terminal mostrando todos os atributos da classe Cabecalho_Bit_Oriented
    def to_string(self):
        print(f"Transcrição: {self.converte_lista_em_string(self.transmissao)}")
        print(f"User Data: {self.converte_lista_em_string(self.user_data)}")
        print(f"Framing_flag: {self.converte_lista_em_string(self.FRAMING_FLAG)}")
        print(f"Indices Flags{self.indices_flags}")

    # Retorna uma string com os valores de uma lista (os valores saem juntos e sem espaços) ex: lista = [0, 1, 2] saida: 012
    def converte_lista_em_string(self, lista):
        string = ''
        for valor in lista:
            string += str(valor)
        
        return string

if __name__ == "__main__":
    mensagem = input("Mensagem em bits: ")

    user_data = []
    for bit in mensagem:
        if bit != '0' and bit != '1':
            user_data.clear()
            print("Valores Inválidos para o tipo orientado a bit!")
            break
            
        user_data.append(int(bit))

    if user_data:
        # Cria um objeto da classe Cabecalho_Bit_Oriented
        cabecalho = Cabecalho_Bit_Oriented(user_data)

        print("Cabeçalho Montado")
        cabecalho.monta_cabecalho()
        cabecalho.to_string()
        print("Cabeçalho Desmontado")
        cabecalho.desmonta_cabecalho()
        cabecalho.to_string()
