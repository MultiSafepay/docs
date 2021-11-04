---
title: "Google Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Google Pay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/google-pay/payment-flow'
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
| 1. | The customer selects Google Pay at checkout and is prompted by Google to select their card and authorize the payment. | Initialized | Initialized |
| 2. | MultiSafepay receives the customer's credit card details as an encrypted token.|  |  |
| 3. | MultiSafepay decrypts the card details and processes the payment as a credit card transaction. | | |
| 4. | The transaction passes through MultiSafepay's automated fraud filter. |  |  |
| 5. | If necessary, manually authorize or decline the transaction. {{< br >}} See [Evaluating Uncleared credit card transactions](/faq/finance/evaluating-uncleared-card-transactions/). | Uncleared | Uncleared |
| 6. | MultiSafepay collects the funds and settles them in your MultiSafepay balance. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The issuer has declined the transaction. {{< br >}} For more information, see [Declined status](/faq/general/declined-status). | Declined | Declined   |
| The transaction has been cancelled. | Void   | Void   |
| The customer didn't complete the payment within 1 hour and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |
| The customer requested their bank to force reversal of funds. {{< br >}} See [About chargebacks](/faq/chargebacks/about-chargebacks/). | Chargeback | Completed   |

For more information about the Google Pay payment flow, see Google Pay – [Overview](https://developers.google.com/pay/api/web/overview).
