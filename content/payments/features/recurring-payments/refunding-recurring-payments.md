---
title : "Refunding Recurring Payments"
weight: 54
meta_title: "Refunding Recurring Payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/recurring-payments/
---

You can only refund recurring transactions to customers when the [transaction status](/payments/multisafepay-statuses/) is **Completed**. 

To refund a transaction, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click it.
4. In the **Transaction details** page, click **Refund**.
5. Enter the amount that you want to refund to the customer.
6. Click **Confirm**.

By default, you cannot refund more than the amount of the original transaction. To check if you are eligible to refund more, email your account manager at <sales@multisafepay.com>

The transaction status is now **Initialized**. As long as the transaction status is **Initialized**, the refund can be cancelled. When the status changes to **Completed**, the refund is processed correctly. 

The customer receives the refund in the bank account from which the transaction was paid within the next business day.
