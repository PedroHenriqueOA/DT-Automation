import glob
import os
import pandas as pd
from pandas import DataFrame

# -----Adicionar metodo para deletar o arquivo depois de ler, para evitar que ele seja lido novamente no futuro, ou criar uma pasta para mover os arquivos lidos-----

list_of_files = glob.glob(
    "C:\\Users\\pedro\\Downloads\\*"
)  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

report = pd.read_excel(latest_file)
report_cpf = report.iloc[3:, 1]
escalamento = pd.read_csv(r"C:\Users\pedro\Downloads\Escalamento.csv")

print("--------------REPORT---------------------------")
print
print(report_cpf)

report_cpf = report_cpf.rename("cpf")
print("---------------REPORT AFTER RENAME--------------------------")
print(report_cpf)
# DataFrame.rename(report_cpf, columns={0: 'cpf'})
DataFrame.to_csv(
    report_cpf, r"C:\Users\pedro\Downloads\Escalamento.csv", index=False, mode="w"
)

# DataFrame.to_clipboard(report_cpf,header=False, index=False)

print("---------------ESCALAMENTO AFTER RENAME--------------------------")
escalamento = pd.read_csv(r"C:\Users\pedro\Downloads\Escalamento.csv")
print(escalamento.iloc[0:])
