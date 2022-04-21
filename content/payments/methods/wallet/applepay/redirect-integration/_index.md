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

If a customer lands on an Apple Pay payment page with an unsupported device, the customer can't complete the payment. To avoid this, check whether Apple Pay is supported on the customer's device before creating the payment page.

``` 
try {
    if (window.ApplePaySession && ApplePaySession.canMakePayments()) {
    console.log('Apple Pay available');
    // Create an Apple Pay payment page from your server
    }
    } catch (error) {
    console.debug('An error occurred while verifying if Apple Pay is available:', error);
    }
```