<template>
  <div class="home">
    <Listing :item=item
      :title=item.title
      :img=item.image
    />
  </div>
</template>

<script>
import { db } from "../main";
import Listing from "@/components/Listing.vue";
import router from "../router";

export default {
  name: "Item",
  components: {
    Listing
  },
  data() {
    return {
      items: [],
      item: {}
    };
  },

  firestore() {
    return {
      items: db.collection("items"),
      item: db.collection("items").doc(this.$route.params.itemId)
    };
  }
};
</script>
