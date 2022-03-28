---
title: 'AfterPay overview'
breadcrumb_title: 'Overview'
weight: 10
meta_title: "AfterPay overview - MultiSafepay Docs"
short_description: "Key information, refunds, countries, currencies, and features"
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
| **Refunds** | [Full, partial, and API refunds](/refunds/pay-later/), [discounts](/refunds/discounts/) |
| **Transactions expire after** | 90 days |

## Customer addresses

Customers can provide different billing and shipping addresses, but the customer's first and last name must be at least two characters long. The **Transaction details** page in your MultiSafepay dashboard only shows the billing address. To retrieve other transaction details, make a `GET /orders` request. See API reference – [Retrieve an order](/api/#get-order-details). 

## Surcharges

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/about-payments/surcharges/) to pay later methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM). AfterPay therefore strongly recommends discontinuing any surcharges. 

For more information, see AfterPay – [Merchant support](https://www.afterpay.nl/nl/consumenten/vraag-en-antwoord/).

## See also

[Gift cards and pay later methods](/payment-methods/gift-cards/pay-later-methods/)







