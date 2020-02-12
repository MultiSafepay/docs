---
title: "Direct Debit, How does it work?"
weight: 21
meta_title: "Direct Debit, how does it work? - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
## How does it work?
As the merchant files the Direct Debit request, an order with status _initialized_ will be created (after MultiSafepay has conducted a background check on the provided customer data).

Every night, all Direct Debits will be sent to our bank and the status will change to _uncleared_.
From this moment on, it is no longer possible to cancel the transaction.

The next business day, we will receive the first feedback from our bank in case of a wrong IBAN or BIC.
When the money is received on our end, the order status changes to _completed_, but the transaction status remains _uncleared_.
The number of days that a Direct Debit has a transaction status _uncleared_ depends on the transaction amount.

### Clearing

For amounts smaller than 500 euro, clearing will take 7 business days.

Fpr amounts larger than 500 euro, clearing will take 20 business days.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

 

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized   | Initialized    | Created but not yet processed by the bank.   |
| Uncleared     | Uncleared      | Processed by the bank waiting for clearing period (depending on amount and settings of the merchant).   |
| Completed     | Completed      | Payment has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Declined      | Declined       | Rejected during uncleared period.   |
| Cancelled      | Cancelled       | Transaction has been cancelled or incorrectly entered by webshop

#### Refund flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 
| Chargeback     | Completed   | Forced reversal of funds initiated by customer’s bank (issuer). The chargeback cannot be challenged. | 

The full API reference for Direct Debit can be found [here](/api/#direct-debit)


### E-mandate
MultiSafepay creates an e-mandate automatically, based on IBAN and SiteID.
A Direct Debit can be **First** or **Recurrent**.
Two different batches are made for this.
The First orders are processed after 5 days by the bank, while the Recurrent orders after 2 days.


### Chargebacks by customer
A Direct Debit payment is not fully guaranteed. The customer has 56 days to retrieve the payment that took place. However, when it is an unauthorized transaction (i.e. without verifiable debtor consent) it can even be 13 months. As this process involves staff intervention in both the Debtor Bank and the Creditor Bank the costs can be as high as 65 EUR.

### Product rules
Some rules may apply to certain payment methods. For Direct Debit, the following rules apply:

* Refunding more than the stated amount of the original transaction is not possible with Direct Debit. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page

* Successful Direct Debit transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* As a collection payment method, Direct Debit has a different payment flow and the setting of days or seconds active will have no influence. 

       
Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/) FAQ page.<br>

* Payments done through Direct Debit are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay/)


