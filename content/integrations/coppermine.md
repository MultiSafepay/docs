---
title : "Coppermine integration for MultiSafepay"
category: 62962dd7e272a6002ebbbbc5
order: 202
hidden: false
parentDoc: 62a9a54aba9800011a8bda88
slug: 'coppermine'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/coppermine-docs.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

MultiSafepay has partnered with [Coppermine](https://www.coppermine.nl/), which offers a complete ecommerce suite including CRM, B2B, B2C, subscriptions, customer service, logistics, and finance.

To integrate MultiSafepay as your payment service provider, follow these steps:

# 1. In your dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Website settings** and [add the required site(s)](/account/managing-websites/#adding-websites) to your account.
3. In the **Website settings** page for each site:
    - [Activate the required payment methods](/payments/activating-payment-methods/).
    - In the **Notification URL** field, add the Coppermine webhook endpoint for sending status updates and other notifications. For more information, see [Webhook](/integrations/webhooks/).
4. Copy your:
    - Account ID (top-right corner of the dashboard)
    - [Site ID, API key, and secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code)

# 2. In Coppermine

1. Sign in to your Coppermine backend, and then go to **Settings**.
2. To configure the MultiSafepay PaymentMethod Gateway, enter your:
    - MultiSafepay account ID
    - Site ID, API key, and secure code

# 3. Testing

1. Place some test orders in your webshop and Coppermine backend.
2. Check the transactions in Coppermine and your MultiSafepay dashboard. 
3. When everything is working correctly, in your Coppermine backend, set the PaymentMethod Gateway to **Production** mode.