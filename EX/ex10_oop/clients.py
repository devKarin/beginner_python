"""
EX10 - Client.

This program gets information about bank clients.

Available classes:
Client; Client class

Functions in Client class:
__init__; Client constructor.
    -> Every client has: a name, the name of the bank they are a client of, the age of account in days,
    the starting amount of money and the current amount of money.
__repr__; Client representation. Returns client name.
earnings_per_day(self);

Available functions:
read_from_file_into_list(filename: str) -> list;
    -> Reads data from the file, creates client objects using the data and returns client list.
filter_by_bank(filename: str, bank: str) -> list;
    -> Finds the clients of the bank.
largest_earnings_per_day(filename: str) -> Optional[Client];
    -> Finds the client that has earned the most money per day.
largest_loss_per_day(filename: str) -> Optional[Client];
    -> Find the client who has lost the most money per day.

"""


from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or
        save it into a new attribute and return the value.
        """
        if self.account_age <= 0:
            return self.current_amount - self.starting_amount
        return (self.current_amount - self.starting_amount) / self.account_age


def read_from_file_into_list(filename: str) -> list:
    """
    Read data from the file, create client objects using the data, create and return client list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clients_data = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # Remove whitespace.
            client = line.strip()
            # Separate client data fields into list items.
            client = client.split(",")
            # Create new Client object for every client using the client data from list and converting
            # it into a proper data type.
            clients_data.append(Client(client[0], client[1], int(client[2]), int(client[3]), int(client[4])))
    return clients_data


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    # Use previous function to create list of clients.
    clients = read_from_file_into_list(filename)
    # Create list of clients of the bank by using built-in filter function.
    return list(filter(lambda client: client.bank == bank, clients))


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with the largest earnings.
    """
    # Create client list based on the data from file by using predefined function.
    clients = read_from_file_into_list(filename)
    # Sort the client list first by earnings per day descending and then by the time during the money has been earned.
    sorted_by_largest_earnings = sorted(clients, key=lambda client: (-client.earnings_per_day(), client.account_age))
    # Filter the clients who have earned money, not lost.
    # For that compare the amount of money when the account was opened and the amount of money the client has now.
    sorted_by_largest_earnings = \
        list(filter(lambda client: client.current_amount > client.starting_amount, sorted_by_largest_earnings))
    # Return the client who has earned the most money per day. If the list is empty (no-one has earned money),
    # return None.
    if not sorted_by_largest_earnings:
        return
    return max(sorted_by_largest_earnings, key=lambda client: client.earnings_per_day())


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with the largest loss.
    """
    # Create client list based on the data from file by using predefined function.
    clients = read_from_file_into_list(filename)
    # Sort the client list first by earnings per day ascending and then by the time during the money has been lost.
    # The client, who has earned the less comes before others.
    # The client, who has been client for the shortest time comes before others.
    sorted_by_largest_loss = sorted(clients, key=lambda client: (client.earnings_per_day(), client.account_age))
    # Filter the clients who have lost the money, not earned.
    # For that compare the amount of money when the account was opened and the amount of money the client has now.
    sorted_by_largest_loss = \
        list(filter(lambda client: client.current_amount < client.starting_amount, sorted_by_largest_loss))
    # Return the client who has lost the most money per day. If the list is empty (no-one has lost money),
    # return None.
    if not sorted_by_largest_loss:
        return
    return min(sorted_by_largest_loss, key=lambda client: client.earnings_per_day())


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]

    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]

    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh

    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
