---
title : "Pay later refunds"
weight: 40
layout: "single"
meta_title: "Pay later refunds - MultiSafepay Docs"
short_description: "Refund pay later orders via your dashboard or our API."
read_more: "."
url: "/refunds/pay-later/"
---
## MultiSafepay dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**, and click on the relevant transaction to open the **Transaction details** page.
3. Under **Order summary**, click **Refund order**.
{{< details title= "Full refund" >}} 
To refund the full amount:

- Click **Refund complete order**.
- Add any relevant comments in the **Description** field.
- Click **Save item changes**.  
  The order status changes to **Void**.
{{< /details >}}
{{< details title= "Partial refund" >}} 
To refund part of the amount:

- Click **Change order**.
- In the **Quantity** field, enter the number of units to refund.
- In the **Name** field, enter the name of the item to refund.
- In the **Unit price** field, enter the single unit price as a _negative_ number, e.g. -10.
- From the **Tax** list, select **None (0.0%)**. 
- Click **Add**.
- Check that the **New total** amount is correct. 
- To display a field to enter add any relevant comments, click **Description**.
- Click **Save item changes**.  
  A new refund transaction is generated and the order status is **Completed**.
{{< /details >}}

## API

See API reference – [Refund order](https://docs-api.multisafepay.com/reference/refundorder) > Pay later refund.

## Support

For support, email <support@multisafepay.com>