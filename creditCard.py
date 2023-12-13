
class CreditCard:

    def __init__(self, limit):
        self.av_limit = limit
        self.balance = 0
        self.pending_transactions = {}
        self.pending_payments = {}

    def __repr__(self):
        return f'Credit Card - ${self.av_limit} credit limit'

    ### TRANSACTIONS ###
    def authorize(self, id, amt):
        if amt <= self.av_limit:
            self.av_limit -= amt
            self.pending_transactions[(id,'payment')] = amt

    def settle(self, id, extra=0):
        if id in self.pending_transactions:
            self.av_limit -= extra
            self.balance += self.pending_transactions[id] + extra
            del self.pending_transactions[id]

    def clearTransaction(self, id):
        if id in self.pending_transactions:
            self.av_limit += self.pending_transactions[id]
            del self.pending_transactions[id]

    ### PAYMENTS ###

    def initiate_payment(self, id, amt):
        self.balance -= amt
        self.pending_payments[id] = amt

    def post_payment(self,id):
        if id in self.pending_payments:
            self.limit += self.pending_payments[id]
            del self.pending_payments[id]

    def clearPayment(self, id):
        if id in self.pending_payments:
            self.bal += self.pending_payments[id]
            del self.pending_payments[id]






c = CreditCard(1000)

print(c.av_limit)
print(c.balance)

c.authorize(1,200)
print(c.av_limit)
print(c.balance)

c.settle(1,5)
print(c.av_limit)
print(c.balance)

c.authorize(2,-100)
print(c.av_limit)
print(c.balance)

c.settle(2)
print(c.av_limit)
print(c.balance)
