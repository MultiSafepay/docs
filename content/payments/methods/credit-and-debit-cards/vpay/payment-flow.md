---
title: "V Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "V Pay payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/vpay/how-does-vpay-work/
---

The table below shows a successful transaction flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of settlement in your MultiSafepay balance

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer enters their credit card details, verifies their identify via [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/), and completes the payment. | | |
| 4. | The transaction passes through the automated MultiSafepay fraud filter. |  |  |
| 5. | Manually authorize or decline the transaction. {{< br >}} See [Evaluating Uncleared credit card transactions](/faq/finance/evaluating-uncleared-card-transactions/). | Uncleared | Uncleared |
| 6. | The transaction is successful. |  |  |
| 7. | MultiSafepay collects the funds and adds them to your MultiSafepay balance. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer's bank has declined the transaction. {{< br >}} For more information, see [Declined status](/payments/methods/credit-and-debit-cards/american-express/user-guide/declined-status/). | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |
| The customer requested their bank to force reversal of funds. {{< br >}} See [About chargebacks](/faq/chargebacks/about-chargebacks/).  | Chargeback | Completed   |

For refund statuses, see [Processing refunds](/payments/methods/credit-and-debit-cards/vpay/user-guide/processing-refunds/).


