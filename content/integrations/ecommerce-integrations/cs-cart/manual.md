---
title : "MultiSafepay CS-Cart installation and configuration manual"
meta_title: "CS-Cart plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /plugins/cs-cart/manual
    - /integrations/plugins/cs-cart/manual
    - /integrations/cs-cart/manual
---

This technical manual is for installing and configuring the MultiSafepay plugin for CS-Cart.

We recommend first installing the plugin in a test environment following the recommended Shopware 6 installation procedure. Make sure you have made a backup.

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/getting-started/).
- CS-Cart 4.x
- Tested on PHP 7.0

### Installation
 1. Unpack the content of the .ZIP file in the root of your CS-Cart webshop.
 2. To trigger the installation, go to `yourdomain.com/msp_installer.php`. 
 3. Delete the `msp_installer.php` file.
 4. In your [MultiSafepay Control](https://merchant.multisafepay.com), provide your [notification URL](/tools/multisafepay-control/set-your-notification-url).

### Configuration
1. Log in to your CS-Cart backend.
2. Go to **Administration** > **Payment methods**.
3. To add payment methods, click the **+** button.
4. In the next screen, enter a name for the payment method to display during checkout. 
5. In the **Processing unit** field, specify the payment method. 
6. Fill out the other fields as required.
7. Click **Create**.
8. In the **Configure** tab, enter your account ID, site ID, and site code. {{% account_info %}}
Your account ID appears in the top right corner of your MultiSafepay Control.

Extra options such as **IP-Validation** and **debugmode** are intended for developers. Leave them unchanged.

For any questions about the plugin, email the Integration Team at <integration@multisafepay.com>
