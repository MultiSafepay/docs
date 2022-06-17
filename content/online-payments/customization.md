---
title : 'Payment component customization'
category: 6278c92bf4ad4a00361431b0
order: 303
hidden: false
slug: 'payment-component-customization'
parentDoc: 62a848399bb3eb004023f291
---
After integrating the payment component, the default user interface (UI) styling is applied. 

You can customize the styling to match your brand's visual identity, including fonts, colors, and layout. 

# How to customize the UI

To edit the default styling of the component:

1. Select each CSS class you want to edit.
2. Add the relevant [CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference) and set the values. 

<details id="css-class-selectors">
<summary>CSS class selectors</summary>
<br>

|CSS class|What it does|
|---|---|
|`.msp-container-ui`|Selects the payment component|
|`.msp-ui-payment-form`|Selects the payment form|
|`.msp-ui-method-header`|Selects the payment `.msp-ui-method-image` and heading|
|`.msp-ui-method-image`|Selects the payment method logo|
|`.msp-ui-form-group`|Contains the `.msp-ui-form-control` and `.msp-ui-form-label`|
|`.msp-ui-form-label`|Selects the field labels in the payment form|
|`.msp-ui-form-control`|Selects the fields in the payment form|
|`.msp-ui-row`|Contains two `.msp-ui-col-2` elements|
|`.msp-ui-col-2`|Contains `.msp-ui-form-group`|
|`.msp-ui-separator`|Selects the space before and after the form fields|

</details>

<img src=""https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/CCC_CSS.svg" align ="center"/>

## Example

Add the following to your CSS to edit the payment component to add a: 

- 5-pixel `border-radius` to the form fields
- Shadow to the fields on `focus`
- 10-pixel `border-radius` to the component container
- Light grey `background-color` to the component container

  ```
  .msp-ui-form-control {
    border-radius: 5px
  }

  .msp-ui-form-control:focus {
    box-shadow: 0 7px 7px rgba(0, 15, 45, 0.2)
  }

  .msp-container-ui {
    border-radius: 10px;
    background-color: #f8f9fa;
  }
  ```

The payment component now looks like this:

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Screenshot-Payment-Component.png" align ="center"/>
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)