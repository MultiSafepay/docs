---
pagetitle: "Server to Server integration for credit card"
weight: 74
title: "Server to Server"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
By requesting the credit card details on the webshop, a 'direct' transaction can be created. Customers can finalize a credit card payment without being redirected to a MultiSafepay payment page, resulting in a faster checkout experience and more control for merchants.

### Supported cards

| Card | Supported for direct server-to-server payments |
|---|---|
|Visa | 3D verified by Visa and NON 3D |
|Mastercard | [3D Secure](/faq/general/glossary/#3d-secure) code and NON 3D |
|Maestro | Only 3D |
|American Express | American Express Safekey. Only transactions lower than 30 EUR are exempt from mandatory Safekey verification |
|Bancontact | Only 3D |

## Transaction flow
Transaction flow is the ways a transaction can be processed for each payment method.

* Order status      
Indicates the status of the order independent of the incoming or outgoing payment of the transaction. Example statuses: **Completed**, **Pending**, or **Rejected**. 

* Transaction status       
Indicates the payment status of the transaction, e.g. **Completed**, **Pending**, or **Rejected**. Once the transaction status is **Completed**, the amount of the transaction is added to your MultiSafepay balance.

All credit card transactions pass through our fraud filter. 

## Transaction statuses

| Order status                      | Transaction status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful credit card  transaction has been received and the funds will be added to your MultiSafepay balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission from the merchant to accept/decline the payment. For more information, see [Evaluating uncleared credit card transactions](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction).  | 
| Declined    | Declined    | Rejected by the issuing bank. For more information, see [Declined status](/faq/general/declined-status). | 
| Expired     | Expired     | Unfinished transactions automatically expire after a predefined period.  | 
| Void        | Cancelled    | The transaction was cancelled.   | 


### Transaction flow when processing on own MID 
> When using an own MID (MerchantID) from American Express, the funds are not processed by MultiSafepay. Instead, the funds will be added to your own balance at American Express.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Uncleared   | Initialized | Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)  | 
| Completed   | Initialized | A successful credit card  transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 


### Refund flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund was successfully processed.  | 
| Chargeback     | Completed   | Forced reversal of funds initiated by customer’s bank (issuer). Only applicable to SEPA Direct Debit and credit card payments. For more information, see [About chargebacks](/faq/chargebacks/what-is-a-chargeback).         |      

For more information about 3D Secure, see [About 3D Secure](/faq/payment-regulations/about-3d-secure).

###  Credit card settings for direct credit card 3D Secure payments
3D Secure is a technical standard to enhance security. Credit card transactions which are processed with the 3D Secure protocol require a form of authentication of the customer during the payment process. This is usually done via a password connected to the card.

By default, all card orders are processed with 3D Secure.    

For more information about Dynamic 3D Secure, see [Dynamic 3D Secure](/tools/server2server/3d-dynamics).


