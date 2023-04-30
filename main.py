import traceback


class Entry:
    name: str
    price: float

    def __init__(self, name: str, price: str):
        self.name = name
        self.price = float(price[4:].replace(",", "."))

    def apply_discount(self, discount: str):
        self.price -= float(discount[:-2].replace(",", "."))


def file_path_to_array(path: str) -> [str]:
    with open(path) as file:
        return file.read().split("\n")


def parse_data(products_path: str, prices_path: str) -> [Entry]:
    raw_products: [str] = file_path_to_array(products_path)
    raw_prices: [str] = file_path_to_array(prices_path)

    assert len(raw_products) == len(raw_prices)

    entries: [Entry] = []
    for i in range(len(raw_products)):
        raw_product: str = raw_products[i]
        raw_price: str = raw_prices[i]
        if raw_product.startswith("  SCONTO"):
            assert raw_price.endswith("-S")
            entries[len(entries) - 1].apply_discount(raw_price)
        else:
            entries.append(Entry(raw_product, raw_price))
    return entries


def output_data(entries: [Entry], path: str):
    with open(path, "w+") as file:
        for entry in entries:
            file.write(entry.name + "\t" + str(entry.price) + "\n")


if __name__ == '__main__':
    try:
        cleaned_entries: [Entry] = parse_data("data/products_in.txt", "data/prices_in.txt")
        output_data(cleaned_entries, "data/out.txt")
    except BaseException as e:
        print("ERROR")
        traceback.print_exc()
