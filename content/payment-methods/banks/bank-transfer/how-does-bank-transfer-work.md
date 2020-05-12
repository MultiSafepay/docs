---
title: "Bank transfer, How does it work?"
weight: 21
meta_title: "Bank Transfer, how does it work? - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
## How does it work?
When the customer selects bank transfer as payment method, the bank account details of MultiSafepay will be sent by email. Based on the settings, the sender can be MultiSafepay itself or your ecommerce platform. The email will be sent to the email address provided by the customer when placing the order.

When the bank transfer is confirmed by the customer, the transaction will be visible in your overview with the status _initialized_. The customer needs to transfer the payment from his or her bank to MultiSafepay's bank account. This can be done through online banking or in person via a bank teller.

> _Please be advised that it can take between 1 and 3 business days for the funds to appear in the receiving account_.

After we receive the payment on one of our bank accounts with the proper amount and reference, we can match the payment with the transaction and a _completed_ notification will be sent to your [MultiSafepay Control](https://merchant.multisafepay.com) and ecommerce platform.

> _When MultiSafepay receives a bank transfer payment that has incorrect data and/or amount, the payment will not be linked to the outstanding transaction and will be refunded to the customer_.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized  | Initialized  | A payment link has been generated, but no payment has been received yet.    |
| Completed   | Completed   | A successful Bank transfer transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

#### Refund flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 


The full API reference for bank transfers can be found [here](/api/#bank-transfer).

### Product rules
Some rules may apply to certain payment methods. For bank transfer, the following rules apply:

* Refunding more than the stated amount of the original transaction is possible with bank transfers. More information available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page

* Successful bank transfer transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* The days and seconds active does not apply to the payment method bank transfer. The customer processes the payment from his/her own banking environment. As a result, it has a different payment flow and the setting of a days or seconds active will have no influence
 
However, the payment link that is provided in the Bank transfer email to the customer can be adjusted by setting a days_active_ or seconds_active. Bank transfer transactions are active for 60 days. By default, payment links expires after 30 days. 

Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/) FAQ page<br>

* If you would like to make changes in the validation of bank transfers, check whether this is possible in your ecommerce platform

* In order to provide your customer with a local bank account from MultiSafepay (where available), please add the appropriate [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) code in the transaction request (i.e. "country": "DE",)

* Payments done through bank transfers can be processed in the following [currencies](/faq/general/which-currencies-are-supported-by-multisafepay/):

     * Euros (EUR)
     * Pounds (GBP)
     * Czech koruna (CZK)
     * Hungarian forint (HUF)
     * Polish złoty (PLN)

