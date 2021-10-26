---
title: "Apple Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Apple Pay payment flow - MultiSafepay Docs"

short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/apple-pay/payment-flow/'
aliases: 
    - /payment-methods/wallet/applepay/apple-pay-how-does-it-work
    - /payments/methods/wallet/applepay/payment-flow/
---

The table below shows a successful transaction flow from start to finish. 

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects Apple Pay at checkout and is redirected to a [MultiSafepay payment page](/payment-pages/). | Initialized | Initialized |
| 2. | The customer completes the payment on an iOS device, using either [Touch ID or Face ID](https://www.apple.com/apple-pay). |   |  |
| 3. | MultiSafepay receives the customer's credit card details as an encrypted token. |   |  |
| 4. | MultiSafepay decrypts the card details and authorizes the payment as a standard credit card transaction. | | |
| 5. | The transaction passes through the automated MultiSafepay fraud filter. |  |  |
| 6. | You manually authorize or decline the transaction. {{< br >}} See [Evaluating Uncleared credit card transactions](/faq/finance/evaluating-uncleared-card-transactions/). | Uncleared | Uncleared |
| 7. | MultiSafepay collects the funds and settles them in your MultiSafepay balance. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The issuer has declined the transaction. {{< br >}} For more information, see [Declined status](/faq/general/declined-status). | Declined | Declined   |
| The transaction has been cancelled. | Void   | Void   |
| The customer didn't complete the payment and the transaction expired after the 1-hour period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |
| The customer requested their bank to force reversal of funds. {{< br >}} See [About chargebacks](/faq/chargebacks/about-chargebacks/). | Chargeback | Completed   |

For more information about using Apple Pay, see Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).



