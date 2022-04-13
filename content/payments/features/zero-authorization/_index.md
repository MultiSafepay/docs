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

Zero Authorization is a MultiSafepay solution that lets you verify credit cards without charging the cardholder. We charge an amount of 0 EUR (with or without [3D Secure](/glossaries/credit-cards/#3d-secure)) to the credit card, store the card details as a token, and then check if the card is legitimate. 

You can then also use the token for [recurring payments](/features/recurring-payments).

Zero Authorization supports Maestro, Mastercard, and Visa, and is available in all countries and currencies.

For how Zero Authorization can benefit your business, see [0-Authorization](https://www.multisafepay.com/blog/manage-your-subscriptions).

## Statuses

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

| Action | Description | Order status | Transaction status |
|---|---|---|---|
|  Zero amount transaction | A transaction for 0 EUR has been processed. | Completed   | Completed  |

## Activation
Email a request to activate Zero Authorization to <sales@multisafepay.com>

## Integration

See API recipe – [Verify a card with Zero Authorization](https://docs-api.multisafepay.com/recipes/verify-a-card-with-zero-authorization).

Zero Authorization is not supported in our [ready-made integrations](/integrations/ready-made/) by default, but you can customize it via our API.

For support, email <integration@multisafepay.com>
