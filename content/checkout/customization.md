---
title: 'Payment component customization'
category: 62bd999547298d001abc714c
order: 3
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
2. Go to **Websites**, and then click the relevant website.
3. On the **Website profile** page, under **Style your checkout solution** > **Payment component**, click **Edit**. 
4. On the **Components settings** page, under **Preview - Default**, select whether you want to:

- Apply the styling from another saved template.
- Edit an existing template. 
- Style a new single payment method component.
- Style a new multiple payment method component. 
- View the style in JSON format. 

5. Under **Configure page style**, you can customize the appearance of your payment components. Click on each section below to expand the options:

    <details id="container">
    <summary>Template simulator</summary>
    <br>

   The template simulator provides a preview of your payment page. Here, you can:

   - Set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background and text.
   - Set the <a href="https://www.w3schools.com/cssref/css_units.php" target="_blank">size in pixels (px)</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> the font.
   - Set the font family, style and weight.

   <br />

    </details>

    <details id="fields">
    <summary>Payment methods</summary>
    <br>

   Customize the look of all payment methods and forms. Here, you can:

   - Set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, text, and borders. You can also set a color for when the user hovers over each payment method.
   - Set the <a href="https://www.w3schools.com/cssref/css_units.php" target="_blank">size in pixels (px)</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the font, border width and radius, and box shadow.
   - Set the font family, style and weight.
   - Set the border style.

   <br />

    </details>

    <details id="settings-for-payment-form">
    <summary>Payment form</summary>
    <br>

   Customize the appearance of your payment forms using the settings below. These options are divided into two categories:

   Under **General**:

   - Set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color code</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for general background color, text, border, links and labels.
   - Set the <a href="https://www.w3schools.com/cssref/css_units.php" target="_blank">size in pixels (px)</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the labels.
   - Set the label's font weight.

   <br />

   Under **Inputs**:

   - Set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color code</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the input's background, text, borders, placeholder text, focus and errors.
   - Set the <a href="https://www.w3schools.com/cssref/css_units.php" target="_blank">size in pixels (px)</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the input's font, border width and radius.
   - Set the font family, style and weight. Set the border style.

   <br />

   </details>

    <details id="gatewayss">
    <summary>Gateways settings</summary>
    <br>

   Customize the color and text for **Apple Pay** and **Google Pay** payment components.  
   To preview the changes, go to **Review - Default**, click **Select component view** > **Express methods (Google & Apple Pay)**.

   - Click on the **Style Apple Pay** checkbox to enable customization for **Apple Pay**.
   - Click on the **Style Google Pay** checkbox to enable customization for the **Google Pay**.

   <br />

    </details>

   <details id="gateways">
    <summary>Settings</summary>
    <br>

   - Click the **Embed mode** checkbox to embed your payment component into your page. Enabling this settings will disable background and border customization for payment forms. Inputs can still be customized.  
     **⚠️ Note:** This only applies to **single components**.
   - Enable the **MultiSafepay Payment Button** for multiple payment components clicking the checkbox. To customize the appearance of this button, go to the **Primary Button**.

   <br />

    </details>

   <details id="pay-button">
    <summary>Primary button</summary>
    <br>

   If you've enabled the **MultiSafepay Payment Button** in the **Settings** section, you can customize its appearance:

   - Set the <a href="https://www.w3schools.com/colors/colors_picker.asp" target="_blank">Hex color code</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> for the background, text and border. You can also change the color for mouseovers.
   - Set the <a href="https://www.w3schools.com/cssref/css_units.php" target="_blank">size in pixels (px)</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> to change font size, border width, shadow and radius.
   - Set the font weight clicking the **Font weight** dropdown menu.

    </details>
6. To set this as your default template, select the **Set as default template** checkbox. 
7. In the **Save template as** field, enter the name of the template (used as the `template_id`), and then click **Submit settings**.

***

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]


[Top of page](#)