---
title : "MultiSafepay Lightspeed installation & configuration manual"
meta_title: "Lightspeed plugin manual - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
aliases:
    - /support-tab/lighstpeed/manual
---

### Introduction
This is a beta version of the Lightspeed app, please contact the Integration team when using it. You can find the contact details below. For the core Lightspeed integration, please find information [here](https://docs.multisafepay.com/integrations/hosted/lightspeed_core/)

{{% introduction_hosted "Lightspeed" %}}

### Requirements
The application is tested using the default, onestep and onepage checkout using the default thema.

For the optimal experience of the user we included some Javascript and use our own images. This allows us to add, for example, a dropdown for iDEAL and our own icons for other payment methods. Some themas or users added scripts can cause issue, such as missing images for payment methods. To resolve these issue can require a developer.

But don't worry if the javascript files are not loaded, all payment methods will keep working. And if you want to use our payment icons you can find them [here!](https://github.com/MultiSafepay/MultiSafepay-icons)

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

After installing the MultiSafepay Payments application, you can access the settings page. You will be redirected to this page automatically after the installation or you can go there by clicking on the _Go to App_ button in your Lightspeed backend when you go to your apps and select the MultiSafepay Payments app.