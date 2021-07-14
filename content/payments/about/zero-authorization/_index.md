---
title: 'Zero authorization'
weight: 40
meta_title: "Zero authorization - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "single"
logo: '/svgs/Zero_Authorization.svg'
short_description: 'Verify credit card information with a 0 EUR transaction.'
aliases:
    - /tools/zero-authorization/what-is-zero-authorization/
    - /tools/zero-authorization/how-to-activate-zero-authorization/
---

Zero Authorization is a way of verifying a credit card without charging the cardholder. We charge an amount of 0 EUR (with or without [3D Secure](/payments/methods/credit-and-debit-cards/user-guide/glossary/#3d-secure)) to the credit card, store the card details as a token, and then check if the card is legitimate. 

You can then also use the token for [tokenization](/payments/about/tokenization) or [Recurring Payments](/payments/about/recurring-payments/).

Zero Authorization supports Maestro, Mastercard, and Visa, and is available in all countries and currencies.

For how Zero Authorization can benefit your business, see [0-Authorization](https://www.multisafepay.com/blog/manage-your-subscriptions).

## Statuses

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of settlement in your MultiSafepay balance

{{< /details >}}

| Action | Description | Order status | Transaction status |
|---|---|---|---|
|  Zero amount transaction | A transaction for 0 EUR has been processed. | Completed   | Completed  |

## Activation
Email requests to activate Zero Authorization in your MultiSafepay account to the Risk Team at <risk@multisafepay.com>

## Integration
To integrate Zero Authorization using our API, see API Reference – [Zero Authorization](/api/#zero-authorization).

Zero Authorization is not supported in our [ecommerce integrations](/integrations/ecommerce-integrations) by default, but you can customize it via our API.

For any questions, email the Integration Team at <integration@multisafepay.com>
