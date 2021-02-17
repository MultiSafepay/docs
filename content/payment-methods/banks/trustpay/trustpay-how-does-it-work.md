---
title: "TrustPay, How it works"
weight: 21
meta_title: "TrustPay, How it works - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
aliases: [/payment-methods/trustpay/trustpay-how-does-it-work/]
---
## How it works
If the transaction is approved by TrustPay, the transaction status will change to _completed_ and MultiSafepay will add the funds to the balance of your MultiSafepay Control.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status | Transaction Status | Description                                                                                                          |
|--------------|------------------|----------------------------------------------------------------------------------------------------------------------|
| Initialized  | Initialized      | A payment link has been generated, but no payment has been received yet.                                             | 
| Completed    | Completed        | A successful Alipay transaction has been received and the funds will be added to your MultiSafepay Control balance.  | 
| Declined     | Declined         | Transaction has been rejected.                                                                                       | 
| Expired      | Expired          | An unfinished transaction will automatically expire after a predefined period.                                       | 
| Void         | Cancelled        | Transaction has been cancelled.                                                                                       | 


#### Refund flow

| Order Status   | Transaction Status | Description                              |
|----------------|------------------|------------------------------------------|
| Reserved       | Reserved         | A refund has been requested.             | 
| Completed      | Completed        | Refund has been successfully processed.  | 

The full API reference for TrustPay can be found [here](/api/#trustpay)

### Product Rules
Some rules may apply to certain payment methods. For TrustPay, the following rules apply:

* Refunding more than the stated amount of the original transaction is possible with TrustPay. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Successful TrustPay transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* As a direct banking payment method, TrustPay has a different payment flow and therefore the setting of days or seconds active will have no influence. The customer processes the payment from his/her own banking environment. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page

* As it is a standard bank transfer method, an expiry date exception for TrustPay transactions has been set to 10 days

* TrustPay transactions are processed in [Czech Koruna (CZK)](/faq/general/which-currencies-are-supported-by-multisafepay) 
   
 