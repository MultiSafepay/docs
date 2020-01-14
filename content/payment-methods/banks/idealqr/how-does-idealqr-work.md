---
title : "How does it work?"
weight: 21
meta_title: "How does it work? - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
## How it works
MultiSafepay supports seamless integration for iDEAL QR. As a merchant, you must either:

* Be able to able to retrieve and process the PNG image for the QR code on your side, in order to display it to the customer

    **or**

* Redirect the customer to our payment page similarly with other payment methods.

With iDEAL QR you can also produce a generic link that can be used multiple times. The QR code can be printed on leaflets. You can also enable an option to allow the customer change the amount.

> Please note that currently only 7 customer banks support iDEAL QR within their own banking app (Knab, Rabobank, ING, ABN AMRO, ASN Bank, RegioBank and SNS Bank). All other customers must use the dedicated iDEAL app.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful iDEAL QR transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 


#### Refund flow 

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized    | Initialized | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 

The full API reference for iDEAL QR can be found [here](/api/#ideal-qr).

### Product rules
Some rules may apply to certain payment methods. For iDEAL QR, the following rules apply:

* Refunding more than the stated amount of the original transaction is possible with iDEAL QR. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page

* Successful iDEAL transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* Payments done through iDEAL QR are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay/).