---
title : "Can I refund orders?"
meta_title: "Lightspeed plugin - Can I refund orders? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

Yes you can refund orders as well as credit notes. By default you can create a refund in your [MultiSafepay Control](https://merchant.multisafepay.com), however, refunding directly from your Lightspeed backend is possible.

To allow refunds you first have to enable this setting. Login to [lightspeed.multisafepay.com](https://lightspeed.multisafepay.com/settings), scroll down to "Enable Refunds" or click "Enable refunds" in the sidebar.

If any refund is placed using the lightspeed backend a short message will be placed in the notes section of an order. This message can contain a error if anything happens.

## Known issue
Currently there are some know issue related refunds. 

### Errors

#### Refund of amount and item at same time is not allowed.
Some [billing suite](https://docs.multisafepay.com/payment-methods/billing-suite/) payment methods, like AfterPay, do not allow a partial amount and a full item in a single request.
For example:

- A shopping has 3 items and 1.70€ shopping cost. If you refund 1 item and 0.40€ this will fail. 

Refunding a item and a amount separately will not cause any issue.

#### Same refund done in short period
We do not allow multiple refunds with the same amount, even if the refund contains different items. The current delay is 5 minutes.

## Help & questions
If you need any help with refunds or have any questions, feel free to contact us at <integration@multisafepay.com>
