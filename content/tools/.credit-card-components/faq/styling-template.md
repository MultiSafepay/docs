---
title : "How can I change the styling of the template?"
layout: "faqdetail"
read_more: "."
---

### CSS styling

Our CSS is designed to give you full styling control over the component. Below is an example of the main classes of our component:

{{< br >}}
{{< responsive_svg src="/diagrams/svg/CCC_CSS" alt="TEST" align="center" >}}
{{< br >}}
{{< br >}}

These classes can be customized to match the exact look and feel of your webshop environment. Below is an example of some basic styling done on the main classes from the component:

```
.msp-container-ui .msp-ui-payment-form {
padding: 15px;
border: 1px solid #ff002c;
margin: 0;
}
 
.msp-container-ui .msp-ui-form-label {
font-weight: 500;
display: block;
}
 
.msp-container-ui .msp-ui-form-control {
background-color: #fff;
border: 1px solid #ccc;
color: #666;
font-weight: 400;
font-size: 14px;
padding: 6px 12px;
display: block;
width: 100%;
}
 
.msp-container-ui .msp-ui-form-control .msp-ui-credit-card-input {
background-repeat: no-repeat;
background-attachment: scroll;
background-position: 98% 3px;
padding-right: 40px;
}
```