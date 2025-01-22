---
title: 'Bizum'
category: 6298bd782d1cf4006032e765
parentDoc: 62a728d48b97080046c1d220
order: 5
slug: 'bizum'
---

<img src="https://cdn.billink.nl/assets/lockup/svg/billink-logo-default.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.billink.nl/" target="_blank">Billink</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>is a Dutch BNPL payment method available for both B2C and B2B transactions. It allows customers to receive goods before payment, settling the invoice within a typically 14-day period. Billink performs real-time credit checks and assumes the risk of non-payment.



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

| Description                                                                     | Order status | Transaction status |
| ------------------------------------------------------------------------------- | ------------ | ------------------ |
| Billink's credit check is in progress.                                          | Initialized  | Initialized        |
| The order is created.                                                           | Completed    | Uncleared          |
| Billink declined the transaction.                                               | Declined     | Declined           |
| **⚠️ Note:** To capture the funds, manually change the order status to Shipped. | Shipped      | Unclear            |
| MultiSafepay has collected the payment.                                         | Shipped      | Completed          |
| The customer initiated the payment process but didn't finalize it.              | Expired      | Expired            |
| **Refunds:** Billink has successfully processed a full or partial refund.       | Completed    | Completed          |
| **Refunds:** The refund was declined.                                           | Declined     | Declined           |



# Activation

1. Email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com)  
   We check your eligibility and if approved, activate the payment method for your account.
2. Once approved, to activate the method in your dashboard, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
   - All sites, go to **Settings** > **Payment methods**.
   - A specific site, go to **Sites**, and then click the relevant site.
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

- (Expiry to be added)

- For <<glossary:direct>> orders, you must display your terms and conditions in your checkout.

## Ready made solutions

The payment method will soon be available in our plugins.

## Testing

Testing will soon be available for this payment method.

***

# User guide

## Addresses

Different billing and shipping addresses are supported.

## Amount limits

Minimum and maximum order amounts apply. Email [sales@multisafepay.com](mailto:[sales@multisafepay.com](mailto:sales@multisafepay.com))

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
- If the customer fails to pay within the initial 14 day period, Billink sends reminders of their obligation to pay, in accordance with the Wet Incasso Kosten (WIK). 
- The customer can contact Billink if there is an issue with the payment.
- If the customer still fails to pay, Billink sends the invoice to a debt collector. 
- If necessary, you can delay the collection flow by placing the transaction on hold.

## Refunds

To refund a Billink transaction, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Navigate to **Transactions / Transactions Overview** and find the transaction you want to refund, or search for the transaction you want to refund by using the search bar.
3. Click on the transaction to go to the transaction details page.
4. On the right side of the page are the order details and a blue Refund button.
5. In this section you can remove order lines or refund the complete order.

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

For more information, email [\[sales@multisafepay.com\](mailto:sales@multisafepay.com)](mailto:[sales@multisafepay.com](mailto:sales@multisafepay.com))  
<br>