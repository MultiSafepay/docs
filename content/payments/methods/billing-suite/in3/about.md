---
title: 'About in3'
breadcrumb_title: 'About in3'
weight: 10
meta_title: "About in3 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/svgs/in3.svg'
---

in3 is a Dutch online post-payment method where customers pay in 3 installments at no extra cost and without having to register with the Bureau Krediet Registratie (BKR). in3 processes all the installments and guarantees settlement after receiving the first one. 

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Post-payment method  | |
| **API flow**  | `Direct`/ `Redirect` | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | The Netherlands  | in3 checks the customer's country, and billing/shipping address to confirm. |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full, partial, API  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- The default minimum order amount is 100 EUR and the default maximum amount is 3000 EUR. You can adjust these limits in the backend of our [ecommerce integrations](/payments/integrations/ecommerce-platforms/) to show or hide in3 on your checkout page depending on the order value.

- Customers can provide different billing and shipping addresses.

- See also MultiFactor – [Shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies).

{{< details title="Refunds" >}}

- You can request in3 to process a full or partial refund, either before payout or up to 1&nbsp;year afterwards.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}
