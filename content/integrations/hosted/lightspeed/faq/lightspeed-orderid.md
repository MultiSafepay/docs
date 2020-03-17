---
title: "How do I synchronise a generated payment link with Lightspeed?"
meta_title: "Lightspeed plugin synchronise generated payment link - MultiSafepay Documentation Center"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

When a payment link is generated from [MultiSafepay Control](https://merchant.multisafepay.com), an _orderID_ number is required. This is necessary to link the transaction to the correct _orderID_ in the ecommerce platform of Lightspeed.

However, Lightspeed is displaying a reference number _ORD_ which is often mistaken for an orderID.
Due to this confusion, it happens that when generating a payment link in the MultiSafepay Control, the reference number is used instead of the orderID.
Therefore, when using a reference number, a payment received through a payment link generated in your MultiSafepay control is not linked to the orderID of the ecommerce platform of Lightspeed.

The orderID that should be used when generating a payment link in your MultiSafepay Control is displayed in the URL of the ecommerce platform of Lightspeed.  

In the order detail page of the ecommerce platform of Lightspeed, the correct orderID will be displayed in the URL.

_Example: https://yourdomain.webshop.com/admin/dmin/orders/994152471?offset=7
In this case the orderID is 94152471_.

Contact <info.nl@lightspeedhq.com> for any further questions.
