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

Check the **changelog** for your plugin to read about any recently added features, and bugfixes. 

**💡 Tip!** Before conducting updates, always test via a **staging** environment.

## Third party solutions

**⚠️ Note:**: We cannot guarantee correct behaviour with any third party solutions which are not explicitly mentioned as compatible in our documentation.

If you encounter an issue with payments while using one of our plugin integrations, always try to reproduce the issue with any third party solutions deactivated. This gives valuable insights for further investigation. 

# Payments failing 

If you encounter issues that affect payments, valuable first checks are:

- Log into your Merchant Dashboard and check for any alerts: You see alerts on your main page if we have recently requested information, or your account needs extra configuration.
- Create a [payment link]\(payment link) and verify if the issue occurs as well. (!) 
  This helps narrow down if the cause lies in a payment configuration, or rather within the plugin /API integration.  
  **💡 Tip!**: Always indicate the result of this step when reaching out to us, best with a screenshot.
- Check if the payment method is available for the country and currency selected. 
- Check if a transaction is created (and declined) or if no transaction arrives to the system in the first place. 

With the results of these checks, reach out to us via [info@multisafepay.com](mailto:info@multisafepay.com).

**💡 Tip!** Check our status page for general updates or notifications.

Further checks for plugin integrations:

- Set your backoffice to debug mode.
- Send us the system report / error logs.

Further checks for custom integrations:

- Check if all requirements in the create Order request were met. 
- Send us a sample request. 

# Payment Component not displayed correctly

Possible errors you may encounter incase of misconfigurations are:

- Payment component displayed empty
- _Temporarily not available_  
  If you use our API  
  If you use one of our ready-made solutions, contact [integration@multisafepay.com](mailto:integration@multisafepay.com)

**Checks **we recommend for our **plugins**: 

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
**💡 Tip!** you can do this best via a staging environment. 
- Contact us for support. 
Alternative solutions in the meantime:
- Activate payment components to avoid confusion with your customers.
- Disable the shopping cart via your settings for the payment page in your Merchant Dashboard. 

# Webhook issues

If you encounter one of the following issues:

- **Transaction status** in your backoffice differs from the status on your MultiSafepay Dashboard

You can try the following:

- Relaunch the notification 
- Verify that you have indicated the correct notification URL

With the results of these checks, reach out to us via [integration@multisafepay.com](mailto:info@multisafepay.com).

# Direct payment button issues 

If you notice any troubles during the integration of direct buttons for Apple Pay or Google Pay, we recommend:

## Apple Pay direct integration

- Ensure that card payments, as well as Apple Pay are enabled for your website / account. 
- Ensure you follow our step by step guide.
- When validating your domain, double check to have associated the **correct URL**. 
- Distinguish correctly between **TEST** and **LIVE** environments, and the respective domain validation files. 
- Place the correct validation file, and do NOT copy-paste. 
- Check if you whitelisted  <a href="https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server" target="_blank">Apple Pay's domain & IP addresses</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- When using a protected environment during testing, ensure you have **whitelisted **our IP ranges. You can mention this need to our support team via [info@multisafepay.com](mailto:info@multisafepay.com) who will send the information to you. 
- Check if the issue occurs via the** redirect solution** as well. This result is valuable information when contacting [info@multisafepay.com](mailto:info@multisafepay.com).

## Google Pay direct integration

- Ensure you follow our step by step guide.
- Ensure you have validated the URL correctly.
- Check if the issue occurs via the redirect solution as well. This result is valuable information when contacting [info@multisafepay.com](mailto:info@multisafepay.com).

# Integration contact rules

If all the steps within your topic did not solve the issue, we are always available to help you investigate further.  
When creating a ticket to [integration@multisafepay.com](mailto:integration@multisafepay.com), please **always** indicate the following:

- **Confirm you have executed all the steps we recommend for self-troubleshooting**
- Your **merchant ID** (MID) to identify your account.
- Indicate if you are integrating via our API, or which plugin version you are using.
- Send any examples (transactions, order IDs) and if possible, screenshots.
- When did the issue start occurring?
- Have you done any changes from your side shortly before the issue occurred for the first time?
- We conduct our investigations in a staging or test environment of your ecommerce platform. Create a temporary username and a <a href="https://www.lastpass.com/nl/features/password-generator" target="_blank">strong password</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> to give us access. Always delete the temporary account after we finish the investigation.



> ⚠️ **Note:**
> 
> MultiSafepay assumes **no** responsibility for mistakes in your live environment.  
> We only ask for the credentials for your live ecommerce platform account in extraordinary circumstances. In such cases, we recommended making a backup beforehand, just in case.
> 
> - If we require server access, we work exclusively with SFTP and SSH, using Port 22. For security reasons, we no longer support the FTP protocol.
> 
> - If we cannot reproduce an issue in a standard staging or test environment, we consider it a _time-boxed project_. This means we allocate a limited period of time to work on it further. We cannot guarantee a solution.