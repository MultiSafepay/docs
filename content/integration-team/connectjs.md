---
title: "ConnectJS"
weight: 11
meta_title: "ConnectJS - MultiSafepay Support"
meta_description: "ConnectJS is a simplified checkout process that prevents the punch out which we have when we redirect the consumer to the Connect page for the gateway selection and filling in the additional data"
---

## What it is

ConnectJS is a simplified checkout process that prevents the ‘punch out’ which we have when we redirect the consumer to the Connect page for the gateway selection and filling in the additional data.

The MultiSafepay JavaScript ConnectJS library supports all payment methods and [gift cards](https://docs.multisafepay.com/payment-methods/gift-cards/). The library aims to directly integrate these payment methods in your payment process/checkout in a convenient and secure way. By default, all available payment methods will be visible, but it is also possible to show either a single or selection of payment methods which are all configurable while initiating the library.

## Integration

As a merchant, the first step to integrate Connect is by creating a container where Connect will load; the container could be what the merchant wants.

The first thing to do is to insert the ConnectJS container with the proper ID:

``` 
<div id="multisafepayContainer"></div>  
```

When the pretransaction is created, the reference must be added to a global JavaScript object. The object must also contain a method called onPaymentAction where ConnectJS will send the response to the ecommerce platform when the transaction is executed.

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
Please note: containerId uses 'multisafepayContainer' as class as example. Any classname can be used. 

Include the ConnectJS library:
```
<script src="https://devpay.multisafepay.com/js/connect.js"></script>
```

When the order and the JSON are created, the setting for ConnectJS must be included under the payment_options as show in this example:
```
{
  "type": "redirect",
  "order_id": "apitool_461892",
  "currency": "EUR",
  "amount": "9430",
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
It is possible to customize some parameters like the following ones: 
```
"connectjs": {
  "show_cart": true,
  "hide_coupons": false,
  "settings": {
    "redirect_mode": "iframe" | "redirect" | "modal"
  },
}
```
The show_cart parameters by default is set as "false" and wont show the cart.
The redirect_mode parameter set how the 3D-Secure process must be shown. It allows 3 options: iframe, redirect, modal.
The default value is "redirect".


## Example
Contact us for a working example.
