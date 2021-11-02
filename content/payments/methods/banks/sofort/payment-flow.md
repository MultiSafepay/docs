---
title: "Sofort payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Sofort payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/SOFORT.svg'
url: '/payment-methods/sofort/payment-flow/'
aliases: 
    - /payment-methods/sofort-banking/how-does-sofort-banking-work/
    - /payments/methods/banks/sofort-banking/payment-flow/
    - /payments/methods/banks/sofort/payment-flow/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}
For each payment in your MultiSafepay account, there are two statuses that change as payment progresses:

**Order status:** The progression of the customer's order with you, independent of the payment  
**Transaction status:** The progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer authenticates their account and completes the payment. | | |
| 4. | Settlement is pending. This may take up to 3 business days and applies to all payments regardless of the amount. {{< br >}} Do **not** ship orders during this status. MultiSafepay assumes no responsibility if you ship orders and the transaction fails. | Uncleared | Uncleared |
| 5. | The transaction is successful. {{< br >}} It cannot be reversed by the customer and settlement is guaranteed. | Completed | Completed |
| 6. | MultiSafepay collects the funds and settles them in your MultiSafepay balance.| | |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 1-day period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |






