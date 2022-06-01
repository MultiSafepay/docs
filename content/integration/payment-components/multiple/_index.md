---
title : "Integrating multiple payment components"
breadcrumb_title : "Integrating multiple payment components"
meta_title: "Payment Components - Integrating multiple payment components - MultiSafepay Docs"
layout: "single"
read_more: "."
url: "/payment-components/multiple/"
--- 

## Step 1: Add the elements

**1.** Add the component's CSS to the `<head>` of your checkout page:  
```
<link rel="stylesheet" href="https://testpay.multisafepay.com/sdk/components/v2/components.css">
```

**2.** Add the component's script to the bottom of the `<body>` of your checkout page:  
```
<script src="https://testpay.multisafepay.com/sdk/components/v2/components.js"></script>
```

**3.** Add the DOM element for the component's UI in the `<body>` of your checkout page:
```
<div id="MultiSafepayPayment"></div>
```

### Choose your payment button

Decide if you want to:

- Generate a button with the component (see [Step 2](/payment-components/multiple/step-2/)). **Recommended.**
- Use an existing button, e.g. if your checkout already includes one.
- Create your own button:

```
<button id="payment-button"></button>
```

## Next steps

- Step 2: [Initialize the component](/payment-components/multiple/step-2)
- Step 3: [Create an order](/payment-components/multiple/step-3)
- Step 4: [Go live](/payment-components/multiple/step-4)

{{< two-buttons

href-1="/payment-components/" header-1="Back" text-1="Payment Components" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payment-components/multiple/step-2" header-2="Next" text-2="Step 2: Initialize the component" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
