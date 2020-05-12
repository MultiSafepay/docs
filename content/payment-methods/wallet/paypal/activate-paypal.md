---
title : "How to activate PayPal"
weight: 22
meta_title: "PayPal, how to activate it - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## Activate


> * Please note that specific required actions are highlighted with a blue frame on the screenshots below.

###  Account configuration
1. Login into https://www.paypal.com with your business account
2. Navigate to _Toolsv-> All tools -> API credentials_
3. Click on _Grant API permission_
4. Enter `paypal_api1.multisafepay.com` in the Third-Party Permission Username field. Click on _Lookup_

We need access to these options:

- Use Express Checkout to process payments
- Issue a refund for a specific transaction
- Process your customers credit or debit card payments
- Obtain information about a single transaction
- Obtain authorization for pre-approved payments and initiate pre-approved transactions
- Use Express Checkout to process mobile payments.

In order to ensure a correct integration with PayPal, you must change the language encoding setting of your PayPal account to UTF-8.

To do this, please follow the steps below:

1. Go to [Language Encoding in your PayPal](https://www.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding) account and select the desired language 

2. Click on _More Options_. Change the Encoding to UTF-8 by selecting it from the dropdown menu.</br>
The following question will appear: "Do you want to use the same encoding for data sent from PayPal to you?"</br>
Answer with 'yes' and click on _Save_.

###  MultiSafepay Control configuration
1. Click on the gear icon in the upper right corner and select _Account Settings_ -> _Business information_.

2. Copy your `PayPal Merchant ID`

3. Log in into your [MultiSafepay Control](https://merchant.multisafepay.com)

4. Navigate to _Settings_->_Payment methods_. Select 'PayPal' and enter your `PayPal Account ID`.

Your account is now configured and you are ready to accept MultiSafepay payments. We strongly recommend you perform one or more test transactions in order to ensure everything is working correctly.

If PayPal is not visible as a payment method in your MultiSafepay Control account, please contact the Integrations team at <integration@multisafepay.com> to assist you further.

_Please note that if you have enabled payment methods on a particular website, you should also enable PayPal for that specific website_.
