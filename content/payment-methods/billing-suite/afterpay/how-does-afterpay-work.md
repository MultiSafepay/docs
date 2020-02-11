---
title: "AfterPay, How it works"
weight: 21
meta_title: "AfterPay, How it works - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
# How it works

### The customer  
Pay-after-delivery methods allow customers to pay only for items they keep from an order. This means that sometimes the complete customer journey also consists of a product return process. In the event of the return process taking too long to verify, the collection period can be paused for 2 to 4 weeks by placing it on hold. This can only be done via <merchant@afterpay.com> or via +31 207230230.

* When a customer's transaction is not accepted by AfterPay, only the customer is able to retrieve the reason of rejection by AfterPay due to privacy compliance rules.



* When an AfterPay transaction is marked with the status _uncleared_, AfterPay will authorize or decline the transaction

When a transaction has been accepted, the risk of the merchant is assumed entirely by AfterPay. The customer must fulfill the payment to AfterPay within 14 days after the invoice date, unless otherwise agreed upon in writing.

### The Shipped status
When receiving an order paid for with AfterPay, it is important to keep a number of things in mind.

Upon agreeing with an order _(by actually sending the goods)_, the order status should be changed from _completed_ to _shipped_. You can adjust the order status in the original transaction in your [MultiSafepay Control](https://merchant.multisafepay.com) via change order status (manually) or in some cases, in your ecommerce platform (automatically). Not changing the status to _shipped_ can result in the expiration of the order.

Changing the status to _shipped_ allows AfterPay to initiate the billing process towards the customer. AfterPay will guarantee the payout of the transaction.

The _shipped_ status is therefore important for invoicing the customer and the payout of the transaction on your MultiSafepay balance.

## Delivery address    
AfterPay accepts a difference in invoice and delivery address. However, a different delivery address or pick up address is only forwarded if both the first and last name of the customer share at least two characters. 

The transaction in your MultiSafepay Control will only show the customer information (invoice address). The transaction details can be retrieved through a _GET request_. More information can be found on the [API documenation](/api/#retrieve-an-order) page. 


## Payout AfterPay transaction

The payout of an AfterPay transaction will be added onto your [MultiSafepay Control](https://merchant.multisafepay.com) once received from AfterPay. The payout timeline for this method is determined by AfterPay.

## Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Uncleared  | Uncleared  | When an AfterPay transaction is marked with the status uncleared, AfterPay will authorize or decline the transaction. No action is required.   |
| Completed  | Uncleared  | A successful AfterPay transaction has been received.   |
| Shipped    | Uncleared  | A capture has been send to AfterPay, the transaction has been confirmed. An invoice will be sent to the customer and your payout is guaranteed. |
| Shipped    | Completed  | Payout of an AfterPay transaction has been received and added to your MultiSafepay Control balance.|
| Declined   | Declined   | Transaction has been rejected by AfterPay. Behind the declined status in your [MultiSafepay Control](https://merchant.multisafepay.com/), the reason of rejection is shown.     |
| Void       | Cancelled   | Transaction has been cancelled.  | 
| Expired    | Expired    | When no action is being taken within 90 days of receiving a transaction with the payment method AfterPay, the transaction will automatically expire. | 


### Refund Flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized    | Completed   | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 

The full API reference for Afterpay can be found [here](/api/#afterpay).

## Product rules
Some rules may apply to certain payment methods. For AfterPay, the following rules apply:

* Refunding more than the stated amount of the original transaction is NOT possible with AfterPay. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page.

* Successful AfterPay transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund.

* As a post-payment method, AfterPay has a different payment flow and therefore the setting of days or seconds active will have no influence. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/) FAQ page

* When no action is taken within 90 days of receiving an AfterPay order, the transaction will automatically expire

* When an AfterPay transaction has the order status _shipped_, there will be no time limit on refunding the transaction


* As a rule of thumb, post-payment methods do not allow the use of a [giftcard](/payment-methods/gift-cards/) by a customer when filling in the payment details (after the order has already been placed). This has to do with the accuracy of the order specifications, needed by the collecting party (i.e. AfterPay). Our platform would otherwise interpret the giftcard as a discount (which is not present in the shopping cart specification) and would not reflect the right order information needed, for example, for taxation purposes. However, using giftcards for post-payment can be implemented as an option before placing the order (i.e. on your checkout page, before calling our API). It is the merchant's sole responsibility to enable this feature. Failing to comply with this product rule might result in unexpected errors and unwanted complications

* Payments done through Afterpay are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay/)

* Afterpay requires an additional API key for Belgium. This can be requested directly at Afterpay.