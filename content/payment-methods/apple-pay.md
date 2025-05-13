---
title: 'Apple Pay'
category: 6298bd782d1cf4006032e765
order: 4
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'apple-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/applepay.svg" width="70" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.apple.com/apple-pay/" target="_blank">Apple Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a leading global payment method that lets customers tokenize their payment details in a digital wallet. It supports American Express, Maestro, Mastercard, Visa, and Dutch bank accounts. Customers can make both online and near-field communication (NFC) payments. 

An additional layer of security is provided by 3D Secure, which requires customers to verify their identity.

Read how Apple Pay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/applepay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country) | <a href="https://support.apple.com/en-us/HT207957" target="_blank">Worldwide</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>  | 
| [Currencies](/docs/currencies/) | AED, AUD, BRL, CAD, CHF, CLP, CNY, COP, CZK, DKK, EUR, GBP, HKD, HRK, HUF, ILS, INR, ISK, JPY, KRW, MXN, MYR, NOK, NZD, PEN, PHP, PLN, RON, RUB, SEK, SGD, THB, TRY, TWD, UAH, USD, VEF, ZAR <br> For more information, see Apple - <a href="https://support.apple.com/en-us/HT207957" target="_blank">Multiple</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. | 
| [Chargebacks](/docs/chargebacks/) | Yes | 
| [Payment pages](/docs/payment-pages/) | Yes (current version only)  |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial <br> Customers receive refunds in their Apple Pay account, and they appear on their card statement within the next business day.  |
| [Second Chance](/docs/second-chance/) | Yes |
<br>

> ℹ More information 
>
> See Apple – <a href="https://support.apple.com/en-us/HT201239" target="_blank">How to use Apple Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/apple-pay-payment-flow.svg" alt="Apple Pay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected for 3D Secure authentication, or the <<glossary:card scheme>> is authorizing the transaction. | Initialized | Initialized |
| The card scheme authorized the transaction, but we've flagged it as potentially fraudulent. <br> Review it and then [manually capture or decline](/docs/uncleared/). | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled payment. <br> See [Card errors](/docs/card-errors/). | Declined | Declined   |
| **Refunds:** Refund initiated. | Reserved    | Reserved   |
| **Refunds:** Refund complete.  | Completed  | Completed  |

# Activation 

To activate Apple Pay, you must have [card payments](/docs/card-payments/) activated for your account.

<details id="how-to-activate-cards"> 
<summary>How to activate cards</summary>
<br>

1. Email a request to activate cards to <risk@multisafepay.com> 
    
    Include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 

   We check your eligibility and if approved, activate the payment method for your account. 
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
    - All websites, go to **Settings** > **Payment methods**.
    - A specific website:
      - Go to **Websites**, and then click the relevant website.
      - On the **Website profile** page, under **Payment methods**, click **Select payment methods**.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <support@multisafepay.com>

</details>

Then, apply to MultiSafepay for Apple Pay, and activate it in your dashboard.

<details id="how-to-activate-apple-pay"> 
<summary>How to activate Apple Pay</summary>
<br>

1. Email a request to activate Apple Pay to <risk@multisafepay.com> 
    
    Include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 

   We check your eligibility and if approved, activate the payment method for your account. 
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

</details>

# Integration

### Prerequisites
- Customers must use the Safari browser. 
- An SSL secured connection (HTTPS) is required.

### Direct integration
For <<glossary:direct>> integration with an [API integration](/docs/api-integration/), see [Apple Pay direct integration](/docs/apple-pay-direct/).

### API
- For <<glossary:redirect>> integration, see API reference – [Create order](/reference/createorder/) > Wallet order. 

  <details id="how-to-detect-apple-pay-on-the-customers-device"> 
  <summary>How to detect Apple Pay on the customer's device</summary>
  <br>

  If a customer uses an unsupported device to navigate to an Apple Pay payment page, they won't be able to complete the payment. To prevent this, before creating the payment page, check whether Apple Pay is supported on the customer's device.

  ```javascript
  try {
      if (window.ApplePaySession && ApplePaySession.canMakePayments()) {
      console.log('Apple Pay available');
      // Create an Apple Pay payment page from your server
      }
      } catch (error) {
      console.debug('An error occurred while verifying if Apple Pay is available:', error);
      }
  ```
  
  ---

  </details>

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Apple Pay direct/redirect**.

  <div style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif"
    alt="MultiSafepay Sandbox Test Process GIF"
    style="width: 40%; height: auto;"
  />
  </div>

  </details>

- Transactions expire after 1 hour. 
- For Apple Pay to display on [payment pages](/docs/payment-pages/) and in [payment components](/docs/payment-components), you must have [card payments](/docs/card-payments/) activated for your account. 

### Ready-made integrations
- Apple Pay redirect is supported in most [ready-made integrations](/docs/our-integrations/).
- Exceptions: OsCommerce, VirtueMart, X-Cart, Zen Cart.

### Testing
To test Apple Pay payments, see Testing payment methods - [Wallets](/docs/testing#wallets).

### Branding
When integrating Apple Pay into your website, you must follow Apple's <a href="https://developer.apple.com/apple-pay/marketing" target="_blank">branding guidelines</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
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
