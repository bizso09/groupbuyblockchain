<template>
  <article class="listing row">
    <div class="col-9">
      <h2>{{ title }}</h2>

      <img alt="Product image" src="../assets/Fixed-Gear-Bike-Track-6-Matte-Red.jpg" width="100%">
    </div>
    <div class="col-3">
      <span>Pledge to buy</span>
      <Pledge title="Commit to buying" target="20"/>
    </div>
  </article>
</template>

<script>
import Pledge from '@/components/Pledge.vue';

export default {
  name: 'Listing',
  props: {
    title: String,
    img: String,
  },
  components: {
    Pledge,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
