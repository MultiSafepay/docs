---
title: "About MultiSafepay statuses"
weight: 3
meta_title: "About MultiSafepay statuses - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
url: '/api/multisafepay-statuses/'
aliases:
    - /faq/api/difference-between-status-and-transaction-status
    - /faq/api/difference-between-status-and-financial-status
    - /developer/api/difference-between-status-and-financial-status/
---

There are two statuses in your [MultiSafepay account](https://merchant.multisafepay.com/) that update as payments are processed. 

**Order status**  
The progression of the customer's order with you, independent of the payment, e.g. whether you have shipped the items.   
API attribute: [`status`](/api/#status)

**Transaction status**  
The progression towards settling the funds in your MultiSafepay balance.  
API attribute: [`financial_status`](/api/#financial_status)

Statuses are also valuable for understanding [reports](/business/accounting/reports/).

## Viewing statuses

To view statuses in your MultiSafepay account, go to **Transaction overview** > **Transaction details** page, under **Status history**. 

## Status meanings

The meaning of statuses (or combinations of statuses) varies per payment method. To check specific meanings, see the relevant [payment method](/payments/methods/) page. 

The table below sets out possible order and transaction statuses and what they commonly mean.

| Status | Description |
|---|---|
| Initialized | A payment link has been generated, but the customer hasn't yet completed payment. |
| Shipped | You have shipped the order and the funds can be captured. |
| Uncleared | The customer has completed payment, but the funds are not yet settled. You need to manually [authorize or decline the transaction](/faq/finance/evaluating-uncleared-card-transactions/). |
| Completed | - **Order:** The customer has completed payment and settlement is guaranteed. Proceed with shipment. {{< br >}} - **Transaction:** The funds are settled in your MultiSafepay balance. |
| Declined | The [issuer](/getting-started/glossary/#issuer) has declined the transaction. {{< br >}} See also [About Declined status](/payments/methods/credit-and-debit-cards/user-guide/declined-status/). |
| Void / Cancelled | You have cancelled the transaction. |
| Expired | The customer didn't complete payment and the transaction expired. |

### Refunds and chargebacks

| Status | Description |
|---|---|
|Initialized | The customer has requested a refund.|
| Chargeback | The customer has requested a [chargeback](/payments/chargebacks/).|
| Completed | The refund or chargeback has been  processed successfully. |
| Declined | The payment method has declined the refund request. |
| Reserved | A payout or refund has been temporarily reserved while we check your MultiSafepay balance has sufficient funds. |




