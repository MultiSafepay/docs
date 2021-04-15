---
title : "Can I exclude referrals in Google Analytics?"
meta_title: "FAQ General - Excluding referrals - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

> **We are looking for Magento merchants willing to test Option 2 (please see below), the utm_nooverride=1 parameter method. Please get in touch with our Integration Team at <integration@multisafepay.com> if this is something interesting for you and we will further assist you in setting it up.**

Analytics have opened up a new universe about users' needs and wants, about how you can deliver better experiences and about how you can be closer to your customers. 
For many, Google Analytics is a household name and sometimes the only tool available to better understand your customers.  

In most customers' online shopping journey, a payment gateway or another third-party is almost always involved to facilitate successfully paying online.  In implementing a payment gateway's services, it is sometimes the case that some traffic needs to be sent to the third-party's website and then back to your merchant website. This results in visits to your website that are not correctly tracked and that for example, have the gateway as source and referral as medium instead of your own website as source and direct as medium. 

Google Analytics reports will be this way unreliable and will not capture the right picture of where you convert as a merchant. This happens because Google Analytics will start a new session whenever a user comes to the site from a traffic source different the previous one (and when it's not a direct visit), even though the previous session has not expired.

e.g. A customer chooses to pay through iDEAL (redirect) and is prompted with the bank selection in the checkout phase. The customer will now land on the bank's payment page 
and will "exit" the session momentarily, only to come back to your success page. The customer is now counted as a new visitor, even though a new session has not been initiated.

Fortunately, there are two ways to mitigate this issue.

## Option 1 - the Referral Exclusion List

In [Google Analytics](https://support.google.com/analytics/answer/1008015), it is possible to exclude referral domains. As explained above, this is a common fix to prevent third-party shopping carts from starting second sessions. When the third-party shopping cart is in the exclusion list, a user will no longer initiate a new session, and won't be counted as a referral when they return to your order-confirmation page, after checking out on the third-party site. This way, the customer is not counted as a new visitor to the landing page after a payment is done.

Instructions about this can be found on [the Google Analytics page](https://support.google.com/analytics/answer/2795830)


*This feature is only available for websites using gtag.js or analytics.js.</br>
Using ga.js (Classic Analytics) will stop Referral Exclusions from working.*

To add the domains for exclusion, in your Google Analytics interface, go to _Admin_ > _Tracking Info_ > _Referral Exclusion List_  and type in:


```
*.wlp-acs.com
*.securecode.com
*.arcot.com
3dsecure.icscards.nl
paypal.com
tpeweb.paybox.com
acs.netcetera.ch
3dsecure.paylife.at
3d-secure-code.de
clicksafe.lloydstsb.com
mastercardsecurecode.sparkassen-kreditkarten.de
3ds.e-cartebleue.com
acs-3dsecure.cm-cic.com
*.multisafepay.com
www.abnamro.nl
*.asnbank.nl
ideal.bunq.com
ideal.ing.nl
ideal.knab.nl
betalen.rabobank.nl
*.snsbank.nl
*.regiobank.nl
ideal.triodos.nl
ideal.vanlanschot.com
*.kbc.be
*.belfius.be
*.ing.be
*.paysafecard.com
*.alipay.com
*.trustly.com
verified-by-visa.ing-diba.de
3d-secure.pluscard.de
3dsecure-cardprocess.de
3dsecure.bw-bank.de
3dsecure.deutsche-bank.de
geschuetzteinkaufen.commerzbank.de
giropay.postbank.de
ideal.ing.nl
ps4acs.netcetera-payment.ch
sofort.com
verifiedbyvisa.comdirect.de
```

<br>


## Option 2 - the utm_nooverride=1 parameter

This method dates back to the times when Google Analytics would not start a new session unless an old one has expired. 

utm_nooverride=1 is a parameter that needs to be added to your payment gateway return pages. For example, if the page looks like ```checkout/payment/success```, you will need to provide your gateway with the following URL: ```/checkout/payment/success?utm_nooverride=1```. This way, Google will know that the customer's initial session is still in progress and will ignore the referrer information for the "new" session. 

In your code, the parameter should look like this: ```$this > _redirect('checkout/onepage/success', ['utm_nooverride' => '1'])``` .

Make sure that you do this for all the links from the payment gateway to your website!

For any further information, please refer to the Integration Team at integration@multisafepay.com 