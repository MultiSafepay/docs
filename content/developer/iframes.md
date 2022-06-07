---
title: 'iFrames'
category: 62962df622e99600810c117d
order: 40
hidden: false
---
 
An inline frame, or `<iframe>`, is an HTML document embedded inside another HTML document on a [website](/glossaries/multisafepay-glossary/#website). 
 
Although MultiSafepay doesn't prohibit embedding a payment page as an `<iframe>`, we don't recommend it. This is because:

- Some payment methods may not work if you use an `<iframe>` for privacy and security reasons. 
- Some banks use scripts that can't load in `<iframe>` elements.
- Modern browsers' safety checks on `<iframe>` elements are very strict, which might block them.

Instead, we recommend using [Payment Components](https://docs.multisafepay.com/payment-components/) to embed payments into your website. 

For support, email <integration@multisafepay.com>
 
