from store import Product, Manager
from management import StoreChain


product = Product("Shampoo Shauma", "3.50")
store_chain = StoreChain("Dm Drogerie", "Germany")
manager = Manager("Geisa Lopes", "Dussmann")

product.describe_product()
store_chain.describe_chain()
manager.describe_manager()
