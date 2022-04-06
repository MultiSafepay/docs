---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "WeChat Pay - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing WeChat Pay in your ecommerce platform"
layout: 'child'
url: '/payment-methods/wechat-pay/integration-testing/'
aliases:
    - /payments/methods/wallet/wechatpay/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order. See also Examples > WeChat Pay direct/redirect |
| **Ready-made integrations** | WeChat Pay is supported in our [PrestaShop 1.7 plugin](/prestashop-1-7/). |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |


To display the QR code for WeChat Pay payments, you have two options:

- Use redirect orders to redirect the customer to a [payment page](/payment-pages/) where the QR code is displayed under **Payment methods**.

- Use direct orders, retrieve the `qr_url` and render the QR code in your system to display it to the customer.

## Testing

See [Test payment details](/testing/test-payment-details/#wallets).