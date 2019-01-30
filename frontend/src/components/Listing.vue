<template>
  <article class="listing row">
    <div class="col-9">
      <h2>{{ title }}</h2>
      <button v-on:click="addItem">Create smart contract</button>
      <span>Currently live: {{live}}</span>
      <img alt="Product image" src="../assets/Fixed-Gear-Bike-Track-6-Matte-Red.jpg" width="100%">
    </div>
    <div class="col-3" style="border:3px #999 solid;">
      <span>Pledge to buy</span>
      <Pledge title="Commit to buying" target="20"/>
    </div>
  </article>
</template>

<script>
import Pledge from "@/components/Pledge.vue";
import axios from "axios";

export default {
  name: "Listing",
  props: {
    title: String,
    img: String,
    live: {
      type: Boolean,
      default: false
    }
  },
  components: {
    Pledge
  },

  methods: {
    addItem: function(event) {
      if (this.live === false) {
        var that = this;
        var bodyFormData = new FormData();
        bodyFormData.set("itemId", 100);
        bodyFormData.set("link", "http://localhost:8080/");
        bodyFormData.set("description", "Single speed bike in red");
        bodyFormData.set("price", 80);
        axios({
          method: "post",
          url: "http://127.0.0.1:5000/item",
          data: bodyFormData,
          config: { headers: { "Content-Type": "multipart/form-data" } }
        })
          .then(function(response) {
            console.log(response);
            that.live = true;
          })
          .catch(function(response) {
            //handle error
            console.log(response);
          });
      }
    }
  }
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
