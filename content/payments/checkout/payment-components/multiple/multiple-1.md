---
title : "Step 1: Install"
breadcrumb_title : "Step 1"
meta_title: "Payment Components - Integrating multiple payment methods step 1 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
--- 

## Add elements to your checkout page

**1.** Add the Payment Component CSS to the `<head>` of your checkout page:  
```
<link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v2/components.css">
```

**2.** Add the Payment Component script to the bottom of the `<body>` of your checkout page:  
```
<script src="https://pay.multisafepay.com/sdk/components/v2/components.js"></script>
```

**3.** Add the DOM element for the Payment Component UI in the `<body>` of your checkout page:
```
<div id="MultiSafepayPayment"></div>
```

## Choose your payment button

Decide if you want to:

- Generate a button with the component (see [Step 2](/payments/checkout/payment-components/multiple/multiple-2/))
- Use an existing button e.g. if your checkout already includes one
- Create your own button:

```
<button id="payment-button"></button>
```

{{< two-buttons

href-1="/payments/checkout/payment-components/multiple" header-1="Back" text-1="Integrating multiple payment methods" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payments/checkout/payment-components/multiple/multiple-2" header-2="Next" text-2="Step 2: Initialize" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}


