---
title: "Apple Pay redirect integration"
breadcrumb_title: 'Redirect integration'
weight: 10
meta_title: "Apple Pay redirect - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Apple Pay redirect"
layout: 'single'
url: '/payment-methods/apple-pay/redirect/'
aliases:
    - /payments/methods/wallet/applepay/redirect-integration
---

With redirect integration, customers are redirected to a [payment page](/payment-pages/) to complete payment.

## API
[Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order. See also Examples > Apple Pay redirect.

### Detecting Apple Pay on the customer's device

To avoid an error if the customer’s device doesn’t support Apple Pay, we recommend running this piece of JavaScript to detect Apple Pay on the device.

**Note:** The code still displays Apple Pay as a payment method on a non-supported device. We recommend extending the script as required to hide Apple Pay.

``` javascript
try {
    if (window.ApplePaySession && ApplePaySession.canMakePayments()) {
    console.log('ApplePay available');
    }
    } catch (error) {
    console.debug('An error occurred while verifying if Apple Pay is available:', error);
    }
```