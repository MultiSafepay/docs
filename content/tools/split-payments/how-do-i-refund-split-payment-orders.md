---
title : "Refunding Split Payments"
weight: 83
read_more: '.'
meta_title: "Refunding Split Payments - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

You can only refund Split Payments from the original transaction. Whether the refund is paid in full or in part, the amount will be deducted from the original transaction.

Example: Account A receives a payment of 80 EUR of which 10 EUR is going to account B. The customer receives a refund of 50 EUR which is supplied from account A. Whether it is a partial refund or a full, the amount will always be deducted from account A. 

To refund a split payment, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and open the **Transaction details** page.
4. Click **Refund**.
5. Enter the amount you want to refund to the customer.
6. Click **Confirm refund**.

By default, MultiSafepay does not allow you to refund more than the amount of the original transaction. But you can now refund more than originally received in your MultiSafepay Control, e.g. refunding the return costs incurred by the customer. For more information, see [Refunding more than the original amount](/faq/finance/refund-more-than-original-amount).

The transaction status is now **Initialized**. As long as the transaction status is remains **Initialized**, you can cancel the refund. 

When the transaction status changes to **Completed**, the refund has been processed correctly. The customer will receive the refund in the bank account the transaction was originally paid from on the next business day.
