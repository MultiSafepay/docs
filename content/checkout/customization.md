---
title: 'Payment component customization'
category: 62bd999547298d001abc714c
order: 8
hidden: false
slug: 'payment-component-customization'
parentDoc: 62a848399bb3eb004023f291
---
After integrating the payment component, the default user interface (UI) styling is applied. 

You can customize the styling to match your brand's visual identity, including fonts, colors, and layout in your:

- Checkout page
- Dashboard

# Via your checkout page

To edit the default styling of the component:

1. Select each CSS class you want to edit.
2. Add the relevant <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference" target="_blank">CSS properties</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and set the values. 

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

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/CCC_CSS.svg" width="500" align="center"/>

### Example

Add the following to your CSS to edit the payment component to add a: 

- 5-pixel `border-radius` to the form fields
- Shadow to the fields on `focus`
- 10-pixel `border-radius` to the component container
- Light gray `background-color` to the component container

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

# Via the dashboard

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Integrations** > **Sites**, and then click the relevant site.
3. On the **Site profile** page, under **Style your checkout solution**, for **Payment component** click **Edit**. 
4. On the **Components settings** page, under **Preview - Default**, select whether you want to:
- Apply the styling from another saved template.
- Edit an existing template. 
- Style a new single payment method component.
- Style a new multiple payment method component. 
- View the style in JSON format. 
5. Under **Configure page style**, style the:  

    <details id="container">
    <summary>Container</summary>
    <br>


    - To set the color of the container background, in the **Background color** field, enter the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
    - To set the font for the field labels, from the **Font family** list, select a font.

    </details> 

    <details id="fields">
    <summary>Fields</summary>
    <br>

    - Set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, placeholder text, label text, text entered by the customer, and the borders. 
    - Set the <a href="https://www.w3schools.com/cssref/css_units.php" target="_blank">size in pixels (px)</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the labels, font, border radius, and box shadow.

    </details>

    <details id="settings-for-ideal-issuers">
    <summary>Settings for iDEAL issuers</summary>
    <br>

   - To add the default padding, border, and labels for the issuers container, select the **Embed mode** checkbox. 
   - To specify the layout of the issuers, from the **iDEAL issuer selection** list, choose **Select button**, **List**, or **Dropdown**. 

   </details>

 6. To set this as your default template, select the **Set as default template** checkbox. 

7. In the **Save template as** field, enter the name of the template (used as the `template_id`), and then click **Submit settings**.

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)