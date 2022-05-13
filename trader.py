import json
from random import uniform
from argparse import ArgumentParser


class BigTrader:
    def __init__(self, filename_config, filename_wallet):
        self.filename_config = filename_config
        self.filename_wallet = filename_wallet
        self.wallet_info = self.read_json_file()
        self.uah_amount = self.wallet_info['uah']
        self.usd_amount = self.wallet_info['usd']
        self.usd_course = self.wallet_info['course']

    def read_json_file(self) -> dict:
        if self.filename_wallet:
            with open(self.filename_wallet, 'r') as file:
                start_dict = json.load(file)
        else:
            with open(self.filename_config, 'r') as file:
                start_dict = json.load(file)
        return start_dict

    def rules(self):
        print('''    RATE - получение текущего курса.
    AVAILABLE - получение остатков по счетам.
    BUY - покупка n долларов.
    SELL - продажа n долларов.
    BUY ALL - покупка всех долларов.
    SELL ALL - продажа всех долларов.
    NEXT - получить следующий курс.
    RESTART - начать игру с начала.''')

    def rate(self):
        print(f"{self.usd_course} uah")

    def available(self):
        print(f"usd: {self.usd_amount} uah: {self.uah_amount} ")

    def buy(self, available = 0) -> dict:
        need_uah = available * self.usd_course
        if need_uah > self.uah_amount:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {self.uah_amount}, AVAILABLE {need_uah}")
        else:
            actual_uah = self.uah_amount - need_uah
            actual_usd = available
            self.wallet_info['uah'] = round(actual_uah, 2)
            self.wallet_info['usd'] += round(actual_usd, 2)
        return self.wallet_info

    def sell(self, available: int) -> dict:
        if available > self.usd_amount:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {self.usd_amount}, AVAILABLE {available}")
        else:
            actual_usd: int = self.usd_amount - available
            actual_uah: int = available * self.usd_course
            self.wallet_info['uah'] += round(actual_uah, 2)
            self.wallet_info['usd'] = round(actual_usd, 2)
        return self.wallet_info

    def buy_all(self) -> dict:
        if self.uah_amount == 0:
            print(f"YOUR CURRENT BALANCE UAH {self.uah_amount}")
        else:
            actual_uah: int = 0
            actual_usd: int = self.uah_amount / self.usd_course
            self.wallet_info['uah'] = round(actual_uah, 2)
            self.wallet_info['usd'] += round(actual_usd, 2)
        return self.wallet_info

    def sell_all(self) -> dict:
        if self.usd_amount == 0:
            print(f"YOUR CURRENT BALANCE USD {self.usd_amount}")
        else:
            actual_uah = self.usd_amount * self.usd_course
            actual_usd = 0
            self.wallet_info['uah'] += round(actual_uah, 2)
            self.wallet_info['usd'] = round(actual_usd, 2)
        return self.wallet_info

    def next(self) -> dict:
        actual_course: int = self.usd_course
        delta: int = self.wallet_info["delta"]
        max_range_course: int = actual_course + delta
        min_range_course: int = actual_course - delta
        new_course = uniform(max_range_course, min_range_course)
        self.wallet_info['course'] = round(new_course, 2)
        return self.wallet_info

    def restart(self):
        with open(self.filename_config, 'r') as file:
            star_dict = json.load(file)
        with open(self.filename_wallet, 'w') as file:
            json.dump(star_dict, file, indent=2)


def write_json_file(data):
    with open("wallet.json", 'w') as file:
        json.dump(data, file, indent=2)


args = ArgumentParser()
args.add_argument("INPUT")
args.add_argument("MULT", type=str, nargs='?', default=0)
args = vars(args.parse_args())
amount = args["MULT"]
class_BigTrader = BigTrader("config.json", "wallet.json")
if args["INPUT"] == "HELP":
    class_BigTrader.rules()
elif args["INPUT"] == "RATE":
    class_BigTrader.rate()
elif args["INPUT"] == "AVAILABLE":
    class_BigTrader.available()
elif args["INPUT"] == "BUY" and args["MULT"] != "ALL":
    write_json_file(class_BigTrader.buy(int(amount)))
elif args["INPUT"] == "SELL" and args["MULT"] != "ALL":
    write_json_file(class_BigTrader.sell(int(amount)))
elif args["INPUT"] == "BUY" and args["MULT"] == "ALL":
    write_json_file(class_BigTrader.buy_all())
elif args["INPUT"] == "SELL" and args["MULT"] == "ALL":
    write_json_file(class_BigTrader.sell_all())
elif args["INPUT"] == "NEXT":
    write_json_file(class_BigTrader.next())
elif args["INPUT"] == "RESTART":
    class_BigTrader.restart()