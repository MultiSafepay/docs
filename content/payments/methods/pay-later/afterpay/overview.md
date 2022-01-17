---
title: 'AfterPay overview'
breadcrumb_title: 'Overview'
weight: 10
meta_title: "AfterPay overview - MultiSafepay Docs"
short_description: "Key information, supported countries, currencies, and features"
layout: 'child'
logo: '/logo/Payment_methods/AfterPay.svg'
url: '/payment-methods/afterpay/overview/'
aliases:
    - /payments/methods/billing-suite/afterpay/about/
    - /payments/methods/afterpay/product-rules/
    - /payment-methods/afterpay/product-rules/
---
[AfterPay](https://www.afterpay.nl/en/) is a widely used pay later method in the Netherlands and Belgium. Customers pay for orders after receiving them, and are only charged for items they keep from the order. AfterPay bears the risk and guarantees settlement.
 
|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands, Belgium  | 
| **Currencies**  | EUR  | 
| **Chargebacks**  | No – See [Chargebacks](/payments/chargebacks/). | 
| **Refunds** | [Full and partial refunds](/refunds/full-partial/), [discounts](/refunds/discounts/), [API refunds](/refunds/pay-later/) |
| **Transactions expire after** | 90 days |

## Notes

Customers can provide different invoice and delivery addresses, but the customer's first and last name must be at least two characters long. The **Transaction details** page in your MultiSafepay dashboard only shows the invoice address. To retrieve other transaction details, make a `GET /orders` request. See API reference – [Retrieve an order](/api/#get-order-details). 

## See also

[Gift cards and pay later methods](/payment-methods/gift-cards/pay-later-methods/)







