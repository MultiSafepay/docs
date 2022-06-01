---
title : "Adding payment method logos"
meta_title: "Lightspeed app - Adding payment method logos"
read_more: "."
url: "/lightspeed/payment-method-logos/"
aliases:
  - /integrations/hosted/lightspeed_app/faq/footer-icons
  - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/adding-payment-method-footer-icons/
  - /integrations/ecommerce-integrations/lightspeed_app/faq/missing-payment-method-logos/
  - /lightspeed/payment-method-icons/
---

By default, our Lightspeed app does not support adding logos for payment methods to your website footer. You can either:  

- Ask your developer to add the logos to your theme. Themes can differ and you may need to make some changes for it to function, **or**

- Use our automated script, follow these steps: 

1. Sign in to your Lightspeed app.
2. Go to **Settings** > **Storefront payment icons**.
3. Click the **copy to clipboard** button. 
5. In your **Lightspeed admin area**, go to **Settings** > **Web extras and custom Javascript**. 
6. Paste the script into the **Javascript textbox**.
7. Set the status to **Enable**.
8. Click **Save**. The logos appear in the footer.

**Display order**  
Depending on the storefront, the display order of the logos is determined by the settings at the time of generation. If you update these settings, you need to update the script as well.

**Size**  
By default the logos are 16px high. In most themes, footer logos are found in the "div.payment-methods p". If needed, you can change the selector based on the theme.

To resize logos, follow these steps:

1. In the JavaScript for displaying the logos, locate the following `img` element near the end of the script:

    ```<img src="${msplt[e]}" alt="${e}" />```

2. Specify the height and width in pixels as required, e.g.:

    ```<img height="16" width="37" src="${msplt[e]}" alt="${e}" />```

**Missing logos**  

Logos may be missing due to your website theme settings. 

To add missing payment method logos, follow these steps:

1. Download the logos from our [Github repo](https://github.com/MultiSafepay/MultiSafepay-icons).
2. Rename the file with upper case formatting, e.g applepay.png > APPLEPAY.png.
3. Sign in to your Lightspeed app.
4. Go to **Design** > **Theme editor** > **Advanced** > **Edit code** > **Assets**, and drop in the logos.  

The logos won't appear instantly. It takes a little time.
