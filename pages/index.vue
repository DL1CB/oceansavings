<template>
  <b-container>
    <div class="p-2 my-3 display-3 text-center text-white">Ocean Savings</div>
    <br />

    <b-row class="h-50 d-flex justify-content-center">
      <b-col md="4" sm="6" xs="12" class="p-2 my-2 align-items-center">
        <div
          class="h-100 p-4 text-center shadow"
          style="background-color: rgba(255, 255, 255, 0.9)"
        >
          <h3>Store Discount</h3>
          <br />
          <h2 class="text-center">
            <animatednumber
              class="h1"
              :value="discount(item.weight,600,20)"
              :duration="500"
              :delay="100"
              round="1"
            />%
          </h2>
        </div>
      </b-col>
      <b-col md="1" sm="1" xs="12" class="p-0 align-self-center align-items-center">
        <h2 class="h-100 text-center">
          <fa icon="link" transform="grow-4" />
        </h2>
      </b-col>

      <b-col md="4" sm="6" xs="12" class="p-2 my-2 align-items-center">
        <div
          class="h-100 p-4 text-center shadow"
          style="background-color: rgba(255, 255, 255, 0.9)"
        >
          <h3>Weight</h3>
          <br />
          <h2 class="text-center">
            <fa-layers class="text-center">
              <fa icon="trash" transform="grow-5" />
              <fa
                icon="futbol"
                transform="shrink-6 down-2"
                :style="{ color: 'rgba(0, 231, 255, 1)' }"
              />
            </fa-layers>
            <animatednumber
              class="h2"
              :value="item.weight"
              :formatValue="formatToKilogram"
              :duration="500"
              :delay="100"
              round="1"
            />kg
          </h2>
        </div>
      </b-col>
    </b-row>

    <b-row class="h-50 justify-content-center">
      <b-col md="4" sm="6" xs="12" class="p-2 my-2 align-items-center">
        <div
          class="h-100 p-4 text-center shadow"
          style="background-color: rgba(255, 255, 255, 0.9)"
        >
          <h3>Collected</h3>
          <br />
          <h2 class="text-center">
            <animatednumber
              class="h2"
              :value="39765+item.weight"
              :duration="500"
              :delay="100"
              round="1"
            />kg
          </h2>
        </div>
      </b-col>
      <b-col md="4" sm="6" xs="12" class="p-2 my-2 align-items-center">
        <div
          class="h-100 p-4 text-center shadow"
          style="background-color: rgba(255, 255, 255, 0.9)"
        >
          <h3>Goal</h3>
          <br />
          <h2 class="text-center">70,000 kg</h2>
        </div>
      </b-col>

      <b-col md="4" sm="6" xs="12" class="p-2 my-2 align-items-center">
        <div
          class="h-100 p-4 text-center shadow"
          style="background-color: rgba(255, 255, 255, 0.9)"
        >
          <h3>Follow</h3>
          <br />

          <b-img class="w-25 img-fluid" src="~/assets/qrcode.png"></b-img>
        </div>
      </b-col>
    </b-row>

    <b-row class="h-50 justify-content-center">
      <b-col md="12" class="p-2 align-items-center">
        <div
          class="h-100 p-4 text-center shadow"
          style="background-color: rgba(255, 255, 255, 0.9)"
        >
          <b-carousel
            :interval="8000"

            fade
            img-width="1024"
            img-height="200"
            style="text-shadow: 1px 1px 2px #333;"
          >
            <b-carousel-slide img-src="https://picsum.photos/1024/200/?image=1001&blur=3">
              <div class="display-4">save the oceans</div>
              <div class="display-4">while saving</div>
            </b-carousel-slide>

            <b-carousel-slide img-src="https://picsum.photos/1024/200/?image=1002&blur=1">
              <div class="display-4">prevent</div>
              <div class="display-4">ocean plastic</div>
            </b-carousel-slide>

            <b-carousel-slide img-src="https://picsum.photos/1024/200/?image=1069&blur=1">
              <div class="display-4">recycle the old</div>
              <div class="display-4">enjoy the new</div>
            </b-carousel-slide>

            <b-carousel-slide img-src="https://picsum.photos/1024/200/?image=124&blur=1">
              <div class="display-4">explore the store </div>
              <div class="display-4">while the discount rises</div>
            </b-carousel-slide>

          </b-carousel>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import animatednumber from "animated-number-vue";

export default {
  created: function() {
    //this.$store.dispatch('device/fetch', this.id)
    this.$store.dispatch("device/observe");
  },
  computed: {
    item() {
      return this.$store.getters["device/item"];
    }
  },

  methods: {
    formatToKilogram(value) {
      value = parseInt(value);
      value = value / 1000;
      return `${value.toFixed(2)}`;
    },
    discount(weight, goal, maxdiscount) {
      //var result = (weight / 600000) * 20
      var result = (weight / 6000) * 20;
      return Math.min(maxdiscount, result);
    }
  },

  components: {
    animatednumber
  }
};
</script>

<style>
body {
  background: url("https://picsum.photos/1920/1080/?image=218") no-repeat center
    center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  background-size: cover;
  -o-background-size: cover;
}

.carousel-caption {
  position: block;
  right: 15%;
  top: 0%;
  left: 15%;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
}
</style>

