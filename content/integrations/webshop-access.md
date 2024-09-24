---
title : "Integration Troubleshooting Guide"
category: 62962dd7e272a6002ebbbbc5
order: 500
hidden: false
slug: 'help-us-help-you'
---

We test all our ready-made integrations before release, but due to external factors or incompatibility with third party solutions, your integration may still encounter configuration issues or a bug.

Here are some common checks that we recommend doing before investigating together with our technical support team.

# Basics

Via our ready-made plugins, we offer solutions that require minimal manual configuration from your side.  
We strive for correct functionality, and support you best as possible with any configuration. 

## Plugin versions 

Always ensure your **plugin version is up to date**. Only then, we can guarantee correct functioning of our solutions.  
Seek assistance from your developer to make sure the basic configurations are in place. 

Check the **changelog **for your plugin to read about any recently added features, and bugfixes. 

**Tip**: Before conducting updates, always test via a **staging **environment.

## Third party solutions

**Note: We cannot guarantee correct behaviour with any third party solutions which are not explicitly mentioned as compatible in our documentation. **

If you encounter an issue with payments while using one of our plugin integrations, always try to reproduce the issue with any third party solutions deactivated. This gives valuable insights for further investigation. 

# Payments failing 

If you encounter issues that affect payments, valuable first checks are:

- Log into your Merchant Dashboard and check for any alerts: You see alerts on your main page if we have recently requested information, or your account needs extra configuration.
- Create a [payment link](/docs/payment-links/) and verify if the issue occurs as well.This helps narrow down if the cause lies in a payment configuration, or rather within the plugin/API integration.  
  **Tip**: Always indicate the result of this step when reaching out to us, best with a screenshot.
- Check if the payment method is available for the country and currency selected. 
- Check if a transaction is created (and declined) or if no transaction arrives to the system in the first place. 

With the results of these checks, reach out to us via [info@multisafepay.com](mailto:info@multisafepay.com).

**Tip**: Check our status page for general updates or notifications.

Further checks for plugin integrations:

- Set your backoffice to debug mode.
- Send us the system report / error logs.

Further checks for custom integrations:

- Check if all requirements in the create Order request were met. 
- Send us a sample request. 

# Payment Component not displayed correctly

Possible errors you may encounter in case of misconfigurations are:

- Payment component displayed empty
- _Temporarily not available_  
  - If you use our API  
  - If you use one of our ready-made solutions, contact [integration@multisafepay.com](mailto:integration@multisafepay.com)

**Checks** we recommend for our **plugins**: 

- **Always** ensure that the setting Payment component is set to "enabled" within the payment method. 
- Review which themes you are using and indicate these to us. 
- Set your backoffice to debug mode.
- Send us the system report / error logs.



**Checks** we recommend for **API** solutions:

- Ensure you have followed all instructions in the Payment component guide.
- Reach out to us via [integration@multisafepay.com](mailto:integration@multisafepay.com)

As a temporary fix, while we investigate the issue, you can use our payments via redirect.

# Amounts differ between shopping cart and payment page

- Check if the issue occurs also when deactivating any 3rd party solutions
**Tip**: you can do this best via a staging environment. 
- Contact us for support.

Alternative solutions in the meantime:

- Activate payment components to avoid confusion with your customers.
- Disable the shopping cart via your settings for the payment page in your Merchant Dashboard. 

# Webhook issues

If you encounter one of the following issues:

- **Transaction status** in your backoffice differs from the status on your MultiSafepay Dashboard.

You can try the following:

- Relaunch the notification 
- Verify that you have indicated the correct notification URL

With the results of these checks, reach out to us via [integration@multisafepay.com](mailto:info@multisafepay.com).

# Direct payment button issues 

If you encounter any issues while integrating direct payment buttons for Apple Pay or Google Pay, please follow these recommendations:

## Apple Pay direct integration

- Ensure that card payments, as well as Apple Pay are enabled for your website. 
- Ensure you follow our step by step guide.
- When validating your domain, double check to have associated the **correct URL**. 
- Ensure that you correctly distinguish between the **TEST** and **LIVE** environments, as well as the corresponding domain validation files for each. 
- Place the correct validation file, and do NOT copy-paste. 
- Check if <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server" target="_blank">Apple Pay's domain & IP addresses</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> are whitelisted. 
- When testing in a protected environment, ensure our IP ranges are **whitelisted**. You can request this information by contacting our support team at [info@multisafepay.com](mailto:info@multisafepay.com). 
- Verify if the issue also occurs with the **redirect solution**. This information will be valuable when contacting [info@multisafepay.com](mailto:info@multisafepay.com).

## Google Pay direct integration

- Ensure you follow our step by step guide.
- Ensure the URL has been validated.
- Verify if the issue also occurs with the **redirect solution**. This information will be valuable when contacting [info@multisafepay.com](mailto:info@multisafepay.com).

# Guidelines for contacting Integration Support

**Ensure that you have completed each of the steps mentioned above.** If the issue persists, please reach out to us for further assistance.  
When creating a ticket with [integration@multisafepay.com](mailto:integration@multisafepay.com), please **ensure** to include the following information:

- Your **merchant ID** (MID).
- Specify whether you are using our API or a plugin. In case of the latter, kindly indicate the version.
- Please share any examples, such as transactions or order IDs, and attach screenshots if possible.
- When did you first experience the issue?
- Did you make any changes before the issue first occured?
- We will conduct our investigation in a staging environment of your ecommerce platform. Please create a temporary username and a <a href="https://www.lastpass.com/nl/features/password-generator" target="_blank">strong password</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> to grant us access. Remember to delete the temporary account once the investigation is complete.



> ⚠️ **Note:**
> 
> MultiSafepay **is not responsible** for any errors that occur in your live environment.  
> We request credentials for your live ecommerce platform account only in extraordinary circumstances. We recommended making a backup beforehand.
> 
> - If server access is required, we exclusively use SFTP and SSH through Port 22. For security reasons, we no longer support the FTP protocol.
> 
> - If we cannot reproduce an issue in a standard staging or test environment, we classify it as a _time-boxed project_. This means we allocate a limited amount of time to investigate the issue further. Please keep in mind that a solution is not guaranteed.