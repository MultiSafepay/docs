---
title : "Customizing payment components"
meta_title: "Payment components - Customizing payment components - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: 'single'
read_more: '.'
weight: 3
---

After integrating the Payment Component, the default user interface (UI) styling is applied. 

You can customize the styling to match your brand's visual identity, including fonts, colors, and layout. 

## Customizing the UI

To edit the default styling of the Payment Component:

1. Select each CSS class you want to edit.
2. Add the relevant [CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference) and set the values. 

### CSS class selectors

{{< details title="View CSS class selectors" >}}

|CSS class|What it does|
|---|---|
|`.msp-container-ui`|Selects the Payment Component|
|`.msp-ui-payment-form`|Selects the payment form|
|`.msp-ui-method-header`|Selects the payment `.msp-ui-method-image` and heading|
|`.msp-ui-method-image`|Selects the payment method logo|
|`.msp-ui-form-group`|Contains the `.msp-ui-form-control` and `.msp-ui-form-label`|
|`.msp-ui-form-label`|Selects the field labels in the payment form|
|`.msp-ui-form-control`|Selects the fields in the payment form|
|`.msp-ui-row`|Contains two `.msp-ui-col-2` elements|
|`.msp-ui-col-2`|Contains `.msp-ui-form-group`|
|`.msp-ui-separator`|Selects the space before and after the form fields|

{{< /details >}}

{{< screen src="/diagrams/svg/CCC_CSS.svg" align="center" class="medium-img desktop-radius" >}}

### Example

To edit the form fields to: 
- Add a 5-pixel `border-radius`
- Set a light-grey `background-color`
- Change the `font-family` to Helvetica
 
Add the following to your CSS:

```
.msp-ui-form-control {
  border-radius: 5px;
  background-color: #e9ecef;
  font-family: Helvetica;
}
```
