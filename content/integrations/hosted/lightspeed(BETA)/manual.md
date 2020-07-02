---
title : "MultiSafepay Lightspeed installation & configuration manual"
meta_title: "Lightspeed plugin manual - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

## Introduction

{{% introduction_hosted "LightSpeed 2" %}}

### 1. Installation 
Follow the following instructions to install the MultiSafepay Lightspeed app:

1. Log in to your backend
2. Navigate to Apps in the left side panel
3. Search for the MultiSafepay Payments app
4. Click on the app and then on "Install App" in the top right corner
5. You will be redirected to a login page
6. Log in using your lightspeed credentials
7. Proceed to _Next_ and then approve the required permissions
8. After approving the installation you will be redirected to <https://lightspeed.multisafepay.com/install>
9. Complete the Signup page and click on "Create Account and continue"
10. Fill in your [MultiSafepay API key](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key/), select the corresponding environment (test/live) and then click the "Register Account and continue button".

__Congratulations__

You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>

### 2. Configuration
After installing the MultiSafepay Payments application you can access the settings page. You will be redirected to this page automatically after the installation or you can go there by clicking on the "Go to App" button in your lightspeed backend when you go to your apps and select the MultiSafepay Payments app.

#### 2.1 Ordering payment methods
The section “Payment methods ordering” on the settings page allows you to change the order in which the payment methods are shown on the checkout. The order can be changed by dragging and dropping the items in the list. Do not forget to save the settings after making a change!

If you want a different payment method order for different languages, you can configure it here as well. In the dropdown menu under the “Payment methods ordering” header you can select a country and make a change on a per language basis.
The “Default” order is used if no specific ruleset for a country is set up.


#### 2.2 Minimal order amount per payment method
You can change the minimal order amount for a payment method to be displayed to the customer. To do so, you have to open the payment method in the “Payment methods ordering” list by clicking on the "+" sign and then entering an amount in EUR cents.

_For example, if you input a minimal value of 1500 for iDEAL, it means that iDEAL will not be displayed in the checkout unless the total order amount equals 15.00 EUR or more._

If you want different minimal order amounts for different languages you can configure this as well. In the dropdown menu under the “Payment methods ordering” header you can select a country and make a change on a per language basis.
“Default” is used if no specific ruleset for a language is specified.


#### 2.3 Maximum order amount per payment method
You can change the maximum order amount for a payment method to be shown in the checkout. To do so, you have to open the payment method in the “Payment methods ordering” list by clicking on the "+" sign. Then you need to enter an amount in EUR cents into the maximum field. If you do not want a maximum amount enter “-1”.

_For example, iDEAL with a maximum value of 1500 means that iDEAL will not be displayed in the checkout unless the total order amount is less then 15.00 EUR._

If you want different maximum order amounts for different languages, you can configure this in the dropdown menu under the “Payment methods ordering” header where you need to select a country and make a change on a per language basis.
“Default” is used if no specific ruleset for a language is set up.


#### 2.4 Changing the API keys or environment
In the settings page click on the “Environment & API key”. You will be redirected to another page. 
Here you can update the API key or the environment, or both. 

#### 2.5 Disabling payment methods
If you do not want certain payment methods to be displayed at all, you can disable them in the payment methods ordering list. You will see the disabled payment methods in the payment methods ordering list with a strikethrough.

If you want different payment methods disabled for different languages, you can make these adjustments in the dropdown menu under the “Payment methods ordering” header where you first need to select a country and then make change on a per language basis. “Default” is used if no specific ruleset for a language is found.

Are you missing any payment methods? Make sure that the payment methods are first enabled in the [MultiSafepay Control](https://docs.multisafepay.com/tools/multisafepay-control/) and then go to the settings page of our lightspeed app and enable the respective payment method there again. By default newly activated payment methods in the MultiSafepay Control are disabled in the lightspeed MultiSafepay Payments settings so you need to enable them in both places. 

#### 2.6 Inline buy button
If you want to put an extra buy button near the selected payment method you can configure this in the settings page by going to “Inline Buy button” and selecting “Show inline” option. 

#### 2.7 Inline newsletter button
If you want to put a newsletter checkmark near the selected payment method you can do so by going to “Inline newsletter” on your settings page and choosing “Show inline”.