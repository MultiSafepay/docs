---
title: 'iDEAL'
category: 6298bd782d1cf4006032e765
order: 11
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'ideal'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/ideal.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

> ⚠️ Note:
> 
> We are gradually migrating to iDeal 2.0, an enhanced version of this payment method. 
> 
> Changes:
> 
> - For users of our redirect solution:  
>   Our **payment page** no longer displays an issuer list when iDeal is selected.  
>   Instead, the customer is redirected to the iDeal environment to select the issuer. 
> - For users of our direct solution (via API):  
>   The issuer is selected within the iDeal environment. The parameter  `issuer_id` is no longer required for requests with type  `direct`.

<a href="https://www.ideal.nl/en/" target="_blank">iDEAL</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is the leading payment method in the Netherlands and links all major Dutch retail banks. Customers pay via mobile banking app, [QR code](#ideal-qr), or in their own online banking environment. Once a payment is completed, the customer cannot reverse it and iDEAL guarantees <<glossary:settlement>>.

Read how iDEAL can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/ideal" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Netherlands  | 
| [Currencies](/docs/currencies/)  | EUR | 
| [Chargebacks](/docs/chargebacks/)  | No |
| [Payment components](/docs/payment-components/) | Yes | 
| [Payment pages](/docs/payment-pages/) | Yes (Banking: Current and deprecated versions, QR: Current only) |
| [Recurring payments](/docs/recurring-payments/) | Yes (banking only) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/ideal-payment-flow.svg" alt="iDEAL payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses   

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via their bank. | Void   | Void/Cancelled   |
| iDEAL processing error. | Declined   | Declined   |
| The customer didn't complete payment within 1 hour. | Expired | Expired |
| **Refunds:** Refund initiated. | Initialized | Initialized |
| **Refunds:** Refund pending (banking only).  | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <support@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Banking order. 

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **iDEAL direct/QR/redirect**.

  <div style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif"
    alt="MultiSafepay Sandbox Test Process GIF"
    style="width: 40%; height: auto;"
  />
  </div>

  </details>

- Transactions expire after 1 hour.

### Ready-made integrations
- Banking is supported in most [ready-made integrations](/docs/our-integrations/), **except** ZenCart. 
- QR is supported in:
    - [Craft Commerce](/docs/craft-commerce/)
    - [CS-Cart](/docs/cs-cart/)
    - [Drupal 8](/docs/drupal/)
    - [Magento 1](/docs/magento-1/) & [Magento 2](/docs/magento-2/)
    - [Odoo](/docs/odoo/)
    - [OpenCart](/docs/opencart/)
    - [PrestaShop](/docs/prestashop/)
    - [Shopware 5](/docs/shopware-5/)
    - [VirtueMart 3](/docs/virtuemart-3/)
    - [VirtueMart 4](/docs/virtuemart-4/)
    - [WooCommerce](/docs/woocommerce/)
    - [X-Cart](/docs/x-cart/)

### Testing
To test iDEAL payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).
<br>

---
# User guide

## Brand recognition

To increase brand recognition for customers, the name of your website appears on the iDEAL payment page and "[Your website name] by MultiSafepay" on the customer's bank statement.

## iDEAL QR
 
<a href="https://ideal.nl/en/products/ideal-qrcode" target="_blank">iDEAL QR</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> has a wide range of applications. Customers can scan QR codes off screens or paper (e.g. invoices, receipts), and change the amount to pay. This makes it particularly suitable for hospitality, charity collectors, and home deliveries. You can specify whether the same QR code can be used more than once.

Not all Dutch banking apps support iDEAL QR yet, so we recommend that customers scan QR codes with their camera or a general QR reader. This redirects to the ideal.nl payment page, which works for all banks. 

## iDEAL redirection

For iDEAL redirect flows, customers are automatically redirected to the iDEAL environment after selecting it as their payment method. To disable this, set `payment_options.settings.gateways.IDEAL.show_pre` to `true`.

#### Example
```json
{
  "payment_options": {
    "close_window": false,
    "settings": {
      "gateways": {
        "IDEAL": {
          "show_pre": true
        }
      }
    }
  },
  "customer": {
    "locale": "en_US",
    "disable_send_email": false
  },
  "checkout_options": {
    "validate_cart": false
  },
  "days_active": 30,
  "seconds_active": 2592000,
  "gateway":"IDEAL",
  "type": "redirect",
  "order_id": "test-order-0001",
  "currency": "EUR",
  "amount": 1000,
  "description": "Test order description"
}
```

## Issuers

iDEAL supports a number of Dutch <<glossary:issuers>>:

<details id="supported-issuers"> 
<summary>Supported issuers</summary>
<br>

- ABN AMRO 
- ASN Bank 	
- bunq
- Buut
- ING 
- Knab 
- Nationale Nederlanden
- N26
- Rabobank 
- Regio Bank 
- Revolut 
- SNS Bank
- Triodos Bank
- Van Lanschot Kempen
- Yoursafe

</details>
---

## iDEAL redirection


For iDEAL redirect requests, the customer will be automatically redirected to the iDEAL payment page after clicking your payment link. To disable this, set `payment_options.settings.gateways.IDEAL.show_pre` to `true`.

#### Example
```json
{
  "payment_options": {
    "close_window": false,
    "settings": {
      "gateways": {
        "IDEAL": {
          "show_pre": true
        }
      }
    }
  },
  "customer": {
    "locale": "en_US",
    "disable_send_email": false
  },
  "checkout_options": {
    "validate_cart": false
  },
  "days_active": 30,
  "seconds_active": 2592000,
  "gateway":"IDEAL",
  "type": "redirect",
  "order_id": "test-order-0001",
  "currency": "EUR",
  "amount": 1000,
  "description": "Test order description"
}
```
---

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
