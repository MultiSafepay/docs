---
title : "Language of the MultiSafepay payment page and messages sent to the customer"
meta_title: "WooCommerce plugin available payment methods - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
aliases: [/integrations/woocommerce/faq/how-can-i-customize-the-language-of-payment-page-and-emails/]
---

MultiSafepay supports sending messages (second chance emails, links, order confirmation) and shows the payment page to the customer in several languages. 

However, Wordpress - WooCommerce only delivers us the language of the shop itself, no matter what the language or country of the customer is; or the current language of the store for the customer if you are using any third party plugin to have a multi language webshop. 

The MultiSafepay plugin for WooCommerce defines the language of the payment page and the language of the emails taking the locale code from get_locale(), which is a function built in Wordpress.

If you want to change this behavior it is possible implementing the the filter hook “multisafepay_customer_locale” built in our plugin.

Ask your developer to read:

+ [Filters in Wordpress](https://developer.wordpress.org/plugins/hooks/filters/)
+ [What does Locale do?](https://docs.multisafepay.com/faq/api/locale/)
+ [MultiSafepay Customer Locale Filter](https://github.com/MultiSafepay/WooCommerce/blob/master/src/Services/CustomerService.php#L179-L181)

&nbsp;

A simple example of how to implement this will be the following: 

``` 
add_filter('multisafepay_customer_locale', 'return_my_own_locale');
function return_my_own_locale($locale) {
  // Your conditions and logic to return a valid locale code
  return $custom_locale;
}
```
