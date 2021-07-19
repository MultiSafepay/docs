---
title : "MultiSafepay app for Lightspeed"
meta_title: "Lightspeed plugin - MultiSafepay Docs"
faq: "."
changelog_url: '.'
changelog: 'https://lightspeed.multisafepay.com/changelog'
layout: 'single'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: "/logo/Integrations/Lightspeed.svg"
weight: 04
title_short: "Lightspeed app"
description_short: "Free app to integrate MultiSafepay payment solutions into your Lightspeed webshop"
aliases: 
    - /integrations/hosted/lightspeed/
    - /integrations/hosted/lightspeedbeta/
    - /hosted/lightspeed_app
    - /integrations/hosted/lightspeed_app
    - /integrations/lightspeed_app
    
---

This technical manual is for installing and configuring our free app for integrating MultiSafepay payment solutions into your Lightspeed webshop. 

For our Lightspeed core integration, see [Lightspeed core](/payments/integrations/ecommerce-platforms/lightspeed_core).

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the app in a test environment following the recommended Lightspeed installation procedure. Make sure you have made a backup.

This app is tested using the default one-step and one-page checkout using the default theme.

{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}
- MultiSafepay account – See [Getting started](/getting-started/).
- A MultiSafepay [API key](/tools/multisafepay-control/get-your-api-key))

{{< /details >}}

{{< details title="Payment icons" >}}

To use MultiSafepay payment icons, see GitHub [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< /details >}}

{{< details title="JavaScript" >}}

For the best user experience, we provide some Javascript and images, e.g. to add a drop-down for iDEAL and MultiSafepay icons for other payment methods. 

Some user-added themes or scripts may cause issues, e.g. missing images for payment methods. 

For assistance, ask your developer. 

All payment methods still work if you don't use the Javascript files. 

{{< /details >}}


## Installation 

1. Sign in to your Lightspeed backend.
2. Go to **Apps** on the left-hand side of the dashboard.
3. Search for the **MultiSafepay payments app**.
4. Click on the app, and then on **Install app** in the top-right corner.  
5. In the login page that appears, Sign in using your Lightspeed credentials.
6. Click **Next**, and then approve the required permissions.  
    You are redirected to <https://lightspeed.multisafepay.com/install>.
7. Complete the Signup page, and then click **Create account and continue**.
8. Fill in your MultiSafepay API key.
9. Select **Test** or **live** environment, and then click **Register account and continue**.


