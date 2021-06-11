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

1. Log in to the MultiSafepay Control App.
2. Go to **Settings** > **Footer icons**.
3. Click the **Generate script** button. A script appears in the text area below. 
4. Copy the script to your clipboard.
5. In your **Lightspeed Admin area**, go to **Settings** > **Web extras and custom Javascript**. 
6. Paste the script into the **Javascript textbox**.
7. Set the status to **Enable**.
8. Click **Save**. The icons appear in the footer.

Depending on the storefront, the display order of the generated icons is determined by the settings at the time of generation. If you update the settings, you need to update the script as well.
