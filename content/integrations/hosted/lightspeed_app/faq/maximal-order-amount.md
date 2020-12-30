---
title : "Can I set a maximun order value for a payment method to show up?"
meta_title: "Lightspeed plugin - Can I set a maximun order value for a payment method to show up? - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
Yes, you can change the maximum order amount for a payment method to be shown in the checkout. To do so, you have to open the payment method in the _Payment methods ordering_ list by clicking on the "+" sign. Then you need to enter an amount in EUR cents into the maximum field. If you do not want a maximum amount enter “-1”.

_For example, iDEAL with a maximum value of 1500 means that iDEAL will not be displayed in the checkout unless the total order amount is less then 15,00 EUR._

If you want different maximum order amounts for different languages, you can configure this in the dropdown menu under the _Payment methods ordering_ header where you need to select a country and make a change on a per language basis.
_Default_ is used if no specific ruleset for a language is set up.
