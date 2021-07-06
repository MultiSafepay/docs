---
title : "MultiSafepay Drupal 8 & 9 installation & configuration manual"
meta_title: "Drupal 8 & 9 plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

### Introduction  
This manual helps merchants process MultiSafepay payments as quickly as possible from a Drupal 8 & 9 webshop. For some steps in this manual, assistance from your technical partner may be required.

The installation can be carried out in three ways:

+ Composer
+ SFTP
+ Backend

In this manual we describe the installation via Composer.

**Please note**: Security updates for Drupal 8.9.x are no longer provided by Drupal. Drupal 8.9.x receives bugfix support until early 2021 and security fixes until November 2021. To learn more about upgrading from Drupal 8 to Drupal 9, visit [Drupal's documentation](https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher)

{{% introduction_plugin "Drupal 8 & 9" %}}

### 1. Requirements  - Drupal 8.9 and above or Drupal 9.x
- Tested on PHP 7.2
- Drupal Commerce 2.x

### 2. Installation
For installing the latest stable version of our Drupal Commerce 2.x plugin please run the following command in your terminal

```
composer require drupal/commerce_multisafepay_payments
```

After running these commands, the latest stable release is downloaded and installed within your Drupal Commerce 2.x webshop.

### 3. Configuration  
1. Login on the backend of your webshop and navigate to _Commerce_ -> _Configuration_ -> _Payments_ -> _MultiSafepay settings_.
On this page you can fill in your API details. {{% account_info %}}
2. Navigate to _Commerce_ -> _Configuration_ -> _Payments_ -> _Payment gateways_.
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>
