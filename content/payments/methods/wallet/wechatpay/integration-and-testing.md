---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "WeChat Pay - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing WeChat Pay in your ecommerce platform"
layout: 'child'
url: '/payment-methods/wechat-pay/integration-testing/'
aliases:
    - /payments/methods/wallet/wechatpay/integration-and-testing/
---

To process WeChat Pay payments via our API, see API Reference – [WeChat Pay](/api/#wechat-pay).

To display the QR code for WeChat Pay payments, you have two options:

- Use [redirect](/api/#wechat-pay---redirect) orders, to redirect the customer to a [MultiSafepay payment page](/payment-pages/) where the QR code is displayed under **Payment methods**.

- Use [direct](/api/#wechat-pay---direct) orders, retrieve the `qr_url` and render the QR code in your system to display it to the customer.

For the WeChat Pay logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="Test statuses" >}}

Sample statuses:

 Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |

{{< /details >}}
