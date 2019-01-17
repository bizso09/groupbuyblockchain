
<template>
  <div v-on:click="currentPledges += 1">
    <button>{{title}}</button>
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
export default {
  name: 'Pledge',
  props: {
    title: String,
    target: Number,
    currentPledges: {
      type: Number,
      default: 0,
    },
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
