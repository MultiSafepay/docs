---
title: 'Amazon Pay'
category: 6298bd782d1cf4006032e765
order: 503
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'amazon-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/amazonpay.svg" width="150" align="right" style="margin: 20px; max-height: 100px"/>

<a href="https://pay.amazon.eu/" target="_blank">Amazon Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a payment method that Amazon customers can use to purchase goods on other sites using their Amazon account. Amazon customers can use any of their stored addresses or payment methods, such as credit or debit cards.

<!-- Read how Amazon Pay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/amazon-pay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> -->

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country) | Austria, Belgium, Cyprus, Denmark, France, Germany, Hungary, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain, Sweden, and Switzerland | 
| [Currencies](/docs/currencies/)  | AUD, CHF, DKK, EUR, GBP, HKD, JPY, NOK, NZD, SEK, USD, ZAR | 
| [Chargebacks](/docs/chargebacks/)  | Yes |
| [Discounts](/docs/discounts/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only)  |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds | 
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/amazon-pay-payment-flow.svg" alt="Amazon Pay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

> ℹ **Note** 
> MultiSafepay does **not** collect funds for Amazon Pay transactions.

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Amazon Pay. | Initialized | Initialized |
| The customer has confirmed the order. | Initialized | Completed |
| Amazon Pay has declined the order. | Declined | Declined |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete.  | Completed | Completed |

# Activation 

1. Email a request to <risk@multisafepay.com> 
  We check your eligibility and if approved, activate the payment method for your account. 
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. Go to **Settings** > **Payment methods**.
4. Under **Additional payment methods**, click **Amazon** > **Merchant registration**. 
  You are redirected to create an Amazon Payments merchant account at Amazon Pay – <a href="https://pay.amazon.com/signup" target="_blank">Sign up</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
5. Enter the required information to create an account.
  Amazon sends you a confirmation email.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

# Integration

Our integration with Amazon Pay supports an additional payment button. 
For more information, see Amazon Pay – <a href="https://developer.amazon.com/docs/amazon-pay-recurring-apb-checkout/additional-payment-button-overview.html" target="_blank">Additional payment button</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

### API
- See API reference – [Create order](/reference/createorder/) > Wallet order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Amazon Pay direct/redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- Transactions expire after 24 hours.

### Ready-made integrations

Coming soon in our [integrations](/docs/our-integrations/).

<!--Supported in:

- Magento 2
- Magento 1
- OpenCart
- Prestashop 1.7
- Prestashop 1.6
- Shopware 5
- Shopware 6
- WooCommerce

-->

### Testing
To test Amazon Pay payments, see Testing – [Wallets](/docs/testing#wallets).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
