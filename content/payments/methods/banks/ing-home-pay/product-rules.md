---
title: "ING Home'Pay product rules"
breadcrumb_title: "Product rules"
weight: 10
meta_title: "ING Home'Pay product rules - MultiSafepay Docs"
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/ING_Homepay.svg'
url: '/payment-methods/ing-home-pay/product-rules/'
aliases: 
    - /payment-methods/ing-home-pay/what-is-ing-home-pay/
    - /payments/methods/banks/ing-home-pay/about/
    - /payments/methods/ing-home-pay/product-rules/
---

|   |   |   |
|---|---|---|
| **Countries**  | Belgium  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#ing-home-pay-direct) / [Redirect](/api/#ing-home-pay-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 5 days | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- MultiSafepay doesn't automatically receive the IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed. You can process refunds after 1 business day.

- You can refund more than the original transaction value. See [Refunds](/payments/refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}
