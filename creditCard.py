class CreditCard:

    def __init__(self, limit):
        # Initializing the credit card with the specified limit, balance, and pending transactions/payments.
        self.av_limit = limit  # Available credit limit
        self.balance = 0  # Current balance
        self.pending_transactions = {}  # Dictionary to store pending transaction IDs and amounts
        self.pending_payments = {}  # Dictionary to store pending payment IDs and amounts

    def __repr__(self):
        # Representation of the Credit Card object
        return f'Credit Card - ${self.av_limit} credit limit'

    ### TRANSACTIONS ###

    def authorize(self, id, amt):
        # Authorize a transaction by reserving credit for a pending transaction.
        # Updates available credit and adds the transaction to pending_transactions.
        if amt <= self.av_limit:
            self.av_limit -= amt
            self.pending_transactions[(id, 'payment')] = amt

    def settle(self, id, extra=0):
        # Settle a pending transaction, updating available credit and balance.
        # Finalizes the transaction, adds any extra fees, and removes it from pending_transactions.
        if id in self.pending_transactions:
            self.av_limit -= extra
            self.balance += self.pending_transactions[id] + extra
            del self.pending_transactions[id]

    def clearTransaction(self, id):
        # Cancel a pending transaction and reclaim reserved credit.
        # Reverts the available credit by adding the pending transaction amount.
        if id in self.pending_transactions:
            self.av_limit += self.pending_transactions[id]
            del self.pending_transactions[id]

    ### PAYMENTS ###

    def initiate_payment(self, id, amt):
        # Initiate a payment by reducing the balance by a specified amount (marked as pending).
        self.balance -= amt
        self.pending_payments[id] = amt

    def post_payment(self, id):
        # Finalize a pending payment, increasing available credit.
        # Updates available credit by adding the pending payment amount.
        if id in self.pending_payments:
            self.av_limit += self.pending_payments[id]
            del self.pending_payments[id]

    def clearPayment(self, id):
        # Reverse a pending payment and adjust the balance accordingly.
        # Reverts the balance by adding the pending payment amount.
        if id in self.pending_payments:
            self.balance += self.pending_payments[id]
            del self.pending_payments[id]

