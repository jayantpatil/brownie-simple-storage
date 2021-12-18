from brownie import accounts, config, SimpleStorage


def read_contract():
    #  -1 index gets most recent transaction
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
