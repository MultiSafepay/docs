---
title: 'About Dankort'
breadcrumb_title: 'About Dankort'
weight: 10
meta_title: "About Dankort - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies"
layout: 'child'
read_more: '.'
aliases:
    - /payment-methods/branded-credit-cards/dankort-what-is-it/
    - /payment-methods/credit-and-debit-cards/branded-credit-cards/dankort-what-is-it/
    - /payment-methods/credit-and-debit-cards/dankort-what-is-it/
---

Dankort is a popular Visa-branded credit card in Denmark. An additional layer of security is provided by Verified by Visa (Visa's version of 3D Secure), which requires cardholders to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Credit card  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Denmark  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/credit-and-debit-cards/dankort/processing-refunds/) | 
| **Recurring payments**  | Yes | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | Yes | [More information](/faq/chargebacks) {{< br >}} You are solely liable for paying chargebacks.  |


### How to activate Dankort?
For Dankort to be available as a payment method on the payment page of MultiSafepay, the following are required:

1. The Visa gateway needs to be enabled
2. The locale needs to be da_DK (Denmark) in the transaction call received by MultiSafepay.

The [locale](/faq/api/locale) is leading in this to show the desired payment method Dankort on the payment page of MultiSafepay.

Upon adding Dankort as payment method on the checkout page, you can download the Dankort logo from MultiSafepay's [collection](/faq/general/where-find-logo-payment-methods) and upload it to your ecommerce platform. 

### How to refund a Dankort transaction?
Dankort (Visa) transactions can be refunded to the customer within 180 days.

Please follow these steps to refund a Dankort transaction:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction > transaction_
3. Find the transaction through search
4. Open transaction
5. Select _refund_
6. Fill in the amount that you want to refund to the customer  
7. _Confirm_.

_MultiSafepay does not allow you to refund more than the stated amount of the original transaction. Moreover, no credit card scheme allows refunds of more than the original transaction amount._


> _Please note that credit card payments that are refunded by the merchant to the customer, will be sent to the card issuing bank and its partners within 1 business day by MultiSafepay. Whether or not the refund will be visible to the customer depends on the reports, statements and online tools that are made available by the issuing bank_.

### Testing

For more information about the possibilities of testing with Dankort, please refer to our [test payment details](/faq/getting-started/test-payment-details/#dankort)