from fpdf import FPDF
from num2words import num2words
from datetime import date
import os

# Coleta de dados
cliente = input("Informe o nome do cliente: ").strip()
consulta = input("Informe o tipo da consulta: ").strip()
vlr = float(input("Informe o valor da consulta (apenas números): ").replace(',', '.'))

# Formatando valores
vlr_formatado = f"R$ {vlr:,.2f}".replace('.', ',')
vlr_extenso = num2words(vlr, lang='pt-br')
vlr_extenso_msg = f"{vlr_extenso} reais"

# Data
hoje = date.today()
dia, mes, ano = hoje.day, hoje.month, hoje.year

# Iniciando PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 16)
pdf.set_text_color(0, 0, 0)
pdf.image("dados/rec.jpg", x=0, y=0)

# Campos preenchidos
pdf.set_xy(162, 45)  # Valor no canto superior
pdf.cell(0, 10, vlr_formatado)

pdf.set_xy(70, 86)  # Cliente
pdf.cell(0, 10, cliente)

pdf.set_xy(70, 108)  # Valor por extenso
pdf.cell(0, 10, vlr_extenso_msg)

pdf.set_xy(70, 135)  # Consulta
pdf.cell(0, 10, consulta)

# Data com texto branco
pdf.set_text_color(255, 255, 255)
pdf.set_xy(30, 193)
pdf.cell(10, 10, str(dia))

pdf.set_xy(50, 193)
pdf.cell(10, 10, str(mes))

pdf.set_xy(70, 193)
pdf.cell(10, 10, str(ano))

# Nome do arquivo sem espaços e caracteres problemáticos
nome_arquivo = f"{cliente}_{dia}_{mes}_{ano}".replace(" ", "_").replace("/", "-")
os.makedirs("recibos", exist_ok=True)
pdf.output(f"recibos/{nome_arquivo}.pdf")

print(f"Recibo gerado com sucesso: recibos/{nome_arquivo}.pdf")
