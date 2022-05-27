---
title : "Full and partial refunds"
weight: 30
layout: "single"
meta_title: "Full and partial refunds - MultiSafepay Docs"
short_description: "Via your dashboard, ready-made integration, or our API."
read_more: "."
url: "/refunds/full-partial/"
---

You can process full and partial refunds via your MultiSafepay dashboard, our ready-made integrations, and our API. 

For pay later methods, see [Pay later refunds](/refunds/pay-later/).

## Dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).  
2. Go to **Transactions** > **Transaction overview**.  
3. Search for the transaction you want to refund and click to open the **Transaction details** page.  
4. Click **Refund order**:    
    - Partial refund: In the **Amount** field, enter the amount to refund.
    - Full refund: Don't change the amount.  
5. Click **Continue**, and then click **Confirm**.

The refund becomes a new transaction, which you can find on the original **Transaction details** page under **Related transactions**.

The status of the refund starts as **Reserved**, and changes to **Completed** at midnight. 
{{< alert-notice >}}Refunds are only processed if there are enough funds in your MultiSafepay balance. {{< /alert-notice >}}

## Ready-made integrations

You can process refunds in most of our [ready-made integrations](/integrations/ready-made/). 

See the user guide for the relevant integration.

## API

See API reference – [Refund order](https://docs-api.multisafepay.com/reference/refundorder). 

## Support

For support, email <support@multisafepay.com>
