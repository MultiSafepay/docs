---
title : "Updating the plugin"
meta_title: "Magento 2 plugin - Updating the plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
weight: 2
aliases: 
    - /integrations/magento2/faq/how-can-i-update-the-plugin-for-magento2/
---

You can update the plugin via [Composer](https://getcomposer.org).

To update the plugin in your backend, follow these steps:

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. Sign in to your Magento 2 backend.
3. Run the following commands via the CLI:
```
composer update multisafepay/magento2 --with-dependencies
php bin/magento setup:upgrade
php bin/magento setup:di:compile
```

4. Depending on your webserver/webshop configuration, you may also need to:

    - Check the 'rights' on files are correct. For the MultiSafepay files, see vendor/multisafepay.
    - Empty static files when running in production mode.
    - Clear your cache.


