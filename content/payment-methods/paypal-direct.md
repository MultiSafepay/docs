---
title: "PayPal button integration"
category: 6298bd782d1cf4006032e765
order: 9
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'paypal-direct'
---

The **PayPal** button enables customers to complete the payment with a one-click checkout solution without being redirected to a <<glossary:payment page>>. The checkout solution allows customers to pay in 4 or monthly installments using <a href="https://www.paypal.com/us/business/accept-payments/checkout" target="_blank">PayPal BNPL</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> method.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/payPayHero.png" align ="center"/>

# Prerequisites

- You need to have a <a href="https://www.paypal.com" target="_blank">PayPal business account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- PayPal must be [activated in your MultiSafepay account](/docs/paypal#activation).

# 1. Initialize

To get the JavaScript SDK URL, include your `api_key` in the request:

```javascript
curl --location --request GET 'https://api.multisafepay.com/v1/json/wallets/configs/paypal?currency=EUR' \
--header 'Authorization: Bearer <api_key>'
```

- Replace  `api_key` with your API key.
- `currency` is defaulted to EUR and is **optional**.

Sample response:

```json
{
    "data": {
        "client_id": "demo-1xswpeBTDCq8PuDPYecrfdd2aPTU3RcvrgNQWy7-bgJd_TpzZMAif38cuz2C4EeTBPo",
        "js_sdk_url": "https://www.paypal.com/sdk/js?client-id=demo-1xswpeBTDCq8PuDPYecrfdd2aPTU3RcvrgNQWy7-bgJd_TpzZMAif38cuz2C4EeTBPo&merchant-id=MJJQECQYBTMRC&currency=EUR",
        "merchant_id": "demo-ASKJDKFUIRJFNDED"
    },
    "success": true
}
```

Use `js_sdk_url` from the response to add the SDK. 

# 2. Add the SDK

 To integrate the PayPal JS SDK, add `js_sdk_url`  in the script tag:

```Text JavaScrpit
<script src="%js_sdk_url%"></script>
```

Alternatively, you can use `client_id` and `merchant_id` to  load the SDK as a module, for example: 

```
import { loadScript } from "@paypal/paypal-js";
loadScript({ "client-id": client_id,"merchant-id":merchant_id })
.then((paypal) => {
    // start to use the PayPal JS SDK script
})
.catch((err) => {
    console.error("failed to load the PayPal JS SDK script", err);
});
```

- Replace `client-id` with your `client_id`.
- Replace `merchant-id` with your `merchant_id`.

> ⚠️ Note
> 
> The naming convention for MultiSafepay is in underscores (_), whereas for PayPal, it is in dashes (-).

For more information about JavaScript SDK, see PayPal Developer - <a href="https://developer.paypal.com/sdk/js/configuration/" target="_blank">JS SDK script configuration.</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

## Display the PayPal checkout button

Create an element in the `<body>` where you want to display the **PayPal** checkout button:

```html
<div id="paypal-button-container"></div>
```

## Render the PayPal button

For information about styling your **PayPal** button, see - <a href="https://developer.paypal.com/sdk/js/reference/#style" target="_blank">style PayPal button.</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

# 3. Create order

- When the customer clicks the PayPal button, the `createOrder` function is called.
- From your server, [create an order](/reference/createorder/) > Wallet order > **PAYPAL**.<br> In response to the request, you receive `payment_details.external_transaction_id`.
- The button launches the PayPal checkout experience.

# 4. Capture order

- When customer approves the payment, the button calls the `onApprove` function, to finalize the transaction. 
- From your server, [capture an order.](/reference/capturepayment/)

Server sample:

````javascript
paypal.Buttons({
            // Call your server to create an order
            createOrder: function(data, actions) {
              ... //Parse order from your server and return
             return order.payment_details.external_transaction_id
            },

            // Call your server to capture the transaction
            onApprove: function(data, actions) { 
              ... //Parse response from your server 
              
               if(order.message == 'INSTRUMENT_DECLINED') {
            return actions.restart();
        }
            }
        }).render('#paypal-button-container');
        ```
````

For more information, see PayPal Developer - <a href="https://developer.paypal.com/sdk/js/reference/#createorder" target="_blank">PayPal JS SDK reference.</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

# 5. Test your integration

After you've implemented the steps above, to test your integration:

PayPal must be [onboarded in your MultiSafepay account](/docs/paypal#activation).

1. In the <a href="https://docs.multisafepay.com/reference/environments" target="_blank">Test environment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, follow all the steps above.
2. On the **Test platform** page, click the **PayPal** button.  
  <br>A popup appears containing the PayPal test store.
3. Select **Pay now**, and then click **Save**. <br> The order is successfully completed.

**⚠️ Note:** If you select the card payment option from test scenario list, you will receive an `INSTRUMENT_DECLINED` error.
