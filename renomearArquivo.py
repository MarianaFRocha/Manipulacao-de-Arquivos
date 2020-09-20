import os

# exemplo alterado de  EX_10.5.py para 10_5.py
for nome in os.listdir('./Minicurso/Minicurso API'):
    # alterar conforme sua necessidade de geração de nomes e layout de arquivos    

    os.rename("./Minicurso/Minicurso API/"+nome, "./Minicurso/Minicurso API/"+nome+"_Minicurso_API.png")
    print("arquivo " + nome + " alterado para " +nome+"_Minicurso_API")