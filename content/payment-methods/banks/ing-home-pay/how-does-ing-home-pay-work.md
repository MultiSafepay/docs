---
title: "ING Home'Pay, How does it work?"
weight: 21
meta_title: "ING Home'Pay, how does it work? - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases: [/payment-methods/ing-home-pay/how-does-ing-home-pay-work/]
---
## How it works
ING Home'Pay is a banking payment method that allows ING Home'Pay customers to pay directly using their ING bank account. ING Home'Pay is similar to any bank payment. A customer chooses to pay with ING Home'Pay, authenticates their account, and confirms to pay.

> ING Home'Pay payments can only be processed on our new payment page starting with [PayV2](/tools/payment-pages/what-is-payv2)

In the event which a customer makes a successful payment, but does not finalize the process by pressing the "return to website" button, no status update will be received on our end. The transaction status will therefore remain _initialized_. However, we import our bank statements daily and all incoming payments which have not been completed yet will then be completed.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful ING Home'Pay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 


#### Refund flow 

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized    | Initialized | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 

The full API reference for ING Home'Pay can be found [here](/api/#ing-home-pay)

### Product rules
Some rules may apply to certain payment methods. For ING Home'Pay, the following rules apply:

* Refunding more than the stated amount of the original transaction is possible with ING Home'Pay. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Successful ING Home'Pay transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page.


* Payments done through ING Home'Pay are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay)
