---
title : "Setting your notification URL"
weight: 9
meta_title: "MultiSafepay Control - Setting your notification URL - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/multisafepay-control/set-your-notification-url
---

If you [manually generate a payment link](/tools/multisafepay-control/manually-generated-payment-link) in your MultiSafepay Control and your [Notification URL](/faq/api/notification-url/) is correctly set, your webshop automatically updates the pending order in your backend.

If the notification URL is not correctly set, the order does not update and you may need to manually enter a URL in the **Notification URL** field in your MultiSafepay Control:

| Plugin | Notification URL                  |
|----------|-----------------------|
| CS-Cart    | https://www.example.com/index.php?dispatch=payment_notification.notify&payment=multisafepay_ideal            |
| Drupal 7     | https://www.example.com/multisafepay/callback                 |
| Lightspeed    | https://www.example.com/index.php?dispatch=payment_notification.notify&payment=multisafepay_ideal<br>  For more information, see FAQ - [Lightspeed plugin](/integrations/hosted/lightspeed_core/faq/).          |
| Magento 1    | https://www.example.com/index.php/msp/standard/notification           |
| Magento 2    | https://www.example.com/storeview/multisafepay/connect/notification          |
| OpenCart    | https://www.example.com/index.php?route=extension/payment/multisafepay/callback          |
| OsCommerce     | https://www.example.com/ext/modules/payment/multisafepay/notify.php                 |
|PrestaShop 1.7   |  http://www.example.com/module/multisafepay/validation              |
| VirtueMart     | https://www.example.com/index.php?option=com_virtuemart&view=multisafepayresponse&mode=notify&type=initial&task=notify          |
| WooCommerce    | https://example.com/wc-api/multisafepay_{ID-OF-PAYMENT-METHOD}?transactionid={ORDER-NUMBER}&timestamp={TIME-STAMP} |
| Zen Cart    | https://www.example.com/ext/modules/payment/multisafepay/notify_checkout.php?type=initial |

Email the Integration Team at <integration@multisafepay.com> for:

- CCV Shop
- Drupal 8
- PrestaShop 1.6
- ShopFactory
- Shopify
- Shopware 5 and 6
- X-Cart 
