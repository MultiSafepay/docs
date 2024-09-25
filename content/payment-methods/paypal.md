---
title: 'PayPal'
category: 6298bd782d1cf4006032e765
order: 8
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'paypal'
---

> ⚠️ Action required
> 
> If you have an existing PayPal account connected to your MultiSafepay dashboard, we recommend you to [upgrade to the latest PayPal API](/docs/paypal#activation) as soon as possible.
> 
> Under the latest PayPal API, you can:
> 
> - Add  an [invoice_id](/docs/paypal#integration) in your request.
> - Add a [shopping cart](/docs/paypal#integration) in your request.
> - Integrate the [PayPal smart button](/docs/paypal-direct). 

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/paypal.svg" width="125" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.paypal.com/nl/home" target="_blank">PayPal</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a leading global payment method that lets customers pay by credit or debit card or create a digital wallet linked to multiple payment methods.

Read how PayPal can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/paypal" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Worldwide  | 
| [Currencies](/docs/currencies/)  | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HRK, HUF, JPY, MXN, MYR, NOK, NZD, PHP, PLN, RUB, SEK, SGD, THB, TRY, TWD, USD <br> For more information, see PayPal – <a href="https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies/" target="_blank">PayPal supported currencies</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. | 
| [Chargebacks](/docs/chargebacks/)  |  Yes  |
| [Payment components](/docs/payment-components/) | Yes | 
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial (see guidance below) | 
| [Second Chance](/docs/second-chance/) | Yes | 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/paypal-payment-flow.svg" alt="PayPal payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

> ℹ **Note** 
>
> MultiSafepay does **not** collect funds for PayPal transactions.

# Payment statuses 

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to PayPal. | Initialized | Initialized |
| Awaiting the customer to pay in their PayPal account, **or** <br> PayPal is authorizing the transaction, **or** <br> You may need to enable the currency and then authorize the payment in your PayPal business account.  | Uncleared | Initialized |
| PayPal has collected payment. | Completed | Initialized |
| The customer cancelled the payment in PayPal. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 14 days. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Initialized |
| **Refunds:** Refund complete.  | Completed | Initialized |
| Refund declined. | Declined | Declined |
| PayPal is authorizing the refund, **or** <br> There are not enough funds in your PayPal business account to process the refund. <br> For more information, see your PayPal business account. | Uncleared | Initialized   |

# Activation

To activate PayPal, follow these steps:

<details id="how-to-activate-your-paypal-account">
<summary>How to configure your PayPal account</summary>
<br>

1. Email a request to <support@multisafepay.com>
2. After we confirm activation, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. Go to **Settings** > **Payment methods**
4. In the **PayPal** tab, click on **Set up PayPal** button <br> You are redirected to PayPal to sign in to your PayPal business account.                              
5. Grant PayPal access to connect with your MultiSafepay account.
6. Your **PayPal Merchant ID** is now displayed in your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 

If your **PayPal Merchant ID** isn't displayed in your dashboard, you can add it manually.

<details id="how-to-configure-your-paypal-account">
<summary> How to add your PayPal Merchant ID</summary>
<br>

1. Sign in to your business account at <a href="https://www.paypal.com" target="_blank">PayPal</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. On the navigation menu > mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Business information** tab, copy your PayPal Merchant ID.
4. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
5. To set manually your PayPal Merchant ID:

- Go to **Settings** > **Payment methods**> **PayPal ** tab.
- Click **add PayPal ID** link at the bottom of **PayPal** tab.
- In the **PayPal merchant ID** field, paste your PayPal Merchant ID.
- Click **Save changes**.

✅ PayPal has been successfully configured in your MultiSafepay account.

> 📘 **Note:** 
> 
> If you already have a PayPal account connected to MultiSafepay dashboard, we recommend upgrading to the latest PayPal API as soon as possible by following all the steps above. No other actions are required after this step.

We strongly recommend [testing transactions](/docs/testing/) before processing live payments.

</details>

</details>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Wallet order. 

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **PayPal direct/redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- A `shopping_cart` object can be included in your [create order](/reference/createorder) request, see Recipe – <a href="https://docs.multisafepay.com/recipes/include-shopping_cart-in-order" target="_blank">Include shopping_cart in order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

- An `invoice_id`  can be included in your [create order](/reference/createorder) request, which appears in the transaction history.<br> **Note:** If no `invoice_id` is set, the `order_id` defaults to `invoice_id`.

- Transactions expire after 14 days.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/).

### Testing
To test PayPal payments, see Testing payment methods - [Wallets](/docs/testing#wallets).
<br>

---

# User guide

## PayPal Seller Protection

PayPal Seller Protection covers you in the event of claims, chargebacks, or <<glossary:reversals>> due to unauthorized purchases or items the customer didn't receive. You are covered for the full amount of all eligible transactions.

To be eligible, for specific countries, transaction requests must contain the correct `state` in the `customer_address`. 

- For a list of the countries, see PayPal API – <a href="https://developer.paypal.com/api/rest/reference/state-codes/" target="_blank">State codes</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- For more information, see PayPal – <a href="https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156" target="_blank">What is Seller Pretection</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

**⚠️ Note:** For disputes and disbursement information, further details appear in a transaction note  in your dashboard under  **Transaction overview** > **Transaction summary**.

## Refunds

Refunds are only processed if there are enough funds in your PayPal business account. Otherwise, PayPal issues an <a href="https://www.paypal.com/us/smarthelp/article/what-is-an-echeck-faq1082" target="_blank">eCheck</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 

To avoid PayPal cancelling the refund, in your PayPal account, authorize PayPal to withdraw funds from another bank account instead. 

For support, contact PayPal – <a href="https://www.paypal.com/us/smarthelp/home" target="_blank">Help Center Home</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Shopping carts

You can include shopping cart in your [create order](/reference/createorder/) request, which is displayed on the PayPal checkout page, and PayPal communications.

## Your logo in PayPal's checkout

You can no longer display your logo; your website name is displayed in the PayPal checkout.


## Troubleshooting

If you encounter any issues with PayPal, for example a system error, do the following checks:

- [You have upgraded to the latest PayPal API](/docs/paypal#activation)
- PayPal is activated for your account


<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
