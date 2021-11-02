---
title: "American Express payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "American Express payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/credit-and-debit-cards/american-express/how-does-american-express-work/
---

The table below shows a successful transaction flow from start to finish.  

{{< details title="About order and transaction statuses" >}}
For each payment in your MultiSafepay account, there are two statuses that change as payment progresses:

**Order status:** The progression of the customer's order with you, independent of the payment  
**Transaction status:** The progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects American Express at checkout and is redirected to a [MultiSafepay payment page](/payment-pages/). | Initialized | Initialized |
| 2. | The customer enters their credit card details, verifies their identify via [Safekey](/security-and-legal/payment-regulations/about-3d-secure/), and completes the payment. | | |
| 3. | The transaction passes through the automated MultiSafepay fraud filter. |  |  |
| 4. | You manually authorize or decline the transaction. {{< br >}} See [Evaluating Uncleared credit card transactions](/faq/finance/evaluating-uncleared-card-transactions/). | Uncleared | Uncleared |
| 5. | MultiSafepay collects the funds and settles them in your MultiSafepay balance. {{< br >}} **Or** {{< br >}} If you use your American Express MID (MerchantID), Amercian Express settles the funds directly in your business bank account. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer's bank has declined the transaction. {{< br >}} For more information, see [Declined status](/faq/general/declined-status/). | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 1-hour period. | Expired | Expired |
| The customer requested their bank to force reversal of funds. {{< br >}} See [About chargebacks](/faq/chargebacks/about-chargebacks/). | Chargeback | Completed   |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |
| The customer requested their bank to force reversal of funds. {{< br >}} See [About chargebacks](/faq/chargebacks/about-chargebacks/). | Chargeback | Completed   |



