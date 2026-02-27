import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        nome = entrada_nome.get()
        atividade = float(entrada_atividade.get())
        trabalho = float(entrada_trabalho.get())
        pb = float(entrada_pb.get())

        soma = atividade + trabalho + pb

        resultado_label.config(
            text=f"Nota final de {nome}: {soma:.2f}",
            foreground="blue"
        )

        # Limpar campos após o cálculo
        entrada_nome.delete(0, tk.END)
        entrada_atividade.delete(0, tk.END)
        entrada_trabalho.delete(0, tk.END)
        entrada_pb.delete(0, tk.END)

        # Retornar o foco para o primeiro campo
        entrada_nome.focus()

    except ValueError:
        resultado_label.config(
            text="Erro: Digite apenas números válidos nas notas.",
            foreground="red"
        )

# Janela principal
janela = tk.Tk()
janela.title("Calculadora de Notas - Versão Piloto")
janela.geometry("600x420")
janela.resizable(width=False, height=False)

# Frame central
frame = ttk.Frame(janela, padding=20)
frame.pack(fill="both", expand=True)

# Estilos
fonte_label = ("Arial", 14)
fonte_entry = ("Arial", 14)
fonte_botao = ("Arial", 16, "bold")
fonte_titulo = ("Arial", 20, "bold")

# Título
titulo = ttk.Label(frame, text="Calculadora de Média Bimestral", font=fonte_titulo)
titulo.grid(row=0, column=0, columnspan=2, pady=15)

# Campo nome
ttk.Label(frame, text="Nome do aluno:", font=fonte_label).grid(row=1, column=0, sticky="w", pady=8)
entrada_nome = ttk.Entry(frame, width=35, font=fonte_entry)
entrada_nome.grid(row=1, column=1, pady=8)

# Campo atividades
ttk.Label(frame, text="Nota das atividades:", font=fonte_label).grid(row=2, column=0, sticky="w", pady=8)
entrada_atividade = ttk.Entry(frame, width=10, font=fonte_entry)
entrada_atividade.grid(row=2, column=1, pady=8)

# Campo trabalho
ttk.Label(frame, text="Nota do trabalho:", font=fonte_label).grid(row=3, column=0, sticky="w", pady=8)
entrada_trabalho = ttk.Entry(frame, width=10, font=fonte_entry)
entrada_trabalho.grid(row=3, column=1, pady=8)

# Campo prova bimestral
ttk.Label(frame, text="Nota da prova bimestral:", font=fonte_label).grid(row=4, column=0, sticky="w", pady=8)
entrada_pb = ttk.Entry(frame, width=10, font=fonte_entry)
entrada_pb.grid(row=4, column=1, pady=8)

# Bindings para avanço automático com Enter
entrada_nome.bind("<Return>", lambda e: entrada_atividade.focus())
entrada_atividade.bind("<Return>", lambda e: entrada_trabalho.focus())
entrada_trabalho.bind("<Return>", lambda e: entrada_pb.focus())
entrada_pb.bind("<Return>", lambda e: calcular())  # Enter no último campo já calcula

# Botão calcular
style = ttk.Style()
style.configure("TButton", font=fonte_botao, padding=10)

botao = ttk.Button(frame, text="Calcular Nota", command=calcular)
botao.grid(row=5, column=0, columnspan=2, pady=20)

# Resultado
resultado_label = ttk.Label(frame, text="", font=("Arial", 16))
resultado_label.grid(row=6, column=0, columnspan=2, pady=15)

# Foco inicial
entrada_nome.focus()

janela.mainloop()
