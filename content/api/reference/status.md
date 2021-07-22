---
weight: 640
meta_title: "API Reference - status - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#transaction-statuses
---
{{< code-block hide >}}
{{< /code-block >}}

{{< description >}}
## status

**Note:** In your MultiSafepay account, this is known as the [order status](/api/multisafepay-statuses/).

Transactions can have the following `status`:

| Status   | Name   | Description     |
|----|----|---------|
| completed        | Completed        | The customer has completed payment and settlement is guaranteed. Proceed with shipment.      |
| initialized      | Initialized      | A payment link has been generated, but the customer has not yet completed payment.                         |
| uncleared        | Uncleared        | The customer has completed payment, but the funds are not yet settled. You need to manually [authorize or decline the transaction](/faq/finance/evaluating-uncleared-card-transactions/).                |
| declined         | Declined         | The [issuer](/getting-started/glossary/#issuer) has declined the transaction. See also [About Declined status](/payments/methods/credit-and-debit-cards/user-guide/declined-status/).  |
| cancelled        | Cancelled        | You have cancelled the transaction. (only applies to the status Initialized, Uncleared or Reserved). 
| void             | Void             | You have cancelled the transaction.                 |
| expired          | Expired          | The customer didn't complete payment and the transaction expired. |
| refunded         | Refunded         | The payment has been refunded to the customer in full.                                             |
| partial_refunded | Partial Refunded | The payment has been partially refunded to the customer.                                             |
| reserved         | Reserved         | A payout or refund has been temporarily reserved while we check your MultiSafepay balance has sufficient funds. |
| chargedback      | Chargedback      | The customer has requested a [chargeback](/payments/chargebacks/). Only applicable to SEPA Direct Debit and credit card payments. |
| shipped          | Shipped          | You have shipped the order and the funds can be captured. |


{{% /description %}}
