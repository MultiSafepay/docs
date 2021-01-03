---
title: "Dankort, What it is"
meta_title: "Dankort, What it is - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## Dankort
### What is Dankort
Dankort - a Visa co-branded product - is one of the best-known and most commonly used Danish credit cards. Every credit card with the 'Verified by Visa' logo can be safely used for online payments.

| Payment type   | [Payment flow](https://docs.multisafepay.com/faq/api/difference-between-direct-and-redirect/)      | Countries | Currencies | Refund options  | [Recurring](https://docs.multisafepay.com/tools/recurring-payments/)   | [Chargebacks](https://docs.multisafepay.com/faq/chargebacks/)   |
|----------------|-------------------|-----------|------------|------------------|------------|---------------|
|Credit/Debit|Direct/Redirect|DK|Multiple|Full/Partial|Yes|Yes|

### How Dankort works
Dankort payments are processed through the Visa gateway.

### How to activate Dankort?
For Dankort to be available as a payment method on the payment page of MultiSafepay, the following are required:

1. The Visa gateway needs to be enabled
2. The locale needs to be da_DK (Denmark) in the transaction call received by MultiSafepay.

The [locale](/faq/api/locale) is leading in this to show the desired payment method Dankort on the payment page of MultiSafepay.

Upon adding Dankort as payment method on the checkout page, you can download the Dankort logo from MultiSafepay's [collection](/faq/general/where-find-logo-payment-methods/) and upload it to your ecommerce platform. 

### How to refund a Dankort transaction?
Dankort (Visa) transactions can be refunded to the customer within 180 days.

Please follow these steps to refund a Dankort transaction:

1. Login into your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction -> transaction_
3. Find the transaction through search
4. Open transaction
5. Select _refund_
6. Fill in the amount that you want to refund to the customer  
7. _Confirm_.

_MultiSafepay does not allow you to refund more than the stated amount of the original transaction. Moreover, no credit card scheme allows refunds of more than the original transaction amount._


> _Please note that credit card payments that are refunded by the merchant to the customer, will be sent to the card issuing bank and its partners within 1 business day by MultiSafepay. Whether or not the refund will be visible to the customer depends on the reports, statements and online tools that are made available by the issuing bank_.
