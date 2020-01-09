---
title : "Notification URL"
weight: 34
meta_title: "MultiSafepay Control - How to set notification URL? - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
## What do I need to fill in the notification URL field in MultiSafepay Control?

When you create a [payment link](/tools/multisafepay-control/manually-generated-payment-link/) in your [MultiSafepay Control](https://merchant.multisafepay.com), the shop will automatically update the pending order in its backend if the notification URL is correctly set.

However, if the notification URL is not correctly set, the order will not update and it may be necessary to manually set it in MultiSafepay Control, as follows:

* CCV Shop  
Contact Integration Team at <integration@multisafepay.com>

* CS-Cart  
https://www.yourdomain.com/index.php?dispatch=payment_notification.notify&payment=multisafepay_ideal

* Drupal  
http://www.drupalshopurl.com/multisafepay/callback

* HikaShop  
Contact Integration Team at <integration@multisafepay.com>

* Lightspeed  
https://www.yourdomain.com/payment/multisafepay/notify/ - More information can be found on [our Lightspeed plugin FAQ](/integrations/lightspeed/faq/#how-do-i-synchronise-a-generated-payment-link-with-lightspeed)

* Magento 1  
https://www.yourdomain.com/index.php/msp/standard/notification

* Magento 2  
https://yourdomain.com/storeview/multisafepay/connect/notification

* OpenCart  
https://yourdomain.com/index.php?route=extension/payment/multisafepay/callback

* OsCommerce  
Contact Integration Team at <integration@multisafepay.com>

* PrestaShop  
Contact Integration Team at <integration@multisafepay.com>

* ShopFactory  
Contact Integration Team at <integration@multisafepay.com>

* Shopify  
Contact Integration Team at <integration@multisafepay.com>

* Shopware  
Contact Integration Team at <integration@multisafepay.com>

* VirtueMart  
Contact Integration Team at <integration@multisafepay.com>

* WooCommerce  
Contact Integration Team at <integration@multisafepay.com>

* X-Cart  
Contact Integration Team at <integration@multisafepay.com>

* Zen Cart  
Contact Integration Team at <integration@multisafepay.com> 


> Please note that if for any reason the notification URL setup fails, you can manually create a backend order and use the payment link that our plugin places in the notes.


Read more about [how the notification URL works](/faq/api/how-does-the-notification-url-work/).


