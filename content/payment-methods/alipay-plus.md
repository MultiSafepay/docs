---
title: 'Alipay+'
category: 6298bd782d1cf4006032e765
order: 1
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'alipay-plus'
---

> ℹ️ For migrating merchants
> 
> If you are migrating from Alipay, you first need to [activate Alipay+](/docs/alipay-plus#activation) for your account. 
>
> Then, if using:
> - A [ready-made integration](/docs/our-integrations/), activate Alipay+ in your plugin or app
> - An [API integration](/docs/api-integration), use the gateway ID `ALIPAYPLUS`


<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/alipayplus.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.alipayplus.com/" target="_blank">Alipay+</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is the next generation of Alipay: a leading global payment method that lets customers link their card or bank account to a wide range of Asian wallets. It supports online, QR, and contactless <<glossary:POS>> payments, as well as international money transfers.

For Chinese customers, Alipay accounts are verified and linked to their Chinese bank account. Non-Chinese customers can also pay with Alipay using the Tour Pass.

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Worldwide (50 active countries) <br> Primary countries: China, Hong Kong, Indonesia, Macau, Malaysia, Philippines, South Korea, Taiwan, Thailand. | 
| [Currencies](/docs/currencies/)  | EUR, USD (currency conversion in EUR only)  | 
| [Chargebacks](/docs/chargebacks/)  | No, Alipay+ has its own disputes process.  |
| [Discounts](/docs/discounts/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only)  |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds | 
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/alipay-plus-payment-flow.svg" alt="Alipay+ payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Alipay+. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 10 minutes. This status appears after 1 hour in our system. | Expired | Expired |
| The customer cancelled the transaction, or clicked **Back** after selecting Alipay+. | Void | Void |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete.  | Completed | Completed |

# Activation 

1. Email a request to <sales@multisafepay.com> 
   We check your eligibility and onboard you with Alipay+. We may contact you for information.
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
3. To activate the payment method for:
- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Wallet order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Alipay(+) direct/redirect**. 
  Set `gateway` to `ALIPAYPLUS`, and `type` to `direct` or `redirect`.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- Transactions expire after 10 minutes on Alipay+, and after 1 hour in our system.
- Required field: Merchant country code

### Ready-made integrations
Coming soon in [our integrations](/docs/our-integrations/).

### Testing
To test Alipay+ payments, see Testing payment methods - [Wallets](/docs/testing#wallets).
<br>

---
# User guide

## Amount limits

Minimum and maximum amounts apply to some wallets.

<details id="amount-limits">
<summary>See all amount limits</summary>
<br>

| Wallet | Currency | Minimum | Maximum |
|---|---|---|---|
| AlipayHK | Hong Kong dollar (HKD) | 0.10 | HKD 9,999,999  |
| Dana | Indonesian rupiah (IDR) | 300 | 20,000,000 |
| GCash | Philippine peso (PHP) | 1 | PHP 100,000 |
| KakaoPay | South Korean won (KRW) | 50 | 2,000,000 |
| TnGD | Malaysian ringgit (MYR) | 0.10 | 9,999,999 |
| TrueMoney | Thai baht (THB) | 1  | - |

</details>

## Branding requirement

Alipay+ requires all merchants to display the Alipay+ partner logo **and** the logos of at least 3 of its [supported wallets](#wallets) in every payment interface, e.g. [payment pages](/docs/payment-pages/), [payment components](/docs/payment-components/), [FastCheckout](/docs/fastcheckout/). 

#### Example

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Alipay+Logos.png" align ="center"/>

For all logos, see MultiSafepay GitHub – <a href="https://github.com/MultiSafepay/MultiSafepay-icons" target="_blank">Icons</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Wallets

Alipay+ aggregates a wide range of Asian wallets. 

<details id="supported-wallets">
<summary>Supported wallets</summary>
<br>

- Alipay China and AlipayHK
- Boost
- BPI
- Dana
- Ezlink
- KakaoPay
- RLP
- Touch 'n Go
- Truemoney GCash

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
