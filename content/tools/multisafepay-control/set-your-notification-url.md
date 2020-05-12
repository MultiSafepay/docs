---
title : "Notification URL"
weight: 34
meta_title: "MultiSafepay Control - How to set notification URL? - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## What do I need to fill in the notification URL field in MultiSafepay Control?

When you create a [payment link](/tools/multisafepay-control/manually-generated-payment-link/) in your [MultiSafepay Control](https://merchant.multisafepay.com), the webshop will automatically update the pending order in its backend if the notification URL is correctly set.

However, if the notification URL is not correctly set, the order will not update and it may be necessary to manually set it in MultiSafepay Control, as follows:

* CCV Shop  
Contact the Integration Team at <integration@multisafepay.com>

* CS-Cart  
https://www.example.com/index.php?dispatch=payment_notification.notify&payment=multisafepay_ideal

* Drupal  7
https://www.example.com/multisafepay/callback

* Drupal  8
Contact the Integration Team at <integration@multisafepay.com>

* HikaShop  
Contact the Integration Team at <integration@multisafepay.com>

* Lightspeed  
https://www.example.com/payment/multisafepay/notify/ - More information can be found on [our Lightspeed plugin FAQ](/integrations/lightspeed/faq/#how-do-i-synchronise-a-generated-payment-link-with-lightspeed)

* Magento 1  
https://www.example.com/index.php/msp/standard/notification

* Magento 2  
https://www.example.com/storeview/multisafepay/connect/notification

* OpenCart  
https://www.example.com/index.php?route=extension/payment/multisafepay/callback

* OsCommerce  
https://www.example.com/ext/modules/payment/multisafepay/notify.php

* PrestaShop  1.6
Contact the Integration Team at <integration@multisafepay.com>

* PrestaShop  1.7
http://www.example.com/module/multisafepay/validation

* ShopFactory  
Contact the Integration Team at <integration@multisafepay.com>

* Shopify  
Contact the Integration Team at <integration@multisafepay.com>

* Shopware 5
Contact the Integration Team at <integration@multisafepay.com>

* Shopware 6
Contact the Integration Team at <integration@multisafepay.com>

* VirtueMart  
https://www.example.com/index.php?option=com_virtuemart&view=multisafepayresponse&mode=notify&type=initial&task=notify

* WooCommerce  
https://www.example.com/?page=multisafepaynotify

* X-Cart  
Contact the Integration Team at <integration@multisafepay.com>

* Zen Cart  
https://www.example.com/ext/modules/payment/multisafepay/notify_checkout.php?type=initial


> Please note that if for any reason the notification URL setup fails, you can manually create a backend order and use the payment link that our plugin places in the notes.


Read more about [how the notification URL works](/faq/api/how-does-the-notification-url-work/)


