> ⚠️ Note:
> 
> These plugins represent older versions of our solutions and are no longer under active development or maintenance. They may contain security vulnerabilities, compatibility issues, and lack the latest features. MultiSafepay provides no support for these plugins.
> 
> If you are interested in maintaining any of these repositories and have the expertise and authority to become a maintainer, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

<div class="auto-grid">
    <div class="card-container">
        <a href="/docs/craft-commerce/" style="text-decoration: none;">
            <div class="card">
                <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Craft_Commerce.svg">
                <div class="container">
                    <h4><b>Craft Commerce</b></h4>
                </div>
            </div>
        </a>
    </div>
    <div class="card-container">
        <a href="/docs/oscommerce/" style="text-decoration: none;">
            <div class="card">
                <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/OsCommerce.svg">
                <div class="container">
                    <h4><b>Os Commerce</b></h4>
                </div>
            </div>
        </a>
    </div>
    <div class="card-container">
        <a href="/docs/scandipwa/" style="text-decoration: none;">
            <div class="card">
                <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/ScandiPWA.svg">
                <div class="container">
                    <h4><b>ScandiPWA</b></h4>
                </div>
            </div>
        </a>
    </div>
    <div class="card-container">
        <a href="/docs/virtuemart-3/" style="text-decoration: none;">
            <div class="card">
                <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/VirtueMart.svg">
                <div class="container">
                    <h4><b>VirtueMart 3</b></h4>
                </div>
            </div>
        </a>
    </div>
    <div class="card-container">
        <a href="/docs/vue-storefront/" style="text-decoration: none;">
            <div class="card">
                <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Vue_Storefront.svg">
                <div class="container">
                    <h4><b>Vue Storefront</b></h4>
                </div>
            </div>
        </a>
    </div>
    <div class="card-container">
        <a href="/docs/x-cart/" style="text-decoration: none;">
            <div class="card">
                <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/X-Cart.svg">
                <div class="container">
                    <h4><b>X-Cart</b></h4>
                </div>
            </div>
        </a>
    </div>
    <div class="card-container">
        <a href="/docs/zen-cart/" style="text-decoration: none;">
            <div class="card">
                <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Zen_Cart.svg">
                <div class="container">
                    <h4><b>Zen Cart</b></h4>
                </div>
            </div>
        </a>
    </div>
 </div>

<style>
b {
  color: #384248 !important;
}

.auto-grid {
  --auto-grid-min-size: 200px;

  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 1rem;
  padding: 0 1rem;  /* Add padding to the left and right */
}
  
.card-container {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  padding: 10px;
  text-align: center;
  background-color: #fff;
  border-radius: 5px;
  max-height: 180px;
  min-height: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center; /* Center horizontally */
  align-items: center;
}

.card-container:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.card img {
  max-height: 50px;
  margin-top: 15px;
  pointer-events: none;
}

.card.container h4{
  text-align: center;
  }

.card .container {
  margin-bottom: 10px; /* Increase bottom margin*/
  display: -webkit-box; /* Add this */
  -webkit-line-clamp: 2; /* This is the number of lines you want to show */
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card h4 {
  font-size: 0.9em;
  margin: 0.5em 0;
}

@media (max-width: 768px) { /* Example breakpoint for mobile devices */
  .auto-grid {
    grid-template-columns: repeat(2, 1fr); /* 2 columns on smaller screens */
    padding: 0 0.5rem;  /* Adjust padding on smaller screens if needed */
  }
}

@media (max-width: 480px) { /* Example breakpoint for very small screens */
  .auto-grid {
    grid-template-columns: 1fr; /* 1 column on very small screens */
    padding: 0 0.5rem; /* Adjust padding on very small screens if needed */
  }
}
Use code with caution.
Css
Explanation:

padding: 0 1rem;: This adds 1rem of padding to the left and right of the auto-grid container. The 0 means no padding is added to the top and bottom. This creates some space between the cards and the edge of the screen.

I've also added padding adjustments within the media queries to fine-tune the spacing on smaller screens.

Approach 2: Use clamp() for Dynamic Padding (More Advanced)

A more advanced (and possibly more responsive) approach would be to use clamp() to define a dynamic minimum padding based on the viewport width. This requires a bit more understanding of CSS functions, but it can result in a more fluid layout.


</style>