from cnab_transactions.models import CnabTransactions


def normalize_file_txt(file) -> dict:
    read_file = file.read().decode("utf-8")
    format_file = read_file.split("\r\n")

    for line in format_file:
        if len(line) < 62:
            continue
        cnab_data = {
            "type": line[0],
            "date": f"{line[1:5]}-{line[5:7]}-{line[7:9]}",
            "value": round(int(line[9:19]) / 100, 2),
            "cpf": line[19:30],
            "card": line[30:42],
            "hour": f"{line[1:5]}-{line[5:7]}-{line[7:9]} {line[42:44]}:{line[44:46]}:{line[46:48]}",
            "owner": line[48:62].strip(),
            "store": line[62:].strip(),
        }

        CnabTransactions.objects.create(**cnab_data)
