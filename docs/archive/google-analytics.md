---
title: "Google Analytics"
category: 
slug: 'google-analytics'
excerpt: 'Follow customer journeys with Google Analytics.'
---
Google Analytics is a popular web analytics service used to analyze data collected from your website, e.g. website activity and session duration.



| Version | Javascript library | Google support |
|---|---|---|
| <a href="https://developers.google.com/analytics/devguides/collection/gajs?hl=en" target="_blank">Classic Google Analytics (GA1)</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i> | `ga.js` | Deprecated |
| <a href="https://developers.google.com/analytics/devguides/collection/analyticsjs" target="_blank">Universal Analytics (GA2)</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i> | `analytics.js` | Until July 1, 2023 |
| <a href="https://developers.google.com/analytics/devguides/collection/gtagjs" target="_blank">Universal Analytics (GA3)</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i> | `gtag.js` | Until July 1, 2023 |
| <a href="https://developers.google.com/analytics/devguides/collection/ga4" target="_blank">Google Analytics 4 (GA4)</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i> | `gtag.js` with a different data model | Supported |

# Data models
Universal Analytics is an older version of Google Analytics that uses a data model based on sessions and page views. Google Analytics 4 is the most recent version and uses a data model based on events and parameters.

# Javascript libraries

If you use `analytics.js`, Google gives you a **tracking ID** that you need to add to every page on your website, e.g. `UA-00000-2`. The tracking ID tells Google Analytics which account and property (website) the collected data belongs to.

If you use `gtag.js`, then you use **tags** instead of tracking IDs. The `gtag.js` library adds a single tag to your website to connect with multiple Google products and services, including Google Analytics.

**⚠️ Note:** All Google Analytics accounts since 2017 use `gtag.js`. Prior to 2017, `analytics.js` was the default method for tagging.


## API integrations

You can add your tracking ID or tag in your integration by adding it in `google_analytics.account` when you [create an order](/reference/createorder/).

# Errors

Sometimes Google Analytics can miss or incorrectly report part of a customer's journey if they are redirected away from your website. This can be because:

- The customer pays but doesn't return to your website's success page.
- When the customer is redirected to your success page, a different browser opens. Google Analytics considers this a new session. For example, from an in-app browser to the default browser, or from the customer's preferred browser to the default browser.
- When the customer is redirected to your success page from a third-party website. Google Analytics considers this a new session from a different source.
- The customer has blocked third-party cookies.

This can impact the reliability of Google Analytics reports, and they won't accurately capture <<glossary:conversion>> rates. There are some ways to mitigate this.

## Client side solutions

### How to exclude referrals

To prevent third-party shopping carts initiating new sessions, you can exclude referral domains. This prevents the customer being counted as a referral when they return to your success page.

**⚠️ Note:** This feature is only available for websites using `gtag.js` or `analytics.js`.

For instructions, see Google Analytics – <a href="https://support.google.com/analytics/answer/2795830" target="_blank">Referral exclusions</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i>.

When you click **+Add referral exclusion**, enter the following:

<details id="referral-exclusion-list">
<summary>Referral exclusion list</summary>
<br>

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
</details>

### How to keep sessions alive

To tell Google that the customer's initial session is still in progress and to ignore referral information for the "new" session, add the `utm_nooverride=1` parameter to your payment <<glossary:gateway>> success pages.

For example, for the page URL `/checkout/payment/success`, pass your gateway the following URL: `/checkout/payment/success?utm_nooverride=1`.

In your PHP code, the parameter should look like this: `$this→_redirect('checkout/onepage/success', ['utm_nooverride' => '1'])`.

Make sure you do this for **all** links from the payment gateway to your website.

&nbsp; **💡 Tip!** Our ready-made integrations for Magento 1 and 2 do this automatically.

## Server-side solutions

These solutions need a server environment and may require significant development effort.

**⚠️ Note:**
- Server-side solutions are still in their infancy and could require regular adjustment and maintenance.
- It is not possible to use client-side and server-side solutions at the same time.

### How to send additional data
To send additional event data to Google Analytics, you can use Google's <a href="https://developers.google.com/analytics/devguides/collection/protocol/ga4" target="_blank">Measurement protocol</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i>.

To send additional information about a customer's journey, you can use notifications from our [webhook](/docs/webhook/). For example, that payment was successful or that the <<glossary:order>> was cancelled.

### How to process data on your server

Instead of collecting data client side and sending it directly to Google Analytics, you can first send data to your server for further processing before forwarding to Google Analytics using Google Tag Manager server side tagging.

This provides several benefits:
- It moves data processing from client side to server side, which reduces page load time.
- If your server is hosted on a subdomain of your website, you collect customers' data yourself instead of a third party. This avoids conflicts with third-party cookies.
- You can add additional event data from other sources like MultiSafepay's [webhook notifications](/docs/webhook/).

For more information, see Google Tag Manager - <a href="https://developers.google.com/tag-platform/tag-manager/server-side" target="_blank">Server-side tagging</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i>.

### How to follow customers between sessions

To follow a customer's journey between different sessions or browsers, in addition to using Google Tag Manager server-side tagging, you need to also update the data layer of your website to capture information that accurately identifies the customer. For more information, see Google Tag Manager - <a href="https://developers.google.com/tag-platform/tag-manager/web/datalayer" target="_blank">The data layer</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i>.

<br>

---

[block:html]
{
"html": "<blockquote className=\"callout callout_info\">\n <h3 className=\"callout-heading false\">\n <span className=\"callout-icon\">💬</span>\n <p>Support</p>\n </h3>\n <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)



