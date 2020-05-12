---
title: "Google Analytics tracking through API"
weight:
meta_title: "FAQ API - Google Universal Analytics tracking - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

It is possible to track the behavior of your customers through Google Universal Analytics [tracking](/api/#create-an-order)  
However, this is restricted only to direct orders. If a customer reaches the MultiSafepay payment page, the UA-code will be loaded and you will be able to see that in the corresponding HTML.

For redirected orders (e.g. iDEAL redirect, some cases of Klarna, Afterpay, etc.), there is NO tracking available, as customers will not pass through a MultiSafepay page after checkout and before the successful payment page. 

> We are currently working on updating the documentation on Google Analytics to accommodate as many of your possible querries as possible. Please check again soon! 