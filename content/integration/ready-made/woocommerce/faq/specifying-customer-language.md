---
title : "Specifying customer language"
meta_title: "WooCommerce plugin - Specifying customer language - MultiSafepay Docs"

layout: "faqdetail"
read_more: "."
url: '/woo-commerce/customer-language/'
aliases: 
    - /integrations/woocommerce/faq/how-can-i-customize-the-language-of-payment-page-and-emails/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/payment-page-and-messages-to-customer-in-other-language/
---

MultiSafepay supports payment pages and messages to customers (e.g. Second Chance emails, links, order confirmations) in several languages. 

However, WooCommerce only supports the language of your ecommerce platform, irrespective of the customer's language or country, or the language of the webshop (if you use a third-party plugin for a multi-lingual webshop). 

Our plugin sets the language for payment pages and messages based on the locale code `get_locale()` - a Wordpress function.

To change this behavior, use the `multisafepay_customer_locale` filter hook in our plugin.

Ask your developer to read WordPress Developer Resources - [Filters in Wordpress](https://developer.wordpress.org/plugins/hooks/filters/)
&nbsp;

Example implementation: 

``` 
add_filter('multisafepay_customer_locale', 'return_my_own_locale');
function return_my_own_locale($locale) {
  // Your conditions and logic to return a valid locale code
  return $custom_locale;
}
```
