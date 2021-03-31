---
title : "How can I delete the deprecated Magento 2 plugin?"
meta_title: "Magento 2 delete deprecated plugin - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
---

The deprecated plugin could be installed through various ways, depending on the way you installed it, it can be deleted as follows:

### 1. Composer
You can either choose to only remove the code base or a full uninstallation including database entries and configuration removal.

#### Option 1: Removing the code base
``` 
composer remove multisafepay/magento2msp
php bin/magento setup:upgrade
```

#### Option 2: Complete uninstall (including database entries and configuration removal)
``` 
bin/magento module:uninstall MultiSafepay_Connect --remove-data --clear-static-content
php bin/magento setup:upgrade
```

You can also optionally choose to create a backup of certain parts of the plugin by adding the following parameters: _--backup-code_, _--backup-media_ and _--backup-db_

Please take a look at the [Magento docs](https://devdocs.magento.com/guides/v2.4/install-gde/install/cli/install-cli-uninstall-mods.html#instgde-cli-uninst-mod-uninst) for all the available parameters.

### 2. app/code
First disable the plugin:
``` 
php bin/magento module:disable --clear-static-content
php bin/magento setup:upgrade
```

To remove the code base, you can delete the app/code/MultiSafepay/Connect directory:
```
cd app/code/MultiSafepay
rm -rf Connect
```

### 3. Marketplace
If you have installed the plugin via the Magento Marketplace inside the Magento admin backend, you can delete the plugin by navigating to the following location:

_System_ ⇒ _Web Setup Wizard_ ⇒ _Extension Manager_ ⇒ _Update / Uninstall_