import qrcode

# Dado URL ou texto
data = "https://docs.google.com/forms/d/e/1FAIpQLSdooNVhyb2GzSQFToI5Jk60p8bWiz6CmPvn8shjxlBV4aCDVA/viewform"

# Instanciar objeto QRCode
qr = qrcode.QRCode(
    version=1,  # controle o tamanho do QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controle a correção de erro
    box_size=10,  # controle a espessura de cada “caixa” ou “módulo” no QR
    border=4,  # controle quantas “caixas” a borda do QR Code deve ter
)

# Adicionar dados
qr.add_data(data)
qr.make(fit=True)

# Criar imagem do QR Code
img = qr.make_image(fill='black', back_color='white')

# Salvar a imagem
img.save("meu_qr_code.png")
