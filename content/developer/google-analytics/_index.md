---
title : "Google Analytics"
weight: 30
meta_title: "Google Analytics - MultiSafepay Docs"
read_more: "."
layout: 'single'
url: '/developers/google-analytics/'
short_description: 'Use Google Analytics to track customer behaviour on payment pages. '
aliases:
    - /faq/general/google-analytics-referral-exclusions
    - /developer/general/excluding-referrals-in-google-analytics/
    - /developer/excluding-referrals-in-google-analytics/
    - /developer/api/google-analytics-tracking/
---
## Tracking payment pages

You can gain insight into customer behavior on [payment pages](/payment-pages/) through Google Analytics tracking.

When the customer reaches the payment page, the UA-code is generated and appears in the HTML.

## Excluding referrals in Google Analytics
For redirect payment methods where customers are directed to a third-party site to complete payment and then back to your website, Google Analytics doesn't correctly track these visits to your website, e.g.:

- Gateway: Source (instead of your website) 
- Referral: Medium (instead of direct) 

Google Analytics starts a new session whenever a customer comes to your site from a different source to the previous one and when it's not a direct visit, even though the previous session hasn't expired.

For example, a customer selects iDEAL (redirect) and then specifies their bank. They are redirected to the bank's payment page and briefly "exit" the session on your site, before returning to your success page. The customer is now counted as a new visitor, even though no new session is initiated.

This makes Google Analytics reports unreliable, and they don't accurately capture conversion rates. There are two ways to mitigate this.

### Referral exclusion list

To prevent third-party shopping carts initiating new sessions, you can exclude referral domains. 

The customer isn't counted as a referral when they return to your success page. 

**Note:** This feature is only available for websites using gtag.js or analytics.js.
It is not supported for ga.js (Classic Analytics).

For instructions, see Google Analytics – [Referral exclusions](https://support.google.com/analytics/answer/2795830).

When you click **+Add referral exclusion**, enter the following:

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

### utm_nooverride=1 parameter

Add the utm_nooverride=1 parameter to your payment gateway success pages. 

For example, for the page URL ```checkout/payment/success```, pass your gateway the following URL: ```/checkout/payment/success?utm_nooverride=1```. 

This tells Google that the customer's initial session is still in progress and Google ignores the referral information for the "new" session. 

In your code, the parameter should look like this: ```$this→_redirect('checkout/onepage/success', ['utm_nooverride' => '1'])``` .

Make sure you do this for all links from the payment gateway to your website.

For more information, email <integration@multisafepay.com>

**Note:** Our ready-made integrations for Magento 1 and 2 do this automatically. 
