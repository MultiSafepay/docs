---
title: "Processing refunds"
breadcrumb_title: 'Processing refunds'
weight: 40
meta_title: "Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Rules and instructions for processing refunds for Paysafecard transactions"
layout: 'child'
aliases:
    - /payment-methods/prepaid-cards/paysafecard/refund-paysafecard
---

{{< details title="Paysafecard refund rules" >}}

- You can refund more than original amount. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Transactions paid with Paysafecard in full: You can't refund these from your MultiSafepay balance because we don't receive any payment details or bank account details from the customer to refund to. You can refund these transactions in your own online banking environment. 

- Transactions paid with Paysafecard **and** another payment method (e.g. iDEAL): You can refund these in full from your MultiSafepay balance. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

{{< details title="Refund statuses" >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed. | Completed | Completed |

{{< /details >}}
  
To refund a transaction paid with a gift card **and** another payment method, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Full refund**.
5. Click **Save**.
