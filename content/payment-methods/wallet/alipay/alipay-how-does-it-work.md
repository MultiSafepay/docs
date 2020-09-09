---
title: "Alipay, How it works"
weight: 21
meta_title: "Alipay, How it works - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

##  How it works
Alipay is wallet-based payment method. Customers can input their credit card or bank account details to an Alipay account to create a wallet system. They can easily process payments from within their Alipay account.

Customers opting in for an Alipay payment have the possibility to pay through a QR code using the Alipay app or by filling in their Alipay account details.

If the transaction is approved by Alipay, the transaction status will change to _completed_ and MultiSafepay will add the funds to the balance of your MultiSafepay Control.

{{< alert-notice >}} Please note: The Alipay payment method can only be used with a verified Alipay account that is linked to a Chinese bank. All other transactions will be unsuccessful. {{< /alert-notice >}} 


### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful Alipay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Declined    | Declined    | Transaction has been rejected   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 


#### Refund flow 

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 


The full API reference for Alipay can be found [here](/api/#alipay)

### Product rules
Some rules may apply to certain payment methods. For Alipay, the following rules apply:

* __Important!__ Due to limitations, the Alipay payment method can only be used with a __verified__ Alipay account that is __linked to a Chinese bank__.

    Transactions will be unsuccessful if the abovementioned conditions are not met. Therefore, it would be wise to add Alipay to your website only if you intend on targeting Chinese customers with a working Alipay account.


* Refunding more than the stated amount of the original transaction is possible with Alipay. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Successful Alipay transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active.   
Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page
<br>

* Payments done through Alipay are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay)

* Alipay is a Chinese payment method. The currency conversion is processed in Euros (EUR) only.
