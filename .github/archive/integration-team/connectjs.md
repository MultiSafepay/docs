---
title: "ConnectJS"
weight: 11
meta_title: "ConnectJS - MultiSafepay Docs"
meta_description: "ConnectJS is a simplified checkout process that prevents the punch out which we have when we redirect the customer to the Connect page for the gateway selection and filling in the additional data"
---

ConnectJS is a simplified checkout process that prevents the ‘punch out’ that occurs when we redirect customers to a [MultiSafepay payment page](/docs/payment-pages/) to select a gateway and enter their payment details.

MultiSafepay's ConnectJS JavaScript library supports all payment methods and [gift cards](/docs/gift-cards/). It lets you directly integrate them in your payment process/checkout quickly and securely. By default, all available payment methods appear, but you can also display just one payment method or a selection. You can configure all payment methods while initiating the library.

## Integration

1. Create a container for the payment page to load in.

2. Insert the following ID into the ConnectJS container:

``` 
<div id="multisafepayContainer"></div>  
```

3. When the <<glossary:order>> is created, add the reference to a global JavaScript object. The object must also contain the `onPaymentAction` method where ConnectJS sends the response to the ecommerce platform when the <<glossary:transaction>> is executed.

```
MultiSafepay = {
    containerId: 'multisafepayContainer' | '#multisafepayContainer',
    containerIframe: '',
    referenceId: 'HERE THE REFERENCE ID',
    onPaymentAction : function(e) {
        console.log('payment action event', e.message);
    },
    onError : function(e) {
        console.log('onError event',e);
    }
}
```
**⚠️ Note:** The `containerId` uses `multisafepayContainer` as an example class name. You can enter your own container name. 

4. Add the ConnectJS library:
```
<script src="https://devpay.multisafepay.com/js/connect.js"></script>
```

When making the create order request, include the setting for ConnectJS in the `payment_options` object. 

Example:  
```
{
  "type": "redirect",
  "order_id": "my-order-id-1",
  "currency": "EUR",
  "amount": 9430,
  "description": "Order with cart",
  "var1": "",
  "var2": "",
  "var3": "",
  "items": "",
  "manual": "false",
  "payment_options": {
    "notification_url": "http://localapitest.multisafepay.com/client/json-local/notification?type=notification",
    "redirect_url": "http://localapitest.multisafepay.com/client/json-local/notification?type=redirect",
    "cancel_url": "http://localapitest.multisafepay.com/client/json-local/notification?type=cancel",
    "close_window": true,
    "connectjs": {
      "version": "1.0",
      "show_cart": true,
      "hide_coupons": true,
      "settings": {
        "redirect_mode": "modal"
      },
    }
  },
……..
}
```

## Settings
You can customize certain parameters, for example: 
```
"connectjs": {
  "show_cart": true,
  "hide_coupons": false,
  "settings": {
    "redirect_mode": "iframe"
  },
}
```
----------------
`show_cart` | boolean

Sets whether to display the shopping cart.  
Default: `false` - doesn't display the cart.

----------------
`redirect_mode` | string

Sets how to display [3D Secure](/docs/3ds2/) verification.  
Options: `iframe`, `redirect`, `modal`.  
Default: `redirect`.

## Example
For a proof of concept, email <integration@multisafepay.com>
