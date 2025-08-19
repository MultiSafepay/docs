---
title: Zinia
category:
  uri: Payment methods
slug: zinia
position: 7
privacy:
  view: anyone_with_link
parent:
  uri: bnpl
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/zinia-logo.svg" width="80" align="right" style={{margin: '20px 20px 20px 30px', maxHeight: '75px'}} />

<a href="https://www.zinia.com/" target="_blank">Zinia</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i> is a <Glossary>BNPL</Glossary> methods that lets customers pay now, in 14 days **or**  3 equal installments within a period of time. 

Read how Zinia can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/zinia" target="_blank">multisafepay.com</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i>

| Supports                                                      | Details                             |
| ------------------------------------------------------------- | ----------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Netherlands                         |
| [Currencies](/docs/currencies/)                               | EUR                                 |
| [Chargebacks](/docs/chargebacks/)                             | No                                  |
| [Partial capture](#partially-ship-order)                      | Yes                                 |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)          |
| [Refunds](/docs/refund-payments/)                             | Yes: Full, partial, and API refunds |
| [Second Chance](/docs/second-chance/)                         | Yes                                 |

# Payment flow

The diagrams below show the flow of a successful transaction. Click to magnify.

**Payment flow for 14 days:**

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/zinia.svg" alt="Zinia payment flow" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

***

**Payment flow for installments:**

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/zinia-installment.svg" alt="Zinia installments payment flow" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

***

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

**Payment statuses for 14 days**

| Description                                                                                                                | Order status | Transaction status |
| :------------------------------------------------------------------------------------------------------------------------- | :----------- | :----------------- |
| The customer has been redirected to Zinia. You can still cancel the transaction.                                           | Initialized  | Initialized        |
| Zinia has authorized the transaction. You can no longer cancel. You can only refund.                                       | Completed    | Initialized        |
| The order has been shipped. The payout period has started.  <br/> [Manually change the order status to Shipped](#shipment). | Shipped      | Uncleared          |
| MultiSafepay has settled the order, and funds have been added to your account.                                             | Shipped      | Completed          |
| Zinia declined the transaction.                                                                                            | Declined     | Declined           |
| The transaction was cancelled.                                                                                             | Void         | Void               |
| The order wasn't shipped within 30 days and the transaction has expired.                                                   | Expired      | Expired            |
| **Refunds:** Refund initiated.                                                                                             | Initialized  | Initialized        |
| **Refunds:** Refund complete.                                                                                              | Completed    | Completed          |

***

**Payment statuses for installments**

| Description                                                                                                                                   | Order status | Transaction status |
| :-------------------------------------------------------------------------------------------------------------------------------------------- | :----------- | :----------------- |
| The customer has been redirected to Zinia. You can still cancel the transaction.                                                              | Initialized  | Initialized        |
| Zinia authorized the transaction and received the first payment from the customer. You can no longer cancel. You can only refund.             | Completed    | Initialized        |
| The order has been shipped. The payout period has started.                                                                                    | Shipped      | Uncleared          |
| MultiSafepay has settled the order, and funds have been added to your account.                                                                | Shipped      | Completed          |
| Zinia declined the transaction.                                                                                                               | Declined     | Declined           |
| The transaction was cancelled.                                                                                                                | Void         | Void               |
| The customer didn't pay the first installment within 15 minutes, **or** you didn't ship the order within 10 days of creating the transaction. | Expired      | Expired            |
| **Refunds:** Refund initiated.                                                                                                                | Initialized  | Initialized        |
| **Refunds:** Refund complete.                                                                                                                 | Completed    | Completed          |

***

# Activation

1. Email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com)  

* We check your eligibility and if approved, you will receive the Zinia contract.
* Once signed, we activate the payment method for your account.

2. Once approved, to activate the method in your dashboard, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i>.
3. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.

4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [integration@multisafepay.com](mailto:intergration@multisafepay.com)

# Integration

### API

See API reference – [Create order](/reference/createorder/) > BNPL order. 

<details id="example-requests"> 
<summary>Example requests</summary>
<br/>

For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Zinia direct/redirect**.

<div style={{textAlign: 'center'}}>
  <img
    src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif"
    alt="MultiSafepay Sandbox Test Process GIF"
    style={{width: '40%', height: 'auto'}}
  />
  </div>

***

</details>

### Ready-made integrations

You can use Zinia [gateway](/reference/gateway-ids) ID using a generic gateway in several of our [ready-made integrations](/docs/our-integrations/) (<Glossary>redirect</Glossary>).

# User guide

## Addresses

The customer's billing and shipping addresses must be the **same** to prevent fraud. 

## Amount limits

Minimum and maximum order amounts apply. Email [sales@multisafepay.com]((mailto:sales@multisafepay.com)

## Cancellation

You can cancel the order **before** shipment or **after** partial shipment.

<details id="how-to-cancel-an-order">
<summary>How to cancel an order</summary>
<br/>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i>. 
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Cancel**.
4. Add a description of what happened with the order, and then click **Complete**.\
   The <Glossary>order status</Glossary> changes to **Void** and the <Glossary>transaction status</Glossary> to **Cancelled**.

</details>

## Collection flow

<details id="the-collection-flow-14-days">
<summary>Collection flow for 14 days</summary>
<br/>

* The collection only starts after the order has been shipped to the customer.
* Zinia sends the customer an invoice after the order is shipped in full, **or** partially shipped, and the remaining items cancelled. 
* If the customer fails to pay within 14 days, Zinia sends reminders of their obligation to pay with an added fee. 
* The customer can contact Zinia if there is an issue with the payment.
* If the customer still fails to pay, Zinia sends the invoice to a debt collector. 

***

</details>

<details id="the-collection-flow-for-installments">
<summary>Collection flow for installments</summary>
<br/>

* The collection only starts when the customer pays installment 1 of the order.
* Zinia sends the customer an invoice for the second installment after installment first payment is made. The second installment is due within 30 days.
* Zinia sends reminders to the customer 5 days before and on the day of each installment due.
* If the customer fails to pay within 14 days of overdue installments, Zinia sends reminders of their obligation to pay with an added fee.
* The customer can contact Zinia if there is an issue with the payment.
* If the customer still fails to pay, Zinia sends the invoice to a debt collector.

</details>

## Expiration and extensions

<details id="the-collection-flow-for-installments">
<summary>Expiration period for 14 days</summary>
<br/>

The default expiration period for an order is **30** days after it was created. If the order is not at least [partially shipped](#partially-ship-order) within this period, it is cancelled and [refunded](#refunds).

After the first partial shipment, the expiration period is reduced. You have **30** days to ship the remaining items, or the order expires. The capture period can be extended twice, each by **14** days.

If an order cannot be shipped within **30** days and you do not want to cancel the order, you can extend the expiration period to a maximum of **180** days. After this time, the order is canceled and refunded. 

</details>

<details id="the-collection-flow-for-installments">
<summary>Expiration period for installments</summary>
<br/>

The default expiration period for an order is **10** days after it was created. If the order is not at least [partially shipped](#partially-ship-order) within this period, it is cancelled and [refunded](#refunds).

After the first partial shipment, the expiration period is reduced. You have **10** days to ship the remaining items, or the order expires. The capture period can be extended twice, each by **14** days.

You cannot extend the shipping period of an installment transaction. After **10** days, the order is canceled and refunded. 

</details>

After an order expires, the expiration period cannot be extended.

<details id="how-to-extend-an-order">
<summary>How to extend an order</summary>
<br/>

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Extend**.\
   While extended, the <Glossary>order status</Glossary> remains **Completed** and the <Glossary>transaction status</Glossary> remains **Uncleared**.

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
<br/>

For partial refunds:

| Amount paid                | Outcome                                                     |
| -------------------------- | ----------------------------------------------------------- |
| Equal to new order amount  | The order is completed.                                     |
| Less than new order amount | The order is updated.                                       |
| More than new order amount | The order is completed and the outstanding amount refunded. |

***

</details>

To refund a Zinia transaction, follow these steps:

<details id="via-your-dashboard">
<summary>Via your dashboard</summary>
<br/>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i>.
2. Go to **Transactions** > **Transactions Overview** and select the relevant transaction.
3. Click on the transaction to go to the **Transaction summary** page.
4. Under **Order summary**, click **Edit order**.
5. Click **Refund whole order** to process a full refund.\
   For partial refunds, you have two options:
   * Click the (❌) **remove** icon to process a refund for all units of a specific item, or
   * Click **Change**, enter the item's **name**, the **quantity** of items you want to refund, **unit price**, and select the **tax** rate. Click **Add**.
6. Click **Save changes**.

</details>

<details id="via-the-api">
<summary>Via the API</summary>
<br/>

See API reference - <a href="https://docs.multisafepay.com/reference/refundorder" target="_blank">Refund order</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i><br/>\
Use the <a href="https://docs.multisafepay.com/reference/getorder" target="_blank">Get order</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i> request to retrieve the order details.

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

* Share the track & trace details with the customer and MultiSafepay, if relevant. 
* You can ship orders in full or in multiple parts. See [Partially ship order](#partially-ship-order) below.
* **For 14 days:**  You must update the <Glossary>order status</Glossary> to  **Shipped** within **30** days, or otherwise the order expires. See [Update the order status](#update-the-order-status) below.
* **For installments:** You must update the <Glossary>order status</Glossary> to  **Shipped** within **10** days, or otherwise the order expires. See [Update the order status](#update-the-order-status) below.

### Partially ship order

<details id="how-to-partially-ship-an-order">
<summary>How to partially ship an order</summary>
<br/>

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

You receive a webhook notification when the <Glossary>order status</Glossary>  of each partial shipment changes to **Shipped**.

The status of the main transaction never changes to **Completed**. It remains **Initialized**, with a flag.

**Refunds**

You must must refund partial shipments separately, using the specific **shipment** `order_id`, instead of the original **invoice** `order_id`.

See API reference – [Refund order](/reference/refundorder).

**⚠️ Note:** To partially ship an order, email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com)

***

</details>

### Update the order status

<details id="how-to-update-the-order-status">
<summary>How to update the order status</summary>
<br/>

When you ship the order, you **must** update the <Glossary>order status</Glossary> via the dashboard or your integration from **Completed** to **Shipped** to receive your payout, and to prevent the order from expiring.

**In your dashboard**

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i>.
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

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <Glossary>BNPL</Glossary> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, email [sales@multisafepay.com](mailto:sales@multisafepay.com) 

## Terms and conditions

* [Direct flow](/reference/introduction#direct-vs-redirect): You must display our terms and conditions in your checkout.
* [Redirect flow](/reference/introduction#direct-vs-redirect): Zinia terms and conditions are displayed by default on [payment pages](/docs/payment-pages/).

<br/>

<blockquote className="callout callout_info">
    <h3 className="callout-heading false">
        <span className="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
