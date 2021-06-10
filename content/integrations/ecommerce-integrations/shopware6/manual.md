---
title : "MultiSafepay Shopware 6 installation and configuration manual"
meta_title: "Shopware 6 plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /plugins/shopware6/manual
    - /integrations/plugins/shopware6/manual
    - /integrations/shopware6/manual
---

This technical manual is for installing and configuring the MultiSafepay plugin for Shopware 6.

We recommend first installing the plugin in a test environment following the recommended Shopware 6 installation procedure. Make sure you have made a backup.

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/guides/getting-started/).
- Shopware 6.2.x, 6.3.x, 6.4.x _([Starter Edition](https://www.shopware.com/en/pricing) supported)_*
- Tested on PHP 7.2.0

For support for Shopware 6 Professional/Enterprise, email your account manager at <sales@multisafepay.com>

### Installation and configuration
1. Navigate to our [Shopware 6 GitHub repository](https://github.com/MultiSafepay/shopware6/releases).
2. Under **Assets**, download the latest release, which starts with Plugin_Shopware6_x.x.x.zip.
3. Log in to your Shopware 6 backend.
4. Go to **Settings** > **System** on the left hand side.
5. Select **Plugins**.
6. Click **Upload plugin** at the top of the page, and then select the file you downloaded in step 2.
7. When the plugin appears, make sure the **Activated** button is toggled.
8. Click the **...** (more) button, and then select **Config**.
9. In the drop-down menu, select **Test**.
10. In the **API key** field, enter your [API key](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key).
11. Fill out the other fields as required.

#### Marketplace installation

Get the free MultiSafepay plugin from the [Shopware 6 marketplace](https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html) and connect your webshop with your Shopware account.

#### Composer installation

Run the following command in the root of your Shopware root directory. Make sure the composer is installed on your hosting server.

```
composer require multisafepay/shopware6
```

### Further support
For any questions about the plugin:

- Email the Integration Team at <integration@multisafepay.com>
- Join the official [Shopware 6 Slack channel](https://join.slack.com/t/shopwarenederland/shared_invite/zt-61exftia-TFYlw5LzmIBnz7Epq07goQ) 
- Join the private MultiSafepays [Shopware 6 Slack channel](https://shopwarenederland.slack.com/archives/G0146NKFJTT)
