
<template>
  <div>
    <input v-model="message" placeholder="edit me">
    <p>Message is: {{ message }}</p>
    <button v-on:click="pledge">{{title}}</button>
    <div class="progress">
      <div
        class="progress-bar"
        role="progressbar"
        v-bind:style="{width: currentPledges/target*100 + '%'}"
        :aria-valuenow="currentPledges"
        aria-valuemin="0"
        :aria-valuemax="target"
      ></div>
    </div>
    <span>{{currentPledges}} out of a target of {{target}}.</span>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Pledge",
  props: {
    title: String,
    target: Number,
    currentPledges: {
      type: Number,
      default: 0
    },
    message: String
  },
  methods: {
    pledge: function(event) {
      this.currentPledges += 1;
      if (this.currentPledges >= this.target) {
        var bodyFormData = new FormData();
        bodyFormData.set('itemId', 100);
        bodyFormData.set('link', "http://localhost:8080/");
        bodyFormData.set('description', "Single speed bike in red");
        bodyFormData.set('price', 80);
        
        axios({
          method: "post",
          url: "http://127.0.0.1:5000/item",
          data: bodyFormData,
          config: { headers: { "Content-Type": "multipart/form-data" } }
        })
          .then(function(response) {
            //handle success
            console.log(response);
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

button {
  padding: 1em 2em;
  margin: 1em;
}
</style>
