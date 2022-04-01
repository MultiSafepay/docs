---
title: "Integrating and testing Dankort"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Dankort - MultiSafepay Docs"
short_description: "Options for integrating Dankort and testing payments"
layout: 'child'
url: '/payment-methods/dankort/integration-testing/'
aliases:
    - /payments/methods/credit-and-debit-cards/dankort/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | See API reference – [Create order](https://api-docs.multisafepay.com/reference/createorder) > Card order. See also Examples > Credit card redirect. {{< br >}} **Bundled credit cards** {{< br >}} You can also bundle multiple credit cards together on your MultiSafepay credit card payment page. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits. {{< br >}} To make Dankort available as a payment method on the MultiSafepay credit card payment page, set the [`locale`](/developer/api/using-locale-parameters) to `da_DK` (Denmark) in transaction requests. |
| **Ready-made integrations** | You can integrate using the Visa gateway (redirect) in all our [ready-made integrations](/integrations/ready-made/).   |
| **Checkout options** | [Payment Components](/payment-components/) (embedded) {{< br >}} [Multisafepay payment pages](/payment-pages/) (hosted) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

See [Test payment details](/testing/test-payment-details/#banking-methods).
