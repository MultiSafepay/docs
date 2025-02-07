---
title: "Coppermine"
category: 62962dd7e272a6002ebbbbc5
order: 0
hidden: false
parentDoc: 62a9a54aba9800011a8bda88
slug: 'coppermine'
excerpt: "Free integration for MultiSafepay payment solutions."
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/coppermine-docs.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

MultiSafepay has partnered with <a href="https://www.coppermine.nl/" target="_blank">Coppermine</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, which offers a complete ecommerce suite including CRM, B2B, B2C, subscriptions, customer service, logistics, and finance.

# How to integrate

To integrate MultiSafepay as your payment service provider, follow these steps:

## 1. In your dashboard

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Websites**, and [add the required website(s)](/docs/sites/) to your account.
3. In the **Website profile** page for each website:
    - [Activate the required payment methods](/docs/payment-methods/).
    - In the **Webhook URL** field, add the Coppermine webhook endpoint for sending status updates and other notifications. <br> For more information, see [Configure your webhook endpoint](/docs/webhook/).
4. Copy your:
    - Account ID (top-right corner of the dashboard)
    - [Website ID, API key, and security code](/docs/sites#site-id-api-key-and-security-code)

## 2. In Coppermine

1. Sign in to your Coppermine <<glossary:backend>>, and then go to **Settings**.
2. To configure the MultiSafepay PaymentMethod Gateway, enter your:
    - MultiSafepay account ID
    - Site ID, API key, and security code

## 3. Testing

1. Place some test orders in your webshop and Coppermine backend.
2. Check the transactions in Coppermine and your MultiSafepay dashboard. 
3. When everything is working correctly, in your Coppermine backend, set the PaymentMethod Gateway to **Production** mode.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <ul>\n    <li>For technical queries about the integration, see <a href=\"https://www.coppermine.nl/support\">Coppermine support</a></li>\n    <li>To contact MultiSafepay, email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)