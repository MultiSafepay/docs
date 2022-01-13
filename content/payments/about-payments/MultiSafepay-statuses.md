---
title: "MultiSafepay statuses"
weight: 20
meta_title: "MultiSafepay statuses - MultiSafepay Docs"
read_more: "."
url: '/about-payments/multisafepay-statuses/'
aliases:
    - /payments/multisafepay-statuses/
    - /faq/api/difference-between-status-and-transaction-status
    - /faq/api/difference-between-status-and-financial-status
    - /developer/api/difference-between-status-and-financial-status/
---

There are two statuses for each transaction that update as it is processed. 

In your [MultiSafepay account](https://merchant.multisafepay.com/), go to **Transaction overview**, and then select the relevant transaction to open the **Transaction details** page. Under **Status history**, you can see the order status and transaction status: 

### Order status
Changes as the customer's order with you progresses towards shipment (independent of payment).  
API attribute: `status`

### Transaction status
Changes as the funds progress towards settlement in your MultiSafepay balance.  
API attribute: `financial_status`

## Status meanings

The meaning of statuses (or combinations of statuses) varies per payment method. To check specific meanings, see the relevant [payment method](/payment-methods/) page. 

The table below sets out possible order and transaction statuses and what they commonly mean.

| Description | Order status | Transaction status |
|---|---|--|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void | Cancelled |
| The customer has requested a chargeback. | Void | Void |
| The customer didn't complete payment and the transaction expired. {{< br >}} Transaction expiry times vary per payment method. | Expired | Expired |
| The [issuer](/glossaries/multisafepay-glossary/#issuer) or [acquirer](/glossaries/multisafepay-glossary/#acquirer) has declined the transaction. {{< br >}} See also [About Declined status](/credit-cards-user-guide/declined-status/). | Declined | Declined |
| Manually [authorize or decline the transaction](/faq/finance/evaluating-uncleared-card-transactions/). | Uncleared | Uncleared |
| Manually change the order status to shipped. | Shipped | Uncleared |

### Refunds and chargebacks

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund.| Initialized/Reserved | Initialized/Reserved |
| The refund/chargeback is complete. | Completed | Completed |
| The refund has been processed successfully.| Refunded | Refunded |
| The [partial refund](/payments/refunds/) has been processed successfully.| Partial_refunded | Partial_refunded |
| The refund was declined. | Declined | Declined |


If the status of the refund  is **Reserved**, it may mean: 

- The refund hasn't been processed yet. Refunds are passed to the customer's bank at midnight on the day they are initiated, and then the status changes to **Completed**. The bank is now responsible for processing the payment. Refunds may be delayed by the issuing bank.
- The refund cannot be processed due to insufficient funds in your MultiSafepay account. To top up your balance, see [Adding funds to your MultiSafepay balance](https://docs.multisafepay.com/faq/finance/adding-funds-to-your-multisafepay-balance).

