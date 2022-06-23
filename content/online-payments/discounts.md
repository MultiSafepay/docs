---
title: 'Discounts'
category: 6278c92bf4ad4a00361431b0
order: 200
hidden: false
slug:  'discounts'
---
You can apply discounts to orders via your dashboard or the API.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- AfterPay
- Alipay
- E-Invoicing
- in3
- Klarna
- Pay After Delivery

</details>

## How to discount in your dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).  
2. Go to **Transactions** > **Transaction overview**.  
3. Search for the transaction you want to discount and click to open the **Transaction details** page.  
4. Under **Order details**, click **Checkout editor**.  
5. Click **Change order**.

    <details id="discount-specific-items">
    <summary>Discount specific items</summary>
    <br>

    - In the **Quantity** field, enter the number of units to discount.
    - In the **Name** field, enter the name of the item to discount.
    - In the **Unit price** field, enter the single unit price as a _negative_ number, e.g. -10.
    - From the **Tax** list, select **None (0.0%)**. 
    - Click **Add**.
    - Check that the **New total** amount is correct. 
    - To display a field to enter add any relevant comments, click **Description**.
    - Click **Save item changes**.  
      A new transaction is generated and the order status is **Completed**.

    </details>

    <details id="discount-specific-amount">
    <summary>Discount a specific amount</summary>
    <br>

    - In the **Quantity** field, enter **1**.
    - In the **Name** field, enter a description of the discount.
    - In the **Unit price** field, enter the discount amount as a _negative_ number, e.g. -10.
    - From the **Tax** list, select **None (0.0%)**. 
    - Click **Add**.
    - Check that the **New total** amount is correct. 
    - To display a field to enter add any relevant comments, click **Description**.
    - Click **Save item changes**.  
      A new transaction is generated and the order status is **Completed**.

    </details>

## How to discount via the API 

To discount:

- Pay later orders, see API recipe – [Discount a pay later order](https://docs-api.multisafepay.com/recipes/discount-a-pay-later-order)
- Orders with other payment methods, see API recipe – [Discount an order](https://docs-api.multisafepay.com/recipes/discount-an-order)


See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder).

To discount: 
      
- An entire order, enter a reduced `amount`. 
- Specific items in the order, in the `shopping_cart`, reduce the `unit_price` of the relevant items.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)