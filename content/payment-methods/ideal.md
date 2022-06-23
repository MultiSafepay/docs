---
title: 'iDEAL'
category: 6298bd782d1cf4006032e765
order: 110
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'ideal'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/iDeal.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

[iDEAL](https://www.ideal.nl/en/) is the leading payment method in the Netherlands and links all major Dutch retail banks. Customers pay via mobile banking app, QR code, or in their own online banking environment. Once a payment is completed, the customer cannot reverse it and iDEAL guarantees settlement.

Read how iDEAL can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/ideal)

| Overview | Details |
|---|---|
| **Chargebacks**  | No |
| **Countries**  | The Netherlands  | 
| **Currencies**  | EUR | 
| **Expiration** | Transactions expire after 1.5 hours. |
| **Payment components** | [Yes](/payment-components/) | 
| **Payment pages** | [Yes](/payment-pages/) (Banking: Current and deprecated versions, QR: Current only) |
| **Recurring payments** | [Yes](/recurring-payments/) (banking only) |
| **Refunds** | [Yes](/refunds/): Full and partial |
| **Second Chance** | [Yes](/second-chance/) |

> **Note** 
> To increase transparency for customers, the name of your website appears on the iDEAL payment page and "Your-website-name by MultiSafepay" on the customer's bank statement.

# iDEAL QR
 
[iDEAL QR](https://www.ideal.nl/en/businesses/offer-ideal-qr/) has a wide range of applications. Customers can scan QR codes off screens or paper (e.g. invoices, receipts), and change the amount to pay. This makes it particularly suitable for hospitality, charity collectors, and home deliveries. You can specify whether the same QR code can be used more than once.

Not all Dutch banking apps support iDEAL QR yet, so we recommend that customers scan QR codes with their camera or a general QR reader. This redirects to the ideal.nl payment page, which works for all banks. 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/ideal-payment-flow.svg" alt="iDEAL payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses   

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via their bank. | Void   | Void/Cancelled   |
| iDEAL processing error. | Declined   | Declined   |
| The customer didn't complete payment within 1.5 hours. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Initialized | Initialized |
| Refund pending (banking only).  | Reserved | Reserved |
| Refund complete. | Completed | Completed |

</details>

# Activation

You can activate iDEAL yourself in your dashboard.

<details id="how-to-activate-ideal"> 
<summary>How to activate iDEAL</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

> 💬  Support
> If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

</details>

# Integration

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > iDEAL direct/redirect/QR |
| **Ready-made integrations** | Banking is supported in all our [ready-made integrations](/integrations/ready-made/), **except** ZenCart. <br> QR is supported in [Craft Commerce](/craft-commerce/), [CS-Cart](/cs-cart/), [Drupal 8](/drupal/), [Magento 1](/magento-1/), [Magento 2](/magento-2/), [Odoo](/odoo/), [OpenCart](/opencart/), [PrestaShop 1.7](/prestashop/), [Shopware 5](/shopware/), [VirtueMart](/virtuemart/), [WooCommerce](/woo-commerce/), [X-Cart](/x-cart/). |
<br>

> ℹ️ Testing
> To test iDEAL payments, see [Testing](/testing/#banking-methods).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
