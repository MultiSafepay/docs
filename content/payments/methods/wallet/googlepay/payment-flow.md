---
title: "Google Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Google Pay payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
noindex: '.'
---

The table below shows a successful transaction flow from start to finish. 

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a payment. | Initialized | Initialized |
| 3. | The customer completes the payment through their Google Pay account |  |  |
| 4. | MultiSafepay receives the customer's credit card details as an encrypted token. |   |  |
| 5. | MultiSafepay decrypts the card details and authorizes the payment as a standard credit card transaction. | | |
| 6. | The transaction passes through the automated MultiSafepay fraud filter. |  |  |
| 7. | If necessary, manually authorize or decline the transaction. {{< br >}} See [Evaluating Uncleared credit card transactions](/faq/finance/evaluating-uncleared-card-transactions/). | Uncleared | Uncleared |
| 8. | MultiSafepay collects the funds and adds them to your MultiSafepay balance. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The issuer has declined the transaction. {{< br >}} For more information, see [Declined status](/faq/general/declined-status). | Declined | Declined   |
| The transaction has been cancelled. | Void   | Void   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |
| The customer requested their bank to force reversal of funds. {{< br >}} See [About chargebacks](/faq/chargebacks/about-chargebacks/). | Chargeback | Completed   |

For more information about the Google Pay payment flow, see Google Pay – [Overview](https://developers.google.com/pay/api/web/overview).
