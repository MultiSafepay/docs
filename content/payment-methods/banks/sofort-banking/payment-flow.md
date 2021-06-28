---
title: "SOFORT Banking payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "SOFORT Banking payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/SOFORT.svg'
aliases: 
    - /payment-methods/sofort-banking/how-does-sofort-banking-work/
---

The table below shows a successful SOFORT Banking payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer authenticates their account, and confirms to pay. | | |
| 4. | Settlement is pending. This may take up to 3 business days and applies to all payments regardless of the amount. {{< br >}} Do **not** ship orders during this status. MultiSafepay assumes no responsibility if you ship orders and the transaction fails. | Uncleared | Uncleared |
| 5. | The transaction is successful. {{< br >}} It cannot be reversed by the customer and settlement is guaranteed. | Completed | Completed |
| 6. | SOFORT Banking settles the funds with MultiSafepay.| | |
| 7. | MultiSafepay adds the funds to your MultiSafepay balance.| | |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

For refund statuses, see [Processing refunds](/payment-methods/banks/sofort-banking/user-guide/processing-refunds/).






