---
title : "MultiSafepay VirtueMart installation and configuration manual"
meta_title: "VirtueMart plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /plugins/virtuemart/manual
    - /integrations/plugins/virtuemart/manual
    - /integrations/virtuemart/manual

---

This technical manual is for installing and configuring the MultiSafepay plugin for VirtueMart.

We recommend first installing the plugin in a test environment following the recommended VirtueMart installation procedure. Make sure you have made a backup.

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/guides/getting-started/).
- Joomla 2.5 & 3.x + Virtuemart 2.x & 3.x
- Tested on PHP 7.0

### Installation
1. Log in to your VirtueMart backend.
2. Go to **Extensions** > **Extension manager**.
3. Install the Plugin_VirtueMart_x.x.x.zip file using **Drag and drop** or **Browse for file**. 
4. Click **Upload & install**.

### Configuration
1. Log in to your VirtueMart backend.
2. Go to **Extensions** > **Plugins**.
3. In the search box, enter **MultiSafepay**, and then set the plugin status to **Enabled**.
4. Go to **Components** > **VirtueMart**. 
5. Click **Shop** > **Payment methods**. 
6. To install and configure each payment method separately:
  - Click **New**.
  - Set the payment method to **VirtueMart - Payment, MultiSafepay**.
  - To install, save the **Payment method name**.
7. On the **Configuration** tab, enter your:
  - API key
  - Account ID
  - Site ID
  - Site secure code  
  - Gateway ID  
  {{% account_info %}} 

For any questions about the plugin, email the Integration Team at <integration@multisafepay.com>
