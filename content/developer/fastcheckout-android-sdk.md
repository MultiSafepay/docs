---
title: FastCheckout Android SDK
category:
  uri: Developers
slug: fastcheckout-android
position: 2
privacy:
  view: anyone_with_link
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/1281f9320696f2d256d0859421ec2cfa2350e644/static/logo/Integrations/Fastcheckout_Android.svg" width="100" align="right" />

The FastCheckout Android SDK enables a fast, frictionless, native checkout experience by storing and reusing customer data.

<a href="https://github.com/MultiSafepay/fastcheckout-android-sdk" target="_blank">View on GitHub</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />

# How it works

Simply provide a valid transaction ID or [create an order](/reference/createorder/). The SDK generates the checkout automatically and sends status updates for each transaction.

The checkout flow includes:

1. Shipping: Select a saved address, or add new shipping details.
2. Billing: Select saved payment details or a gift card, or add new payment details.
3. Confirmation: Confirm the order.

The SDK provides the following features:

* Secure sign up and sign in functionality
* Open seamless support tickets for specific orders

For more information, see the documentation in the SDK, which contains all classes, methods, and troubleshooting.

For how to create, update and retrieve orders, see the [API reference](/reference/introduction/).

# Preview

See how to:

<details id="sign-in-with-registered-email">
  <summary>Sign in with registered email address</summary>

  <br />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-1.png" width="300" />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-2.png" width="300" />
</details>

<details id="sign-in-with-unregistered-email">
  <summary>Sign in with unregistered email address</summary>

  <br />

  The customer is automatically redirected to the **Register** screen:

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-3.png" width="300" />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-4.png" width="300" />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-5.png" width="300" />
</details>

<details id="change-email">
  <summary>Change an email address</summary>

  <br />

  1. If a registered customer changes their email address, the SDK automatically sends a new security code to the email provided:

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-6.png" width="300" />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-7.png" width="300" />

  2. If the security code is received via SMS, it is automatically added to the appropriate field, or the customer enters the code.

  3. The customer enters a new PIN.

  4. The SDK provides biometric options, including face recognition:

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-8.png" width="300" />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-9.png" width="300" />
</details>

<details id="place-order">
  <summary>Place an order</summary>

  <br />

  1. The **Delivery** screen contains available shipping options.

  2. When the customer clicks **Continue**, the SDK moves to the **Payment** screen.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-10.png" width="300" />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-11.png" width="300" />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-12.png" width="300" />

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-13.png" width="300" />

  3. Once payment is complete, the SDK proceeds to the **Transaction complete** screen. The SDK callback notifies the client app of the \<\<glossary:transaction status>>.

  4. The customer clicks **Back to shop**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-14.png" width="300" />
</details>

# Requirements

* Android Studio version 3 or higher
* Android version 4.4 or higher
* Java or Kotlin

# Installation

1. Copy your [website API key](/docs/sites#site-id-api-key-and-security-code) to get the SDK from our <a href="https://github.com/MultiSafepay/fastcheckout-android-sdk" target="_blank">GitHub repository</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

2. Add the `msp-android-sdk-release.aar`:
   * As an embedded framework into your project
   * Into your library’s /lib folder.

3. In your build.gradle (Module.app) in the dependencies script, add the following:

   ```gradle
   implementation(name: 'msp-android-sdk-release', ext: 'aar')

   repositories {
      flatDir {
         dirs 'libs'
      }
   }
   ```

4. Sync Gradle.

> **✅ Success!**\
> You can now start using the Android SDK in your app.

# How to integrate

To integrate the Fastcheckout Android SDK into your app, follow these steps:

1. To set up the Android SDK, add the following to your MainActivity or Class:

```java
import com.multisafepay.sdk.FastCheckoutSDK;

//declare the FastCheckoutSDK as a member variable:
private static FastCheckoutSDK SDK = FastCheckoutSDK.getInstance();

//you must implement this interface and then set the listener:
Public class MainActivity extends AppCompatActivity 
implements ISDKCommunicator.sdkStatus {

//in your onCreate method initialize the SDK:
SDK.setApiKey(API_KEY);
…
…
}
```

The SDK is thread safe, but you cannot access the main UI elements from background threads. Creating and accessing UI controls from background thread is **not** thread safe.

#### Update the UI from a background thread in Android

**⚠️ Note:** For integration based on JAVA/Android versioning, see the official Android developers website – <a href="https://developer.android.com/guide/components/processes-and-threads" target="_blank">Threads</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

```java
…
…
YourActivity.this.runOnUiThread(new Runnable() {
    public void run() {

        //UI update here...

    }
});
…
…
```

#### Change the environment

To change the running environment from **live** to **test**, add the following line of code after `SDK.setApiKey(API_KEY)`:

```java
…
…
SDK.setApiKey(API_KEY);
//changing the environment to TEST
SDK.setEnvironment(FastCheckoutSDK.ENV_TEST)
…
…
```

Remember to comment out or delete this line of code before you release your app.

```java
…
…
//setting the environemnt to the default value (LIVE)
//SDK.setEnvironment(FastCheckoutSDK.ENV_TEST)
…
…
```

#### Custom settings

```java
…
…
//to set anonymous checkout: true (enabled) / false (dissable)
//with anonymous checkout there is no login
SDK.setAnonymous(boolean);

//skip checkout initial view (list of items): true (enabled) / false (dissable)
SDK.skipCheckoutInit(boolean);
…
…
```

2. Start a checkout and add callback interface to your Activity:

```java
//your class should implement the FastCheckoutSDK.Callback interface 
FastCheckoutSDK.Callback

//add registration to your onCreate method:
sdk.registerCallback(this); 

//then, start your checkout:
sdk.startCheckout(transaction_id, this);

//get results in your callback method:
@Override
public void callback(FastCheckoutSDK.Result result) {

   if (result.getResult() == FastCheckoutSDK.Result.FCO_RESULT_UNCLEARED) {
      
   }

   if (result.getResult() == FastCheckoutSDK.Result.FCO_RESULT_OK) {
      
   }

   if (result.getResult() == FastCheckoutSDK.Result.FCO_RESULT_CANCELLED) {

   }
}
```

3. Set up styles in your Application class (can be changed to suit your theme).

#### Fonts

The fonts used in this demo are not part of the code provided, but are part of your application.

* Download the fonts you want to use.
* Put them in **SRC** folder > **Main** folder (created for you by Android Studio when you create a project) > **Assets** folder (if you don't have an assets folder already, create one).
* Add the fonts as Typeface to your code as shown in the demo.

```java
Styles.Builder builder = new Styles.Builder();
builder.set("mainColor", "#FF7E03");
builder.set("mainFontSize", 30);

{
Typeface typeface = Typeface.createFromAsset(this.getAssets(), "fonts/nunito/Nunito-Medium.ttf");
   Styles.Font font = new Styles.Font("#000000", typeface, null);
   builder.setObject("labelFont", font);
}

{
 Typeface typeface = Typeface.createFromAsset(this.getAssets(), "fonts/nunito/Nunito-Medium.ttf");
   Styles.Font font = new Styles.Font("#FFFFFF", typeface, null);
   builder.setObject("buttonFont", font);
}

{
 Typeface typeface = Typeface.createFromAsset(this.getAssets(), "fonts/nunito/Nunito-ExtraLight.ttf");
   Styles.Font font = new Styles.Font("#000000", typeface, null);
   builder.setObject("editFont", font);
}

{
   Typeface typeface = Typeface.createFromAsset(this.getAssets(), "fonts/galada_regular.ttf");
   Styles.Font font = new Styles.Font("#000000", typeface, null);
   builder.setObject("titleFont", font);
   builder.set("title", "qwindo");
}
Styles styles = builder.build();
FastCheckoutSDK sdk = FastCheckoutSDK.getInstance();
sdk.setStyles(styles);
```

# Example

```java
import com.multisafepay.sdk.FastCheckoutSDK;

public class MainActivity extends AppCompatActivity implements FastCheckoutSDK.Callback{

private static FastCheckoutSDK SDK;
private Button btnStartNewTransaction;

@Override
protected void onCreate(Bundle savedInstanceState) {
   super.onCreate(savedInstanceState);
   setContentView(R.layout.main_activity);

   btnStartNewTransaction = findViewById(R.id.btn_transaction);

   SDK = FastCheckoutSDK.getInstance();
   SDK.setAnonymous(false);
   SDK.skipCheckoutInit(false);
   SDK.setApiKey(API_KEY);

   btnLogOut.setOnClickListener(view > SDK.startCheckout(transaction_id, this));

   }

@Override
public void callback(FastCheckoutSDK.Result result) {

   if (result.getResult() == FastCheckoutSDK.Result.FCO_RESULT_UNCLEARED) {
      
   }

   if (result.getResult() == FastCheckoutSDK.Result.FCO_RESULT_OK) {
      
   }

   if (result.getResult() == FastCheckoutSDK.Result.FCO_RESULT_CANCELLED) {

   }

  }
}
```

```java
import com.multisafepay.sdk.FastCheckoutSDK;

public class YourApplicationClassName extends Application {

@Override
protected void onCreate(Bundle savedInstanceState) {
   super.onCreate(savedInstanceState);
   setContentView(R.layout.main_activity);

   Styles.Builder builder = new Styles.Builder();
   builder.set("mainColor", "#FF7E03");
   builder.set("mainFontSize", 30);

{
Typeface typeface = Typeface.createFromAsset(this.getAssets(), "fonts/nunito/Nunito-Medium.ttf");
   Styles.Font font = new Styles.Font("#000000", typeface, null);
   builder.setObject("labelFont", font);
}

{
 Typeface typeface = Typeface.createFromAsset(this.getAssets(), "fonts/nunito/Nunito-Medium.ttf");
   Styles.Font font = new Styles.Font("#FFFFFF", typeface, null);
   builder.setObject("buttonFont", font);
}

{
 Typeface typeface = Typeface.createFromAsset(this.getAssets(), "fonts/nunito/Nunito-ExtraLight.ttf");
   Styles.Font font = new Styles.Font("#000000", typeface, null);
   builder.setObject("editFont", font);
}

{
   Typeface typeface = Typeface.createFromAsset(this.getAssets(), "fonts/galada_regular.ttf");
   Styles.Font font = new Styles.Font("#000000", typeface, null);
   builder.setObject("titleFont", font);
   builder.set("title", "qwindo");
}
Styles styles = builder.build();
FastCheckoutSDK sdk = FastCheckoutSDK.getInstance();
sdk.setStyles(styles);

   }
}

```

<br />

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
