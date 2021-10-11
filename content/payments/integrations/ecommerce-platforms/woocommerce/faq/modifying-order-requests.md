---
title : "Modifying order requests"
meta_title: "WooCommerce - Modifying order requests - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
url: '/woo-commerce/modifying-order-requests/'
aliases: 
    - /integrations/woocommerce/faq/how-can-i-customize-the-language-of-payment-page-and-emails/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/modifying-order-requests/
---

To change something in the OrderRequest before the transaction is processed, use the `multisafepay_order_request` filter hook in our plugin.

First, read the following:

+ [Filters in Wordpress](https://developer.wordpress.org/plugins/hooks/filters/)
+ [MultiSafepay PHP-SDK](https://github.com/MultiSafepay/php-sdk/)

&nbsp;

Example of how to implement and overwrite the shopping cart: 

``` 
add_filter('multisafepay_order_request', 'return_my_multisafepay_order_request');
function return_my_own_locale( \MultiSafepay\Api\Transactions\OrderRequest $order_request) {
    // Your conditions and logic to return a valid order request
    // Register a CartItem
    $shopping_cart_items = array();
    $cart_item = new \MultiSafepay\ValueObject\CartItem();
    $cart_item->addName( 'The product name' )
              ->addQuantity( (int) 1 )
              ->addMerchantItemId( (string) 'SKU' )
              ->addUnitPrice( \MultiSafepay\WooCommerce\Utils\MoneyUtil::create_money( (float) 10.00, (string) 'EUR' ) )
              ->addTaxRate( '21' );
    $shopping_cart_items[] = $cart_item;
    // Register the CartItem in the ShoppingCart     
    $shopping_cart = new MultiSafepay\Api\Transactions\OrderRequest\Arguments\ShoppingCart($shopping_cart_items);
    // Overwrite the ShoppingCart    
    $order_request->addShoppingCart( $shopping_cart );
    // Overwrite the total amount of the transaction
    $order_request->addMoney(\MultiSafepay\WooCommerce\Utils\MoneyUtil::create_money( 12.10, 'EUR' ));
    return $order_request;
}
```
