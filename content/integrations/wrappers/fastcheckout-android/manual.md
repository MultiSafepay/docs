---
title : "FastCheckout SDK Android configuration manual"
meta_title: "FastCheckout SDK Android configuration manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases: [/integrations/fastcheckout-android/manual/]
---
### Introduction

The FastCheckout SDK is a library that you can integrate into your native Android, iOS and/or React Native application providing connection to MultiSafepay services. The FastCheckout SDK adds a smooth, fast and native checkout experience to your mobile app, and by storing and reusing data it is the fastest checkout process available for shopping apps.

As an integrator, you only need to provide a valid MSP transaction identifier or create a transaction. The FastCheckout SDK leverages the checkout process for you, providing notifications for all possible outcomes (success, pending, cancelled, etc.) once it completes a transaction. The checkout process flow includes:

* Shipping details:
    * Preferred shipping details
    * Add shipping details
* Payment methods:
    * Preferred payment methods
    * Add payment methods
    * Gift cards
* Confirmation details

#### Additional details

The FastCheckout SDK provides the additional following features:

* Authentication into FastCheckout: 
    * It provides secure sign-up/login functionality
* Check orders:
    * Open seamless support tickets to related orders
* Support orders:
    * Easily open a support ticket related to an order
* Edit payment information:
    * List and edit user’s stored payment details
* Manage shipping addresses:
    * List, add and edit shipping information

*If you need more information, please check the documentation that you will find inside the SDK, which contains all classes, methods, common troubleshooting and more details.*

Please refer to the MultiSafepay API Documentation to perform different calls through which you can start transactions, update transactions, perform refunds and receive information about transactions: https://docs.multisafepay.com/api/#orders

#### Advanced Setup
The SDK has two environments on which it operates, LIVE, the default environment, and TEST. You might want to use the TEST environment to test your integration before releasing your App. No real transaction is performed in TEST environment. 

Check the example below to see how you can setup the environment you want to use. 

### Requirements

* Android Studio 3 and up
* Android version 4.4 and up
* Java or Kotlin


### Installation

First you have to access into your Back Office and get a valid [API key](/faq/general/glossary/#api-key) (_Settings_ > _Website Settings_).

Once you have your valid API key, you can get the SDK on our [GitHub repository](https://github.com/MultiSafepay/fastcheckout-android-sdk)

Add the msp-android-sdk-release.aar as an embedded framework into your project. The next steps will guide you through the process:

1. Add the msp-android-sdk-release.aar into your library’s /lib folder.
2. In your build.gradle (Module.app) inside of the dependencies script add the following

   ```gradle
   implementation(name: 'msp-android-sdk-release', ext: 'aar')

   repositories {
      flatDir {
         dirs 'libs'
      }
   }
   ```

3. Sync Gradle

You can now start using the Android SDK in your App.

### Demo

You can easily integrate the Fastcheckout Android SDK into your app, you just need to follow the next steps:

1. Setup the Android SDK. Add the following to your MainActivity or Class:

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

If you want to change the running environment from LIVE to TEST, add the following line of code after SDK.setApiKey(API_KEY):

```java
…
…
SDK.setApiKey(API_KEY);
//changing the environment to TEST
SDK.setEnvironment(FastCheckoutSDK.ENV_TEST)
…
…
```

Remember to comment out or delete this line of code before you release your App.

```java
…
…
//setting the environemnt to the default value (LIVE)
//SDK.setEnvironment(FastCheckoutSDK.ENV_TEST)
…
…
```

2. Start checkout and add callback interface to your Activity

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
3. Setup styles in your Application class (these styles might be changed to suit your theme):

#### One note on fonts

The fonts used in this demo are not part of the code that is provided to you. These fonts are part of your application, not the SDK.
You will need to download the fonts you want to use, place them inside of a folder called assets (if you don't see it, create one) which is inside of the main foder (the main folder is inside of the src folder, and it is created for you by Android Studio when you create a project). Add the fonts as Typeface to your code accordingly as shown in the demo.

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
### SDK Snapshots:

1. The following snapshots will walk you through some of features offered by the Fastcheckout Android SDK. The Fastcheckout iOS SDK provides the same functionalities.
    * Logging in with a registered email: 
        
      {{< zoom_able class="img-size zoomable" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-1.png" title="screenshot 1">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-2.png" title="screenshot 2">}}

    * Logging in with a non-registered email will automatically take the user to the register SDK screen: 

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-3.png" title="screenshot 3">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-4.png" title="screenshot 4">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-5.png" title="screenshot 5">}}

    * If the user is registered and resets its email account, the SDK  will automatically send a new security code to new entered email: 

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-6.png" title="screenshot 6">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-7.png" title="screenshot 7">}}

    * Once the user enters the security code received by email (if the security code is received via SMS it will automatically get added to appropriate field, and the SDK will move into the following state) the SDK will ask for a new security PIN, once entered, the SDK will provide Biometric options (in iOS face recognition is also available):

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-8.png" title="screenshot 8">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-9.png" title="screenshot 9">}}

    * The checkout process follows. From a merchant’s webshop checkout option, the SDK enters into the checkout process. The first view will be the delivery view with shipping options if available. Once the continue button is selected, the SDK moves into the Payment screen and the payment logic follows.

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-10.png" title="screenshot 10">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-11.png" title="screenshot 11">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-12.png" title="screenshot 12">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-13.png" title="screenshot 13">}}
    
    * Once the payment process is completed the SDK will proceed to the “transaction is complete” screen. The SDK callback will notify the client app about this or any other results (uncleared, cancel, etc.). Pressing the button “Back to Shop” will redirect the user to the Merchant’s webshop.

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-android/fastcheckout-android-14.png" title="screenshot 14">}}