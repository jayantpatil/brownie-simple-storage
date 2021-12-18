from brownie import accounts, config


def deploy_simple_storage():
    # account = accounts.add(config["wallets"]["from_key"])
    account = accounts[0]
    print(account)


def main():
    deploy_simple_storage()
