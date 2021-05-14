---
title : "Can I refund orders?"
meta_title: "Lightspeed plugin - Can I refund orders? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
    - /hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/lightspeed_app/faq/refunding-lightspeed
---

Yes, you can refund orders as well as credit notes. By default, you can create a refund in your [MultiSafepay Control](https://merchant.multisafepay.com), however, refunding directly from your Lightspeed backend is possible.

To allow the possibility of refunding, you must firstly enable this setting:

1. Log in to [lightspeed.multisafepay.com](https://lightspeed.multisafepay.com/settings)
2. Navigate _Enable Refunds_ by scrolling down or click _Enable refunds_ on the sidebar.

_When creating a credit memo for a refund, make sure to set the status as "Not Paid". We will ignore the "Paid" status._

If any refund is placed using the lightspeed backend a short message will be placed in the notes section of an order. This message can contain an error if anything happens.

## Known issue
Currently there are some know issue related refunds. 

### Errors

#### Refund of amount and item at same time is not allowed.
Some [billing suite](https://docs.multisafepay.com/payment-methods/billing-suite/) payment methods, like AfterPay, do not allow a partial amount and a full item in a single request.
For example:

- A shopping has 3 items and 1.70€ shopping cost. If you refund 1 item and 0.40€ this will fail. 
- Refunding an item and an amount separately will not cause any issue.


#### Same refund done in short period
We do not allow multiple refunds with the same amount, even if the refund contains different items. The current delay is 5 minutes.

## Help & questions
If you need any help with refunds or have any questions, feel free to contact us at <integration@multisafepay.com>
