---
title : "Refunding recurring payments"
weight: 54
meta_title: "Refunding recurring payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/recurring-payments/
---

You can only refund recurring transactions to customers when the financial status of the transaction is marked as **Completed**. 

To refund a transaction, follow these steps:

1. In your [MultiSafepay Control](https://merchant.multisafepay.com), go to **Transactions** > **Transaction overview**.
2. Search for the transaction and open the **Transaction details** page.
3. Select **Refund**.
5. Enter the amount that you want to refund to the customer.
6. Click **Confirm**.

By default, you cannot refund more than the amount of the original transaction. To check if you are eligible to refund more, email your account manager at <sales@multisafepay.com>

The transaction status is now **Initialized**. As long as the transaction status is **Initialized**, the refund can be cancelled. When the status changes to **Completed**, the refund is processed correctly. 

The customer receives the refund in the bank account from which the transaction was paid within the next business day.
