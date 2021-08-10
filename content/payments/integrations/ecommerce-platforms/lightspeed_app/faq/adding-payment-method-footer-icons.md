---
title : "Adding payment method icons in footers"
meta_title: "Lightspeed app - Adding payment method icons in footers"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
  - /integrations/hosted/lightspeed_app/faq/footer-icons
---

You can add icons for standard Lightspeed payment methods to your footer. 

The Lightspeed app does not support this by default. Ask your developer to add the icons to your theme. Themes can differ and you may need to make some changes for it to function.

To automatically add icons using a MultiSafepay script, follow these steps: 

1. Sign in to your Lightspeed app.
2. Go to **Settings** > **Storefront payment icons**.
3. Click the **copy to clipboard** button. 
5. In your **Lightspeed Admin area**, go to **Settings** > **Web extras and custom Javascript**. 
6. Paste the script into the **Javascript textbox**.
7. Set the status to **Enable**.
8. Click **Save**. The icons appear in the footer.

Depending on the storefront, the display order of the generated icons is determined by the settings at the time of generation. If you update the settings, you need to update the script as well.

By default the icons are 16px of height. In most themes the footer icons are found in the "div.payment-methods p". In needed you can change the selector based on the thema.
