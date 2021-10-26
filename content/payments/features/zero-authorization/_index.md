---
title: 'Zero Authorization'
weight: 60
meta_title: "Zero Authorization - MultiSafepay Docs"

layout: "single"
logo: '/svgs/Zero_Authorization.svg'
short_description: 'Verify credit card information with a 0 EUR transaction.'
url: '/features/zero-authorization/'
aliases:
    - /tools/zero-authorization/what-is-zero-authorization/
    - /tools/zero-authorization/how-to-activate-zero-authorization/
    - /payments/features/zero-authorization/
---

Zero Authorization is a MultiSafepay solution that lets you verify credit cards without charging the cardholder. We charge an amount of 0 EUR (with or without [3D Secure](/payments/methods/credit-and-debit-cards/user-guide/glossary/#3d-secure)) to the credit card, store the card details as a token, and then check if the card is legitimate. 

You can then also use the token for [recurring payments](/features/recurring-payments).

Zero Authorization supports Maestro, Mastercard, and Visa, and is available in all countries and currencies.

For how Zero Authorization can benefit your business, see [0-Authorization](https://www.multisafepay.com/blog/manage-your-subscriptions).

## Statuses

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Action | Description | Order status | Transaction status |
|---|---|---|---|
|  Zero amount transaction | A transaction for 0 EUR has been processed. | Completed   | Completed  |

## Activation
Email requests to activate Zero Authorization in your MultiSafepay account to your account manager at <sales@multisafepay.com>

## Integration
To integrate Zero Authorization using our API, see API reference – [Zero Authorization](/api/#zero-authorization-orders).

Zero Authorization is not supported in our [ecommerce integrations](/integrations/ecommerce-integrations) by default, but you can customize it via our API.

For any questions, email the Integration Team at <integration@multisafepay.com>
