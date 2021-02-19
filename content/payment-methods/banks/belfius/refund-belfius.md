---
title: "How to refund a Belfius transaction"
weight: 22
meta_title: "Belfius, how to refund a transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
aliases: [/payment-methods/belfius/refund-belfius/]
---
## Request refund 
> An IBAN is not automatically received when a transaction is marked with the status completed. However, we import our bank statements daily and all incoming payments which have not yet been completed will then be finalized. Refunds can therefore be done after 1 business day.

Please follow these steps to refund a Belfius transaction:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction → transaction overview_
3. Find the transaction through search
4. Open transaction
5. Select _refund_
6. Fill in the amount that you want to refund to the customer
6. Confirm the refund.

* Refunding more than the stated amount of the original transaction is possible with Belfius (e.g. refunding the return costs incurred by the customer). More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page. Please bear in mind that by default, MultiSafepay does not allow refunds larger than  the original transaction amount and that this needs to be changed in your MultiSafepay Control

* The transaction status is now _initialized_. As long as the transaction status is marked as _initialized_, the refund can be cancelled. When the transaction status is marked as _completed_, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day.

>_A refund will only be processed if your balance on your MultiSafepay Control is sufficient_.

In the event of a failed Belfius refund, please contact our support team at <support@multisafepay.com> to assist you.



