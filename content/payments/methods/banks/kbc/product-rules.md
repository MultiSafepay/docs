---
title: "Product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "KBC product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/KBC.svg'
url: '/payments/methods/kbc/product-rules/'
aliases: 
    - /payment-methods/kbc/what-is-kbc/
    - /payments/methods/banks/kbc/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Belgium  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#kbc-direct) / {{< br >}} [Redirect](/api/#kbc-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 5 days | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- MultiSafepay doesn’t automatically receive the IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed. You can process refunds after 1 business day.

- You can refund more than the original transaction value. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

The payment method functions the same for both the KBC branch and the CBC branch. However, MultiSafepay's payment gateway includes KBC and CBC as separate options because customers of one branch can't pay through the other.