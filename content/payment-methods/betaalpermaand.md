---
title: 'Betaal per Maand (Deprecated)'
category: 6298bd782d1cf4006032e765
order: 0
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: betaal-per-maand
---

 
⚠️ Note:
 
>Santander betaal per maand is discontinued as from 01/01/2024, and no new orders will be accepted. Existing orders will be handled up to 31/03/2024, after which no operations are possible anymore.


<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/betaalplan-nl.svg" width="200" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.santander.nl/veelgestelde-vragen/betaal-per-maand" target="_blank">Betaal per Maand</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a MultiSafepay <<glossary:BNPL>> method in collaboration with Santander. It is intended for large amounts paid as a one-off payment or in monthly installments. Santander bears the risk and guarantees <<glossary:settlement>>.

Read how Betaal per Maand can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/betaalpermaand-santander" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Netherlands  | 
| [Currencies](/docs/currencies/)  | EUR  | 
| [Chargebacks](/docs/chargebacks/)  | No |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions)  |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/betaalpermaand-payment-flow.svg" alt="Betaal per maand payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Santander. | Initialized   | Initialized  |
| The customer has completed the pre-form and Santander is authorizing the transaction. | Uncleared | Initialized |
| Santander has authorized the transaction and the funds are awaiting capture. <br> You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| **⚠️ Note:** To capture the funds, when you ship the <<glossary:order>> you must manually [change the order status to Shipped](#shipment) and send us the [track-and-trace code](#track-and-trace-codes).  | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| Santander declined the transaction. <br> Only the customer can contact them to find out why (for privacy and compliance reasons). | Declined   | Declined   |
| You cancelled the transaction before capture.   | Void   | Void   |
| The customer didn't complete payment or the funds weren't captured within 1 day. | Expired | Expired  |
| **Refunds:** Refund initiated. | Reserved    | Reserved   |
| **Refunds:** Refund complete.  | Completed      | Completed   |

# Activation 

You must:

- Have a [MultiSafepay account](/docs/getting-started-guide/)
- Be registered with a Dutch Chamber of Commerce (no exceptions)
- Have an annual turnover of more than 500,000 EUR (unless agreed otherwise with Betaal per Maand)
- Sell products or services to European citizens with a residential or delivery address in the Netherlands (no exceptions)
- Connect to MultiSafepay via our API or [ready-made integrations](/docs/our-integrations/)

To activate:

1. Email a request to <sales@multisafepay.com>
2. In the request, let us know if you already have a Santander account. If you don't, we'll submit an application for you. 
3. We check your eligibility and type of connection. 
4. Once approved, we activate the payment method for your account.

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > BNPL order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Betaal per Maand direct/redirect**.
  Set `type` to `direct` or `redirect`.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- A `shopping_cart` object is required for all BNPL orders. See Recipes – <a href="https://docs.multisafepay.com/recipes/include-shopping_cart-in-order" target="_blank">Include shopping_cart in order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

- Transactions expire after 1 day.
- For <<glossary:direct>> orders, you must display your terms and conditions in your checkout. 

### Ready-made integrations
- Supported in most [ready-made integrations](/docs/our-integrations/).
- Exceptions: Shopify, OsCommerce, Vue Storefront, Zen Cart

### Testing
- You cannot test Betaal per Maand in your MultiSafepay test account. 
- When activating this method in your live MultiSafepay account, you can test it before going live.
<br>

---

# User guide

## Amount limits

- Minimum order amount: 250 EUR
- Maximum order amount: 8000 EUR

## Cancellation

To cancel an order, email <annuleren@santander.com> with the following details:
- Customer's first and last name
- Order ID
- Transaction ID (MultiSafepay's transaction reference number)

**⚠️ Note:** You cannot cancel a Betaal per Maand order via your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Collection period

If the return process takes too long to verify, you can pause the collection period for 2–4 weeks. 

Have your Betaal per Maand client number ready, and email <klantenservice@santander.nl>

## Gift cards

When paying with a gift card and Betaal per Maand, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. 

This is because Santander collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Known error

The customer's first and last name, and the delivery details must be at least 2 characters long. Anything shorter can cause errors. 

We recommend always requiring full names, not initials, abbreviations, or acronyms.

## Shipment

### Changing orders before shipment

You can still change an order between approval from Santander and shipment.

<details id="how-to-change-orders-before-shipment">
<summary>How to change orders before shipment</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Order summary**, click **Change order status**.
4. Change the status of the initial order to **Shipped**, and then add a **Memo**.
5. Refund the required amount [in full or in part](/docs/refund-payments/). 

You cannot increase the amount of the initial order by default. Email a request to <sales@multisafepay.com>

</details>

### Changing the order status

When you ship the order, you **must** manually change the [order status](/docs/payment-statuses/) from **Completed** to **Shipped** to:

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

- Magento 2 and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

**⚠️ Note:**Some third-party plugins may not support updating the status via our API.

</details>

### Providing track-and-trace codes

<details id="how-to-provide-track-trace-to-multisafepay">
<summary>How to provide track-and-trace codes to MultiSafepay</summary>
<br>

You can provide track-and-trace codes to MultiSafepay:

- In your dashboard when you change the order status to **Shipped**, **or**  
- Via our API – [Update order](/reference/updateorder/) > Ship order
</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
