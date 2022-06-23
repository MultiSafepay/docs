---
title: "FastCheckout Android SDK"
category: 62962df622e99600810c117d
order: 70
hidden: true
slug: 'fastcheckout-android'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/1281f9320696f2d256d0859421ec2cfa2350e644/static/logo/Integrations/Fastcheckout_Android.svg" width="100" align ="right"/>

The FastCheckout Android SDK helps you connect to MultiSafepay from your native Android app. It enables a fast, frictionless, native checkout experience by storing and reusing data.

[View on GitHub](https://github.com/MultiSafepay/fastcheckout-android-sdk)

## Manual

Simply provide a valid transaction ID or [create an order](https://docs-api.multisafepay.com/reference/createorder). The SDK generates the checkout automatically and sends status updates for each transaction.  The checkout flow includes:

- Shipping details:
    - Preferred shipping details
    - Add shipping details
- Payment methods:
    - Preferred payment methods
    - Add payment methods
    - Gift cards
- Confirmation details

#### Features

The FastCheckout SDK provides the following additional features:

- Secure sign up and sign in functionality
- Open seamless support tickets to related orders
- List and edit users' stored payment details
- List, add, and edit shipping information

For more information, see the documentation in the SDK, which contains all classes, methods, and troubleshooting.

To learn more about creating, updating and retrieving orders, see the [API reference](https://docs-api.multisafepay.com/reference/introduction).

#### Advanced setup
The SDK operates in two environments: live (default) and test (no real transactions processed). We recommend testing your integration before releasing your app.  

For how to set up each environment, see the example below. 

### Requirements

- Android Studio version 3 or higher
- Android version 4.4 or higher
- Java or Kotlin

### How to install

1. Copy your [site API key](/docs/sites#site-id-api-key-and-security-code) to get the SDK from our [GitHub repository](https://github.com/MultiSafepay/fastcheckout-android-sdk).
2. Add the msp-android-sdk-release.aar as an embedded framework into your project. 
3. Add the msp-android-sdk-release.aar into your library’s /lib folder.
4. In your build.gradle (Module.app) in the dependencies script, add the following:

   ```gradle
   implementation(name: 'msp-android-sdk-release', ext: 'aar')

   repositories {
      flatDir {
         dirs 'libs'
      }
   }
   ```

5. Sync Gradle.

You can now start using the Android SDK in your app.

### Demo

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

** Updating the UI from a background thread in Android**
(Note: Check Android developers’ official site on [Threads](https://developer.android.com/guide/components/processes-and-threads) for proper integration based on JAVA/Android versioning).

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

To change the running environment from LIVE to TEST, add the following line of code after SDK.setApiKey(API_KEY):

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

Custom settings:

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

2. Start checkout and add callback interface to your Activity:

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
3. Set up styles in your Application class (can be changed to suit your theme):

#### Fonts

The fonts used in this demo are not part of the code provided, but are part of your application.

1. Download the fonts you want to use.
2. Put them in **SRC** folder > **Main** folder (created for you by Android Studio when you create a project) > **Assets** folder (if you don't have an assets folder already, create one). 
3. Add the fonts as Typeface to your code as shown in the demo.

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

###### Complete example

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
### SDK snapshots

1. The following snapshots walk you through some of the features offered by the Fastcheckout Android/iOS SDK. 
    * Logging in with a registered email: 
        
      {{< zoom_able class="img-size zoomable" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-1.png" title="screenshot 1">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-2.png" title="screenshot 2">}}

    * Logging in with an unregistered email automatically takes the customer to the **Register** screen: 

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-3.png" title="screenshot 3">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-4.png" title="screenshot 4">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-5.png" title="screenshot 5">}}

    * If the customer is registered and resets their email account, the SDK automatically sends a new security code to the new email provided: 

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-6.png" title="screenshot 6">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-7.png" title="screenshot 7">}}

    * Once the customer enters the security code received by email (if the security code is received via SMS it is automatically added to the appropriate field, and the SDK moves into the following state) the SDK asks for a new security PIN. Having entered the PIN, the SDK provides biometric options (iOS also supports face recognition):

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-8.png" title="screenshot 8">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-9.png" title="screenshot 9">}}

    * The checkout process follows. From the webshop checkout, the SDK enters into the checkout process. The first screen is the **Delivery** screen, with shipping options (if available). When the customer clicks **Continue**, the SDK moves to the **Payment** screen and the payment logic follows.

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-10.png" title="screenshot 10">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-11.png" title="screenshot 11">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-12.png" title="screenshot 12">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-13.png" title="screenshot 13">}}
    
    * Once the payment process is completed, the SDK proceeds to the **Transaction complete** screen. The SDK callback notifies the client app of the transaction status, e.g. Uncleared, Cancelled. Clicking **Back to shop** redirect the customer back to the webshop.

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-android-14.png" title="screenshot 14">}}
