---
title: "Request to Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Request to Pay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/RTP.svg'
url: '/payment-methods/request-to-pay/payment-flow/'
aliases: 
    - /payment-methods/bancontact/how-does-request-to-pay-work/
    - /payments/methods/banks/request-to-pay/payment-flow/
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
| 1. | The customer initiates a transaction and is redirected to the Deutsche Bank payment page. {{< br >}} They authenticate themselves with the same credentials as for online banking, and authorize a SEPA bank transfer. | Initialized | Initialized |
| 2. | The transaction is successful and the customer is redirected to MultiSafepay. | Uncleared  | Completed |
| 3. | Deutsche Bank settles the funds in your business bank account. {{< br >}} For banks that support instant SEPA, settlement is instant. Otherwise, it is within 24 hours.  | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| Deutsche Bank or the customer's bank has declined the transaction. | Declined | Declined   |
| The customer cancelled the payment in Deutsche Bank online banking. | Void | Void |
| The customer didn't complete the payment and the transaction expired after the 1-hour period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |
| Deutsche Bank has declined the refund. | Declined | Declined |


        


