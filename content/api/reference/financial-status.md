---
weight: 640
meta_title: "API Reference - financial_status- MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#financial-statuses
---
{{< code-block hide >}}
{{< /code-block >}}

{{< description >}}
## financial_status (status)

**Note:** In your MultiSafepay account, this is known as the transaction status.

Transactions can have the following `financial_status`:

| Status   | Description  |
|---|-------|
| Initialized        | A payment link has been generated, but the customer has not yet completed payment.      |
| Uncleared      | The customer has completed payment, but the funds are not yet settled. You need to manually [authorize or decline the transaction](/faq/finance/evaluating-uncleared-card-transactions/).   |
| Completed        | The funds are settled in your MultiSafepay balance. |
| Declined         | The [issuer](/getting-started/glossary/#issuer) has declined the transaction and no funds will arrive. See also [About Declined status](/payments/methods/credit-and-debit-cards/user-guide/declined-status/).  |
| Cancelled/Void        | You have cancelled the transaction and no funds will arrive.
| Expired          | The customer didn't complete payment and the transaction expired. |
| Reserved         | A [payout](/faq/general/multisafepay-glossary/#payout) or refund has been temporarily reserved while we check your MultiSafepay balance has sufficient funds. |

For more information, see [About MultiSafepay statuses](/api/multisafepay-statuses/).

{{% /description %}}
