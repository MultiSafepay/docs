---
title: "Amazon Pay direct integration"
category: 6298bd782d1cf4006032e765
order: 3
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'amazon-pay-direct'
---
With direct integration, the **Amazon Pay** button appears in your checkout page, where customers complete payment without being redirected to a [payment page](/docs/payment-pages/).

<br>
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/amazon-pay-demostore.png"  align ="center"/>

<br>

# Prerequisites

<details id="supported-browsers">
<summary>Supported browsers</summary>
<br>

- Apple Safari
- Google Chrome
- Internet Explorer
- Microsoft Edge
- Mozilla Firefox

---

</details>

- Amazon Pay must be [activated in your MultiSafepay account](/docs/amazon-pay#activation).
- You need to have an <a href="https://pay.amazon.com/signup" target="_blank">Amazon Payments merchant account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- Add all domains that you plan to integrate with Amazon Pay to the JavaScript Origins in <a href="https://sellercentral-europe.amazon.com/external-payments/amazon-pay/integration-central/lwa?" target="_blank">Seller Central</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- All domains must comply with Amazon Pay's <a href="https://pay.amazon.eu/help/6023" target="_blank">Acceptable Use Policy</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# 1. Place the Amazon Pay button

Create an element in the `<body>` of your checkout page where you want to display the **Amazon Pay** button:

```html
<div id="AmazonPayButton"></div>
```

**⚠️ Note:** This element is populated in a later step. For more information, see [Display the Amazon Pay button](#3-display-the-amazon-pay-button) below.

# 2. Create an order

From your server, [create an order](/reference/createorder/) > Wallet order. In the Request pane, see **Examples** > **Amazon Pay direct**.

Extract the `payment_data` object from the response.

# 3. Display the Amazon Pay button

To create an **Amazon Pay** button, in the `AmazonPayButton` element, add a script element with the `src` set to the value returned in `payment_data.js`. Use `amazon.Pay.renderButton()` with the data returned in the `payment_data.payload` object:

```html
<div id="AmazonPayButton"></div>
<script src="{{payment_data.js}}"></script>
<script type="text/javascript" charset="utf-8">
    amazon.Pay.renderButton('#AmazonPayButton', {
        merchantId: 'merchant_id',
        publicKeyId: 'xxxxxxxxxx',
        ledgerCurrency: 'EUR',
        checkoutLanguage: 'en_GB',
        productType: 'PayAndShip',
        placement: 'Checkout',
        buttonColor: 'Gold',
        createCheckoutSessionConfig: {
            payloadJSON: 'payload',
            signature: 'xxxx'
        }
    });
</script>
```
The button is responsive and it inherits the size of the container element. We recommend specifying the size of the container element, or the button may be distorted if the customer zooms in or out on their browser.

<details id="responsive-button-logic">
<summary>Responsive button logic</summary>
<br>

- The button container:
	    - Height must be between 45px and 192px
	    - Width must be between 150px and 500px
	- If you set a value outside these limits, it is adjusted to the closest supported value.
	- If you only specify the:
	    - Height, the width defaults to 500px
	    - Width, the height defaults to 45px
	- If you specify both, the height:width ratio must be between 1:10 and 1:2.6. If the ratio is outside those limits, the width defaults to the specified value and the height is adjusted to a supported ratio value. 
	- If you don't specify either, the button container defaults to 200px by 45px.

---

</details>

When the customer clicks the button, they are redirected to Amazon Pay to complete payment. If you need to control the Amazon Pay button click event, see [Decouple button click and checkout](#decouple-button-click-and-checkout) below.

If payment is: 
- Successful, the customer is redirected to the URL in `redirect_url`
- Unsuccessful, the customer is redirected to the URL in `cancel_url`

## Decouple button click and checkout
To decouple displaying the Amazon Pay button and checkout:
- To display the button, use `amazon.Pay.renderButton()`.
- To start checkout, use`amazonPayButton.initCheckout()`.

```javascript
var amazonPayButton = amazon.Pay.renderButton('#AmazonPayButton', {
   merchantId: 'xxxxx',
   publicKeyId: 'xxxxxxxxxx', 
   ledgerCurrency: 'EUR',          
   checkoutLanguage: 'en_GB', 
   productType: 'PayAndShip', 
   placement: 'Cart',
   buttonColor: 'Gold'
});

amazonPayButton.onClick(function(){
  // Define your custom actions here
  
  amazonPayButton.initCheckout({
    estimatedOrderAmount: { "amount": "109.99", "currencyCode": "EUR"},
    createCheckoutSessionConfig: { 
      payloadJSON: 'payload',
      signature: 'xxxx',
      publicKeyId: 'xxxxxxxxxx'
    }
  });
});
```

# 4. Test your integration

To test your Amazon Pay direct integration, you need a <a href="https://testmerchant.multisafepay.com/" target="_blank">MultiSafepay test account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

To test, follow these steps:

1. [Create an order](/reference/createorder/) > Wallet order.
    Example: Amazon Pay direct
2. On the **Test platform** page, wait for 5 seconds or click **Amazon Pay**.
3. From the **Test scenario** list, select **Completed**.
4. Click **Test**.  
    The payment is processed in your MultiSafepay test account as **Successful**, with <<glossary:order status>> **Completed**, and <<glossary:transaction status>> **Initialized**.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
