---
title: 'E-Invoicing'
category: 6298bd782d1cf4006032e765
order: 1
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'e-invoicing'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/e-invoicing.svg" width="100" align="right" style={{margin: '20px', maxHeight: '75px'}} />

E-Invoicing is a highly flexible MultiSafepay <Glossary>BNPL</Glossary> method that gives you full control of credit management, the collection flow, and customer communications in multiple languages. Optionally, leverage MultiSafepay's powerful customer credibility score technology to reduce fraud.

Read how E-Invoicing can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/e-invoicing" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />

| Supports                                                      | Details                                                                |
| ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Worldwide                                                              |
| [Currencies](/docs/currencies/)                               | EUR                                                                    |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                     |
| [Partial capture](#partially-ship-order)                      | Yes                                                                    |
| [Payment pages](/docs/payment-pages/)                         | Yes (current and deprecated versions)                                  |
| [Refunds](/docs/refund-payments/)                             | Yes: Full, partial, and API refunds, and [discounts](/docs/discounts/) |
| [Second Chance](/docs/second-chance/)                         | Yes                                                                    |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/e-invoicing-payment-flow.svg" alt="E-invoicing payment flow" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                                                                        | Order status   | Transaction status |
| ------------------------------------------------------------------------------------------------------------------ | -------------- | ------------------ |
| The [customer credibility score](#customer-credibility-score) (if requested) is in progress. You can still cancel. | Initialized    | Initialized        |
| MultiFactor has authorized the transaction. <br /> You can no longer cancel. You can only refund.                  | Completed      | Initialized        |
| **⚠️ Note:** [Manually change the order status to Shipped](#shipment). <br /> You must ship to receive payment.    | Shipped        | Initialized        |
| MultiSafepay has collected payment.                                                                                | Completed      | Completed          |
| MultiFactor declined the transaction.                                                                              | Declined       | Declined           |
| The transaction has been cancelled.                                                                                | Void/Cancelled | Void/Cancelled     |
| The customer didn't complete payment, or the order [expired](#expiration-and-extensions).                          | Expired        | Expired            |
| **Refunds:** Refund initiated.                                                                                     | Initialized    | Initialized        |
| **Refunds:** Refund complete.                                                                                      | Completed      | Completed          |

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
2. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.

3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

# Integration

### API

See API reference – [Create order](/reference/createorder/) > BNPL order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **E-Invoicing direct/redirect**.

  <div style={{textAlign: 'center'}}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{width: '40%', height: 'auto'}} />
  </div>
</details>

### Ready-made integrations

Supported in all [ready-made integrations](/docs/our-integrations/) (<Glossary>direct</Glossary> and <Glossary>redirect</Glossary>).

### Testing

See Testing payment methods – [BNPL methods](/docs/testing#bnpl-methods).\ <br />

***

# User guide

## Addresses

Different billing and shipping addresses are supported. Email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com)

## Batches

You can generate E-Invoicing transactions in batches for subscription payments.

<details id="how-to-batch-transactions-for-subscriptions">
  <summary>How to batch transactions for subscriptions</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **E-Invoicing** > **Batches**.
  3. Upload a file in .xls, .xlsx or .csv format.
  4. Follow the templates in your MultiSafepay dashboard.
</details>

## Cancellation

You can cancel the invoice order **before** shipment or **after** partial shipment.

<details id="how-to-cancel-an-order">
  <summary>How to cancel an order</summary>

  <br />

  **In your dashboard**

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
  3. On the **Transaction details** page, click **Cancel**.
  4. Add a description of what happened with the order, and then click **Complete**.\
     The <Glossary>order status</Glossary> changes to **Void** and the <Glossary>transaction status</Glossary> to **Cancelled**.

  **Via the API**

  See API reference – [Update or cancel order](/reference/updateorder).

  ***
</details>

## Collection flow

You can fully customize the collection flow.

<details id="how-to-customize-collection-flows">
  <summary>How to customize collection flows</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **E-Invoicing** > **Workflows**.
  3. Click **Create new**.
  4. Under **Settings**, you can select a previous template, if relevant.
  5. In the **Description** field, enter the name of this collection flow.
  6. From **Drag and drop**, drag and drop the relevant collection flow elements under **Drop elements here**.
  7. For each element, in the **Communication settings** dialog, you can:

     * Rename the communication flow in the **Description** field.
     * Request manual approval before the communication is sent.
     * Adjust the transaction fee by a fixed amount or percentage.
     * Set how many days the payment link is valid for.
     * Schedule when the next step in the collection flow will take place.
     * Specify the day of the week and time of day to send the communication.
  8. Click **Save**.

  ***
</details>

## Communications with the customer

You can fully customize your communications with the customer, including via email, letter (within the EU), SMS, and WhatsApp.

MultiSafepay can also append a PDF invoice (with your custom formatting) to the communication (except for SMS) on request. Email [sales@multisafepay.com](mailto:sales@multisafepay.com)

<details id="how-to-customize-communications">
  <summary>How to customize communications</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **E-Invoicing** > **Actions**.
  3. Click **Add new template**.
  4. Select the delivery method: Email, SMS, or letter.
  5. In the **Description** field, enter the name of the template.
  6. From the **Language** list, select the template language: Dutch, English, French, German, Italian, Portuguese, Russian, Spanish.
  7. In the **From address** field, enter the email address you want the communication to appear to be sent from.
  8. In the **From name** field, enter your company name.
  9. In the **Subject** field, enter the communication subject line.
  10. Edit the text **either** in the **Body plain** field, **or** if you know HTML and CSS, you can fully customize the content and layout in the **Body HTML** field. To view the HTML/CSS code, click **Source**.
  11. Click **Save**.

  ***
</details>

## Customer credibility score

You can request MultiSafepay to perform a credibility assessment of the customer to help reduce fraud.\
Email [sales@multisafepay.com](mailto:sales@multisafepay.com)

## Customer pays you directly

If the customer pays you directly instead of MultiSafepay, to complete the order, simply pay MultiSafepay the order amount from your account balance. This stops MultiSafepay sending the customer an invoice.

If you do so:

* **After** MultiSafepay has paid you out, then we refund you the order amount
* **Before** MultiSafepay pays you out, then we cancel the payout

After paying for an order from your account balance, you can no longer refund the customer.

<details id="how-to-complete-an-order-with-your-own-funds">
  <summary>How to complete an order with your own funds</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
  3. On the **Transaction details** page, click **Complete own funds**.
  4. Add a description of what happened with the order, and then click **Complete**.\
     The <Glossary>transaction status</Glossary> changes to **Completed**.

  ***
</details>

## Expiration and extensions

You define the expiration period for the order, up to a maximum of 180 days (including extensions). If the order is not at least [partially shipped](#partially-ship-order) within this period, it is cancelled and [refunded](#refunds).

<details id="how-to-extend-an-order">
  <summary>How to extend an order</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
  3. On the **Transaction details** page, click **Extend**.\
     While extended, the <Glossary>order status</Glossary> remains **Shipped** and the <Glossary>transaction status</Glossary> remains **Uncleared**.

  ***
</details>

## Gift cards

When paying with a gift card and E-Invoicing, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. Otherwise our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Invoices

MultiSafepay can customize the formatting of your invoices on request. Email [sales@multisafepay.com](mailto:sales@multisafepay.com)

<details id="how-to-view-invoices">
  <summary>How to view invoices</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **E-Invoicing** > **Invoices**.
</details>

<details id="how-to-generate-an-invoice">
  <summary>How to generate an invoice</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **E-Invoicing** > **E-Invoice generator**.
  3. Fill out the shopping cart:

     * In the **Quantity** field, enter the number of units of the item.
     * In the **Name** field, enter the name of the item.
     * In the **Unit price** field, enter the unit price of the item.
     * In the **Tax** field, enter the tax rate that applies to the item.
     * To add a new line for a different type of item, click **Add**.
  4. Fill out the required fields: **Address**, **Birthday**, **City**, **Country**, **Currency**, **Description**, **Email address**, **First name**, **Last name**, **Order ID**, **Phone number**, **Postal code / House number**, **State / Province**.
  5. From the **Website** list, select the relevant website.
  6. From the **Payment flow** list, select the relevant collection flow.
  7. Click **Generate invoice**.

  The invoice is sent to the email address provided.

  ***
</details>

## Payment methods

Customers can pay MultiSafepay using any of our payment methods, **except for** <Glossary>BNPL</Glossary> methods.

## Refunds

After shipment, you can refund the invoice order in full or in part, and with or without the `shopping_cart` object.\
See [Shopping carts](#shopping-carts) below.

<details id="about-partial-refunds">
  <summary>About partial refunds</summary>

  <br />

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

  <br />

  **In your dashboard**

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Transactions** > **Transactions Overview** and select the relevant transaction.
  3. Click on the transaction to go to the **Transaction summary** page.
  4. Under **Order summary**, click **Edit order**.
  5. Click **Refund whole order** to process a full refund.\
     For partial refunds, you have two options:
     * Click the (❌) **remove** icon to process a refund for all units of a specific item, or
     * Click **Change**, enter the item's **name**, the **quantity** of items you want to refund, **unit price**, and select the **tax** rate. Click **Add**.
  6. Click **Save changes**.

  **Via the API**

  See API reference – [Refund order](/reference/refundorder).

  ***
</details>

## Shipment

* You must ship to receive paymen **before** the order expires.
* Share the track & trace details with the customer and MultiSafepay, if relevant.
* You can ship orders in full or in multiple parts. See [Partially ship order](#partially-ship-order) below.
* You must update the <Glossary>order status</Glossary> to **Shipped**. See [Update the order status](#update-the-order-status) below.

### Partially ship order

<details id="how-to-partially-ship-an-order">
  <summary>How to partially ship an order</summary>

  <br />

  If you cannot ship all the items for an order at the same time, you can ship the order in multiple parts.

  See API reference – [Update or cancel order](/reference/updateorder) > **Ship order**.

  **Partial capture**

  If you have partially shipped an order and the order expires, MultiSafepay collects the funds for all shipped items and cancels the unshipped items.

  API integration: In your [Ship order](/reference/updateorder) request, set the `amount` for the first partial shipment lower than the total order `amount` (or the total of the `shopping_cart`) in the original [create order](/reference/createorder) request.

  **Multi-shipment**

  MultiSafepay collects for each partial shipment when it is shipped, until all items are shipped, or you or the customer cancels the outstanding items.

  Multi-shipment is disabled by default. To enable, email [sales@multisafepay.com](mailto:sales@multisafepay.com)

  **Integration**

  A unique shipment `order_id` is generated for each partial shipment.

  See API reference – [Update or cancel order](/reference/updateorder) > **Ship order**.

  **Notifications**

  You receive a webhook notification when the <Glossary>order status</Glossary> of each partial shipment changes to **Shipped**.

  The status of the main transaction never changes to **Completed**. It remains **Initialized**, with a flag.

  **Refunds**

  You must must refund partial shipments separately, using the specific **shipment** `order_id`, instead of the original **invoice** `order_id`.

  See API reference – [Refund order](/reference/refundorder).

  ***
</details>

### Update the order status

<details id="how-to-update-the-order-status">
  <summary>How to update the order status</summary>

  <br />

  When you ship the order, you **must** update the <Glossary>order status</Glossary> via the dashboard or your integration from **Completed** to **Shipped** to receive your payout, and to prevent the order from expiring.

  **In your dashboard**

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
  2. Go to **Transactions** > **Transactions overview**, and then click the relevant transaction.
  3. On the **Transaction details** page, under **Order details**, click **Change order status**.
  4. From the **Change status to** list, select **Shipped**.
  5. In the **Memo** field, enter a comment.
  6. Click **OK**.

  **In your backend**

  If you change the order status in your <Glossary>backend</Glossary>, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

  * Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
  * Shopware 5: When you set the order to **Delivered** in your backend.

  For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

  **⚠️ Note:** Some third-party plugins may not support updating the status via our API.

  ***
</details>

## Shopping carts

You can choose whether or not to include a `shopping_cart` object in your [create order](/reference/createorder) request (we normally recommend this for BNPL orders).

See Recipes – <a href="https://docs.multisafepay.com/recipes/display-shopping-cart" target="_blank">Display shopping cart</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

You can also then refund with or without the `shopping_cart`, but for simplicity we recommend matching the refund request to the original order request.

## Terms and conditions

* For <Glossary>direct</Glossary> flows, you must display your terms and conditions in your checkout.
* For <Glossary>redirect</Glossary> flows, MultiSafepay terms and conditions are displayed by default on [payment pages](/docs/payment-pages/).

<br />

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)