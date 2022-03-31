---
title: "Integrating and testing Edenred"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Edenred - MultiSafepay Docs"
short_description: "Options for integrating Edenred and testing payments"
layout: 'child'
url: '/payment-methods/edenred/integration-testing/'
aliases:
    - /payments/methods/prepaid-cards/edenred/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | See API reference – [Create order](https://api-docs.multisafepay.com/reference/createorder) > Prepaid card order > Examples > Edenred redirect. {{< br >}} By default, all activated Edenred vouchers display at checkout, but you can also specify which Edenred vouchers to display per transaction. |
| **Ready-made integrations** | Edenred is only supported in our [Magento 2](/magento-2/) ready-made integration.   |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can't adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test an Edenred order

1. Make a [redirect](/api/#edenred) API request.
2. On the payment page, click **Add discount**.
3. From the **Test scenario** list, select the relevant discount, and then click **Test**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.
