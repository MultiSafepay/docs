---
title: 'Product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "in3 product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/svgs/in3.svg'
url: '/payments/methods/in3/product-rules/'
aliases:
    - /payments/methods/billing-suite/in3/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands  | in3 checks the customer's country, and billing/shipping address to confirm. |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  | 
| **Payment flow**  | [Direct](/api/#in3-direct) / [Redirect](/api/#in3-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 2 hours | |

{{< details title="Refunds" >}}

- Full, partial, and API refunds are supported. See [Refunds](/payments/refunds/).

- You can request in3 to process a full or partial refund, either before payout or up to 1&nbsp;year afterwards.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

- The default minimum order amount is 100 EUR and the default maximum amount is 3000 EUR. You can adjust these limits in the [backend](/getting-started/glossary/#backend) of our [ecommerce integrations](/payments/integrations/ecommerce-platforms/) to show or hide in3 on your checkout page depending on the order value.

- Customers can provide different billing and shipping addresses.

- See also MultiFactor – [Shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies).