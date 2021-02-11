from typing import List, Optional


class Mutation:
    """
    Pls Add a description
    """
    def __init__(self):
        self.name = None

    def Mutate(self, fields: List[tuple], subfields: List):
        mod_fields = [f"{i[0]}: {str(i[1])}" for i in fields]
        print(mod_fields)
        _args = tuple(i.strip("\'") for i in mod_fields)
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}{_args} {{
                {newline.join(i for i in subfields)}
            }}
        }}
        """
        return result.replace("\'", "")


class CreateDepositAccount(Mutation):
    def __init__(self):
        """
        Create deposit account
        """
        self.name = "createDepositAccount"


# Buy from BuyCoins
class Buy(Mutation):
    def __init__(self):
        """
        Buy crypto
        """
        super().__init__()
        self.name = "buy"

    def Mutate(self, price: str, coin_amount: float, cryptocurrency, subfields: Optional[List]=None):
        if subfields:
            newline = "\n                "
            result = f"""
            mutation {{
                {self.name}(price: \"{f"{price}"}\", coin_amount: {coin_amount}, cryptocurrency: {cryptocurrency})
                {{
                    {newline.join(i for i in subfields)}
                }}
            }}
            """
            return result
        else:
            newline = "\n                "
            result = f"""
            mutation {{
                {self.name}(price: \"{f"{price}"}\", coin_amount: {coin_amount}, cryptocurrency: {cryptocurrency})
                {{
                    id
                    price {{
                        id
                        status
                        cryptocurrency
                        minBuy
                        minSell
                        maxBuy
                        maxSell
                        minCoinAmount
                        expiresAt
                        buyPricePerCoin
                        sellPricePerCoin
                    }}
                    cryptocurrency
                    filledCoinAmount
                    side
                    status
                    totalCoinAmount
                    createdAt
                }}
            }}
            """
            return result
            


class PostLimitOrder(Mutation):
    def __init__(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency, price_type: str, price_type_value: Optional[List[tuple]]=None):
        super.__init__()
        self.name = "postLimitOrder"
        self.order_side = order_side
        self.coin_amount = coin_amount
        self.cryptocurrency = cryptocurrency
        self.price_type = price_type
        
        def Mutate(self):
            newline = "\n                "
            if price_type_value:
                result = f"""
                mutation {{
                    {self.name}(orderSide: {self.order_side}, coinAmount: {self.coin_amount}, cryptocurrency: {self.cryptocurrency}, priceType: {self.price_type}, price_type_value[0][0]: {price_type_value[0][1]})
                    {{
                        {newline.join(i for i in self.subfields)}
                    }}
                }}
                """
            else:
                result = f"""
                mutation {{
                    {self.name}(orderSide: {self.order_side}, coinAmount: {self.coin_amount}, cryptocurrency: {self.cryptocurrency}, priceType: {self.price_type})
                    {{
                        {newline.join(i for i in self.subfields)}
                    }}
                }}
                """
            return result

    
class PostMarketOrder(Mutation):
    def __init_(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency: str):
        self.name = "postMarketOrder"
        self.order_side = order_side
        self.coin_amount = coin_amount
        self.cryptocurrency = cryptocurrency
        self.subfields = subfields

    def Mutate(self):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(orderSide: {self.order_side}, coinAmount: {self.coin_amount}, cryptocurrency: {self.cryptocurrency})
            {{
                {newline.join(i for i in self.subfields)}
            }}
        }}
        """
        return result


class Sell(Mutation):
    def __init__(self, subfields: List, price: str, coin_amount: float, cryptocurrency):
        """
        Sell crypto
        """
        super().__init__()
        self.name = "sell"
        self.price = price
        self.coin_amount = coin_amount
        self.cryptocurrency = cryptocurrency
        self.subfields = subfields

    def Mutate(self):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(price: \"{f"{self.price}"}\", coin_amount: {self.coin_amount}, cryptocurrency: {self.cryptocurrency})
            {{
                {newline.join(i for i in self.subfields)}
            }}
        }}
        """
        return result


class SendCoin(Mutation):
    def __init__(self, cryptocurrency, address, amount, subfields: List):
        super().__init__()
        self.cryptocurrency = cryptocurrency
        self.amount = amount
        self.address = address
        self.subfields = subfields
        self.name = "send"

    def Mutate(self):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(address: \"{f"{self.address}"}\", amount: {self.amount}, cryptocurrency: {self.cryptocurrency})
            {{
                {newline.join(i for i in self.subfields)}
            }}
        }}
        """
        return result


class CreateAddress(Mutation):
    def __init__(self, cryptocurrency, subfields: List):
        super().__init__()
        self.name = "createAddress"
        self.cryptocurrency = cryptocurrency
        self.subfields = subfields

    def Mutate(self):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(cryptocurrency: {self.cryptocurrency})
            {{
                {newline.join(i for i in self.subfields)}
            }}
        }}
        """
        return result


# create_account = createDepositAccount()
# print(create_account.Mutate(
#             fields=[('accountName', "tony stark")],
#             subfields=["accountNumber", "accountName", "accountType", "bankName"]
#         ))

"""
buy = Buy().Mutate(
    "gibebersihhd",0.02,'bitcoin'
)
print(buy)"""