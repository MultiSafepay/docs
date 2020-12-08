---
title : "Why is a specific payment method not visible in my checkout?"
meta_title: "Magento 2 plugin FAQ - Enable Payments - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
---

When you enabled a payment method, it should always be visible, even when your API key is incorrect.

Be sure that when you use the [Rico Neitzel Payment Filter](https://github.com/riconeitzel/PaymentFilter) that you set the payment method as active in that plugin.

Payment methods may also not be visible in the checkout due to one or more of the following reasons:

* One of multiple gateway filters (country, currency, group, amount, shipping) is activated, but not correctly configured
* Every other gateway filter is activated (not just the one from Rico Neitzel's)
* Configure errors in the Magento 2 backend in the database that prevents changes from being saved
* 'app:config:dump' is done, whereby the config can no longer be edited
* Front-end files cannot be read due to wrong user rights (javascript errors in the front-end)
* The 'Enabled in checkout' is unchecked for the 'MultiSafepay payment method'
* The configuration has been executed in the wrong store view.