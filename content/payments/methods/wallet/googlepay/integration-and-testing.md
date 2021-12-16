---
title: "Integrating and testing Google Pay"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Google Pay - MultiSafepay Docs"
short_description: "Options for integrating Google Pay and testing payments"
layout: 'child'
url: '/payment-methods/google-pay/integration-testing'
noindex: '.'
---

## Integration

{{< two-buttons href-2="/payment-methods/google-pay/direct/" text-2="Google Pay™ direct" description-2="Embed Google Pay in your checkout page for the best user experience." img-2="/logo/Payment_methods/GooglePay.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/api/#google-pay" text-2="Google Pay™ redirect" description-2="Easily integrate Google Pay using MultiSafepay payment pages." img-2="/logo/Payment_methods/GooglePay.svg" alt-2="Right arrow" >}}

{{< br >}}

| | |
|---|---|
| **Ready-made integrations** | Google Pay (redirect) is supported in all our [ready-made integrations](/integrations/ready-made/) **except** Magento 2.    |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can adjust the lifetime. |
| **Google branding** | When integrating Google Pay into your ecommerce platform, you must follow [Google's brand guidelines](https://developers.google.com/pay/api/web/guides/brand-guidelines). |

## Testing

To test Google Pay payments, follow these steps:

1. In your checkout, click the **Google Pay** button.  
2. Complete payment using your Google account. 

    Your real card details are never processed in our testing environment, but you must add at least one chargeable card to your Google account.

    Depending on your card's authentication method, you may or may not be redirected to authenticate:

    - **PAN only**: Authentication method for cards stored on file in your Google Account. Returned payment data includes your personal account number (PAN), expiration month, and expiration year. You are redirected to a test 3D Secure page to authenticate the payment.
    - **Cryptogram 3DS**: Authentication method for cards stored as Android device tokens. Returned payment data includes a 3D Secure cryptogram generated on the device. You are not redirected to authenticate the payment.  
    &nbsp;  
    For more information about testing, see Google Pay – [Test with sample tokens](https://developers.google.com/pay/api/web/guides/resources/sample-tokens).
&nbsp;  
3. Check the status of the payment [in your test account](https://testmerchant.multisafepay.com/).

For support, email the Integration Team at <integration@multisafepay.com>