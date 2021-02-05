---
title : "MultiSafepay Odoo installation & configuration manual"
meta_title: "Odoo plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases:
    - /support-tab/odoo/manual
---

### 1. Requirements
- Odoo 13.0
- Tested on Python 3.6

### 2. Installation
1. Download ZIP archive with module
2. Unpack the content of the .ZIP file and add _payment_multisafepay_official_ folder under your custom apps in your Odoo server
   (`/mnt/extra-addons/`)
3. Install the required Python dependencies
    ```shell
    pip3 install -r requirements.txt
    ```
    Alternatively, you can install them manually by doing
    ```shell
    pip3 install multisafepay==0.2.0
    ```
    You can find all the information about the dependencies at this [link](https://pypi.org/project/multisafepay/)
4.  Restart Odoo server
5.  Activate developer mode at Odoo platform
6.  Navigate to Apps menu and click _Update Apps List_
7.  Search and open MultiSafepay payments module (payment_multisafepay_official)
8.  Click _Install_.


### 3. Configuration
Configuration is possible within the _Invoicing_ menu or the _Website_ menu.
1.  Navigate to _Invoicing/Website_ menu and go to _Configuration_ -> _Payment Acquirers_
2.  Select _MultiSafepay_ payment acquirer. Go to _Edit_ mode. By default acquirer state is disabled
3.  Change state, _Enabled_ or _Test_, and enter _Live_ and/or _Test_ _API Key_, set Journal at Configuration tab, and save changes
4.  Click _Pull payment methods_ at Configuration tab to get payment methods from your MultiSafepay account
    
    Be sure that you have the desired payment methods active in your [MultiSafepay Control](https://testmerchant.multisafepay.com)
5.  Configure payment methods you wish to offer. Each payment method will have to be configured separately. 
    
You can configure name, state, supported currency, country, and customer group, which are appropriate for this payment method.

For some payment methods editing country and/or order amount is _disabled_. The reason is this payment method supported 
only in certain countries or it has amount limits.

Also, some payment methods process transactions only in _EUR_. 
For these payment methods, if the order was created not in euros, the amount will be _converted_ to the required currency. 
_Odoo platform currency rate_ is used for conversions and it is configured by a system administrator.

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>

### 5. Updates 
1.  Navigate to _Apps_ menu
2.  Search and open _MultiSafepay payments_ module
3.  Click _Upgrade_.
