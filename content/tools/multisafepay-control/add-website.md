---
title : "Add a website"
weight: 31
meta_title: "MultiSafepay Control- Add Website - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---


## Adding a webshop
**Adding a webshop** to your MultiSafepay Control is the first step into connecting the webshop and MultiSafepay. By adding a webshop in your MultiSafepay Control connection details, for example, an API key will be automatically generated. This will establish the connection between the two platforms.  

1. Login into your MultiSafepay Control

_A live Account ID starts with a 10_ -> [Live MultiSafepay Control](https://merchant.multisafepay.com)  
_A test Account ID starts with a 9_-> [Test MultiSafepay Control](https://testmerchant.multisafepay.com)

2. Navigate to _Settings -> Website settings_

3. Add a new webshop by selecting _Quick add website_

4. Please supply the following information to add a webshop:

   1. Select a category that is related to the webshop
   2.  Provide a description. The description will be displayed on the payment page of MultiSafepay and depending on the payment method, it will also be shown on the bank statement of your customer
   3. Add the webshop URL. This should be the URL from which the actual payments are received
   4.  When available, provide a notification URL. The notification URL is used for sending status updates to your webshop. More information available in [How does the notification URL work?](/faq/api/how-does-the-notification-url-work)
   5.  Only upload a logo when your MultiSafepay Control is created as a FastCheckout account.


5. _Save_ the provided details. 

## Connect your webshop with MultiSafepay
Adding a webshop will automatically supply you with the details needed to make a connection. When opening the webshop in your MultiSafepay Control, an API key, Site ID and Secure code will be shown. 

Follow the following steps to locate your website details:

1. Navigate to _Settings -> Website settings_

2. Open the webshop by clicking on it. The following information will be provided to be able to proceed with establishing the connection:

    * API key
    * Site ID
    * Secure Code
    
    
3. Most plugins supported by MultiSafepay will request an API key, Site ID, Secure code and an Account ID 
    * _Your Account ID is shown in your dashboard in the top right corner behind your company name_ <br>
    
4. Enter the requested information in the backend of your webshop
5. The connection is finalized. Place a test order to validate the connection. 



