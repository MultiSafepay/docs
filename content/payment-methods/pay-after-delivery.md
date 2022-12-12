---
title: 'Pay After Delivery'
category: 6298bd782d1cf4006032e765
order: 21
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'pay-after-delivery-installments'
---

<img src="https://files.readme.io/cf02361-PAD-en.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

Pay After Delivery (Betaal Na Ontvangst) is MultiSafepay's own <<glossary:BNPL>> method for increasing customer confidence and <<glossary:conversion>>. MultiSafepay prefinances you, bears the risk, and guarantees settlement. 

Read how Pay After Delivery can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/pay-after-delivery" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Netherlands  | 
| [Currencies](/docs/currencies/) | EUR  | 
| [Chargebacks](/docs/chargebacks/)  | No  | 
| [Discounts](/docs/discounts/) | Yes |
| [Partial capture](#partially-ship-order) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds| 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/pay-after-delivery-payment-flow.svg" alt="Pay After Delivery payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| MultiSafepay's automated risk analysis is in progress. You can still cancel. | Initialized | Initialized |
| We are authorizing the transaction. | Uncleared | Uncleared |  
| We have authorized the transaction and the funds are awaiting capture. You can no longer cancel. You can only refund. <br> See [Close transactions](#close-transactions). | Completed | Uncleared | 
| ❗️ **Note:** To capture the funds, [manually change the order status to Shipped](#shipment). | Shipped | Uncleared |
| MultiSafepay has collected payment.  | Shipped | Completed |
| The transaction was cancelled. | Void/Cancelled   | Void/Cancelled | 
| MultiSafepay declined the transaction. | Declined | Declined |
| The customer didn't complete payment within 90 days. | Expired | Expired | 
| **Refunds:** Refund initiated. | Initialized | Initialized |  
| **Refunds:** Refund complete. | Completed | Completed | 

# Activation 

1. Email a request to <sales@multisafepay.com> 
   We check your eligibility and if approved, activate the payment method for your account. 
2. Once approved, to activate the method in your dashboard, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
    - All sites, go to **Settings** > **Payment methods**.
    - A specific site:
      - Go to **Integrations** > **Sites**, and then click the relevant site.
      - On the **Site profile** page, under **Payment methods**, click **Select payment methods**.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

# Integration

### API

See API reference – [Create order](/reference/createorder/) > BNPL order. 

<details id="example-requests"> 
<summary>Example requests</summary>
<br>

For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Pay After Delivery direct/redirect**.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

***

</details>

A `shopping_cart` object is required for all BNPL orders. See Recipes – [Include shopping_cart in order](/recipes/include-shopping_cart-in-order).

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/) (direct and redirect).

### Testing
See Testing – [BNPL methods](/docs/testing#bnpl-methods).
<br>

---

# User guide

## Addresses

The customer's billing and shipping addresses must be the **same** to prevent fraud. 

## Amount limits

Minimum and maximum order amounts apply. Email <sales@multisafepay.com>

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

📘 **Note:** Once the <<glossary:transaction status>> changes to **Completed**, the **Complete own funds** button is hidden. You must process a [full refund](/docs/refund-payments/) instead. 

</details>

## Collection flow

- MultiSafepay sends the customer an invoice after the order is shipped in full, **or** partially shipped and the remaining items cancelled. 
- If the customer fails to pay within the initial 14 day period, MultiSafepay sends reminders of their obligation to pay, in accordance with the Wet Incasso Kosten (WIK). 
- The customer can contact MultiSafepay if there is an issue with the payment.
- If the customer still fails to pay, MultiSafepay sends the invoice to a debt collector. 
- If necessary, you can delay the collection flow by placing the transaction on hold.

<details id="how-to-delay-the-collection-flow">
<summary>How to delay the collection flow</summary>
<br>

Email a request to place the transaction on hold to <klantenservice@multifactor.nl>  

Provide the following information:

- Transaction details
- Reason for your request
- When you expect to re-start the collection flow

---

</details>

## Customer pays you directly

If the customer pays you directly instead of MultiSafepay, to complete the order, simply pay MultiSafepay the order amount from your account balance. This stops MultiSafepay sending the customer an invoice or reminders. 

If you do so:
- **After** MultiSafepay has paid you out, then we refund you the order amount
- **Before** MultiSafepay pays you out, then we cancel the payout

After paying for an order from your account balance, you can no longer refund the customer.

<details id="how-to-complete-an-order-with-your-own-funds">
<summary>How to complete an order with your own funds</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Complete own funds**.
4. Add a description of what happened with the order, and then click **Complete**.
   The <<glossary:transaction status>> changes to **Completed**.

---

</details>

## Expiration and extensions

The default expiration period for an invoice order is **30** days after it was created. If the order is not at least [partially shipped](#partially-ship-order) within this period, it is cancelled and [refunded](#refunds).

After a first partial shipment, the expiration period is reduced. You have only **10** days to ship the remaining items from the order, or the order expires. 

If you cannot ship within 30 days, but don't want to cancel the order, you can extend the expiration period by a further 30 days, up to 180 days. After this time, the order is cancelled and refunded. 

<details id="how-to-extend-an-order">
<summary>How to extend an order</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Extend**.
   While extended, the <<glossary:order status>> remains **Completed** and the <<glossary:transaction status>> remains **Uncleared**.

---

</details>


## Payment methods

Customers pay MultiSafepay via [iDEAL](/docs/ideal/) or a [bank transfer](/docs/bank-transfer/).

## Refunds

After shipment, the invoice order can be refunded in full or in part.

<details id="about-partial-refunds">
<summary>About partial refunds</summary>
<br>

For partial refunds:

| Amount paid | Outcome |
|---|---|
| Equal to new order amount | The order is completed. |
| Less than new order amount | The order is updated. |
| More than new order amount | The order is completed and the outstanding amount refunded. |

---

</details>

<details id="how-to-refund-an-order">
<summary>How to refund an order</summary>
<br>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Refund order**.
4. In the **Reason / Description** field, enter the reason for the refund or a description of what happened with the order, and then click **Complete**.
5. In the **Comment** field, enter any additional information.
6. In the **Amount** fields, enter the amount to refund. 
7. Click **Continue**.
8. Review the **Refund confirmation**, and then click **Confirm**.

**Via the API** 

See API reference – [Refund order](/reference/refundorder).

---

</details>

## Shipment

- You must ship to receive payment, and within **30 days** or the order expires.
- Share the track & trace details with the customer and MultiSafepay, if relevant. 
- You can ship orders in full or in multiple parts. See [Partially ship order](#partially-ship-order) below.
- You must update the <<glossary:order status>> to **Shipped**. See [Update the order status](#update-the-order-status) below.
- You must comply with relevant [shipping policies](#shipping-policies). 

### Partially ship order

<details id="how-to-partially-ship-an-order">
<summary>How to partially ship an order</summary>
<br>

If you cannot ship all the items for an order at the same time, you can ship the order in multiple parts.

See API reference – [Update or cancel order](/reference/updateorder) > **Ship order**.

**Collection flow** 

MultiSafepay begins the [collection flow](#collection-flow) after at least 1 partial shipment if all other items from the order are cancelled.

MultiSafepay does **not** invoice partial shipment amounts separately. We invoice the total outstanding amount.

**Expiration**

After the first partial shipment, you have **10** days to ship the remaining items, or the order expires.

**Integration**

A unique shipment `order_id` is generated for each partial shipment.

See API reference – [Update or cancel order](/api/ship-invoice-order/) > **Ship order**.

**Notifications**

You receive a webhook notification when the [order status](/glossary/#order-status) of each partial shipment changes to **Shipped**.

The status of the main transaction never changes to **Completed**. It remains **Initialized**, with a flag.

**Refunds**

You must must refund partial shipments separately, using the specific **shipment** `order_id`, instead of the original **invoice** `order_id`.

See API reference – [Refund order](/api/refund/).

❗️ **Note:** To partially ship an order, email a request to <sales@multisafepay.com>

---

</details>

### Update the order status

<details id="how-to-update-the-order-status">
<summary>How to update the order status</summary>
<br>

When you ship the order, you **must** update the <<glossary:order status>> via the dashboard or your integration from **Completed** to **Shipped** to receive your payout, and to prevent the order from expiring.

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transactions overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Order details**, click **Change order status**.
4. From the **Change status to** list, select **Shipped**.
5. In the **Memo** field, enter a comment.
6. Click **OK**.

**In your backend**

If you change the order status in your <<glossary:backend>>, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

❗️ **Note:** Some third-party plugins may not support updating the status via our API.

---

</details>

### Shipping policies

You must read the following shipping policies:

- <a href="https://www.multifactor.nl/voorwaarden/shipping-policies" target="_blank">MultiFactor shipping policies</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://www.multifactor.nl/voorwaarden/shipping-policies/" target="_blank">Shipping policy Nederland</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 
- <a href="https://mailchi.mp/922285f8ac13/herinnering-aan-onze-shipping-policy" target="_blank">Herinnering aan onze shipping policy</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 

❗️ Failure to comply with these policies can impact on prefinancing and MultiSafepay's settlement guarantee. 

## Surcharges  

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges to Pay After Delivery. 

For more information, email <sales@multisafepay.com> 

## Terms and conditions

- [Direct flow](/reference/introduction#direct-vs-redirect): You must display our terms and conditions in your checkout.
- [Redirect flow](/reference/introduction#direct-vs-redirect): MultiSafepay terms and conditions are displayed by default on [payment pages](/docs/payment-pages/).

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
