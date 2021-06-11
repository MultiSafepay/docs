---
title : "MultiSafepay Lightspeed installation and configuration manual"
meta_title: "Lightspeed app  manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /integrations/hosted/lightspeed/manual
    - /integrations/hosted/lightspeedbeta/manual
    - /hosted/lightspeed_app/manual
    - /integrations/hosted/lightspeed_app/manual
    - /integrations/lightspeed_app/manual
---

This is the Lightspeed app. For the Lightspeed core integration, see [Lightspeed core](/integrations/ecommerce-integrations/lightspeed_core).

This technical manual is for installing and configuring the MultiSafepay app for Lightspeed.

We recommend first installing the app in a test environment following the recommended Lightspeed installation procedure. Make sure you have made a backup.

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/guides/getting-started/).
- A MultiSafepay [API key](/tools/multisafepay-control/get-your-api-key))

### Notes

- The application is tested using the default one-step and one-page checkout using the default theme.

- For the best user experience, we provide some Javascript and images in order to add, for example, a drop-down for iDEAL and MultiSafepay icons for other payment methods. Some user-added themes or scripts may cause issues, e.g. missing images for payment methods. For assistance, ask your developer. All payment methods still work if you don't use the Javascript files. 
- To use MultiSafepay payment icons, see GitHub [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

### Installation 

1. Log in to your Lightspeed backend.
2. Go to **Apps** on the left-hand side of the dashboard.
3. Search for the **MultiSafepay payments app**.
4. Click on the app, and then on **Install app** in the top-right corner.  
5. In the login page that appears, log in using your Lightspeed credentials.
6. Click **Next**, and then approve the required permissions.  
    You are redirected to <https://lightspeed.multisafepay.com/install>.
7. Complete the Signup page, and then click **Create account and continue**.
8. Fill in your MultiSafepay API key.
9. Select **Test** or **live** environment, and then click **Register account and continue**.

### Disabling classic Lightspeed

To disable the classic Lightspeed integration after migrating to the new app, follow these steps:

1. Log in to your Lightspeed backend.
2. Go to **Settings** > **Payment providers** > **MultiSafepay**.
2. At the top of the screen, disable this payment provider.

For any questions about the app, email the Integration Team at <integration@multisafepay.com>

To access the MultiSafepay Payments app **Settings** page:

- You are automatically redirected after installing the app, or 
- Select the MultiSafepay Payments app, and then click **Go to app**.
