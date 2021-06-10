---
title : "Deleting the deprecated plugin"
meta_title: "Magento 2 plugin - Deleting the deprecated plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
aliases:
    - /ecommerce-integrations/magento2/faq/how-to-delete-deprecated-plugin/
---

The way you delete the deprecated plugin depends on the way you installed it:

## Composer
There are two options:

### Option 1: Remove the code base
``` 
composer remove multisafepay/magento2msp
php bin/magento setup:upgrade
```

### Option 2: Do a complete uninstall
This includes removing database entries and configuration.
``` 
bin/magento module:uninstall MultiSafepay_Connect --remove-data --clear-static-content
php bin/magento setup:upgrade
```

#### Backups
You can back up certain parts of the plugin by adding the following parameters: 
- `--backup-code`
- `--backup-media`
- `--backup-db`.

For information about all parameters, see Magento - [Uninstall modules](https://devdocs.magento.com/guides/v2.4/install-gde/install/cli/install-cli-uninstall-mods.html#instgde-cli-uninst-mod-uninst).

## app/code
**1.** Disable the plugin:
``` 
php bin/magento module:disable --clear-static-content
php bin/magento setup:upgrade
```

**2.** To remove the code base, delete the app/code/MultiSafepay/Connect directory:
```
cd app/code/MultiSafepay
rm -rf Connect
```

## Marketplace
If you installed the plugin via the Magento Marketplace in your Magento admin backend, to delete the plugin, go to **System** > **Web setup wizard** > **Extension manager** > **Update / uninstall**.