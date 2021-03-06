---
weight: 640
meta_title: "API Reference - Transaction statuses - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block hide >}}
{{< /code-block >}}

{{< description >}}
## Transaction Statuses

Transactions can have the following statuses:

Read more about the difference between the [Status and the Financial Status](/developer/api/difference-between-status-and-financial-status) on our Documentation Center.

| Status           | Name             | Description                                                                                      |
|------------------|------------------|--------------------------------------------------------------------------------------------------|
| completed        | Completed        | Payment has been successfully completed and [payout](/faq/general/multisafepay-glossary/#payout) is guaranteed. Proceed with fulfillment.      |
| initialized      | Initialized      | A payment link has been generated, but no payment has been received yet.                         |
| uncleared        | Uncleared        | Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)                |
| declined         | Declined         | Rejected by the the issuing bank. Read more about the reason why the transaction is declined in [what does it mean](/faq/general/declined-status)                                                               |
| cancelled        | Cancelled        | Cancelled by the merchant (only applies to the status Initialized, Uncleared or Reserved). 
| void             | Void             | Cancelled by the merchant.                 |
| expired          | Expired          | Depending on the payment method unfinished transactions will close automatically after a predefined period. |
| refunded         | Refunded         | Payment has been refunded (in full) to the customer.                                             |
| partial_refunded | Partial Refunded | Payment has been partially refunded to the customer.                                             |
| reserved         | Reserved         | [payout](/faq/general/multisafepay-glossary/#payout) / refund has been put on reserved, a temporary status, until the merchant's account has been checked on sufficient balance. |
| chargedback      | Chargedback      | Forced reversal of funds initiated by customer’s bank (issuer). Only applicable to SEPA Direct Debit and credit card payments. |
| shipped          | Shipped          | Order for payment has been set to shipped to mark the order as fulfilled and capture the money. |

{{% /description %}}
