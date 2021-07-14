---
title : "Closing transactions"
meta_title: "Pay After Delivery - Closing transactions - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 
---

If you have not yet shipped an order, you can cancel the transaction by performing a full refund. See [Processing refunds](/payments/methods/billing-suite/pay-after-delivery/faq/processing-refunds/).

## Complete own funds

Follow the **Complete own funds** steps if:

- You have shipped an order and the customer fails to pay. You can no longer cancel the order, and must close the transaction instead.

- A customer pays an invoice to you directly. You need to link the payment to the transaction in your MultiSafepay account to change the transaction status to **Completed**. The transaction status changes to **Completed** or **Void**, and the customer no longer receives payment requests. 

{{< alert-notice >}} **Known bug:** Once the transaction status changes to **Completed**, the **Complete own funds** button is hidden and you must process a full refund in your MultiSafepay account instead. {{< /alert-notice >}}

Follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Complete own funds**. 
5. Enter a description about what happened with the order. 
6. Click **Complete**.  
    The total amount of the transaction is deducted from your MultiSafepay balance.  
    The invoice is considered settled.



