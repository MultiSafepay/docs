---
title: "PWA Studio (Venia)"
category: 62962dd7e272a6002ebbbbc5
order: 11
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's plugin."
slug: 'pwa-studio-venia'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Magento_PWA.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration.git" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

</div>

# Prerequisites

- You will need a <a href="https://testmerchant.multisafepay.com/signup" target="_blank">MultiSafepay account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- To support GraphQL queries, install the <a href="https://github.com/MultiSafepay/magento2-graphql" target="_blank">MultiSafepay Magento 2 GraphQL plugin</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- You must also meet Magento's requirements for PWA Studio (Venia). See Magento – <a href="https://magento.github.io/pwa-studio/venia-pwa-concept/setup/#prerequisites" target="_blank">Prerequisites</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Payment methods

Before activating the relevant payment methods in your backend you must first activate them in you MultiSafepay dashboard. See - [How to activate payment methods](/docs/payment-methods#activation).

By default, this plugin supports all [payment methods supported by our Magento 2 plugin](/docs/magento-2#payment-methods) out of the box, except: 
- Alipay+ ™ Partner
- Amazon Pay
- Direct Debit
- E-invoicing
- MyBank
- Pay After Delivery
- Pay After Delivery Installments
- Request To Pay
- WeChat Pay

You can integrate these payment methods yourself.  
See MultiSafepay GitHub – <a href="https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration/tree/master/src/components" target="_blank">PWA Studio components</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Installation

1. Install the MultiSafepay plugin for supporting `GraphQL` queries, which includes the `MultiSafepay Core`, `Frontend`, and `Adminhtml` plugins. For instructions, see MultiSafepay GitHub – <a href="https://github.com/MultiSafepay/magento2-graphql" target="_blank">Magento 2 GraphQL</a>.    
   
2. Configure the MultiSafepay payment methods and API keys in the Magento admin panel.

3. To configure URL redirects for your success and cancellation pages, go to **Stores** > **Configuration** > **MultiSafepay** > **General Settings** > **Advanced Settings** > **Use custom return urls**

  - For the **Custom redirect URL after canceling the payment**, we suggest using the next link: *<your_pwa_url>/cart?maskedId={{quote.masked_id}}&multisafepayRestore=true*

  - For the **Custom "Success page" url**, we suggest using the next link: *<your_pwa_url>/multisafepay/checkout/success/{{order.increment_id}}/maskedId/{{quote.masked_id}}*

4. Setup a PWA Studio storefront following the steps in this  <a href="https://developer.adobe.com/commerce/pwa-studio/tutorials/setup-storefront/" target="_blank">installation guide</a>.

   4.1. Go to the extension folder (or create the directory if this one doesn't exist):
   ``` 
   cd your_project/packages/extensions
   ```

   4.2. Create MultiSafepay extension folder:
   ``` 
   mkdir multisafepay-payment-integration
   ```

   4.3. Clone all extension files from this repository in **multisafepay-payment-integration** folder.
   ``` 
   git clone https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration.git ./multisafepay-payment-integration
   ```

   4.4.If your application is based on a PWA Studio version below 12.X, switch to the proper branch. Backward compatibility is supported by these 3 branches:
   ``` 
   git checkout compatibility-v9
   git checkout compatibility-v10
   git checkout compatibility-v11
   ```

   4.5. Link extension in **venia-concept package.json**.   
   Go to the **venia-concept** folder and open **package.json**:
   ``` 
   cd your_project/
   ```
   
   4.6. Add the next dependency:
   ``` 
   "dependencies": {
        "@multisafepay/multisafepay-payment-integration": "link:./packages/extensions/multisafepay-payment-integration"
    },
   ```
   
   4.7. Go back to the project root folder and execute next commands:
   ``` 
   yarn install && yarn watch:venia
   ```

5. Explore the checkout in your Venia application:
 <img width="1000" alt="Screenshot 2021-03-25 at 12 56 46" src="https://user-images.githubusercontent.com/78361324/112469889-4a728100-8d6a-11eb-98dd-7429f1154952.png">
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+31020\">support@myshop.com</a></li>\n    <li>To contact MultiSafepay, email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)