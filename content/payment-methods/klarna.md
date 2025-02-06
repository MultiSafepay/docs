---
title: 'Klarna'
category: 6298bd782d1cf4006032e765
order: 3
hidden: false
parentDoc: 62bd75142e264000a66d62b5
slug: 'klarna'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/klarna.svg" width="150" align="right" style="margin: 20px 20px 20px 40px; max-height: 75px"/>

<a href="https://www.klarna.com/" target="_blank">Klarna</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a flexible online payment method that lets customers pay now, in 30 days (Pay Later 30), or in 3 interest-free installments. It also offers financing. Klarna bears the risk and guarantees <<glossary:settlement>>.

Read how Klarna can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/klarna" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Austria, Belgium, Denmark, Finland, France, Germany, Italy, Netherlands, Norway, Portugal, Spain, Sweden, UK | 
| [Currencies](/docs/currencies/)  | DKK, EUR, GBP, NOK, SEK | 
| [Chargebacks](/docs/chargebacks/)  | No  | 
| [Discounts](/docs/discounts/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds | 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/klarna-payment-flow.svg" alt="Klarna payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Klarna. You can still cancel with Klarna using the reservation number. | Initialized   | Initialized  |
| Klarna has authorized the transaction and the funds are awaiting capture. You can no longer cancel; you can only refund. | Completed  | Uncleared  |
| **⚠️ Note:** To capture the funds, [manually change the order status to Shipped](#shipment). | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| The transaction expired after 1 day or you didn't [change the order status to shipped](#shipment) within 28 days. <br> See [Expired orders](#expired-orders).  | Expired    | Expired    |
| Klarna authorized the transaction, but either you or the customer cancelled it before capture. | Void   | Void |
| Klarna declined the transaction. <br> Only the customer can contact Klarna to find out why (for privacy and compliance reasons). <br> For merchant support, email <klarna@multisafepay.com> | Declined | Declined |
| **Refunds:** Refund initiated. | Initialized | Completed |
| **Refunds:** Refund complete.  | Completed | Completed |

# Activation 

How to activate Klarna for your MultiSafepay account:

<details id="test-account"> 
<summary>Test account</summary>
<br>

1. Go to <a href="https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/#accessing-the-test-merchant-portal" target="_blank">Klarna</a><i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and click **Log in**.
2. Click **Select environment** > **Playground** to create a test account. Click **Sign Up**.
3. Follow the intructions to complete the registration process.
4. In the Klarna main panel, go to **Settings** and click **Generate new Klarna API credentials** to generate a test username and password.
5. Email these credentials to <support@multisafepay.com>.
6. We will activate your Klarna test account for your MultiSafepay test account.

You can test Klarna payments via the Klarna Portal on your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

</details>
<details id="live-account"> 
<summary>Live account</summary>
<br>

1. To sign up for a live Klarna account, email your Klarna account manager or <distribution.partner.leads@klarna.com>.
2. In your email, include the following details:
   - MultiSafepay as your payment service provider.
   - The websites and countries for which you want to activate Klarna.
3. Sign an agreement with Klarna. This agreement includes the pricing details.
4. We will activate Klarna for your MultiSafepay account. 
5. If you are using a ready-made integration, activate Klarna in your <<glossary:backend>>.

For questions, see Klarna – <a href="https://www.klarna.com/nl/klantenservice" target="_blank">Klantenservice</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

</details>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > BNPL order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Klarna direct/redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- A `shopping_cart` object is required for all BNPL orders. See Recipes –  <a href="https://docs.multisafepay.com/recipes/include-shopping_cart-in-order" target="_blank">Include shopping_cart in order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- Transactions expire after 1 day.
- For <<glossary:direct>> orders, you must display your terms and conditions in your checkout.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/) (<<glossary:redirect>>).

### Testing
To test Klarna payments, see Testing payment methods - [BNPL methods](/docs/testing#bnpl-methods).
<br>

---

# User guide

## Addresses

Different billing and shipping addresses are supported.

## Branding

<details id="how-to-add-your-logo-to-klarna-invoices">
<summary>How to add your logo to Klarna invoices</summary>
<br>

1. Sign in to your Klarna Merchant Account, and then go to **Branding**.
3. Under **Logo**, upload a .png or .jpeg logo. 
    - For best results, use a square image with a transparent background. 
    - Resolution 180x180 px or higher

</details>

<details id="how-to-manage-your-brand-information">
<summary>How to manage your brand information</summary>
<br>

Under **Brand information**, you can set up and manage your brand including:
- Brand name
- Home page
- Instagram URL
- Facebook URL

For support, see Klarna – <a href="https://www.klarna.com/nl/klantenservice/" target="_blank">Klantenservice</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 

</details>

## Collection period

If a customer's return takes too long to verify, you can pauze the collection period for 2-4 weeks. 

Call Klarna on +31 208082853 or email Klarna Sales at <verkoop@klarna.com>

## Expired orders

Orders may expire if you don't change the order status to **Shipped** within 28 days. 

<details id="how-to-handle-expired-orders"> 
<summary>How to handle expired orders</summary>
<br>

You can send the customer a payment link from the existing order or a new order.

**Existing order**

1. Sign in to your MultiSafepay dashboard.
2. Go to **Transactions** > **Transaction overview**, and then select the expired transaction.  
3. Click **Payment link**, and then click **Duplicate this order**.
4. On the **Payment link generator** page, click **Generate payment link**. 
5. Send the payment link to the customer. 

**New order**

1. [Create a new order](/reference/createorder/) > BNPL order.  
See also Examples > Klarna redirect.
2. [Ship the order](/reference/updateorder/) > Ship order.
3. Send the payment link to the customer.

</details>

## Disputes

A dispute is when you and a customer disagree about an order:

- Goods, e.g. the customer returns all or part of the order, or the goods were faulty when delivered
- Payments, e.g. invoicing errors, or the customer paid Klarna instead of you
- Other, e.g. insolvency, or bankruptcy

Klarna provides support for resolving disputes. 
For a step-by-step overview, see Klarna – <a href="https://docs.klarna.com/disputes/" target="_blank">How to handle disputes at Klarna</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

The easiest way to handle disputes is using the Disputes app in the Klarna Merchant Portal. 

<details id="how-to-connect-to-the-klarna-merchant-portal">
<summary>How to connect to the Klarna Merchant Portal</summary>
<br>
  
You'll receive an email from Klarna inviting you to activate your portal account. The link expires within 7 days and is only usable once. 

If your link has expired or you haven't received an email, email <support@multisafepay.com> 

1. In the email, click **Activate account**.
2. Read the Merchant Portal Agreement, agree to the terms and conditions, and then click **Continue**.
3. Enter a password, and then click **Update password**.
4. Enter your first and last names, and then click **Update profile**.
5. To sign in for the first time, enter your email address and the password you just created, and then click **Log in**.

**⚠️ Note:** If viewing orders in the portal, you must still manually change the order status to Shipped to trigger the invoicing process and receive payment.

</details>

<details id="how-to-set-up-two-factor-authentication">
<summary>How to set up two-factor authentication</summary>
<br>

If you want to increase the security of your Klarna Merchant Portal, set up two-factor authentication with the Google Authenticator app.

1. Under **To-dos**, click **Activate two-factor authentication**. 
2. In the dialog, click **Start the setup**.
3. Open the Google Authenticator app and scan the QR code. 
4. Enter the one-time authorization code from the app, and then click **Set up authentication**.

</details>

<details id="how-to-sign-up-for-the-disputes-app">
<summary>How to sign up for the Disputes app</summary>
<br>

To sign up to use the Disputes app, follow these steps:

1. Sign in to the <a href="https://eu.portal.klarna.com/" target="_blank">Klarna Merchant Portal</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. In the side menu, click **Disputes**.
3. Select an email address and preferred language for receiving dispute-related emails, e.g. reminders.
4. Agree to the terms and conditions. 
5. Click **Sign up**. 

Klarna will send you an email when the first dispute appears in the app. 

**Using the Disputes app**

The side menu contains three pre-set filters to view:

- All disputes
- Unauthorized disputes
- Disputes expiring soon

See Klarna – <a href="https://docs.klarna.com/disputes/disputes-app-in-merchant-portal/" target="_blank">Disputes App in Merchant Portal</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for detailed information on:

- Searching and filtering disputes
- Exporting reports
- Dispute statuses
- Managing settings
- Responding to disputes
- Accepting losses

</details>

## Gift cards

When paying with a gift card and Klarna, customers must enter the gift card details **before** placing their order, i.e. on your checkout page. This is because Klarna collects and require precise order specifications. Our platform would interpret the gift card as a discount and generate incorrect order information, e.g. tax calculations.

You are solely responsible for this in your integration.

## Klarna gateway 

Klarna makes your ecommerce platform available in their merchant portal, where your credentials are generated. Use your credentials to configure the Klarna <<glossary:gateway>> for your MultiSafepay account. 

For questions about your Klarna integration and the connection with your MultiSafepay account, email <integration@multisafepay.com>

<details id="known-error">
<summary>Known error</summary>
<br>

If you receive a `code:BAD_VALUE, Bad value: order_lines[0].reference` error from Klarna, try using shorter SKU numbers, e.g. fewer than 9 characters. 

</details>

## Klarna reference numbers

For every transaction, Klarna generates two reference numbers:

- Reservation number for before shipment
- Invoice number for after shipment

Both reference numbers appear in the **Transaction details** page in your dashboard.

## Refunds

To refund a Klarna transaction, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Navigate to **Transactions / Transactions Overview** and find the transaction you want to refund, or search for the transaction you want to refund by using the search bar.
3. Click on the transaction to go to the transaction details page.
4. On the right side of the page are the order details and a blue Refund button.
5. In this section you can remove order lines or refund the complete order.

## Shipment

### Change the order status

When you ship the order, you **must** manually change the [order status](/docs/payment-statuses/) from **Completed** to **Shipped**, which:

- Captures the funds
- Triggers sending the invoice to the customer
- Prevents the order from expiring

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

If you change the order status in your backend, the following [ready-made integrations](/docs/our-integrations/) pass the updated status to your dashboard automatically:

- Lightspeed, Magento 2, and WooCommerce: When you set the order to **Shipped** in your backend.
- Shopware 5: When you set the order to **Delivered** in your backend.

For other ready-made integrations, make an [update order](/reference/updateorder/) API request.

**⚠️ Note:** Some third-party plugins may not support updating the status via our API.

</details>

### Extend the shipping period

If you cannot ship the order within 28 days, you can extend the time period for up to 180 days in segments.

If the order is not captured during this time, the <<glossary:order status>> and <<glossary:transaction status>> change to **expired**.

<details id="how-to-extend-the-shipping-period"> 
<summary>How to extend the shipping period</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, under **Order summary**, click **Extend**.

</details>

## Surcharges  

Due to changes to the Wet op het consumentenkrediet, merchants who apply [surcharges](/docs/surcharges/) to <<glossary:BNPL>> methods are now deemed credit providers under article 7:57 of the Burgerlijk Wetboek. This requires a permit from the Authority for Financial Markets (AFM).  

We therefore strongly recommend **not** applying surcharges. 

For more information, see Klarna – <a href="https://www.klarna.com/nl/zakelijk/webwinkelsupport/welk-bedrag-kan-ik-maximaal-doorberekenen-aan-mijn-klant/" target="_blank">Welk bedrag kan ik maximaal doorberekenen aan mijn klant?</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
