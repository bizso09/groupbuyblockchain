<template>
  <div class="home">
    <div class="row">
      <div class="col-sm">
        <h1>GroupBuy</h1>
        <p>Welcome to groupbuy. Please see our daily deal below.</p>
      </div>
    </div>
    <Listing title="Buy this bike" img="@/assets/Fixed-Gear-Bike-Track-6-Matte-Red.jpg"/>
  </div>
</template>

<script>
// @ is an alias to /src

import Listing from '@/components/Listing.vue';

export default {
  name: 'home',
  components: {
    Listing,
  },
};
</script>
