"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, firstname, lastname, email, password):
        self.email = email
        self.password = password


def read_customer_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {email: Customer object}
    """
    customers_data = {}

    for line in open(filepath):
        (firstname, lastname, email, password) = line.strip().split("|")
        customers_data[email] = Customer(firstname, lastname, email, password)

    return customers_data

def get_by_email(email):
    """Returns email."""

    return customer_file.get(email)


customer_file = read_customer_from_file("customers.txt")
