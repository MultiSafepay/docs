---
title: "Bank Transfer payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Bank Transfer payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/banktransfer-en.svg'
aliases: 
    - /payment-methods/bank-transfer/how-does-bank-transfer-work/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction and provides an email address. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer receives details for a MultiSafepay bank account by email, sent by MultiSafepay or [from your ecommerce integration](/payment-methods/banks/bank-transfer/user-guide/emailing-payment-instructions/).  |   |  |
| 4. | The customer transfers the funds to the MultiSafepay bank account, either online or with a bank teller. {{< br >}} The funds may take 1 to 3 business days to arrive in our account. | | |
| 5. | MultiSafepay collects the funds and matches the payment to the outstanding transaction. {{< br >}} **Note:** If the customer provides incorrect data and/or pays the wrong amount, we won't link the payment to the outstanding transaction and instead refund the payment to the customer. | Completed | Completed |
| 6. | MultiSafepay adds the funds to your MultiSafepay balance.| | |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

For refund statuses, see [Processing refunds](/payment-methods/banks/bank-transfer/user-guide/processing-refunds/).






