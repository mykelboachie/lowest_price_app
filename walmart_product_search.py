## Walmart product search and price return
## Searches for a product in walmart catalog
## Compares all matching keywords and returns the lowest item

import walmart as wal_api
from operator import itemgetter

search_instance = wal_api.start_API()

product_info = {}


def product_search(key_item):
    product_search_return = search_instance.search(key_item)

    for product in product_search_return:
        product_info[product.name] = product.sale_price

    return list(min(product_info.items(), key=itemgetter(1)))





