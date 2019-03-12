<template>

  <!-- welcome section -->
  <section class="xs-screen-height xs-welcome-section xs-bg fundpress-welcome-section">
    <div class="container">
      <div class="row">
        <div class="col-lg-6">
          <div class="xs-welcome-content fundpress-welcome-content">
            <div class="xs-welcome-wraper fundpress-welcome-wraper">
              <div class="xs-welcome-title fundpress-welcome-title">
                <h2 class="color-navy-blue">{{item.title}}</h2>
              </div>
              <span>Currently live: {{live}}</span>
              <Pledge title="Commit to buying" :target="item.requiredQuantity" :price="item.price"/>
              <div class="xs-btn-wraper">
                <a href="#" class="xs-btn round-btn navy-blue-btn icon-btn">
                  <i class="fa fa-heart"></i>invest Now
                </a>
                <a href="#" class="xs-btn round-btn blue-btn icon-btn">
                  <i class="fa fa-facebook"></i>Share Now
                </a>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="xs-welcome-content">
            <div class="fundpress-animate text-center">
              <img :src="item.image" alt>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Pledge from "@/components/Pledge.vue";
import axios from "axios";

export default {
  name: "Listing",
  props: {
    title: String,
    item: {
      title: String,
      image: String,
      price: Number,
      requiredQuantity: Number,
    },
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
