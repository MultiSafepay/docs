---
title: "Request to Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Request to Pay payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/RTP.svg'
aliases: 
    - /payment-methods/bancontact/how-does-request-to-pay-work/
    - /payment-methods/banks/direct-bank-transfer/#how-does-it-work
    - /payment-methods/banks/direct-bank-transfer/#transaction-flow
    - /payment-methods/banks/direct-bank-transfer/#product-rules
---

The table below shows a successful Request to Pay payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

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
| The customer canceled the payment in Deutsche Bank online banking. | Void | Void |
| The customer didn't complete the payment and the transaction expired. | Expired | Expired |

For refund statuses, see [Processing refunds](/payment-methods/banks/request-to-pay/user-guide/processing-refunds/).


        


