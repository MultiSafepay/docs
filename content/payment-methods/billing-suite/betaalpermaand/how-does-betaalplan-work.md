---
title: "Betaal per Maand, How it works"
weight: 21
meta_title: "Betaal per Maand, How it works - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
# How it works

### The customer

Betaal per Maand is an online payment method that allows customers to pay for online purchases after receiving them. A special feature of post-payment is that customers are only charged for the items they keep from an order. This means that sometimes the complete customer journey also consists of a product return process. In the event of this process taking too long to verify, the collection period can be paused by placing it on hold. This can only be done via contact with Betaal per Maand.

* If a transaction is not accepted by Betaal per Maand, it is the customer that must contact Betaal per Maand **personally**, due to privacy compliance rules.

* When a Betaal per Maand transaction is uncleared, Betaal per Maand will authorize or decline the transaction.

When a transaction has been accepted, the risk of the merchant is assumed entirely by Betaal per Maand, who will contact the customer with the payment details. The customer can select the most suitable payback period and ways to fulfill the monthly payment to Betaal per Maand.

### The Shipped status

When receiving a Betaal per Maand transaction, it is important to take the following steps:

Upon agreeing with an order _(by actually sending the goods)_, the order status should be changed from _completed_ to _shipped_.  You can adjust the order status in the original transaction in your [MultiSafepay Control](https://merchant.multisafepay.com) via change order status (manually) or in some cases, in your ecommerce platform (automatically). Not changing the status to _shipped_ can result in the expiration of the order.

Changing the status to _shipped_ allows Betaal per Maand to initiate the billing process towards the customer. Betaal per Maand will guarantee the payout of the transaction.

The _shipped_ status is therefore important for invoicing the customer and the payout of the transaction on your MultiSafepay balance.

## Payout
The payout of a Betaal per Maand transaction will be added onto your [MultiSafepay Control](https://merchant.multisafepay.com) once received from Betaal per Maand. MultiSafepay will process the payout from a Betaal per Maand transaction within 5 business days.

## Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Uncleared   | Uncleared  | When a Betaal per Maand transaction is marked with the status uncleared, Betaal per Maand will authorize or decline the transaction. No action is required.   |
| Uncleared   | Initialized | A payment has been initiated, but no payment has been received yet.  | 
| Completed   | Uncleared  | A successful Betaal per Maand transaction has been received.   |
| Shipped     | Uncleared  | A Capture has been send to Betaal per Maand, the transaction has been confirmed. An invoice will be send to the customer and your payout is guaranteed. |
| Shipped     | Completed  | Payout of a Betaal per Maand transaction has been received and added to your MultiSafepay Control balance.|
| Declined    | Declined   | Transaction has been rejected by Betaal per Maand. Behind the declined status in your [MultiSafepay Control](https://merchant.multisafepay.com), the reason of rejection is shown.     |
| Void        | Cancelled   | Transaction has been cancelled.  | 
| Expired     | Expired    | When no action is being taken when receiving a transaction with the payment method Betaal per Maand, the transaction will automatically expire. | 

### Refund flow 

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 

The full API reference for Betaal per Maand can be found [here](/api/#santander-betaal-per-maand)

## Product rules
Some rules may apply to certain payment methods. For Betaal per Maand, the following rules apply:

* Refunding more than the stated amount of the original transaction is not possible with Betaal per Maand. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Successful Betaal per Maand transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* Payments done through Betaal per Maand are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay)

* As a rule of thumb, post-payment methods do not allow the use of a [gift card](/payment-methods/gift-cards) by a customer when filling in the payment details (after the order has already been placed). This has to do with the accuracy of the order specifications, needed by the collecting party (i.e. Betaal per Maand). Our platform would otherwise interpret the gift card as a discount (which is not present in the shopping cart specification) and would not reflect the right order information needed, for example, for taxation purposes. However, using gift cards for post-payment can be implemented as an option before placing the order (i.e. on your checkout page, before calling our API). It is the merchant's sole responsibility to enable this feature. Failing to comply with this product rule might result in unexpected errors and unwanted complications

* As a post-payment method, Betaal per Maand has a different payment flow and therefore the setting of days or seconds active will have no influence. 
 <br>        

* As an overarching rule for post-payment methods, both first name and last name for the customer details need to be at least 2 characters long. This also applies for the delivery details. Please note that failing to do so might result in unexpected errors. Given the nature of this payment method, we recommend you to always require full names (not initials, abbreviations, acronyms).


Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page.


