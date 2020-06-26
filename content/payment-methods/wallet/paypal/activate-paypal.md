---
title : "How to activate PayPal"
weight: 22
meta_title: "PayPal, how to activate it - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## Activate

These instructions are in English. If your PayPal webpage is in another language, you can change the language easily with the links at the rightside bottom of any page.

###  Account configuration
1. Login into https://www.paypal.com with your business account
2. Navigate to _Toolsv-> All tools -> API credentials_
3. Click on _Grant API permission_
4. Click on the leftside of the menu --> _Integrate PayPal_
5. Enter `paypal_api1.multisafepay.com` in the Third-Party Permission Username field. Click on _Lookup_

The following options can be accessed:

- Use Express Checkout to process payments
- Issue a refund for a specific transaction
- Process your customers credit or debit card payments
- Obtain information about a single transaction
- Obtain authorization for pre-approved payments and initiate pre-approved transactions
- Use Express Checkout to process mobile payments.

In order to ensure a correct integration with PayPal, you must change the language encoding setting of your PayPal account to UTF-8.

To do this, please follow the steps below:

1. Click on the following [page](https://www.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding)

2. Choose _Western European Languages_ including English

3. Click on _More Options_ --> _UTF-8_

4. Click _Yes_ --> _Save_

###  MultiSafepay Control configuration
1. Click on the gear icon in the upper right corner and select _Account Settings_ -> _Business information_.

2. Copy your `PayPal Merchant ID`

3. Log in into your [MultiSafepay Control](https://merchant.multisafepay.com)

4. Navigate to _Settings_->_Payment methods_. Select 'PayPal' and enter your `PayPal Account ID`.

Your account is now configured and you are ready to accept MultiSafepay payments. We strongly recommend you perform one or more test transactions in order to ensure everything is working correctly.

If PayPal is not visible as a payment method in your MultiSafepay Control account, please contact the Integrations team at <integration@multisafepay.com> to assist you further.

_Please note that if you have enabled payment methods on a particular website, you should also enable PayPal for that specific website_.
