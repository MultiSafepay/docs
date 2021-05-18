---
title : "Where are the icons in my footer?"
meta_title: "Lightspeed plugin - Where are the icons in my footer?"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
  - /integrations/hosted/lightspeed_app/faq/footer-icons
---

When using built-in Lightspeed payment methods, icons appear in the footer when a payment method is enabled. The app does not support this by default.

Ask your developer to add the icons to your theme. Themes can differ and you may need to make some changes for it to function.

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
