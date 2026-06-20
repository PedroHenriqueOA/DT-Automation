import glob
import os
import pandas as pd
from pandas import DataFrame


def copyCpf(download_directory, escalamento_path):

    list_of_files = glob.glob(
        download_directory
    )  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    report = pd.read_excel(latest_file)
    report_cpf = report.iloc[3:, 1]
    # escalamento_path = os.path.join(download_directory, "\Escalamento.csv")

    print("--------------REPORT---------------------------")
    print(report_cpf)

    report_cpf = report_cpf.rename("cpf")
    print("---------------REPORT AFTER RENAME--------------------------")
    print(report_cpf)
    # DataFrame.rename(report_cpf, columns={0: 'cpf'})
    DataFrame.to_csv(report_cpf, escalamento_path, index=False, mode="w")

    # DataFrame.to_clipboard(report_cpf,header=False, index=False)

    print("---------------ESCALAMENTO AFTER RENAME--------------------------")
    escalamento = pd.read_csv(escalamento_path)
    print(escalamento.iloc[0:])
    os.remove(latest_file)  # Deleta arquivo no final
