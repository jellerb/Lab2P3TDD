import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

# added test to multiply total "cart" by a number of orders a user would like to submit
def test_CanCalculateOrderNumberPrice(invoice, products):
    invoice.orderNumberPrice(products, 3)
    assert invoice.orderNumberPrice(products, 3) == 208.14

# separated totalDiscount by assignment and calculation, test to make sure assignment and calculation functions are the same
def test_CanCalculateTotalDiscountCalc(invoice, products):
    invoice.totalDiscount(products)
    invoice.totalDiscountCalc(products)
    assert invoice.totalDiscountCalc(products) == 5.62




