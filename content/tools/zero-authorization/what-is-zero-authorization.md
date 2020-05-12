---
title: "Zero Authorization, How it works"
weight: 61
meta_title: "Zero Authorization, How it works - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

Zero Authorization is an account verification method for credit cards that is used to verify a cardholders information __without charging the consumer__. Instead, an amount of zero (€ 0,00) is charged on the card to store the credit card information in the form of a token and to determine whether the card is legitimate or not. After creating the token, is then possible to charge the consumer with a new transaction with either Tokenization or [Recurring Payments](/tools/recurring-payments/)

The zero amount transaction can be executed with or without [3D Secure](/tools/server2server/), depending on the users’ case. This feature can protect merchants against fraud liability for future transactions.

### What are possible 'Zero Authorization' scenarios?

The following scenarios are ways in which Zero Authorization can be used. 

_MultiSafepay would like to mention that these functions can be developed and are not offered by MultiSafepay._

* __Free trial periods__: In this case, the customer sees as transaction of zero (€ 0,00) for a period of time, such as 14 days. After this period, the customer will be charged for a subscription service (e.g. monthly) based on a stored token.
* __Validation__: An amount of zero can be charged on the credit card for validation purposes. This assures merchants’ of future subscription payments which can occur on a monthly basis.
* __User account card management__: An amount of zero can be charged on the credit card to authorize the addition of a card to a user account for a specific platform. This is common among airline and hotel reservation websites. The credit card will be saved on the user account making it easier for the customer to pay for future transactions.
* __Updating personal information__: A merchant may want their customer(s) to update their credit card info when the current credit card information has expired or the account has been blocked. When new card details are entered, a zero amount transaction will authorize the card for future transactions.

### Transaction overview

* __Order status__: The order status indicates the status of the order. A zero authorization will always be _completed_. The order status is independent of the outgoing payment of the transaction.
* __Transaction status__: The transaction status indicates the payment status of the transaction. A zero authorization will always be _completed_. Once the transaction status is _completed_, the amount of the transaction will be displayed as zero (in your designated currency) on your MultiSafepay balance. See below for the transaction status actions:

The full [API documentation](/api/#order-status-authorized-transaction) on Manual Capture will assist in the implementation of the feature.

| Action                         | Order Status     | Transaction Status |   Description                                                      |
|--------------------------------|------------------|------------------|--------------------------------------------------------------------|
|Zero amount transaction | Completed | Completed | A transaction is executed amounting to zero. |

### Supported payment methods

Zero Authorization is suitable for a number of credit cards:

* VISA
* Mastercard
* Maestro

### Supported currencies and countries

Zero authorization transactions can be executed in __all__ currencies and countries.
