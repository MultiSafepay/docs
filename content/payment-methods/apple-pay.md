---
title: 'Apple Pay'
category: 6298bd782d1cf4006032e765
order: 503
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'apple-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Apple.svg" width="70" align="right" style="margin: 20px; max-height: 75px"/>

[Apple Pay](https://www.apple.com/apple-pay/) is a leading global payment method that lets customers tokenize their payment details in a digital wallet. It supports Maestro, Mastercard, and Visa, and Dutch bank accounts. Customers can make both online and near-field communication (NFC) payments. 

An additional layer of security is provided by 3D Secure, which requires customers to verify their identity.

Read how Apple Pay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/applepay)

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country) | [Worldwide](https://support.apple.com/en-us/HT207957)  | 
| [Currencies](/docs/currencies/) | [Multiple](https://support.apple.com/en-us/HT207957)  | 
| [Chargebacks](/docs/chargebacks/) | Yes | 
| [Payment pages](/docs/payment-pages/) | Yes (current version only)  |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial <br> Customers receive refunds in their Apple Pay account, and they appear on their credit card statement within the next business day.  |
| [Second Chance](/docs/second-chance/) | Yes |
<br>

> ℹ️ More information 
> See Apple – [How to use Apple Pay](https://support.apple.com/en-us/HT201239).

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/apple-pay-payment-flow.svg" alt="Apple Pay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the <<glossary:card scheme>> is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/docs/uncaptured/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. <br> See [Card errors](/docs/card-errors/). | Declined | Declined   |
| **Refunds:** Refund initiated. | Reserved    | Reserved   |
| **Refunds:** Refund complete.  | Completed  | Completed  |

# Activation 

First, apply to MultiSafepay and then activate Apple Pay in your dashboard.

<details id="how-to-activate-apple-pay"> 
<summary>How to activate Apple Pay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
    
    Include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 

2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
4. Go to **Settings**. 
5. To activate the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### Prerequisites
- Customers must use the Safari browser. 
- An SSL secured connection (HTTPS) is required.

### API
- [Create order](/reference/createorder/) > Wallet order. 
- Examples > Apple Pay direct/redirect.
- Transactions expire after 1 hour. 

### Ready-made integrations
- Apple Pay redirect is supported in most [ready-made integrations](/docs/our-integrations/).
- Exceptions: OsCommerce, VirtueMart, X-Cart, Zen Cart.

### Self-made integration
- [Direct integration](/docs/apple-pay-integration#direct-integration) 
- [Redirect integration](/docs/apple-pay-integration#redirect-integration)

### Testing
To test Apple Pay payments, see [Testing](/docs/testing#wallets).

### Branding
When integrating Apple Pay into your website, you must follow Apple's [branding guidelines](https://developer.apple.com/apple-pay/marketing).
<br>

---

# User guide

## Gateways

American Express, Maestro, Mastercard, and Visa <<glossary:gateways>> are supported. 

## Known errors

For most of our ready-made integrations, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page. 

For our [OpenCart plugin](/docs/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
