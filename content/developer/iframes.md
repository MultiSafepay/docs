---
title: 'iFrames'
category: 62962df622e99600810c117d
order: 40
hidden: false
slug: 'iframes'
---
 
An inline frame, or `<iframe>`, is an HTML document embedded inside another HTML document on a site. 
 
Although MultiSafepay doesn't prohibit embedding a payment page as an `<iframe>`, we don't recommend it. This is because:

- Some payment methods may not work if you use an `<iframe>`, for privacy and security reasons. 
- Some banks use scripts that can't run within `<iframe>` elements.
- Modern browsers' can block them due to stricter security checks.

Instead, we recommend using [Payment Components](https://docs.multisafepay.com/payment-components/) to embed payments into your site. 
 
[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]