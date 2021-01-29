---
title : "Where are the icons in my footer?"
meta_title: "Lightspeed plugin - Where are the icons in my footer?"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

__This feature will be released in 1.0.11__

When using built-in Lightspeed payment methods, icons will appear in the footer when a payment method is enabled. Apps do not support this by default.

You can add ask your developer to add the images to your theme or you can add them by yourself.

To help you, we have created a script which can automatically add the icons. Please note that that every theme can be different and you may have to make some changes for it to function.

In order to obtain the script, go to the Settings page of our app. Below _Footer icons_, you will find a generated script button. This will output a script in the text area below. Copy this script.

Go to your Lightspeed Admin area, Settings, Web extras and Custom Javascript. Paste the script into the Javascripts textbox, set the status to enable and click _Save_. Icons should now be visible in the footer.

The generated icons update depending on the storefront and are ordered depending on the setting at the time of generation. If you update the settings, you would have to update the script as well.