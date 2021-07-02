---
title: "Apple Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Apple Pay payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/wallet/applepay/apple-pay-how-does-it-work
---

The table below shows a successful transaction flow from start to finish. 

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer completes the payment on an iOS device, using either [Touch ID or Face ID](https://www.apple.com/apple-pay). |   |  |
| 4. | MultiSafepay receives the customer's credit card details as an encrypted token. |   |  |
| 5. | MultiSafepay decrypts the card details and authorizes the payment as a standard credit card transaction. | | |
| 6. | The transaction passes through the automated MultiSafepay fraud filter. |  |  |
| 7. | Manually authorize or decline the transaction. {{< br >}} See [Evaluating Uncleared credit card transactions](/faq/finance/evaluating-uncleared-card-transactions/). | Uncleared | Uncleared |
| 8. | MultiSafepay collects the funds and adds them to your MultiSafepay balance. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The issuer has declined the transaction. {{< br >}} For more information, see [Declined status](/faq/general/declined-status). | Declined | Declined   |
| The transaction has been cancelled. | Void   | Void   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

For refund statuses, see [Processing refunds](/payment-methods/wallet/applepay/user-guide/processing-refunds/).

For more information about using Apple Pay, see Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).



