---
title: "Trustly payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Trustly payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/trustly.svg'
aliases: 
    - /payment-methods/trustly/how-does-trustly-work/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction, and selects their country and their bank. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer authenticates their account and completes the payment. | | |
| 4. | MultiSafepay collects the funds and adds them to your MultiSafepay balance.| Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| Trustly has declined the transaction. | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |
| In rare cases, the transaction is marked as **Uncleared**. {{< br >}} Trustly then informs MultiSafepay of the correct status, which may be **Completed**, **Declined**, or **Expired**. {{< br >}} The **Uncleared** status automatically expires after 5 days. | Uncleared | Uncleared   |

For refund statuses, see [Processing refunds](/payment-methods/banks/trustly/user-guide/processing-refunds/).





