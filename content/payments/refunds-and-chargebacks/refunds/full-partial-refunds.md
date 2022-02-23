---
title : "Full and partial refunds"
weight: 30
layout: 'single'
meta_title: "Full and partial refunds - MultiSafepay Docs"
short_description: "Via your MultiSafepay dashboard, ready-made integration, or API"
read_more: "."
url: '/refunds/full-partial/'
---

You can process full and partial refunds via your MultiSafepay dashboard, our ready-made integrations, and our API. 

For support, email the Support Team at <support@multisafepay.com>

## MultiSafepay dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).  
2. Go to **Transactions** > **Transaction overview**.  
3. Search for the transaction you want to refund and click to open the **Transaction details** page.  
4. Click **Refund order**:    
    - Partial refund: In the **Amount** field, enter the amount to refund.
    - Full refund: Don't change the amount.  
5. Click **Continue**, and then click **Confirm**.

The refund becomes a new transaction, which you can find on the original **Transaction details** page under **Related transactions**.

The status of the refund starts as **Reserved**, and changes to **Completed** at midnight. 
{{< alert-notice >}}If there are insufficient funds in your MultiSafepay balance, the refund is **not** processed. {{< /alert-notice >}}

## Ready-made integrations

You can process refunds in most of our [ready-made integrations](/integrations/ready-made/). See the user guide for the relevant integration.

## API

For all payment methods except [pay later methods](/refunds/about/), see API reference – [Refund an order](/api/#refund-an-order).


