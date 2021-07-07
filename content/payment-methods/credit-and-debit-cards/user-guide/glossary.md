---
title : "Credit card glossary"
weight: 10
meta_title: "Credit card user guide - About chargebacks - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
---
### 3D Secure
An authentication protocol that provides an additional layer of security for online credit and debit card payments to reduce fraud. Also known by brand names such as Mastercard Identity Check, Visa Secure, and American Express SafeKey. May use a 3D Secure code.

### acquirer
A financial institution that processes credit and debit card payments with card issuers on behalf of merchants. MultiSafepay is an acquirer for Visa, Mastercard, and Bancontact.

### acquirer reference number (ARN)
A unique number assigned to credit card payments as they move from the merchant's bank (acquiring bank) to the cardholder's bank (issuing bank). Banks can use ARNs to trace refunds.

### cardholder
A customer who uses a card issued by a bank to make cashless payments to a merchant.

### card scheme
A financial institution that issues credit cards, provides infrastructure, and processes payments for a fee, e.g. Visa, Mastercard, American Express.

### card verification code (CVC)
A 3 or 4 digit code customers enter as an additional layer of security for online credit or debit card payments. Not required for all cards, or for recurring payments.

### chargeback
When a customer disputes a credit card transaction and the transaction is reversed. See [About chargebacks](/faq/chargebacks/).

### credit card
A card issued by a bank, building society, or card scheme that lets the holder pay for products or services on credit.

### debit card
A card issued by a bank that transfers funds directly from the customer's bank account.

### dispute
If a customer wants a merchant to return funds that have already been captured, the customer can request a refund. If the merchant refuses, the customer may request their bank to make a chargeback. If the merchant disagrees, they can dispute the chargeback.

### fraud
When a person tries to receive products without paying for them by tricking a customer or merchant.

### issuer
The customer's bank, which verifies transaction information and sends funds to the collecting party. For credit or debit card payments, the bank issues the card.

### liability
The risk of accepting credit card payments and responsibility for paying for chargebacks.

### retrieval
When a customer cancels a credit card transaction within 24 hours. The funds have not yet left the customer's bank account, so they don't receive a credit.

### reversal
When a customer cancels an order paid by debit card and takes the funds back. 

### token/tokenization
Tokenization is storing customer payment details as a token (a unique string of numbers). For customers, it makes future payments faster and easier. For merchants, it enables repeatedly debiting customers, e.g. for subscriptions. 

### Uncleared transactions
When a customer has initiated a transaction, but the funds are reserved while the transaction is checked and authorized, e.g. because the MultiSafepay fraud filter detected unusual or risky patterns in the order data. Once authorized, the funds are captured and transferred to the collecting party. For credit card payments, merchants must manually check and authorize Uncleared transactions.

