---
title : "PayPal, How it works"
weight: 21
meta_title: "PayPal, How it works - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## How it works
MultiSafepay supports seamless integration with PayPal with the PayPal API. Funds are transferred directly to the merchant’s PayPal business account, while the transaction statuses and payment validation are managed by MultiSafepay. In order to integrate your PayPal Business account with MultiSafepay, the PayPal account API settings must be configured. Once the integration is completed, you can receive payments through this gateway by using one of our plugins or by implementing a custom integration with our API.

The transaction status refers to the status of the actual payment. MultiSafepay uses the order status for PayPal transactions. Since we do not collect the funds of completed PayPal transactions (as they are directly sent to your PayPal account), the financial status will remain _initialized_.

Please note the various descriptions of statuses and how they should be interpreted.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

_Please note that MultiSafepay does not collect funds for PayPal_

{{< alert-notice >}} Within PayPal, the order status will be sent as _Completed_ and the financial status will be marked as _Initialized_. If the financial status is marked as _Initialized_, the order will not be delivered. Therefore, it is important to mention that the order in your backend has to be marked as _Completed_ when the order status is received as _Completed_ to ensure fulfillment of the order. MultiSafepay will not issue a _Completed_ notification for the financial status of an order. {{< /alert-notice >}}

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.


| Order Status                   | Transaction Status         | Description |
|--------------------------------|--------------------------|-----------------------------------------------------------------------------------------|
| Initialized                    | Initialized              | A payment link has been generated, but no payment has been received yet.  | 
| Completed                      | Initialized              | A successful PayPal transaction has been received and the funds will be added to your PayPal balance.   | 
| Declined                       | Declined                 | Transaction has been rejected   | 
| Expired                        | Expired                  | An unfinished transaction will automatically expire after a predefined period.  | 
| Void                           | Cancelled                | Transaction has been cancelled.   | 
| Uncleared                      | Initialized                | An 'Uncleared' transaction without a reason is due to a configuration in your PayPal business account. The 'Uncleared' transactions are paid in a currency that is not enabled in your PayPal account. It is important to enable that specific currency in your PayPal account in order for the order status to change to 'Completed' in your MultiSafepay Control. |


### Refund flow


| Order Status                    | Transaction Status        | Description |
|---------------------------------|-------------------------|-----------------------------------------------------------------------------------------|
| Reserved                        | Initialized             | A refund has been requested. | 
| Completed                       | Initialized             | Refund has been successfully processed.  |
| Uncleared                       | Uncleared               | Refund has been initiated but PayPal account funds are insufficient. Refund will only be processed if funds are present.    | 

View the full [API reference](/api/#paypal) for PayPal and credit cards.

### What is Seller Protection
PayPal Seller Protection covers you in the event of claims, chargebacks, or reversals that are a result of unauthorized purchases or items your buyer did not receive. With PayPal Seller Protection, you are covered for the full amount of all eligible transactions.

Full documentation on [What is Seller Pretection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156) with PayPal transactions. 

### Product rules
Some rules may apply to certain payment methods. For PayPal, the following rules apply:

* To be eligible for PayPal Seller Protection, the transaction request needs to have the correct state in the customer address details for the following [countries](https://developer.paypal.com/docs/nvp-soap-api/state-codes)

* Refunding more than the stated amount of the original transaction is not possible for PayPal. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Successful PayPal transactions have a maximum refund period of 60 days. After this period, it is advised to process the requested refund by different means

* A PayPal payment link is valid for 14 days. The lifetime of the payment link is set by PayPal. Therefore, a payment link created with PayPal will automatically expire after 14 days. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page

* Uncleared transactions can only be declined or accepted within your PayPal account

* Refunds will be processed only when your PayPal account balance is sufficient

* For information on which currencies are supported, please contact PayPal.

