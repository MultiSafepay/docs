---
title : "MultiSafepay Lightspeed installation & configuration manual"
meta_title: "Lightspeed plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases:
    - /support-tab/lighstpeed/manual
---

### Introduction
This is a beta version of the Lightspeed app. Please contact the Integration Team at <integration@multisafepay.com> if you wish to use the app. The core Lightspeed integration can be found [here](https://docs.multisafepay.com/integrations/hosted/lightspeed_core)

{{% introduction_hosted "Lightspeed" %}}

### Requirements
The application is tested using the default, one-step and one-page checkout using the default theme.

For the optimal experience of the user, we included some Javascript and use our own images. This allows us to add, for example, a drop-down for iDEAL and our own icons for other payment methods. Some themes or users added scripts may cause issues, such as missing images for payment methods. To resolve these issues, a developer may be required.

If the Javascript files are not loaded, all payment methods will continue to work. If you want to use our payment icons, you can find them on our [Github page](https://github.com/MultiSafepay/MultiSafepay-icons)

To use the app, an API key is required. To obtain this key you need a MultiSafepay account. You can create a test account on https://testmerchant.multisafepay.com/signup

### 1. Installation 
Instructions to install the MultiSafepay Lightspeed app:

1. Log in to your backend
2. Navigate to _Apps_ on the left-hand side of the dashboard
3. Search for the _MultiSafepay Payments app_
4. Click on the app and then on _Install App_ in the top right corner
5. You will be redirected to a login page
6. Log in using your Lightspeed credentials
7. Proceed to _Next_ and then approve the required permissions
8. After approving the installation, you will be redirected to <https://lightspeed.multisafepay.com/install>
9. Complete the Signup page and click on _Create Account and continue_
10. Fill in your [MultiSafepay API key](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key), select the corresponding environment (_test / live_) and then click the _Register Account and continue_ button.

### 2. Disabling the old Lightspeed integration

When you have successfully migrated to the new Lightspeed app, you will be able to disable the old integration. You can do this by following these instructions:

1. Login into your backend and navigate to _Settings_ -> _Payment Providers_ -> _MultiSafepay_
2. On the top of the screen you can disable this payment provider.

__Congratulations__

You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>

After installing the MultiSafepay Payments application, you can access the settings page. You will be redirected to this page automatically after the installation. Alternatively, navigate to your apps, select the MultiSafepay Payments app and click on the _Go to App_ button.
