<template>
  <div>
  <b-container fluid>
    <b-row class="p-0 " >
      <b-col >
        <b-card overlay img-src="https://picsum.photos/1024/480/?image=1001&blur=5">
          <b-card-body>

          <h2>Store</h2>
          <b-row class="p-0">
            <b-col md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.6)">
                <h3>Weight</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="weight" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <animatednumber class="h2" :value='item.weight' :duration='500' :delay='100' round='1'/> kg
                </h2>
              </div>
            </b-col>

            <b-col md="4" sm="6" xs="12" class="align-items-center ">
              <div class="my-2 h-100 p-4 text-center shadow rounded" style="background-color: rgba(255, 255, 255, 0.6)">
                <h3>Goal</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="carrot" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <animatednumber class="h2" value='600' :duration='500' :delay='100' round='1'/> kg
                </h2>
              </div>
            </b-col>

            <b-col md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 1)">
                <h3>Store Discount</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="award" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <animatednumber class="h2" :value='item.weight / 600 * 20' :duration='500' :delay='100' round='1'/>%
                </h2>
              </div>
            </b-col>
          </b-row>

          <br/>

          <h2>Germany</h2>
          <b-row class="p-0">
            <b-col md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Weight</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="weight" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <animatednumber class="h2" :value='7256+item.weight' :duration='500' :delay='100' round='1'/> kg
                </h2>
              </div>
            </b-col>

            <b-col md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Goal</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="carrot" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  7,000 kg
                </h2>
 

              </div>
            </b-col>

          </b-row>

         <br/>
          
          <h2>Global</h2>
          <b-row class="p-0">
            <b-col md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Weight</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="weight" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <animatednumber class="h2" :value='39765+item.weight' :duration='500' :delay='100' round='1'/> kg
                </h2>
              </div>
            </b-col>

            <b-col md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Goal</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="carrot" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  70,000 kg
                </h2>
                <div class="text-center">
                  in celebration of 70 years of Adidas
                </div>
              </div>
            </b-col>

          </b-row>

          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
  </div>
</template>

<script>

  
import animatednumber from 'animated-number-vue'
import VueSlider from 'vue-slider-component/dist-css/vue-slider-component.umd.min.js'
import 'vue-slider-component/dist-css/vue-slider-component.css'
import 'vue-slider-component/theme/default.css'

import Swatches from 'vue-swatches'
import "vue-swatches/dist/vue-swatches.min.css"

import usesmonthchart from '@/components/charts/usesmonthchart'
import fluidmonthchart from '@/components/charts/fluidmonthchart'

import { mapGetters } from 'vuex'

export default {

  data() {
    return {
      id: this.$route.params.id,
      hygeneindexgoal:82,
      hygeneindexrecord:75,
      hygeneindextrend:2,
      dosage: 30,
      color: '#1CA085',
      colors: [
        ['#51e5db', '#74ebe3', '#96f0ea', '#b9f5f1', '#dcfaf8', '' ]
      ],
      luminosity:80
    }
  },
  created: function(){
    //this.$store.dispatch('device/fetch', this.id)
    this.$store.dispatch('device/observe')
  },
  computed: {
    item() {
      return this.$store.getters['device/item']
    },
    current() {
      return {} //this.$store.getters['device/item'].current[0]
    }
  },

  methods: {
    owneraddress(location) {
      return location.street +' '+
             location.number +', '+
             location.city +' '+
             location.country +' '+
             location.postalcode 
    }
  },
  
  components: {
    animatednumber,
    VueSlider,
    Swatches,
    usesmonthchart,
    fluidmonthchart
  }
}
</script>

