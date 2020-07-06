---
title : "MultiSafepay Lightspeed installation & configuration manual"
meta_title: "Lightspeed plugin manual - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

## Introduction

{{% introduction_hosted "Lightspeed" %}}

### 1. Installation 
Follow the following instructions to install the MultiSafepay Lightspeed app:

1. Log in to your backend
2. Navigate to _Apps_ in the left side panel
3. Search for the MultiSafepay Payments app
4. Click on the app and then on _Install App_ in the top right corner
5. You will be redirected to a login page
6. Log in using your Lightspeed credentials
7. Proceed to _Next_ and then approve the required permissions
8. After approving the installation you will be redirected to <https://lightspeed.multisafepay.com/install>
9. Complete the Signup page and click on _Create Account and continue_
10. Fill in your [MultiSafepay API key](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key/), select the corresponding environment (_test/ live_) and then click the _Register Account and continue_ button.

__Congratulations__

You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>


#### 1.1 Migration from old integration to Lightspeed app
If you are using the [old Lightspeed MultiSafepay payment integration](https://docs.multisafepay.com/integrations/hosted/lightspeed_core/):

1. Complete the above mentioned steps to install the Lightspeed app

2. Make sure that the new integration works as intended by placing a test order

3. Open the [old MultiSafepay payment gateway settings](https://services.webshopapp.com/login/?redirect=/payment_providers/859452) and disable the payment provider

4. If at any point you would like to switch back to the old integration, you can uninstall the app from the app store and re-enable the old integration.


### 2. Configuration
After installing the MultiSafepay Payments application, you can access the settings page. You will be redirected to this page automatically after the installation or you can go there by clicking on the _Go to App_ button in your Lightspeed backend when you go to your apps and select the MultiSafepay Payments app.

#### 2.1 Ordering payment methods
The _Payment methods ordering_ section on the settings page allows you to change the order in which the payment methods are shown in the checkout. The order can be changed by dragging and dropping the items in the list. Do not forget to save the settings after making a change!

If you want a different payment method order for different languages, you can configure it here as well. In the dropdown menu under the _Payment methods ordering_ header you can select a country and make a change on a per language basis.
The _Default_ order is used if no specific ruleset for a country is set up.


#### 2.2 Minimal order amount per payment method
You can change the minimal order amount for a payment method to be displayed to the customer. To do so, you have to open the payment method in the _Payment methods ordering_ list by clicking on the "+" sign and then entering an amount in EUR cents.

_For example, if you input a minimal value of 1500 for iDEAL, it means that iDEAL will not be displayed in the checkout unless the total order amount equals 15.00 EUR or more._

If you want different minimal order amounts for different languages you can configure this as well. In the dropdown menu under the _Payment methods ordering_ header you can select a country and make a change on a per language basis.
_Default_ is used if no specific ruleset for a language is specified.


#### 2.3 Maximum order amount per payment method
You can change the maximum order amount for a payment method to be shown in the checkout. To do so, you have to open the payment method in the _Payment methods ordering_ list by clicking on the "+" sign. Then you need to enter an amount in EUR cents into the maximum field. If you do not want a maximum amount enter “-1”.

_For example, iDEAL with a maximum value of 1500 means that iDEAL will not be displayed in the checkout unless the total order amount is less then 15.00 EUR._

If you want different maximum order amounts for different languages, you can configure this in the dropdown menu under the _Payment methods ordering_ header where you need to select a country and make a change on a per language basis.
_Default_ is used if no specific ruleset for a language is set up.


#### 2.4 Changing the API keys or environment
In the settings page click on _Environment & API key_. You will be redirected to another page. 
Here you can update the API key or the environment, or both. 

#### 2.5 Disabling payment methods
If you do not want certain payment methods to be displayed at all, you can disable them in the payment methods ordering list. You will see the disabled payment methods in the payment methods ordering list with a strikethrough.

If you want different payment methods disabled for different languages, you can make these adjustments in the dropdown menu under the _Payment methods ordering_ header where you first need to select a country and then make change on a per language basis. _Default_ is used if no specific ruleset for a language is found.

Are you missing any payment methods? Make sure that the payment methods are first enabled in the [MultiSafepay Control](https://docs.multisafepay.com/tools/multisafepay-control/) and then go to the settings page of our Lightspeed app and enable the respective payment method there again. By default newly activated payment methods in the MultiSafepay Control are disabled in the Lightspeed MultiSafepay Payments settings, so you need to enable them in both places. 

#### 2.6 Inline buy button
If you want to put an extra buy button near the selected payment method you can configure this in the settings page by going to _Inline Buy button_ and selecting _Show inline_ option. 

#### 2.7 Inline newsletter button
If you want to put a newsletter checkmark near the selected payment method you can do so by going to _Inline newsletter_ on your settings page and choosing _Show inline_.