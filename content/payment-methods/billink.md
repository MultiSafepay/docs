---
title: 'Billink'
category: 6298bd782d1cf4006032e765
parentDoc: 62bd75142e264000a66d62b5
order: 1
slug: 'billink'
---

<img src="https://cdn.billink.nl/assets/lockup/svg/billink-logo-default.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.billink.nl/" target="_blank">Billink</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>is a Dutch BNPL payment method available for both B2C and B2B transactions. It allows customers to receive goods before payment, settling the invoice within 30 days. Billink performs real-time credit checks and assumes the risk of non-payment.



| Supports                                                      | Details                       |
| ------------------------------------------------------------- | ----------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Netherlands, Belgium, Germany |
| [Currencies](/docs/currencies/)                               | EUR                           |
| [Chargebacks](/docs/chargebacks/)                             | No                            |
| [Payment pages](/docs/payment-pages/)                         | Yes                           |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial         |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/diagrams/svg/billink-payment-flow.svg" alt="Pay After Delivery payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description                                                                                                                                        | Order status | Transaction status |
| :------------------------------------------------------------------------------------------------------------------------------------------------- | :----------- | :----------------- |
| Billink's credit check is in progress.                                                                                                             | Initialized  | Initialized        |
| The transaction was cancelled.                                                                                                                     | Void         | Void               |
| Billink declined the transaction.                                                                                                                  | Declined     | Declined           |
| Billink has authorized the transaction and the funds are awaiting capture.                                                                         | Completed    | Uncleared          |
| **⚠️ Note:** <a href="https://docs.multisafepay.com/docs/e-invoicing#shipment" target="_blank">Manually change the order status to Shipped</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.<br> Order status must be changed to **Shipped** to be able to capture the funds.                                                                       | Shipped      | Uncleared          |
| MultiSafepay has collected the payment.                                                                                                            | Shipped      | Completed          |
| The order has not been payed within **30 days**.                                                                                                   | Expired      | Expired            |
| **Refunds:** Billink has successfully processed a full or partial refund.                                                                          | Completed    | Completed          |
| **Refunds:** The refund was declined.                                                                                                              | Declined     | Declined           |



# Activation

1. Email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com)  
   We check your eligibility and if approved, activate the payment method for your account.
2. Once approved, to activate the method in your dashboard, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
   - All websites, go to **Settings** > **Payment methods**.
   - A specific website, go to **Websites**, and then click the relevant website.
4. Select the checkbox for the payment method, and then click **Save**.

💬 Support: If the payment method isn't visible in your dashboard, email [integration@multisafepay.com](mailto:integration@multisafepay.com)  
<br />

# Integration

### API

See API reference – [Create order](/reference/createorder/) > BNPL order. 

<details id="example-requests"> 
<summary>Example requests</summary>
<br>

For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Billink redirect**.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

</details>

- A `shopping_cart` object is required for all BNPL orders. See Recipes – <a href="https://docs.multisafepay.com/recipes/include-shopping_cart-in-order" target="_blank">Include shopping_cart in order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

- VAT rates are limited to 0%, 5%, 6%, 7%, 9%, 16%, 19%, 20%, and 21%. Keep this in mind when setting `shopping_cart.items.tax_table_selector`

- For <<glossary:direct>> orders, you must display your terms and conditions in your checkout.

## Ready made solutions

Billink is supported in most <a href="https://docs.multisafepay.com/docs/our-integrations" target="_blank">ready-made integrations</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

- Exceptions:
  - Craft Commerce
  - Odoo
  - OsCommerce
  - Shopify
  - Zen Cart

## Testing

To test Billink payments, see Testing payment methods - [BNPL methods](/docs/testing#bnpl-methods).

***

# User guide

## Addresses

Different billing and shipping addresses are supported.

## Amount limits

Minimum and maximum order amounts apply. Email [sales@multisafepay.com](mailto:sales@multisafepay.com)

## Cancellation

You can cancel the invoice order **before** shipment or **after** partial shipment.

<details id="how-to-cancel-an-order">
<summary>How to cancel an order</summary>
<br>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Cancel**.
4. Add a description of what happened with the order, and then click **Complete**.  
   The <<glossary:order status>> changes to **Void** and the <<glossary:transaction status>> to **Cancelled**.

</details>

## Collection flow

- Billink sends the customer an invoice after the order is shipped in full, **or** partially shipped and the remaining items cancelled. 
- If the customer fails to pay within the initial 30 day period, Billink sends reminders of their obligation to pay, in accordance with the Wet Incasso Kosten (WIK). 
- The customer can contact Billink if there is an issue with the payment.
- If the customer still fails to pay, Billink sends the invoice to a debt collector. 
- If necessary, you can delay the collection flow by placing the transaction on hold.

## Refunds

To refund a Billink transaction, follow these steps:

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

When you ship the order, you **must** manually change the [order status](/docs/payment-statuses/) from **Completed** to **Shipped**, which:

- Captures the funds
- Prevents the order from expiring

<details id="how-to-change-order-status-to-shipped">
<summary>How to change the order status to shipped</summary>
<br>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transactions overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Order details**, click **Change order status**. 
4. Change the status to **Shipped**.
5. Send the customer the track and trace details, if relevant.

**In your backend**

If you change the order status in your backend, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

**⚠️ Note:** Some third-party plugins may not support updating the status via our API.

***

</details>

### Surcharges

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, email [sales@multisafepay.com](mailto:sales@multisafepay.com)  
<br>
