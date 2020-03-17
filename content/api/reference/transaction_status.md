---
weight: 640
meta_title: "API - Transaction statuses - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}
{{< /code-block >}}

{{< description >}}
## Transaction Statuses

Transactions can have the following statuses:

Read more about the difference between the [Status and the Financial Status](/faq/api/difference-between-status-and-transaction-status/) on our Documentation Center.

| Status           | Name             | Description                                                                                      |
|------------------|------------------|--------------------------------------------------------------------------------------------------|
| completed        | Completed        | Payment has been successfully completed and [payout](/faq/getting-started/glossary/#payout) is guaranteed. Proceed with fulfillment.      |
| initialized      | Initialized      | A payment link has been generated, but no payment has been received yet.                         |
| uncleared        | Uncleared        | Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction/)                |
| declined         | Declined         | Rejected by the the issuing bank. Read more about the reason why the transaction is declined in [what does it mean](/payment-methods/creditcards/creditcard-status-declined-what-does-this-mean-/)                                                               |
| cancelled        | Cancelled        | Cancelled by the merchant (only applies to the status Initialized, Uncleared or Reserved). 
| void             | Void             | Cancelled by the merchant.                 |
| expired          | Expired          | Depending on the payment method unfinished transactions will close automatically after a predefined period. |
| refunded         | Refunded         | Payment has been refunded (in full) to the customer.                                             |
| partial_refunded | Partial Refunded | Payment has been partially refunded to the customer.                                             |
| reserved         | Reserved         | [payout](/faq/getting-started/glossary/#payout) / refund has been put on reserved, a temporary status, until the merchant's account has been checked on sufficient balance. |
| chargedback      | Chargedback      | Forced reversal of funds initiated by customer’s bank (issuer). Only applicable to SEPA Direct Debit and credit card payments. |
| shipped          | Shipped          | Order for payment has been set to shipped to mark the order as fulfilled and capture the money. |

{{% /description %}}
