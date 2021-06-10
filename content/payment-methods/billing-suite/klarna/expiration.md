---
title: "Klarna Expiration"
weight: 24
meta_title: "Klarna, Expiration - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---

## Expiration

Once a Klarna order has been accepted, the order must be shipped within 28 days. If this is not possible, you have the option to extend this time period in the [MultiSafepay Control](https://merchant.multisafepay.com) via the Extend button. This time can be extended for a total of 180 days in segments.

If the order is not captured before the expiration time has been reached, it will go to the status Expired | Expired. Once the order has expired, it can't be reactivated. The financial status of the order will only go to _Completed_ after the order has been shipped.


| Order Status                      | Transaction Status      |
|--------------------------------|-----------|
| Expired   | Expired  |

Once an order has been expired, this is cannot be reverted and a new order should be made.
