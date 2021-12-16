---
title: 'in3 overview'
breadcrumb_title: 'Overview'
weight: 10
meta_title: "in3 overview - MultiSafepay Docs"
short_description: "Key information, supported countries, currencies, and features"
layout: 'child'
logo: '/svgs/in3.svg'
url: '/payment-methods/in3/overview/'
aliases: 
    - /payments/methods/billing-suite/in3/about/
    - /payments/methods/in3/product-rules/
    - /payment-methods/in3/product-rules/
---
in3 is a Dutch online payment method where customers pay in 3 installments after receiving their order, at no extra cost and without having to register with the Bureau Krediet Registratie (BKR). 

in3 processes all the installments and guarantees settlement after receiving the first one.

|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands – in3 checks the customer's country, and billing/shipping address to confirm.  | 
| **Currencies**  | EUR  | 
| **Chargebacks**  | No – See [Chargebacks](/payments/chargebacks/). | 
| **Refunds** | [Full and partial refunds](/refunds/full-partial/), [discounts](/refunds/discounts/), [API refunds](/refunds/pay-later-refunds) {{< br >}} You can request in3 to process a full or partial refund, either before payout or up to 1&nbsp;year afterwards. |
| **Payment features** | [Second Chance](/features/second-chance/) |
| **Transactions expire after** | 2 hours |

## Notes

- The default minimum order amount is 100 EUR and the default maximum amount is 3000 EUR. You can adjust these limits in the [backend](/glossaries/multisafepay-glossary/#backend) of our [ready-made integrations](/payments/integrations/ecommerce-platforms/) to show or hide in3 on your checkout page depending on the order value.

- Customers can provide different billing and shipping addresses.

## See also

[Gift cards and pay later methods](/payment-methods/gift-cards/pay-later-methods/)