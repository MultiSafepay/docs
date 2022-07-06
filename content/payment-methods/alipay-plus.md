---
title: 'Alipay+'
category: 6298bd782d1cf4006032e765
order: 502
hidden: true
parentDoc: 62a6ec51d7a8100053916d99
slug: 'alipay-plus'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/AlipayPlus.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

[Alipay+](https://www.alipayplus.com/) is the next generation of Alipay: a leading global payment method that lets customers link their credit card or bank account to a wide range of Asian wallets. It supports online, QR, and contactless POS payments, as well as international money transfers.

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

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/alipay-plus-payment-flow.svg" alt="Alipay+ payment flow" style="display: block;
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

First apply to MultiSafepay, and then activate in your dashboard. 

<details id="how-to-activate-Alipay"> 
<summary>How to activate Alipay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
2. We check your eligibilty and onboard you with Alipay+. We may contact you for information.
3. Once approved, sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
4. Go to **Settings**. 
5. To activate the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

</details>

# Integration

### API
- [Create order](/reference/createorder/) > Wallet order.
- Examples > Alipay+ direct/redirect.
- Transactions expire after 10 minutes on Alipay+, and after 1 hour in our system.
- Required field: Merchant country code

### Ready-made integrations
Coming soon in [our integrations](/docs/our-integrations/).

### Testing
To test Alipay+ payments, see [Testing](/docs/testing#wallets).
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