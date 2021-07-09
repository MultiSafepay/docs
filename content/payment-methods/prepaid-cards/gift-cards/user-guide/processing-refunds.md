---
title : "Processing refunds"
meta_title: "Gift cards - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 10
aliases: 
    - /payment-methods/prepaid-cards/gift-cards/refund-gift-card
    - /payment-methods/gift-cards/refund-gift-card
---

{{< details title="Gift card refund rules" >}}

- You cannot [refund more than the original transaction value](/faq/finance/refunding-more-than-original-transaction/).

- Transactions paid with a gift card in full: You can't refund these from your MultiSafepay balance because we don't receive any payment details or bank account details from the customer to refund to. You can refund these transactions in your own online banking environment. 

- Transactions paid with a gift card **and** another payment method (e.g. iDEAL): You can refund these in full from your MultiSafepay balance. 

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

 



