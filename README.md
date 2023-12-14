# A Simple Python Credit Card System

This project implements a basic credit card system in Python with functionalities for managing credit limits, transactions, and payments.

## Features

- **Set Credit Limit:** Define the initial spending limit for your card.
- **Transactions:**
  - *Authorization:* Reserve credit for a pending transaction.
  - *Settlement:* Finalize a pending transaction, updating available credit and balance.
  - *Cancellation:* Undo a pending transaction and reclaim reserved credit.
- **Payments:**
  - *Initiation:* Reduce your balance by a specified amount (marked as pending).
  - *Post:* Finalize a pending payment, increasing available credit.
  - *Cancellation:* Reverse a pending payment and adjust your balance accordingly.

## Benefits

- **Learn:** Explore fundamental concepts of credit card systems and Python implementation.
- **Adapt:** Use this code as a base for building more complex financial systems.
- **Contribute:** Fork this repository and add your own features and improvements!

## Quick Start

1. Clone this repository to your local machine.
2. Install any dependencies (if needed).
3. Run `python creditCard.py` to explore the functionalities interactively.

## Example Usage

```python
# Create a card with a $1000 limit
card = CreditCard(1000)

# Check available credit and balance
print(f"Available credit: ${card.available_credit}")
print(f"Balance: ${card.balance}")

# Authorize a transaction (pending)
card.authorize(1, 200)

# See updated available credit
print(f"Available credit after authorization: ${card.available_credit}")

# Settle the transaction with a $5 fee
card.settle(1, extra_fee=5)

# Check updated balance and available credit
print(f"Balance: ${card.balance}")
print(f"Available credit after settlement: ${card.available_credit}")

# Try an invalid authorization
card.authorize(2, -100)

# Ensure no change in available credit
print(f"Available credit after invalid authorization: ${card.available_credit}")

# Settle a valid second transaction
card.settle(2)

# Check final balance and available credit
print(f"Final balance: ${card.balance}")
print(f"Final available credit: ${card.available_credit}")
