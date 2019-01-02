class ProductInStore(object):
    price = 9.99
    name = 'new product'
    qty_in_stock = 0

    def __init__(self, name = 'new product', price = 9.99):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_stock(self, qty):
        self.qty_in_stock = qty
        return self

    def report(self):
        return "%s of '%s' are left" % (self.qty_in_stock, self.name)

abn911 = ProductInStore()
abn911.set_name('Lego Mindstorm v1') \
    .set_price(199.99) \
    .set_stock(5)
print (abn911.name, abn911.price, abn911.qty_in_stock)

class SimpleProductInStore(ProductInStore):
    
    def get_price(self, option = None):
        return super(SimpleProductInStore, self).get_price()

    def report(self):
        return "-----\nsimple product report\n-----\n%s of '%s' are left \ncurrent price is %s" % (self.qty_in_stock, self.name, self.price)

class ConfigurableProductInStore(ProductInStore):
    option_prices = None

    def __init__(self, name, basic_price, add_prices):
        self.name = name
        self.price = basic_price
        self.option_prices = add_prices

    def get_price(self, option = None):
        price = super(ConfigurableProductInStore, self).get_price()
        if option != None and option in self.option_prices:
            price += self.option_prices[option]
        return price

    def report(self):
        report = "-----\nconfigurable product report\n-----\n%s of '%s' are left \ncurrent price is %s" % (self.qty_in_stock, self.name, self.price)
        if len(self.option_prices):
            report += "\nproduct options:"
            for i in self.option_prices:
                report += "\n- %s : %s" % (i, self.option_prices[i])
        return report

abn913 = ConfigurableProductInStore('Lego Mindstorm v1', 199.99, {'v1': 0, 'v1.1': 0, 'v2': 21.0, 'v3': 50.5})
print (abn913.name, abn913.price, abn913.qty_in_stock, \
    abn913.option_prices)
abn914 = SimpleProductInStore('Anakin action figure 921', 56.11)
print (abn914.name, abn914.price, abn914.qty_in_stock)

abn915 = ConfigurableProductInStore('Lego Mindstorm v1', 199.99, {'v1': 0, 'v1.1': 0, 'v2': 21.0, 'v3': 50.5})
print (abn915.report())
print ('price for v3 is %s' % (abn915.get_price('v3')))
abn917 = SimpleProductInStore('Anakin action figure 921', 56.11)
print (abn917.report())
print ('price is %s' % (abn917.get_price()))


x = None
while not x:
    try:
        x = int(input('input number:'))
    except (TypeError, ValueError) as e:
        print ('error { %s } happened. try once more') % (e.message)
print ('finally!')