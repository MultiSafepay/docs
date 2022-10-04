---
title: 'Discounts'
category: 6278c92bf4ad4a00361431b0
order: 10
hidden: false
slug:  'discounts'
---
You can apply discounts to orders via your dashboard or the API.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Alipay
- E-Invoicing
- in3
- Klarna
- Pay After Delivery
- Riverty

</details>

## How to discount in your dashboard

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.  
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Order details**, click **Edit order**.  
4. In the dialog, click **Change**.

    <details id="discount-specific-items">
    <summary>Discount specific items</summary>
    <br>

    - In the **Quantity** field, enter the number of units to discount.
    - In the **Name** field, enter the name of the item to discount.
    - In the **Unit price** field, enter the single unit price as a _negative_ number, e.g. -10.
    - From the **Tax** list, select **None (0.0%)**. 
    - Click **Add**.
    - Check that the **Total** is correct. 
    - To display a field to enter add any relevant comments, click **Description**.
    - Click **Save changes**.

    <br>
    
    A new transaction is generated and the <<glossary:order status>> is **Completed**.

    <br>

    </details>

    <details id="discount-specific-amount">
    <summary>Discount a specific amount</summary>
    <br>

    - In the **Quantity** field, enter **1**.
    - In the **Name** field, enter a description of the discount.
    - In the **Unit price** field, enter the discount amount as a _negative_ number, e.g. -10.
    - From the **Tax** list, select **None (0.0%)**. 
    - Click **Add**.
    - Check that the **Total** amount is correct. 
    - To display a field to enter add any relevant comments, click **Description**.
    - Click **Save changes**.  

    <br>
    
    A new transaction is generated and the <<glossary:order status>> is **Completed**.
    
    </details>

## How to discount via the API 

To discount:

- <<glossary:BNPL>> orders, see Recipes – [Discount a BNPL order](/recipes/discount-a-bnpl-order/)
- Orders with other payment methods, see Recipes – [Discount an order](/recipes/discount-an-order/)


See API reference – [Create order](/reference/createorder/).

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