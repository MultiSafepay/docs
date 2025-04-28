---
title: 'Riverty (AfterPay)'
category: 6298bd782d1cf4006032e765
order: 6
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'riverty'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/afterpay-riverty-transition-logo.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.riverty.com/nl-nl/" target="_blank">Riverty</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> (formerly AfterPay) is a widely used <<glossary:BNPL>> method in the Netherlands and Belgium. Riverty bears the risk and guarantees <<glossary:settlement>>.

Read how Riverty can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/riverty" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Austria, Belgium, Germany, Netherlands, Switzerland | 
| [Currencies](/docs/currencies/)  | EUR  | 
| [Chargebacks](/docs/chargebacks/) | No  |
| [Discounts](/docs/discounts/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) <br> Activate at site level in your dashboard. |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.


<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/riverty-payment-flow.svg" alt="Riverty payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds. 

| Description | Order status | Transaction status |
|---|---|---|
| Riverty has authorized the transaction and the funds are awaiting capture. You can still cancel. <br> **⚠️ Note:** To capture the funds, when you ship the order you must manually [change the order status to Shipped](#shipment). | Completed  | Uncleared  |
| The funds are captured. <br> You can no longer cancel. You can only refund. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped | Completed |
| Riverty has declined the transaction. <br> Only the customer can contact Riverty to find out why (for privacy and compliance reasons).  | Declined | Declined |
| Riverty authorized the transaction, but you or the customer cancelled it before capture. | Void | Void/Cancelled |
| Riverty authorized the transaction, but you didn't ship within 90 days of creating the transaction **or** the customer didn't complete payment. | Expired | Expired |
| **Refunds:** Refund initiated. | Initialized | Completed |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation 

To activate Riverty for your account, email Riverty at <sales@riverty.com>  

Riverty provides you with an API key per country and per website, and you must accept Riverty's terms and conditions for each. 

# Integration

### API

- You will need an API key from Riverty per country per [website](/docs/sites/).
- See API reference – [Create order](/reference/createorder/) > BNPL order.
  
  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Riverty direct/redirect**.
  Set `type` to `direct` or `redirect`.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- A `shopping_cart` object is required for all BNPL orders. See Recipes – <a href="https://docs.multisafepay.com/recipes/include-shopping_cart-in-order" target="_blank">Include shopping_cart in order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- The `gateway_info` object is required for Riverty.
- Transactions expire after 90 days.
- For <<glossary:direct>> orders, you must display your terms and conditions in your checkout.

### Ready-made integrations

Riverty is supported in many of our ready-made integrations.

<details id="supported-ready-made-integrations"> 
<summary>Supported ready-made integrations</summary>
<br>

- [Craft Commerce](/docs/craft-commerce/)
- [CS-Cart](/docs/cs-cart/)
- [Drupal 8](/docs/drupal/)
- [Magento 1](/docs/magento-1/) & [Magento 2](/docs/magento-2/)
- [Odoo](/docs/odoo/)
- [OpenCart](/docs/opencart/)
- [PrestaShop](/docs/prestashop/)
- [Shopware 5 and 6](/docs/shopware/)
- [WooCommerce](/docs/woocommerce/)
- [X-Cart](/docs/x-cart/)

---

</details>

### Testing

To test Riverty payments, see Testing payment methods – [BNPL methods](/docs/testing#bnpl-methods).
<br>

---

# User guide

## Addresses

Different billing and shipping addresses are supported.  
The **Transaction details** page in your dashboard only shows the billing address. To retrieve other details, see API reference – [Get order](/reference/getorder/).

## Collection period
If the customer returns some items from the order and this takes a long time to verify, you can pause the collection period for 2 to 4 weeks. 

Phone **+31 207 230 230** or email <merchant@afterpay.com> 

## Gift cards

When paying with a gift card and Riverty, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because Riverty collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Refunds

To refund a Riverty transaction, follow these steps:

<details id="via-your-dashboard">
<summary>Via your dashboard</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transactions Overview** and select the relevant transaction.
3. Click on the transaction to go to the **Transaction summary** page.
4. Under **Order summary**, click **Edit order**.
5. Click **Refund whole order** to process a full refund.
   For partial refunds, you have two options:
   - Click the (❌) **remove** icon to process a refund for all units of a specific item, or
   - Click **Change**, enter the item's **name**, the **quantity** of items you want to refund, **unit price**, and select the **tax** rate. Click **Add**.
6. Click **Save changes**.

</details>

<details id="via-the-api">
<summary>Via the API</summary>
<br>

See API reference - <a href="https://docs.multisafepay.com/reference/refundorder" target="_blank">Refund order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i><br>
Use the <a href="https://docs.multisafepay.com/reference/getorder" target="_blank">Get order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> request to retrieve the order details.
1. Under **Path Params**, enter the `order_id` of the transaction you want to refund. 
2. Under **Body Params**, select **BNPL Refund**. Add all items in the shopping cart.
3. Duplicate the object of the items you want to refund and enter a negative value for `quantity`. 

**⚠️Note:** Always include the correct tax rate in `tax_table_selector` for each item in the shopping cart. Excluding it will result in an incorrect refund amount.

#### Example
```curl
curl --request POST \
     --url 'https://testapi.multisafepay.com/v1/json/orders/{order_id}/refunds?api_key={your_api_key}' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "checkout_data": {
    "items": [
      {
        "name": "example_item_1",
        "description": "",
        "unit_price": 100,
        "quantity": 3,
        "merchant_item_id": "1111",
        "tax_table_selector": "none",
        "weight": {
          "unit": "KG",
          "value": 12
        }
      },
      {
        "name": "example_item_2",
        "unit_price": 100,
        "quantity": 4,
        "merchant_item_id": "1212",
        "tax_table_selector": "BTW21"
      },
      {
        "name": "example_item_1",
        "unit_price": 100,
        "quantity": -3,
        "merchant_item_id": "1212",
        "tax_table_selector": "none",
        "weight": {
          "unit": "KG",
          "value": 12
        }
      },
      {
        "name": "example_item_2",
        "unit_price": 100,
        "quantity": -4,
        "merchant_item_id": "1212",
        "tax_table_selector": "BTW21"
      }
    ]
  }
}

```

</details>

## Shipment

When you ship the order, you **must** manually change the <<glossary:order status>> from **Completed** to **Shipped** to:

- Capture the funds
- Trigger sending the invoice to the customer
- Prevent the order from expiring

<details id="how-to-change-order-status-to-shipped">
<summary>How to change order status to shipped</summary>
<br>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transactions overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Order details**, click **Change order status**. 
4. Change the status to **Shipped**.
5. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your <<glossary:backend>>, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Lightspeed, Magento 2, and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

**⚠️ Note:** Some third-party plugins may not support updating the status via our API.

</details>

## Strong customer authentication 

In some cases, the customer is redirected to an authentication page. 
The criteria for when this is triggered are controlled by Riverty.

## Surcharges  
Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

Riverty therefore strongly recommends discontinuing any surcharges. 

For more information, see Riverty – <a href="https://www.afterpay.nl/nl/consumenten/vraag-en-antwoord/" target="_blank">Merchant support</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
