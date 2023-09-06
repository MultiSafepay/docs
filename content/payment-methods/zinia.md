---
title: 'Zinia'
category: 6298bd782d1cf4006032e765
order: 7
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'zinia'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/zinia-logo.svg" width="80" align="right" style="margin: 20px 20px 20px 30px; max-height: 75px"/>

<a href="https://www.zinia.com/" target="_blank">Zinia</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a <<glossary:BNPL>> methods that lets customers pay now, in 14 days **or**  3 equal installments within a period of time. 

Read how Zinia can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/zinia" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Netherlands  | 
| [Currencies](/docs/currencies/) | EUR  | 
| [Chargebacks](/docs/chargebacks/)  | No |
| [Partial capture](#partially-ship-order) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only)|
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

The diagrams below show the flow of a successful transaction. Click to magnify.

**Payment flow for 14 days:**

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/zinia.svg" alt="Zinia payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 100%;"/>

***

**Payment flow for installments:**

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/zinia-installment.svg" alt="Zinia installments payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 100%;"/>

***

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

**Payment statuses for 14 days**

| Description     | Order status | Transaction status |
| :--- | :--- | :-----|
| The customer has been redirected to Zinia. You can still cancel the transaction.    | Initialized  | Initialized |
| Zinia has authorized the transaction. You can no longer cancel. You can only refund. |Completed    | Initialized        |
| The order has been shipped. The payout period has started.  <br> [Manually change the order status to Shipped](#shipment).   | Shipped      | Uncleared  |
| MultiSafepay has settled the order, and funds have been added to your account.      | Shipped      | Completed          |
| Zinia declined the transaction.    | Declined     | Declined           |
| The transaction was cancelled.   | Void         | Void               |
| The order wasn't shipped within 30 days and the transaction has expired. | Expired  | Expired  |
| **Refunds:** Refund initiated.  | Initialized  | Initialized        |
| **Refunds:** Refund complete.  | Completed    | Completed          |

***

**Payment statuses for installments**

| Description     | Order status | Transaction status |
| :--- | :--- | :-----|
| The customer has been redirected to Zinia. You can still cancel the transaction.    | Initialized  | Initialized        |
| Zinia authorized the transaction and received the first payment from the customer. You can no longer cancel. You can only refund. | Completed    | Initialized        |
| The order has been shipped. The payout period has started.     | Shipped      | Uncleared  |
| MultiSafepay has settled the order, and funds have been added to your account. | Shipped      | Completed          |
| Zinia declined the transaction.    | Declined     | Declined  |
| The transaction was cancelled.   | Void         | Void               |
| The customer didn't pay the first installment within 15 minutes, **or** you didn't ship the order within 10 days of creating the transaction. | Expired      | Expired            |
| **Refunds:** Refund initiated.  | Initialized  | Initialized        |
| **Refunds:** Refund complete.  | Completed    | Completed          |

---

# Activation

1. Email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com)  
  - We check your eligibility and if approved, you will receive the Zinia contract.
  - Once signed, we activate the payment method for your account.
2. Once approved, to activate the method in your dashboard, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
- All sites, go to **Settings** > **Payment methods**.
- A specific site, go to **Sites**, and then click the relevant site.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [integration@multisafepay.com](mailto:intergration@multisafepay.com)

# Integration

### API

See API reference – [Create order](/reference/createorder/) > BNPL order. 

<details id="example-requests"> 
<summary>Example requests</summary>
<br>

For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Zinia direct/redirect**.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

***

</details>

### Ready-made integrations

You can use Zinia [gateway](/reference/gateway-ids) ID using a generic gateway in several of our [ready-made integrations](/docs/our-integrations/) (<<glossary:redirect>>).

# User guide

## Addresses

The customer's billing and shipping addresses must be the **same** to prevent fraud. 

## Amount limits

Minimum and maximum order amounts apply. Email [sales@multisafepay.com]((mailto:sales@multisafepay.com))

## Cancellation

You can cancel the order **before** shipment or **after** partial shipment.

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

<details id="the-collection-flow-for-installments">
<summary>Collection flow for 14 days</summary>
<br>

- The collection only starts after the order has been shipped to the customer.
- Zinia sends the customer an invoice after the order is shipped in full, **or** partially shipped, and the remaining items cancelled. 
- If the customer fails to pay within 14 days, Zinia sends reminders of their obligation to pay with an added fee. 
- The customer can contact Zinia if there is an issue with the payment.
- If the customer still fails to pay, Zinia sends the invoice to a debt collector. 

***

</details>

<details id="the-collection-flow-for-installments">
<summary>Collection flow for installments</summary>
<br>

- The collection only starts when the customer pays installment 1 of the order.
- Zinia sends the customer an invoice for the second installment after installment first payment is made. The second installment is due within 30 days.
- Zinia sends reminders to the customer 5 days before and on the day of each installment due.
- If the customer fails to pay within 14 days of overdue installments, Zinia sends reminders of their obligation to pay with an added fee.
- The customer can contact Zinia if there is an issue with the payment.
- If the customer still fails to pay, Zinia sends the invoice to a debt collector.

</details> 
---
## Expiration and extensions

<details id="the-collection-flow-for-installments">
<summary>Expiration period for 14 days</summary>
<br>

The default expiration period for an order is **30** days after it was created. If the order is not at least [partially shipped](#partially-ship-order) within this period, it is cancelled and [refunded](#refunds).

After the first partial shipment, the expiration period is reduced. You have **30** days to ship the remaining items, or the order expires. The capture period can be extended twice, each by **14** days.

If an order cannot be shipped within **30** days and you do not want to cancel the order, you can extend the expiration period to a maximum of **180** days. After this time, the order is canceled and refunded. 

</details>

<details id="the-collection-flow-for-installments">
<summary>Expiration period for installments</summary>
<br>

The default expiration period for an order is **10** days after it was created. If the order is not at least [partially shipped](#partially-ship-order) within this period, it is cancelled and [refunded](#refunds).

After the first partial shipment, the expiration period is reduced. You have **10** days to ship the remaining items, or the order expires. The capture period can be extended twice, each by **14** days.

You cannot extend the shipping period of an installment transaction. After **10** days, the order is canceled and refunded. 

</details>

After an order expires, the expiration period cannot be extended.

<details id="how-to-extend-an-order">
<summary>How to extend an order</summary>
<br>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Extend**.  
   While extended, the <<glossary:order status>> remains **Completed** and the <<glossary:transaction status>> remains **Uncleared**.

**Via API**

See API reference – [Put PAD order on hold](/reference/padputorderonhold).   

***

</details>

## Payment methods

Customers pay Zinia via [iDEAL](/docs/ideal/) or a [bank transfer](/docs/bank-transfer/).

## Refunds

After shipment, the order can be refunded fully or partially.

<details id="about-partial-refunds">
<summary>About partial refunds</summary>
<br>

For partial refunds:

| Amount paid                | Outcome                                                     |
| -------------------------- | ----------------------------------------------------------- |
| Equal to new order amount  | The order is completed.                                     |
| Less than new order amount | The order is updated.                                       |
| More than new order amount | The order is completed and the outstanding amount refunded. |

***

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

***

</details>

## Shipment

- Share the track & trace details with the customer and MultiSafepay, if relevant. 
- You can ship orders in full or in multiple parts. See [Partially ship order](#partially-ship-order) below.
- **For 14 days:**  You must update the <<glossary:order status>> to  **Shipped** within **30** days, or otherwise the order expires. See [Update the order status](#update-the-order-status) below.
- **For installments:** You must update the <<glossary:order status>> to  **Shipped** within **10** days, or otherwise the order expires. See [Update the order status](#update-the-order-status) below.


### Partially ship order

<details id="how-to-partially-ship-an-order">
<summary>How to partially ship an order</summary>
<br>

If you cannot ship all the items for an order at the same time, you can ship the order in multiple parts.

See API reference – [Update or cancel order](/reference/updateorder) > **Ship order**.

**Collection flow** 

Zinia begins the [collection flow](#collection-flow) after at least 1 partial shipment if all other items from the order are cancelled.

Zinia does **not** invoice partial shipment amounts separately. 

**Expiration**

After the first partial shipment, you have **10** days to ship the remaining items, or the order expires.

**Installments**

Partial shipment is supported for installments orders.

**Integration**

A unique shipment `order_id` is generated for each partial shipment.

See API reference – [Update or cancel order](/reference/updateorder) > **Ship order**.

**Notifications**

You receive a webhook notification when the <<glossary:order status>>  of each partial shipment changes to **Shipped**.

The status of the main transaction never changes to **Completed**. It remains **Initialized**, with a flag.

**Refunds**

You must must refund partial shipments separately, using the specific **shipment** `order_id`, instead of the original **invoice** `order_id`.

See API reference – [Refund order](/reference/refundorder).

❗️**Note:** To partially ship an order, email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com))

***

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

**Via the API**

See API reference – [Update or cancel order](/reference/updateorder).

***

</details>


## Surcharges

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, email [sales@multisafepay.com](mailto:sales@multisafepay.com) 

## Terms and conditions

- [Direct flow](/reference/introduction#direct-vs-redirect): You must display our terms and conditions in your checkout.
- [Redirect flow](/reference/introduction#direct-vs-redirect): Zinia terms and conditions are displayed by default on [payment pages](/docs/payment-pages/).

<br>
[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)