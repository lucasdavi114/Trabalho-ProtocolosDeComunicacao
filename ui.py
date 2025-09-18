import customtkinter as ctk
import Cabecalho_Bit_Oriented as bitO
import Cabecalho_Charactere_Oriented as CharO

cabecalho_montado = ''
cabecalho_desmontado = ''


ctk.set_appearance_mode("dark")

def lista_entrada(entrada_usuario):
    user_data = []
    for bit in entrada_usuario:
        if bit != '0' and bit != '1':
            user_data.clear()
            print("Valores Inválidos para o tipo orientado a bit!")
            break        
        user_data.append(int(bit))
    return user_data

window = ctk.CTk()
window.title('Cabecalhos')
window.geometry('600x600')

def montar_cabecalho():
    entrada_usuario = entrada.get()
    user_data = lista_entrada(entrada_usuario)
    cabecalho_bit = bitO.Cabecalho_Bit_Oriented(user_data)
    global cabecalho_montado
    cabecalho_montado = cabecalho_bit.monta_cabecalho()
    cabecalho.configure(text=f"Cabeçalho montado:\n{cabecalho_montado}")

def desmontar_cabecalho():
    entrada_usuario = entrada.get()
    user_data = lista_entrada(entrada_usuario)
    cabecalho_bit = bitO.Cabecalho_Bit_Oriented(user_data)
    global cabecalho_desmontado
    cabecalho_desmontado = cabecalho_bit.desmonta_cabecalho()
    cabecalho_desmontado_label.configure(text=f"Cabeçalho desmontado:\n{cabecalho_desmontado}")

label = ctk.CTkLabel(window, text='Entrada')
label.pack(pady=10)

entrada = ctk.CTkEntry(window, placeholder_text='Valor')
entrada.pack(pady=10)


botao_montar = ctk.CTkButton(window, text='Montar Cabeçalho',command=montar_cabecalho)
botao_montar.pack(pady=10)

cabecalho = ctk.CTkLabel(window, text=f"Cabeçalho montado:\n{cabecalho_montado}")
cabecalho.pack(pady=10)

botao_desmontar = ctk.CTkButton(window, text=f"Desmontar Cabeçalho", command=desmontar_cabecalho)
botao_desmontar.pack(pady=10)

cabecalho_desmontado_label = ctk.CTkLabel(window, text=f"Cabeçalho desmontado:\n{cabecalho_desmontado}")
cabecalho_desmontado_label.pack(pady=10)

window.mainloop()
