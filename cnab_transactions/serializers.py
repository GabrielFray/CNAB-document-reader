from rest_framework import serializers
from .models import CnabTransactions


class CnabTransactionsSerializer(serializers.ModelSerializer):
    transactions = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = CnabTransactions
        fields = [
            "id",
            "store",
            "currency",
            "transactions",
        ]

    def get_transactions(self, store):
        return transactions_store(store)

    def get_currency(self, store):
        return calculate_store(store)


def get_store(store_name) -> list:
    store = list(store_name.values())[0]
    return CnabTransactions.objects.filter(store=store)


def filter_store(stores) -> list:
    store_names = {store.store for store in stores}
    store_unique = [{"store": store_name} for store_name in store_names]

    return store_unique


def transactions_store(store_name) -> list:
    stores = get_store(store_name)
    transactions_type = {
        "1": "Débito",
        "2": "Boleto",
        "3": "Financiamento",
        "4": "Crédito",
        "5": "Recebimento Empréstimo",
        "6": "Vendas",
        "7": "TED",
        "8": "DOC",
        "9": "Aluguel",
    }
    negative_types = ["2", "3", "9"]

    transactions = [
        {
            "type": transactions_type[transaction.type],
            "value": round(
                (-1 if transaction.type in negative_types else 1) * transaction.value, 2
            ),
        }
        for transaction in stores
    ]

    return transactions


def calculate_store(store_name) -> float:
    stores = get_store(store_name)
    negative = ["2", "3", "9"]

    return sum(
        [
            -round(transaction.value, 2)
            if transaction.type in negative
            else round(transaction.value, 2)
            for transaction in stores
        ]
    )
