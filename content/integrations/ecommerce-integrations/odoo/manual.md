---
title : "MultiSafepay Odoo installation & configuration manual"
meta_title: "Odoo plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /support-tab/odoo/manual
    - /plugins/odoo/manual
    - /integrations/plugins/odoo/manual
    - /integrations/odoo/manual
---

This technical manual is for installing and configuring the MultiSafepay plugin for Odoo.

We recommend first installing the plugin in a test environment following the recommended Odoo installation procedure. Make sure you have made a backup.

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/getting-started/).
- Odoo 13.0
- Tested on Python 3.6

### Installation
1. Download the ZIP archive with module.
2. Unpack the content of the .ZIP file.
3. In your Odoo server (`/mnt/extra-addons/`), under **Custom apps**, add the **payment_multisafepay_official** folder. 
4. Install the required Python dependencies:
    ```
    pip3 install -r requirements.txt
    ```
    Alternatively, you can install them manually:
    ```
    pip3 install multisafepay==0.2.0
    ```
    For more information about dependencies, see Python - [MultiSafepay](https://pypi.org/project/multisafepay).
5. Restart your Odoo server.
6. In your Odoo backend, activate developer mode.
7. Go to the **Apps menu** > **Update apps list**.
8. Search for and open the MultiSafepay payments module `payment_multisafepay_official`.
9. Click **Install**.

### Configuration
1. Sign in to your Odoo backend. 
2. Go to the **Invoicing** or **Website** menu > **Configuration** > **Payment acquirers**.
3. Select **MultiSafepay** payment acquirer. 
4. Go to **Edit** mode. 
5. By default, acquirer state is disabled. To change the state, click **Enabled** or **Test**.
6. Enter **Live** and/or **Test** **API key**.
7. On the **Configuration tab**, set **Journal**.
8. Click **Save**.
9. To get payment methods from your MultiSafepay account,Oo the **Configuration** tab, click **Pull payment methods**.  
    Make sure you have activated the relevant payment methods in your [MultiSafepay account](https://testmerchant.multisafepay.com).
10.  Configure for each payment method separately:  
    - Name  
    - State  
    - Country: Disabled for some payment methods  
    - Customer group  
    - Order amount: Disabled for some payment methods  
    - Supported currency: Some payment methods process transactions only in EUR. Orders not created in EUR are converted to the required currency, using **Odoo platform currency rate**. This can only be configured by a system administrator.

For any questions about the plugin, email the Integration Team at <integration@multisafepay.com>
