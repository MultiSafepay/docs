---
title: 'Paysafecard'
category: 6298bd782d1cf4006032e765
order: 2
hidden: false
parentDoc: 62a32bf042021c00e1cd7e5c
slug: 'paysafecard'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/paysafecard-lock.svg" width="100" align="right" style="margin: 15px; max-height: 75px"/>

<a href="https://www.paysafecard.com/en/" target="_blank">Paysafecard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> lets customers make online payments using secure prepaid vouchers, available for purchase locally. The funds are available immediately. The customer chooses a fixed voucher amount: 10, 25, 50 or 100 EUR. 

Customers enter the voucher code, without providing any personal payment details. Vouchers for different amounts are available in the local currency in 46 countries.

The card balance remains available for 12 months free of charge. After 12 months, customers are charged a monthly administration fee of 3 EUR, which is deducted from the balance.

Read how Paysafecard can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/paysafecard" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Worldwide – Go to <a href="https://www.paysafecard.com/en-gb/" target="_blank">Paysafecard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, and then click the globe icon in the banner.  | 
| [Currencies](/docs/currencies/)  | EUR, GBP, USD  | 
| [Chargebacks](/docs/chargebacks/)  | No | 
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Paid with Paysafecard only: You can't refund via MultiSafepay because we don't receive any customer payment details to refund to. Refund in your own online banking. <br> Paid with Paysafecard **and** another payment method: Full refunds.  |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/paysafecard-payment-flow.svg" alt="Paysafecard payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Paysafecard. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| The customer cancelled the transaction at Paysafecard. | Void   | Void   |
| The customer didn't complete payment within 3 hours. | Expired | Expired |
| **Refunds:** Refund initiated. | Initialized | Initialized |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation 

Paysafecard doesn't require activation. 

To find outlets that sell Paysafecard, see: 

- <a href="https://www.paysafecard.com/en/find-sales-outlet-1/" target="_blank">Find sales outlets</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 
- <a href="https://www.paysafecard.com/nl/verkooppunt-vinden-1/" target="_blank">Verkooppunten zoeken</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> 

For any questions, email <sales@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Prepaid card order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Gift card redirect**.

  <div style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif"
    alt="MultiSafepay Sandbox Test Process GIF"
    style="width: 40%; height: auto;"
  />
  </div>

  </details>

- Transactions expire after 3 hours.

### Ready-made integrations

Supported in:

- [CS-Cart](/docs/cs-cart/)
- [Drupal](/docs/drupal/)
- [OsCommerce](/docs/oscommerce/)
- [Magento 1](/docs/magento-1/)
- [Magento 2](/docs/magento-2/)
- [OpenCart 3](/docs/opencart/)
- [OpenCart 4](/docs/opencart-4/)
- [PrestaShop 1.6](/docs/prestashop-1-6/)
- [PrestaShop](/docs/prestashop/)
- [Shopware 5](/docs/shopware-5/)
- [Shopware 6](/docs/shopware-6/)
- [VirtueMart 3](/docs/virtuemart/)
- [VirtueMart 4](/docs/virtuemart-4/)
- [WooCommerce](/docs/woocommerce/)
- [X-Cart](/docs/x-cart/)
- [Zen Cart](/docs/zen-cart/)

### Testing

- You can’t test Paysafecard in your MultiSafepay test account.
- You can only make test payments in your MultiSafepay live account. 
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
