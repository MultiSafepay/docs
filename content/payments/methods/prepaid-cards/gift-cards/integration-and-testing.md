---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Gift cards - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing gift cards in your ecommerce platform"
layout: 'child'
url: '/payment-methods/gift-cards/integration-testing/'
aliases:
    - /payment-methods/gift-cards/test-gift-cards
    - /payments/methods/prepaid-cards/gift-cards/integration-and-testing/
---

To process gift card payments via our API, see API reference – [Gift cards](/api/#gift-card).

For support, email the Integration Team at <integration@multisafepay.com>

{{< details title="View credentials and testing process" >}}

**Intersolve gift cards**

You can only test gift cards that use the Intersolve connection. 

| Test coupon code     | Balance    |
| ------- | --------- |
| 111115  | € 100  |
| 111112 | € 5  |
| 111110 | No balance  |

Any other coupon code receives an "Invalide card number" error.

**Other gift cards** 

Once activated in the [backend](/getting-started/glossary/#backend) of your ecommerce platform, to check the connection, make a small payment from a gift card. 

**Note:** This is a real payment and the amount is actually deducted from the gift card.

{{< /details >}}


