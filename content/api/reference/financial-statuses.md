---
weight: 640
meta_title: "API - Financial statuses - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}
{{< /code-block >}}

{{< description >}}
## Financial Statuses

Transactions can have the following financial statuses:

Read more about the difference between the [Status and the Financial Status](/faq/api/difference-between-status-and-transaction-status) on our Documentation Center.

| Status             | Description                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------|
| Initialized        | A payment link has been generated, but no payment has yet been received.      |
| Uncleared      | The payment is completed, but funds are still underway.                         |
| Completed        | The payment is finished and the funds are available for payout.                |
| Declined         | Rejected by the the issuing bank and no funds will arrive. Read more about the reason why the transaction is declined in [what does it mean](/faq/general/declined-status)                                                               |
| Cancelled        | Cancelled by the merchant and no funds will arrive.
| Void             | Cancelled by the merchant and no funds will arrive.                 |
| Expired          | Depending on the payment method, unfinished transactions will close automatically after a predefined period. |
| Reserved         | [Payout](/faq/getting-started/glossary/#payout) / refund has been put on reserved, a temporary status, until the merchant's account has been checked on sufficient balance. |

{{% /description %}}
