---
title : "Can I set orders to Shipped automatically in Magento 1?"
meta_title: "Magento 1 plugin automatic shipping - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

Within our Magento 1 plugin, it is possible to set order to _Shipped_ automatically through our API. This is needed to capture the money from AfterPay, E-Invoicing, Klarna, Pay After Delivery and Santander Betaal per Maand.

Login into the backend of your webshop and navigate to _System_ → _Configuration_ → _MultiSafepay x.x.x_ → _Connect Settings_. In the specific gateway settings, look for 'Send shipped status after complete order'. This setting is located at the bottom.