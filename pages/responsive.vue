<template>
<div id="nav-scroller">

  
    <b-container fluid>
      <b-carousel
        id="carousel-fade"
        style="text-shadow: 0px 0px 2px #000"
        fade
        controls
        indicators
        img-width="1024"
        img-height="480"
      >
      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=1001">
        
      <div class="display-1 text-left text"> It's time</div>
        
      </b-carousel-slide>
        <b-carousel-slide
          caption="If hygene is important ... become an owner"
          img-src="https://picsum.photos/1024/480/?image=348"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="earn as you maintain dispencers"
          img-src="https://picsum.photos/1024/480/?image=189"
        ></b-carousel-slide>
      </b-carousel>
    </b-container>  

</div>
</template>

<script>
  export default {
    
  }
</script>
