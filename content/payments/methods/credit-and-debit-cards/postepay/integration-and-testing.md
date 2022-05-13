---
title: "Integrating and testing Postepay"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Postepay - MultiSafepay Docs"
short_description: "Options for integrating Postepay and testing payments"
layout: 'child'
url: '/payment-methods/postepay/integration-testing/'
aliases:
    - /payments/methods/credit-and-debit-cards/postepay/integration-and-testing/
    - /postepay/integration-testing/
    - /postepay/integration-testing/
---
## Integration

| | |
|---|---|
| **API** | See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Card order. See also Examples > Credit card redirect. {{< br >}} **Bundled credit cards** {{< br >}} You can also bundle multiple credit cards together on your MultiSafepay credit card payment page. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits. {{< br >}} To make Postepay available as a payment method on the MultiSafepay credit card payment page, set the `locale` to `it_IT` (Italy) in transaction requests. |
| **Ready-made integrations** | You can integrate using the Visa gateway (redirect) in all our [ready-made integrations](/integrations/ready-made/).   |
| **Checkout options** | [Payment Components](/payment-components/) {{< br >}} [Payment pages](/payment-pages/) – [Current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/) versions {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

See [Test payment details](/testing/test-payment-details/#credit-and-debit-cards).


