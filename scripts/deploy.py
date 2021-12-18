from brownie import accounts, config, network, SimpleStorage


def deploy_simple_storage():
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(100, {"from": account})
    transaction.wait(1)
    print(simple_storage.retrieve())


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
