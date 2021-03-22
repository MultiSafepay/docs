---
title : "Add a website"
weight: 31
meta_title: "MultiSafepay Control - Add a website - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## Add your website to MultiSafepay Control
Adding your website to MultiSafepay Control is the first step to connecting your website and MultiSafepay. An [API key](/faq/general/glossary/#api-key) will be automatically generated once a website is added in your MultiSafepay Control. This will establish a connection between the two platforms.

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com) or [MultiSafepay Control Test environment](https://testmerchant.multisafepay.com)
2. Navigate to _Settings → Website settings_
3. Add a new website by selecting _Quick add website_
4. Please supply the following information to add a website for your ecommerce integration: 

   1. Select a category that is related to the website
   2. Provide a description. The description will be displayed on the payment page of MultiSafepay and depending on the payment method, it will also be shown on the bank statement of your customer
   3. Add the website URL. This should be the URL from which the actual payments are received
   4. When available, provide a notification URL. The notification URL is used for sending status updates to your website. More information available on [How does the notification URL work?](/faq/api/how-does-the-notification-url-work)
   6. Click on _Save_


## Connect your website with MultiSafepay
Adding a website will automatically supply you with the details required to establish a connection. When opening the website in your MultiSafepay Control, an API key, Site ID and Secure code will be shown. 

Follow these steps to locate your website details:

1. Navigate to _Settings → Website settings_
2. Click on the website. An _API key_, _Site ID_ and _Secure code_ will be provided to establish a connection:
3. Most [ecommerce integrations](/integrations/ecommerce-integrations) supported by MultiSafepay will request an API key, Site ID, Secure code and an Account ID. Your Account ID is shown in your dashboard in the top right corner behind your company name. If you are building your own integration with our API, SDK or wrapper, use the API key under your website settings.
4. Enter the requested information in the backend of your website
5. The connection is finalized and you will be able to [place a test order](https://docs.multisafepay.com/api/#orders) to validate the connection. 
