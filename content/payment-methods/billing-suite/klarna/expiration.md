---
title: "Klarna Expiration"
weight: 24
meta_title: "Klarna, Expiration - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## Expiration

Once a Klarna order has been accepted, the order must be shipped within 28 days. If this is not possible, you have the option to extend this time period in the [MultiSafepay Control](https://merchant.multisafepay.com) via the Extend button. This time can be extended for a total of 180 days in segments.

If the order is not captured before the expiration time has been reached, it will go to the status Expired | Expired. Once the order has expired, the order can only be reactivated by Klarna. The financial status of the order will only go to _Completed_ after the order has been shipped.


| Order Status                      | Transaction Status      |
|--------------------------------|-----------|
| Expired   | Expired  |

Once an order has been expired, this is cannot be reverted and a new order should be made.
