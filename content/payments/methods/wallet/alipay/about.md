---
title: 'About Alipay'
breadcrumb_title: 'About Alipay'
weight: 10
meta_title: "About Alipay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases:
    - /payment-methods/wallet/alipay/alipay-what-is-it
---

Alipay is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It supports online, QR, and contactless POS payments, as well as international money transfers.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Wallet  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | |
| **Currencies**  | EUR, USD | [More information](/faq/general/supported-currencies/) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- For Chinese customers, Alipay accounts are verified and linked to their Chinese bank account. Since 2021, non-Chinese customers can also pay with Alipay using the Tour Pass.

- You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).

- Currency conversion is processed in EUR only.

{{< details title="Alipay refund rules" >}}

- You can refund more than original amount. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in the bank account they originally paid from within the next business day.

If a refund fails, email the Support Team at <support@multisafepay.com>

{{< /details >}}
