---
title: 'Google Pay'
category: 6298bd782d1cf4006032e765
order: 505
hidden: false
slug: google-pay
parentDoc: 62a6ec51d7a8100053916d99
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/GooglePay.svg" width="90" align="right" style="margin: 20px; max-height: 75px"/>

Google Pay™ is a digital wallet for in-app and online payments. Customers can tokenize their payment details in their Google Pay account.

Read how Google Pay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/googlepay)

| Supports | Details |
|---|---|
| **Countries**  | Worldwide <br> See Google Pay – [Countries or regions where you can use Google Pay](https://support.google.com/pay/answer/9023773?hl=en#zippy=%2Cpay-online-or-in-apps).  | 
| **Currencies**  | Multiple  | 
| [Chargebacks](/docs/chargebacks/)  | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Recurring payments](/docs/recurring-payments/) | Yes  |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial <br> Customers receive refunds in their Google Pay account, and they appear on their credit card statement within the next business day.  |
| [Second Chance](/docs/second-chance/) | Yes |

> ℹ️ Notes 
> - By processing Google Pay payments, you agree to the [Google API Terms of Service](https://payments.developers.google.com/terms/sellertos).
> - When integrating Google Pay into your ecommerce platform, you must follow [Google's brand guidelines](https://developers.google.com/pay/api/web/guides/brand-guidelines).
> - For more information, see Google Pay – [Overview](https://developers.google.com/pay/api/web/overview).

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/google-pay-payment-flow.svg" alt="Google Pay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the <<glossary:card scheme>> is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/docs/uncaptured/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. See [Card errors](/docs/card-errors/). | Declined | Declined   |
| **Refunds:** Refund initiated. | Reserved | Reserved   |
| **Refunds:** Refund complete.  | Completed | Completed   |

# Activation 

First apply to MultiSafepay, and then activate in your dashboard. 

<details id="how-to-activate-google-pay"> 
<summary>How to activate Google Pay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
    
    Include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 
 
2. Once approved, sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
3. Go to **Settings**. 
4. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
5. Select the checkbox for the relevant payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- To easily integrate Google Pay using MultiSafepay payment pages (redirect), see API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order.
- To embed Google Pay in your checkout page for the best user experience, see [Google Pay™ direct integration](/google-pay-integration).
- Transactions expire after 1 hour.

### Ready-made integrations
- Supported in most [ready-made integrations](/docs/our-integrations/) (redirect). 
- Exceptions: Magento 2 and WooCommerce. For these, you can use a generic gateway. See the relevant manual.

### Testing
To test Google Pay payments, see [Testing](/docs/testing#wallets).
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
