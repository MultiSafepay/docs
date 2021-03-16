---
title: "in3, How it works"
weight: 21
meta_title: "in3, How it works - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## How it works

A single purchase is spread out over three payments which can be fulfilled in the following sequence:

1. A consumer fills in his/her details during checkout and in3 conducts a credit check
2. The first payment is made and the item is shipped
3. The second payment will follow after 30 days, as well as a third after 60 days.

All payments are handled by in3 and the payments are guaranteed for the merchant if the consumer completes the initial payment successfully at the time of placing the order. 

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized  | Initialized  | The consumer is redirected to in3 and a credit check is conducted.   |
| Declined  | Declined  | The credit check has been declined.   |
| Completed    | Uncleared  | The payment has been successful. |
| Void    | Void  | The payment has been declined or abandoned.|
| Uncleared   | Initialized   | The payment is awaiting and the consumer has 5 minutes to complete the payment, otherwise the transaction will be cancelled.  |
| Completed       | Completed   | The transaction has been settled and is complete.  | 


### Refund Flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Completed    | Completed   | A refund or partial refund has been successful. The refund will be processed by in3. | 
| Declined      | Declined   | A refund or partial refund has been unsuccessful.  | 

The full API reference for in3 can be found [here](/api/#in3)

### Product rules

Some rules may apply to certain payment methods. For in3, the following rules apply:

* The initial payment is required for an order to be placed

* Refunds are processed by in3

* Payments can only be completed in Euros (EUR)

* in3 is only available in the Netherlands. A check will be conducted on the country, billing/shipping address entered by the consumer

* The default minimum order amount for an in3 payment is 100 EUR and the default maximum order amount is 3000 EUR. In our ecommerce integrations, the minimum can be raised and the maximum can be lowered in your backend. By doing so, you can change the availability of the in3 payment method depending on your customer's shopping cart value.

* Different billing and shipping addresses may be entered by the consumer

* Once a customer completes the first payment of an in3 order, the full payout will take place after 15 days.
