---
title: "SEPA Direct Debit payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "SEPA Direct Debit payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/directdebit-en.svg'
aliases: 
    - /payment-methods/direct-debit/how-does-direct-debit-work/
    - /payment-methods/banks/direct-debit/how-does-direct-debit-work/
    - /payment-methods/sepa-direct-debit/how-does-sepa-direct-debit-work/
    - /payment-methods/sepa-direct-debit/reason-codes/

---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/api/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | Make a SEPA Direct Debit request to MultiSafepay, providing information about the customer. |  |  |
| 2. | MultiSafepay conducts a background check on the customer's information, and if successful, creates an order. | Initialized  | Initialized |
| 3. | MultiSafepay creates an e-mandate automatically based on the customer's IBAN and your site ID. We specify if it is a `first` debit (processed within 5 days) or `recurring` debit (processed within 2 days). {{< br >}} We send all e-mandates to our bank at the end of every business day. {{< br >}} You can no longer cancel the transaction. | Uncleared | Uncleared |
| 4. | The customer's bank processes the transaction. For reasons why it may not be successful, see [Reason codes](/payments/sepa-direct-debit/reason-codes/). {{< br >}} If the IBAN or BIC is incorrect, our bank informs us the next business day. |  |  |
| 5. | MultiSafepay collects the funds. {{< br >}} For amounts smaller than 500 EUR, settlement takes 7 business days, and for amounts larger than 500 EUR it takes 20 days. | Completed | Uncleared |
| 6. | MultiSafepay adds the funds to your MultiSafepay balance.| Completed | Completed |


## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction was declined while **Uncleared**. | Declined | Declined   |
| The transaction has been cancelled or you provided incorrect customer information. | Cancelled   | Cancelled   |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |
| The customer requested a chargeback. You cannot dispute this. | Chargeback  | Completed | 




