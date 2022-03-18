---
title : "Discounts"
weight: 50
layout: 'single'
meta_title: "Discounts - MultiSafepay Docs"
short_description: "Process discounts via your MultiSafepay dashboard or our API."
read_more: "."
url: '/refunds/discounts/'
---

Discounts are processed as a negative **amount** instead of a negative **quantity**.

Supported payment methods:

- AfterPay
- Alipay
- E-Invoicing
- in3
- Klarna
- Pay After Delivery

## Dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).  
2. Go to **Transactions** > **Transaction overview**.  
3. Search for the transaction you want to discount and click to open the **Transaction details** page.  
4. Under **Order details**, click **Checkout editor**.  
5. Click **Change order**.
{{< details title= "Discount specific items" >}}
To discount specific items:

- In the **Quantity** field, enter the number of units to discount.
- In the **Name** field, enter the name of the item to discount.
- In the **Unit price** field, enter the single unit price as a _negative_ number, e.g. -10.
- From the **Tax** list, select **None (0.0%)**. 
- Click **Add**.
- Check that the **New total** amount is correct. 
- To display a field to enter add any relevant comments, click **Description**.
- Click **Save item changes**.  
  A new transaction is generated and the order status is **Completed**.
{{< /details >}}
{{< details title="Discount specific amount" >}}
To discount a specific amount:

- In the **Quantity** field, enter **1**.
- In the **Name** field, enter a description of the discount.
- In the **Unit price** field, enter the discount amount as a _negative_ number, e.g. -10.
- From the **Tax** list, select **None (0.0%)**. 
- Click **Add**.
- Check that the **New total** amount is correct. 
- To display a field to enter add any relevant comments, click **Description**.
- Click **Save item changes**.  
  A new transaction is generated and the order status is **Completed**.
{{< /details >}}

## API 

See API reference:

- [Discount an order](/api/#discount-an-order)
- [Discount pay later orders](/api/#discount-pay-later-orders)

## Support

Email the Support Team at <support@multisafepay.com>