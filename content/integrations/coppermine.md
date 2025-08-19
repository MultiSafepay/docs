---
title: Coppermine
category:
  uri: Integrations
slug: coppermine
position: 0
privacy:
  view: public
parent:
  uri: partner-integrations
content:
  excerpt: Free integration for MultiSafepay payment solutions.
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/coppermine-docs.svg" width="50" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

MultiSafepay has partnered with <a href="https://www.coppermine.nl/" target="_blank">Coppermine</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />, which offers a complete ecommerce suite including CRM, B2B, B2C, subscriptions, customer service, logistics, and finance.

# How to integrate

To integrate MultiSafepay as your payment service provider, follow these steps:

## 1. In your dashboard

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
2. Go to **Websites**, and [add the required website(s)](/docs/sites/) to your account.
3. In the **Website profile** page for each website:
   * [Activate the required payment methods](/docs/payment-methods/).
   * In the **Webhook URL** field, add the Coppermine webhook endpoint for sending status updates and other notifications. <br /> For more information, see [Configure your webhook endpoint](/docs/webhook/).
4. Copy your:
   * Account ID (top-right corner of the dashboard)
   * [Website ID, API key, and security code](/docs/sites#website-id-api-key-and-security-code)

## 2. In Coppermine

1. Sign in to your Coppermine <Glossary>backend</Glossary>, and then go to **Settings**.
2. To configure the MultiSafepay PaymentMethod Gateway, enter your:
   * MultiSafepay account ID
   * Site ID, API key, and security code

## 3. Testing

1. Place some test orders in your webshop and Coppermine backend.
2. Check the transactions in Coppermine and your MultiSafepay dashboard.
3. When everything is working correctly, in your Coppermine backend, set the PaymentMethod Gateway to **Production** mode.

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <ul>
    <li>For technical queries about the integration, see <a href="https://www.coppermine.nl/support">Coppermine support</a></li>
    <li>To contact MultiSafepay, email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></li>
  </ul>
</blockquote>

[Top of page](#)
