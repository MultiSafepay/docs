---
title: 'Google Pay'
category: 6298bd782d1cf4006032e765
order: 6
hidden: false
slug: google-pay
parentDoc: 62a6ec51d7a8100053916d99
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/googlepay.svg" width="90" align="right" style="margin: 20px; max-height: 75px"/>

Google Pay™ is a digital wallet for in-app and online payments. Customers can tokenize their payment details in their Google Pay account.

Read how Google Pay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/googlepay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Worldwide <br> See Google Pay – <a href="https://support.google.com/pay/answer/9023773?hl=en#zippy=%2Cpay-online-or-in-apps" target="_blank">Countries or regions where you can use Google Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.  | 
| [Currencies](/docs/currencies/)  | AED, AUD, BRL, CAD, CHF, CLP, CNY, COP, CZK, DKK, EUR, GBP, HKD, HRK, HUF, ILS, INR, ISK, JPY, KRW, MXN, MYR, NOK, NZD, PEN, PHP, PLN, RON, RUB, SEK, SGD, THB, TRY, TWD, UAH, USD, VEF, ZAR | 
| [Chargebacks](/docs/chargebacks/)  | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Recurring payments](/docs/recurring-payments/) | Yes  |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial <br> Customers receive refunds in their Google Pay account, and they appear on their card statement within the next business day.  |
| [Second Chance](/docs/second-chance/) | Yes |

> ℹ Notes 
>
> - By processing Google Pay payments, you agree to the <a href="https://payments.developers.google.com/terms/sellertos" target="_blank">Google API Terms of Service</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
> - When integrating Google Pay into your ecommerce platform, you must follow <a href="https://developers.google.com/pay/api/web/guides/brand-guidelines" target="_blank">Google's brand guidelines</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
> - For more information, see Google Pay – <a href="https://developers.google.com/pay/api/web/overview" target="_blank">Overview</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/google-pay-payment-flow.svg" alt="Google Pay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the <<glossary:card scheme>> is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/docs/uncleared/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. See [Card errors](/docs/card-errors/). | Declined | Declined   |
| **Refunds:** Refund initiated. | Reserved | Reserved   |
| **Refunds:** Refund complete.  | Completed | Completed   |

# Activation 

To activate Google Pay, you must have [card payments](/docs/card-payments/) activated for your account.

<details id="how-to-activate-cards"> 
<summary>How to activate cards</summary>
<br>

1. Email a request to activate cards to <risk@multisafepay.com> 
    
    Include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 

2. We check your eligibility and if approved, activate the payment method for your account. 
3. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
4. To activate the payment method for:
- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
5. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <support@multisafepay.com>

</details>

Then, apply to MultiSafepay for Google Pay, and activate it in your dashboard. 

<details id="how-to-activate-google-pay"> 
<summary>How to activate Google Pay</summary>
<br>

1. Email a request to <sales@multisafepay.com> 
    
    Include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 
 
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
    - All websites, go to **Settings** > **Payment methods**.
    - A specific website:
      - Go to **Websites**, and then click the relevant website.
      - On the **Website profile** page, under **Payment methods**, click **Select payment methods**.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

</details>

# Integration

### API
- To easily integrate Google Pay using [payment pages](/docs/payment-pages/) (<<glossary:redirect>> flow), see API reference – [Create order](/reference/createorder/) > Wallet order.
- For Google Pay to display on [payment pages](/docs/payment-pages/) and in [payment components](/docs/payment-components), you must have [card payments](/docs/card-payments/) activated for your account. 

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Google Pay direct/redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- To embed Google Pay in your checkout page for the best user experience, see [Google Pay™ direct integration](/docs/google-pay-direct/).
- Transactions expire after 1 hour.

### Ready-made integrations
- Supported in most [ready-made integrations](/docs/our-integrations/) (<<glossary:redirect>>). 
- Exceptions: Shopware 5. For this one, you can use a generic gateway. See the relevant manual.

### Testing
To test Google Pay payments, see Testing payment methods - [Wallets](/docs/testing#wallets).
<br>

---

# User guide

## Browsers

<details id="supported-browsers">
<summary>Supported browsers</summary>
<br>

- Apple Safari
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Opera
- UCWeb UC Browser

</details>

## Gateways

<details id="supported-gateways">
<summary>Supported gateways</summary>
<br>

- Supported: Maestro, Mastercard, and Visa 
- Not supported: American Express 

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
