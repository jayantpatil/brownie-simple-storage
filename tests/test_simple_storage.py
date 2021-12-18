from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected


def testupdating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    store_value = 100
    transaction = simple_storage.store(store_value, {"from": account})
    updated_value = simple_storage.retrieve()

    # Assert
    assert updated_value == store_value
