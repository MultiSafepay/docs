---
title : "Discounts"
weight: 50
layout: 'single'
meta_title: "Discounts - MultiSafepay Docs"
short_description: "Process discounts via your MultiSafepay account or our API"
read_more: "."
url: '/refunds/discounts/'
---
You can process discounts either via your MultiSafepay account or our API.

Discounts are processed as a negative **amount** instead of a negative **quantity**.

## MultiSafepay account

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).  
2. Go to **Transactions** > **Transaction overview**.  
3. Search for the transaction you want to discount and click to open the **Transaction details** page.  
4. Click **Refund order**.  
5. Click **Edit**.
6. In the checkout editor:  
   - Add the discount as a new page, e.g. Quantity= 1 > Discount= Item or name > Amount (negative) > VAT
   - To deduct the amount of the discount, add a new line to the order.  
7. Click **Save**.

## API discounts

See API reference:

- [Discount added as a unit price](/api/#discount-with-unit-price)
- [Discount with order rule](/api/#discount-with-order-rule)