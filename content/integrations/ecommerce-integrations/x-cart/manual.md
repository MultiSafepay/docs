---
title : "MultiSafepay X-Cart installation and configuration manual"
meta_title: "X-Cart plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /plugins/x-cart/manual
    - /integrations/plugins/x-cart/manual
    - /integrations/x-cart/manual
---

This technical manual is for installing and configuring the MultiSafepay plugin for X-Cart.

We recommend first installing the plugin in a test environment following the recommended X-Cart installation procedure. Make sure you have made a backup.

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/guides/getting-started/).
- X-Cart 5.x        
- Tested on PHP 7.0

### Installation
1. In the root of your webshop, unzip the content of the .ZIP file.
2. Log in to your X-Cart backend.
3. Go to **System tools** > **Cache management** > **Re-deploy the store**.
4. Click **Start**.

### Configuration
1. Log in to your X-Cart backend.
2. Go to **My Addons**, and search for **MultiSafepay**.
3. Locate and enable **MultiSafepay Connect**. This is required to enter your [API key](/faq/general/multisafepay-glossary/#api-key) in a later step.
4. Select the relevant payment methods, and then click **Save changes**.
5. Go to **Store setup** > **Payment methods**.
6. Locate and activate your enabled payment methods.
7. For **MultiSafepay Connect**, click **Configure**.
8. For **Account type**, you have two options: **Live** and **Test**.  
  - Enter your account ID, site ID, site secure code, and your API key.
  - Make sure you enter the correct API key for the account type you want to use. 
  - For where to find your account ID, site ID, site secure code, see [API key](/tools/multisafepay-control/get-your-api-key).
9. Click **Save changes**.  

For any questions about the plugin, email the Integration Team at <integration@multisafepay.com>
