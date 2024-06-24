## Importação da biblioteca CustomCTkinter, Random, String e Pyperclip
import customtkinter as ctk
import random
import string
import pyperclip

## Criação e configuração da janela 
app = ctk.CTk()
app.geometry("600x400")
app.title("Senhas")
app.maxsize(width=1100, height=400)
app.minsize(width=600, height=400)
app.iconbitmap("./img/icon.ico")

## Configuração da coluna para expandir horizontalmente (Titulo e botao gerar senha)
app.columnconfigure(0, weight=1)

## Título na janela
titulo_app = ctk.CTkLabel(app, text="Gerador de senhas aleatórias", font=("arial bold", 20))
titulo_app.grid(row=0, column=0, pady=(30,15), columnspan=2)

## Função de gerar senha
def gerar_senha():
    # Armazena o número inteito do slider em uma variável
    comprimento = int(slider_comp.get())
    
    # Condicional que verifica quais checkboxes foram selecionadas
    caracteres = "" # Variável vazia
    if min_var.get():  # Verifica se a checkbox está marcada (min_var = ctk.BooleanVar)
        caracteres += string.ascii_lowercase # Conjunto de caracteres da biblioteca string
    if maiusc_var.get():  
        caracteres += string.ascii_uppercase
    if num_var.get():  
        caracteres += string.digits
    if esp_var.get():  
        caracteres += string.punctuation
    
    # Verifica se alguma checkbox foi selecionada
    if caracteres == "":
        txt_senha.configure(text="Selecione pelo menos um tipo de caracteres.")
    else:
        # Utiliza a função random.choice da biblioteca random para randomizar um caractere da variavel caracteres
        senha = ''.join(random.choice(caracteres) for i in range(comprimento))
        
        # Atualiza o texto da label de senha com a senha gerada
        txt_senha.configure(text=f"Senha gerada e copiada para a área de transferências: {senha}")

        # Copia a senha para a área de transferência com função da biblioteca Pyperclip
        pyperclip.copy(senha)

## Frame1 e slider
def slider_event(value):
    txt_slider.configure(text=f"Quantidade de caracteres: {int(value)}")

frame1 = ctk.CTkFrame(app)
frame1.grid(row=1, column=0, sticky="ew", pady=10, padx=10)

slider_comp = ctk.CTkSlider(frame1, from_=6, to=100, command=slider_event)
slider_comp.grid(row=2, column=0, sticky="w", padx=15, pady=10)
slider_comp.set(12)

txt_slider = ctk.CTkLabel(frame1, text=f"Quantidade de caracteres: {slider_comp.get()}")
txt_slider.grid(row=1, column=0, sticky="w", padx=15, pady=7.5)

## Frame2 e checkboxes
frame2 = ctk.CTkFrame(app)
frame2.grid(row=3, column=0, sticky="ew", pady=10, padx=10)

min_var = ctk.BooleanVar()  
checkbox_min = ctk.CTkCheckBox(frame2, text="abc - Letras minúsculas", variable=min_var, onvalue=True, offvalue=False)
checkbox_min.grid(row=4, column=0, sticky="w", pady=10, padx=20)

maiusc_var = ctk.BooleanVar()  
checkbox_maiusc = ctk.CTkCheckBox(frame2, text="ABC - Letras maiúsculas", variable=maiusc_var, onvalue=True, offvalue=False)
checkbox_maiusc.grid(row=4, column=1, pady=10, sticky="w", padx=80)

num_var = ctk.BooleanVar()  
checkbox_num = ctk.CTkCheckBox(frame2, text="123 - Números", variable=num_var, onvalue=True, offvalue=False)
checkbox_num.grid(row=5, column=0, sticky="w", pady=10, padx=20)

esp_var = ctk.BooleanVar()  
checkbox_esp = ctk.CTkCheckBox(frame2, text="@#$ - Caracteres especiais", variable=esp_var, onvalue=True, offvalue=False)
checkbox_esp.grid(row=5, column=1, pady=10, sticky="w", padx=80)

## Label para exibir a senha
txt_senha = ctk.CTkLabel(app, text="")
txt_senha.grid(row=6, column=0, pady=5, columnspan=2)

## Botão para gerar e copiar senha
btn_senha = ctk.CTkButton(app, text="Gerar senha", command=gerar_senha)
btn_senha.grid(row=7, column=0, pady=15, columnspan=2)

## Fazendo a janela rodar
app.mainloop()
