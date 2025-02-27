from pathlib import Path

# Supondo que sua data de nascimento seja 140284 (14 de fevereiro de 1984)
birthday = "140284"

# Caminho para o arquivo com os dígitos de Pi
file_path = Path("Chapter 10/pi_million_digits.txt")

# Abrindo o arquivo e lendo todo o conteúdo
with file_path.open() as file:
    pi_digits = file.read()

# Verificando se a data de nascimento está nos dígitos de Pi
if birthday in pi_digits:
    print(
        f"Sua data de nascimento ({birthday}) está contida nos primeiros milhões de dígitos de Pi!"
    )
else:
    print(
        f"Sua data de nascimento ({birthday}) NÃO está contida nos primeiros milhões de dígitos de Pi."
    )
